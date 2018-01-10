#!/usr/bin/env python

"""
A simple python script template.
"""

import os
import sys
import time
import argparse
import logging
import json
import pprint as pp
from prettytable import  PrettyTable
from prettytable import MSWORD_FRIENDLY
import ROOT as rt

import functools, logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class log_with(object):
    '''Logging decorator that allows you to log with a specific logger.'''
    # Customize these messages
    ENTRY_MESSAGE = 'Entering {}'
    EXIT_MESSAGE = 'Exiting {}'

    def __init__(self, logger=None):
        self.logger = logger

    def __call__(self, func):
        '''Returns a wrapper that wraps func. The wrapper will log the entry and exit points of the function with logging.INFO level.'''
        # set logger if it was not set earlier
        if not self.logger:
            logging.basicConfig()
            self.logger = logging.getLogger(func.__module__)
            self.logger.setLevel(logging.WARNING)

        @functools.wraps(func)
        def wrapper(*args, **kwds):
            self.logger.info(self.ENTRY_MESSAGE.format(func.__name__))  # logging level .info(). Set to .debug() if you want to
            f_result = func(*args, **kwds)
            self.logger.info(self.EXIT_MESSAGE.format(func.__name__))   # logging level .info(). Set to .debug() if you want to
            return f_result
        return wrapper

def progress(current, total, status=''):
        fullBarLength = 80
        doneBarLength = int(round(fullBarLength * current / float(total)))

        percents = round(100.0 * current / float(total), 1)
        bar = '>' * doneBarLength + ' ' * (fullBarLength - doneBarLength)

        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()

class MVADistributions(object):
        def __init__(self,jsondic):
                self._jsondic = jsondic
                self._mvadistributions = {}
                self._mva_roc_curves = {}
                self._craneen_tree_name = 'Craneen__Mu'
                self._tmva_tree_name = 'TestTree'
                self._tmva_discriminator_names = ['BDTGSIG500','BDTGSIG20',\
                        'BDTASIG500','BDTASIG20',\
                        'BDTA500','BDTA20',\
                        'BDTG500','BDTG20']
                self._usedhists = {'tmva_b':'h_ttmix_BDTA20','tmva_s':'h_tttt_BDTA20',
                                   'old_b':'hist_total_bg','old_s':'h_tttt_BDT9and10jetsplitNoNjw'}
                self._craneen_discriminator_names = ['BDT9and10jetsplitNoNjw']
                self._histconfig = "(25,-1.,1.)"
                self.Initialize()

        def Initialize(self):
                # build histograms
                self.get_hist_from_tmva_file()
                self.get_signal_and_bg_from_craneens()
                self.get_roc_curves()

        @log_with()
        def get_roc_curves(self):
                #TMVA
                self._mva_roc_curves['tmva'] = rt.TGraph()
                hb = self._mvadistributions['tmva'].FindObject(self._usedhists['tmva_b'])
                hs = self._mvadistributions['tmva'].FindObject(self._usedhists['tmva_s'])
                nbins = hb.GetNbinsX()
                for iBin in range(1,nbins+1):
                        esp_sig = (hs.Integral(iBin,nbins)/hs.Integral(1,nbins))
                        esp_bg = (hb.Integral(iBin,nbins)/hb.Integral(1,nbins))
                        self._mva_roc_curves['tmva'].SetPoint(iBin-1,esp_sig,1.-esp_bg)

                #default mva
                self._mva_roc_curves['oldmva'] = rt.TGraph()
                hb = self._mvadistributions['oldmva'].FindObject(self._usedhists['old_b'])
                hs = self._mvadistributions['oldmva'].FindObject(self._usedhists['old_s'])
                nbins = hb.GetNbinsX()
                for iBin in range(1,nbins+1):
                        esp_sig = (hs.Integral(iBin,nbins)/hs.Integral(1,nbins))
                        esp_bg = (hb.Integral(iBin,nbins)/hb.Integral(1,nbins))
                        self._mva_roc_curves['oldmva'].SetPoint(iBin-1,esp_sig,1.-esp_bg)

        @log_with()
        def fill_tmvadistributions(self,tree,idname,mvaname):
                min = tree.GetMinimum(mvaname)
                max = tree.GetMaximum(mvaname)
                # mva' = (mva-min)/(max-min)*(max'-min') + min'
                rescaled_mva = '({}-{})/({}-{})*(1. - (-1)) + (-1.)'.format(mvaname,min,max,min)
                #background histograms
                histname = "h_ttmix_{}".format(mvaname)
                histconfig = "{}{}".format(histname,self._histconfig)
                bg_cuts = "classID==0"
                tree.Draw("{}>>{}".format(rescaled_mva,histconfig),bg_cuts)
                hist = rt.gDirectory.Get(histname)
                rt.SetOwnership( hist, False )
                if hist:
                        hist.Scale(1./hist.Integral())
                        self._mvadistributions[idname].AddLast(hist)

                #signal histograms
                histname = "h_tttt_{}".format(mvaname)
                histconfig = "{}{}".format(histname,self._histconfig)
                sg_cuts = "classID==1"
                tree.Draw("{}>>{}".format(rescaled_mva,histconfig),sg_cuts)
                hist = rt.gDirectory.Get(histname)
                rt.SetOwnership( hist, False )
                if hist:
                        hist.Scale(1./hist.Integral())
                        self._mvadistributions[idname].AddLast(hist)

        @log_with()
        def get_hist_from_tmva_file(self):
                idname = 'tmva'
                filename = self._jsondic[idname]
                if not filename:
                        logging.error("File name is wrong: {}".format(filename))
                        sys.exit(1)
                rootfile = rt.TFile.Open(filename,"READ")
                rt.SetOwnership(rootfile,False)
                tree = rootfile.Get(self._tmva_tree_name)
                self._mvadistributions[idname] = rt.TList()
                #for each MVA discriminant in the list
                for mvaname in self._tmva_discriminator_names:
                        self.fill_tmvadistributions(tree,idname,mvaname)

        @log_with()
        def fill_craneendistributions(self,tree,idname,mvaname):
                #create entry list to get mininimum and maximum
                # if mva discriminant for selected events only
                cuts = 'nJets==10'
                tree.Draw(">>elist", cuts, "entrylist")
                elist = rt.gDirectory.Get("elist")
                tree.SetEntryList(elist)
                min = tree.GetMinimum(mvaname)
                max = tree.GetMaximum(mvaname)
                # mva' = (mva-min)/(max-min)*(max'-min') + min'
                rescaled_mva = '({}-{})/({}-{})*(1. - (-1)) + (-1.)'.format(mvaname,min,max,min)

                histname = "h_{}_{}".format(idname,mvaname)
                histconfig = "{}{}".format(histname,self._histconfig)

                tree.Draw("{}>>{}".format(rescaled_mva,histconfig),cuts)
                hist = rt.gDirectory.Get(histname)
                rt.SetOwnership( hist, False )
                if hist:
                        # hist.Scale(1./hist.Integral())
                        self._mvadistributions[idname].AddLast(hist)

        @log_with()
        def get_hist_from_craneen_file(self,idname):
                filename = self._jsondic[idname]
                if not filename:
                        logging.error("File name is wrong: {}".format(filename))
                        sys.exit(1)
                rootfile = rt.TFile.Open(filename,"READ")
                rt.SetOwnership(rootfile,False)
                tree = rootfile.Get(self._craneen_tree_name)
                self._mvadistributions[idname] = rt.TList()
                for mvaname in self._craneen_discriminator_names:
                        self.fill_craneendistributions(tree,idname,mvaname)

        @log_with()
        def get_signal_and_bg_from_craneens(self):
                self._mvadistributions['oldmva'] = rt.TList()
                self.get_hist_from_craneen_file('tttt')
                hist_tttt = self._mvadistributions['tttt'].FindObject('h_tttt_BDT9and10jetsplitNoNjw')
                self._mvadistributions['oldmva'].AddLast(hist_tttt)
                hist_tttt.Scale(1./hist_tttt.Integral())

                self.get_hist_from_craneen_file('tt')
                self.get_hist_from_craneen_file('ttz')
                self.get_hist_from_craneen_file('tth')
                hist_total_bg = self._mvadistributions['tt'].FindObject('h_tt_BDT9and10jetsplitNoNjw').Clone('hist_total_bg')
                rt.SetOwnership(hist_total_bg,False)
                hist_total_bg.Reset()
                hist_total_bg.Add(self._mvadistributions['ttz'].FindObject('h_ttz_BDT9and10jetsplitNoNjw'))
                hist_total_bg.Add(self._mvadistributions['tth'].FindObject('h_tth_BDT9and10jetsplitNoNjw'))
                hist_total_bg.Scale(1./hist_total_bg.Integral())
                self._mvadistributions['oldmva'].AddLast(hist_total_bg)

        def set_ttz_cran(self,filename):
                self.rootfile_ttz_cran = rt.TFile.Open(filename,"READ")
        def set_tth_cran(self,filename):
                self.rootfile_tth_cran = rt.TFile.Open(filename,"READ")
        def set_tttt_cran(self,filename):
                self.rootfile_tttt_cran = rt.TFile.Open(filename,"READ")

class Style(object):
        def __init__(self, config_json, model):
                self._json = config_json
                self._model = model
        model = property(None,None)

        @log_with()
        def decorate_model(self):
                print 'Decorating model'

                for el in self._model._mvadistributions['tmva']:
                        el.SetLineWidth(2)
                        if 'total_bg' in el.GetName(): el.SetLineColor(rt.kBlue)
                        elif 'tttt' in el.GetName(): el.SetLineColor(rt.kRed+2)

                for el in self._model._mvadistributions['oldmva']:
                        el.SetLineWidth(2)
                        el.SetLineStyle(2)
                        if 'tttt' in el.GetName(): el.SetLineColor(rt.kRed+2)
                        elif 'total_bg' in el.GetName(): el.SetLineColor(rt.kBlue)

        @log_with()
        def decorate_stack(self, stack):
                print 'Decorating stack'
                stack.SetTitle(';MVA discriminant; 1/N dN/dMVA')
                stack.GetYaxis().SetTitleOffset(1.5)

        @log_with()
        def make_legend(self,c):
                legend = rt.TLegend(0.7,0.89,0.99,0.99)
                rt.SetOwnership(legend,False)
                legend.SetBorderSize(0)
                legend.SetHeader('nJets==10')
                legend.AddEntry(self._model._mvadistributions['tmva'].FindObject(self._model._usedhists['tmva_s']),\
                                "New MVA (t#bar{t}t#bar{t})",'lf')
                legend.AddEntry(self._model._mvadistributions['tmva'].FindObject(self._model._usedhists['tmva_b']),\
                                "New MVA (t#bar{t}+t#bar{t}Z+t#bar{t}H)",'lf')
                legend.AddEntry(self._model._mvadistributions['oldmva'].FindObject(self._model._usedhists['old_s']),\
                                "Default MVA (t#bar{t}t#bar{t})",'lf')
                legend.AddEntry(self._model._mvadistributions['oldmva'].FindObject(self._model._usedhists['old_b']),\
                                "Default MVA (t#bar{t}+t#bar{t}Z+t#bar{t}H)",'lf')
                c.cd()
                legend.Draw()
        @log_with()
        def decorate_canvas(self, canvas):
                print 'Decorating canvas'
                canvas.SetLeftMargin(1.1)
                self.make_legend(canvas.GetPad(1))
                canvas.SetLogy()
                canvas.Update()

class View(object):
        def __init__(self):
                self._model = None
                self._style = None
                self._outfilename = 'out'
                self._outfileextension = 'png'

        def set_style(self,style):
                self._style = style

        style = property(None,set_style)

        def set_model(self,model):
                self._model = model
        def set_outfilename(self,filename):
                if filename: self._outfilename = filename
        def set_extension(self,extension):
                self._outfileextension = extension
        def get_outfile_name(self):
                return '{}.{}'.format(self._outfilename,self._outfileextension)
        def draw(self):
                c = rt.TCanvas('c','cms',5,45,800,400)
                c.Divide(2,1)
                # for el in self._model._mvadistributions: self._model._mvadistributions[el].Print()
                if self._style: self._style.decorate_model()

                h_stack = rt.THStack()
                if 'tmva' in self._model._mvadistributions:
                        h_stack.Add(self._model._mvadistributions['tmva'].FindObject(self._model._usedhists['tmva_b']),"hist")
                        h_stack.Add(self._model._mvadistributions['tmva'].FindObject(self._model._usedhists['tmva_s']),"hist")
                if 'oldmva' in self._model._mvadistributions:
                        h_stack.Add(self._model._mvadistributions['oldmva'].FindObject(self._model._usedhists['old_s']),"hist")
                        h_stack.Add(self._model._mvadistributions['oldmva'].FindObject(self._model._usedhists['old_b']),"hist")
                # h_stack.Add(self._model._mvadistributions['tt'].FindObject('h_tt_BDT9and10jetsplitNoNjw'),"hist")
                # h_stack.Add(self._model._mvadistributions['ttz'].FindObject('h_ttz_BDT9and10jetsplitNoNjw'),"hist")
                # h_stack.Add(self._model._mvadistributions['tth'].FindObject('h_tth_BDT9and10jetsplitNoNjw'),"hist")
                c.cd(1)
                h_stack.Draw("nostack")

                c.cd(2)
                mg = rt.TMultiGraph()
                mg.Add(self._model._mva_roc_curves['tmva'],"*")
                mg.Add(self._model._mva_roc_curves['oldmva'],"c")
                mg.Draw("A")

                if self._style: self._style.decorate_stack(h_stack)
                if self._style: self._style.decorate_canvas(c)

                c.SaveAs(self.get_outfile_name())

def main(arguments):

        # Enforce no garbage collection
        rt.TCanvas.__init__._creates = False
        rt.TFile.__init__._creates = False
	rt.TH1.__init__._creates = False
	rt.TH2.__init__._creates = False
        rt.TList.__init__._creates = False
        rt.TCollection.__init__._creates = False
        rt.TIter.__init__._creates = False

        #Load configuration .json file
        jsondic = None
        with open(arguments.config_json) as json_data:
                jsondic = json.load(json_data)
                logging.debug(pp.pformat(jsondic))

        model = MVADistributions(jsondic)

        style = Style(jsondic,model)

        view = View()
        view.set_model(model)
        view.set_style(style)
        view.set_outfilename(arguments.outfile)
        view.set_extension(arguments.extension)
        view.draw()

        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('-o', '--outfile', help="Output file")
        parser.add_argument('-e', '--extension', help="Plot file extension (.C, .root, .png, .pdf)", default='png')
        parser.add_argument('-j', '--config-json', help="JSON configuration file", required=True)
        parser.add_argument('-b', help="ROOT batch mode", dest='isBatch', action='store_true')
        parser.add_argument(
                        '-d', '--debug',
                        help="Print lots of debugging statements",
                        action="store_const", dest="loglevel", const=logging.DEBUG,
                        default=logging.WARNING,
                        )
        parser.add_argument(
                        '-v', '--verbose',
                        help="Be verbose",
                        action="store_const", dest="loglevel", const=logging.INFO,
                        )

        args = parser.parse_args(sys.argv[1:])

        print(args)

        logging.basicConfig(level=args.loglevel)

        logging.info( time.asctime() )
        exitcode = main(args)
        logging.info( time.asctime() )
        logging.info( 'TOTAL TIME IN MINUTES:' + str((time.time() - start_time) / 60.0))
        sys.exit(exitcode)
