#!/usr/bin/env python

"""
A simple python script template.
"""

import os
import sys
import time
import shutil
import argparse
import logging
import json
import textwrap
import pprint as pp
from prettytable import  PrettyTable
from prettytable import MSWORD_FRIENDLY
import ROOT as rt

import functools, logging

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class log_with(object):
    '''Logging decorator that allows you to log with a specific logger.'''
    # Customize these messages
    ENTRY_MESSAGE = 'Entering {}'
    EXIT_MESSAGE = 'Exiting {}'

    def __init__(self, logger=logging):
        self.logger = logger

    def __call__(self, func):
        '''Returns a wrapper that wraps func. The wrapper will log the entry and exit points of the function with logging.INFO level.'''
        # set logger if it was not set earlier
        if not self.logger:
            logging.basicConfig()
            self.logger = logging.getLogger(func.__module__)
            # self.logger.setLevel(logging.DEBUG)

        @functools.wraps(func)
        def wrapper(*args, **kwds):
            self.logger.debug(self.ENTRY_MESSAGE.format(func.__name__))  # logging level .info(). Set to .debug() if you want to
            f_result = func(*args, **kwds)
            self.logger.debug(self.EXIT_MESSAGE.format(func.__name__))   # logging level .info(). Set to .debug() if you want to
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
                self._objects = {}
                self._mvadistributions = {}
                self._mva_roc_curves = {}
                #self._tmva_discriminator_names = ['BDTGSIG500','BDTGSIG20',\
                #        'BDTASIG500','BDTASIG20',\
                #        'BDTA500','BDTA20',\
                #        'BDTG500','BDTG20']
                self._histconfig = {"nbins":25,	"xmin":-1.0, "xmax":1.0}
                if 'histconfig' in self._jsondic:
                        self._histconfig = self._jsondic['histconfig']
                self._annotation = 'Performance comparision of different MVA discriminants'
                if 'annotation' in self._jsondic:
                        self._annotation = self._jsondic['annotation']
                self.Initialize()

        @log_with()
        def Initialize(self):
                pass

        @log_with()
        def get(self,name):
                if name in self._objects:
                        return self._objects[name]
                else:
                        if 'tmva_b' in name:
                                self._objects[name] = self.build_tmva(name)
                        elif 'tmva_s' in name:
                                self._objects[name] = self.build_tmva(name)
                        elif 'old_b' in name:
                                self._objects[name] = self.build_old_b(name)
                        elif 'old_s' in name:
                                self._objects[name] = self.build_old_s(name)
                        elif 'roc' in name:
                                self._objects[name] = self.build_roc(name)
                return self._objects[name]

        @log_with()
        def build_roc_tmva(self):
                self._mva_roc_curves['tmva'] = rt.TGraph()
                self._mva_roc_curves['tmva'].SetName('roc_tmva')
                hb = self.get('tmva_b')
                hs = self.get('tmva_s')
                nbins = hb.GetNbinsX()
                for iBin in range(1,nbins+1):
                        esp_sig = (hs.Integral(iBin,nbins)/hs.Integral(1,nbins))
                        esp_bg = (hb.Integral(iBin,nbins)/hb.Integral(1,nbins))
                        self._mva_roc_curves['tmva'].SetPoint(iBin-1,esp_sig,1.-esp_bg)
                return self._mva_roc_curves['tmva']

        @log_with()
        def build_roc(self,name):
                #default mva
                logging.debug("ROC name: {}".format(name))
                self._mva_roc_curves[name] = rt.TGraph()
                self._mva_roc_curves[name].SetName(name)
                hist_bg_name = self._jsondic[name]['histbgname']
                hist_sg_name = self._jsondic[name]['histsgname']
                hb = self.get(hist_bg_name)
                logging.debug("hist_bg_name: {}\n{}".format(self._jsondic[name]['histbgname'],hb))
                hs = self.get(hist_sg_name)
                logging.debug("hist_sg_name: {}\n{}".format(self._jsondic[name]['histsgname'],hs))
                nbins = hb.GetNbinsX()
                for iBin in range(1,nbins+1):
                        esp_sig = (hs.Integral(iBin,nbins)/hs.Integral(1,nbins))
                        esp_bg = (hb.Integral(iBin,nbins)/hb.Integral(1,nbins))
                        self._mva_roc_curves[name].SetPoint(iBin-1,esp_sig,1.-esp_bg)
                return self._mva_roc_curves[name]

        @log_with()
        def build_tmva(self,histname):
                idname = 'tmva'
                filename = self._jsondic[histname]['inputfile']
                if not filename:
                        logging.error("File name is wrong: {}".format(filename))
                        sys.exit(1)
                rootfile = rt.TFile.Open(filename,"READ")
                rt.SetOwnership(rootfile,False)
                # tree = rootfile.Get(self._tmva_tree_name)
                tree = rootfile.Get(str(self._jsondic[histname]['treename']))
                if not tree:
                        logging.error("Tree does not exist: {}".format(tree))
                        sys.exit(1)
                #for each MVA discriminant in the list
                mvaname = self._jsondic[histname]['mvaname']
                min = tree.GetMinimum(mvaname)
                max = tree.GetMaximum(mvaname)
                logging.debug("MIN/MAX {}: {}/{}".format(mvaname,min,max))
                # rescale to [-1.,1.] range
                # mva' = (mva-min)/(max-min)*(max'-min') + min'
                rescaled_mva = '(({}-{})/({}-{})*({} - {}) + {})'.format(mvaname,min,max,min,\
                                self._histconfig['xmax'],self._histconfig['xmin'],self._histconfig['xmin'])
                #signal histograms
                # histname = 'tmva_s'
                drawhistconfig = "({},{},{})".format(self._histconfig['nbins'],self._histconfig['xmin'],self._histconfig['xmax'])
                histexpression = "{}{}".format(histname,drawhistconfig) #e.g h_tttt_BDTA20(25,-1.,1.)
                sg_cuts = self._jsondic[histname]['cuts']  #signal events from tmva tree
                logging.debug("Tree draw command: {}".format(histexpression))
                logging.debug("Tree cuts: {}".format(sg_cuts))
                tree.Draw("{}>>{}".format(rescaled_mva,histexpression),sg_cuts)
                hist = rt.gDirectory.Get(str(histname))
                rt.SetOwnership( hist, False )
                if hist:
                        hist.Scale(1./hist.Integral())
                        return hist

        @log_with()
        def fill_craneendistributions(self,tree,idname,mvaname,cuts):
                #create entry list to get mininimum and maximum
                # if mva discriminant for selected events only
                tree.Draw(">>elist", cuts, "entrylist")
                elist = rt.gDirectory.Get("elist")
                tree.SetEntryList(elist)
                min = tree.GetMinimum(mvaname)
                max = tree.GetMaximum(mvaname)
                # mva' = (mva-min)/(max-min)*(max'-min') + min'
                rescaled_mva = '(({}-{})/({}-{})*({} - {}) + {})'.format(mvaname,min,max,min,\
                                                                self._histconfig['xmax'],self._histconfig['xmin'],self._histconfig['xmin'])
                logging.debug(rescaled_mva)
                histname = "h_{}_{}".format(idname,mvaname)
                drawhistconfig = "({},{},{})".format(self._histconfig['nbins'],self._histconfig['xmin'],self._histconfig['xmax'])
                histexpression = "{}{}".format(histname,drawhistconfig)
                tree.Draw("{}>>{}".format(rescaled_mva,histexpression),cuts)
                hist = rt.gDirectory.Get(histname)
                rt.SetOwnership( hist, False )
                if hist:
                        # hist.Scale(1./hist.Integral())
                        self._mvadistributions[idname].AddLast(hist)

        @log_with()
        def get_hist_from_craneen_file(self,configuration):
                idname = configuration['idname']
                filename = configuration['inputfile']
                cuts = configuration['cuts']
                if not filename:
                        logging.error("File name is wrong: {}".format(filename))
                        sys.exit(1)
                rootfile = rt.TFile.Open(filename,"READ")
                rt.SetOwnership(rootfile,False)
                tree = rootfile.Get(str(configuration['treename']))
                self._mvadistributions[idname] = rt.TList()
                mvaname = configuration['mvaname']
                self.fill_craneendistributions(tree,idname,mvaname,cuts)

        @log_with()
        def build_old_s(self,histname):
                if 'oldmva' not in self._mvadistributions: self._mvadistributions['oldmva'] = rt.TList()
                self.get_hist_from_craneen_file(self._jsondic[histname]['tttt'])
                hist_tttt = self._mvadistributions['tttt'].FindObject('h_tttt_BDT9and10jetsplitNoNjw')
                hist_tttt = hist_tttt.Clone(histname)
                hist_tttt.Scale(1./hist_tttt.Integral())
                return hist_tttt

        @log_with()
        def build_old_b(self,histname):
                self.get_hist_from_craneen_file(self._jsondic['old_b']['tt'])
                self.get_hist_from_craneen_file(self._jsondic['old_b']['ttz'])
                self.get_hist_from_craneen_file(self._jsondic['old_b']['tth'])
                hist_total_bg = self._mvadistributions['tt'].FindObject('h_tt_BDT9and10jetsplitNoNjw').Clone(histname)
                rt.SetOwnership(hist_total_bg,False)
                hist_total_bg.Reset()
                hist_total_bg.Add(self._mvadistributions['ttz'].FindObject('h_ttz_BDT9and10jetsplitNoNjw'))
                hist_total_bg.Add(self._mvadistributions['tth'].FindObject('h_tth_BDT9and10jetsplitNoNjw'))
                hist_total_bg.Scale(1./hist_total_bg.Integral())
                return hist_total_bg

class Style(object):
        def __init__(self, config_json, model):
                self._json = config_json
                self._model = model
        model = property(None,None)

        @log_with()
        def decorate(self,obj):
                name = obj.GetName()
                obj.SetLineWidth(2)
                if name in self._json:
                        if 'linecolor' in self._json[name]: obj.SetLineColor(self._json[name]['linecolor'])
                        if 'linestyle' in self._json[name]: obj.SetLineStyle(self._json[name]['linestyle'])
                return obj

        @log_with()
        def decorate_stack(self, stack):
                stack.SetTitle(';MVA discriminant; 1/N dN/dMVA')
                stack.GetYaxis().SetTitleOffset(0.7)
                stack.GetXaxis().SetLabelSize(.082)
                # stack.GetYaxis().SetLabelSize(.082)
                stack.GetXaxis().SetTitleSize(.082)
                stack.GetYaxis().SetTitleSize(.082)

        @log_with()
        def decorate_roc_mg(self,mg):
                mg.SetTitle(';Signal efficiency;Background rejection')
                mg.GetYaxis().SetTitleOffset(0.7)
                mg.GetXaxis().SetLabelSize(.082)
                # mg.GetYaxis().SetLabelSize(.082)
                mg.GetXaxis().SetTitleSize(.082)
                mg.GetYaxis().SetTitleSize(.082)

        @log_with()
        def make_legend(self,c,objlist,**kwargs):
                header=kwargs.get('header',None)
                pos=kwargs.get('pos',(0.25,0.23,0.55,0.6))
                legend = rt.TLegend(*pos)
                legend.SetName("TLeg_"+c.GetName())
                rt.SetOwnership(legend,False)
                legend.SetBorderSize(0)
                if header: legend.SetHeader(header)
                for el in objlist:
                        legend.AddEntry(self._model.get(el),self._json[el]['legend']['name'],self._json[el]['legend']['style'])
                c.cd()
                legend.Draw()

        @log_with()
        def decorate_pad(self, pad):
                pad.SetBottomMargin(0.2)
                pad.SetLeftMargin(0.2)
                pad.SetRightMargin(0.05)
                # pad.SetLogy()
                pad.Update()

        @log_with()
        def decorate_canvas(self, canvas):
                canvas.SetLeftMargin(1.1)
                canvas.SetRightMargin(0.1)
                # canvas.SetLogy()
                canvas.Update()

class View(object):
        @log_with()
        def __init__(self):
                self._model = None
                self._style = None
                self._outfilename = 'out'
                self._outfileextension = 'png'
                self._outputfolder = '.'
        @log_with()
        def set_style(self,style):
                self._style = style
        @log_with()
        def set_model(self,model):
                self._model = model
        @log_with()
        def set_outfilename(self,filename):
                if filename: self._outfilename = filename
        @log_with()
        def set_extension(self,extension):
                self._outfileextension = extension
        @log_with()
        def set_outputfolder(self,folder):
                self._outputfolder = folder
                if not os.path.exists(folder):
                        os.makedirs(folder)
        @log_with()
        def get_outfile_name(self):
                return '{}/{}.{}'.format(self._outputfolder,self._outfilename,self._outfileextension)
        @log_with()
        def draw(self):
                c = rt.TCanvas('c','cms',5,45,800,800)
                c.Divide(2,3,0.,0.)

                c.cd(1)
                h_stack = rt.THStack("MVAs1","")
                objlist = ['tmva_b','tmva_s','old_b','old_s']
                for el in objlist:
                        h_stack.Add(self._style.decorate(self._model.get(el)),"hist")
                h_stack.Draw("nostack")
                if self._style:
                        self._style.decorate_stack(h_stack)
                        self._style.decorate_pad(c.GetPad(1))

                c.cd(2)
                mg = rt.TMultiGraph("ROCs1","")
                objlist = ['roc_tmva','roc_tmva_train','roc_oldmva_mu','roc_oldmva_el']
                for el in objlist:
                        mg.Add(self._style.decorate(self._model.get(el)),"c")
                mg.Draw("A")
                if self._style:
                        self._style.decorate_roc_mg(mg)
                        self._style.make_legend(c.GetPad(2),objlist,header='nMtag = 2')
                        self._style.decorate_pad(c.GetPad(2))

                c.cd(3)
                h_stack = rt.THStack("MVAs2","")
                objlist = ['2tmva_b','2tmva_s','2old_b','2old_s']
                for el in objlist:
                        h_stack.Add(self._style.decorate(self._model.get(el)),"hist")
                h_stack.Draw("nostack")
                if self._style:
                        self._style.decorate_stack(h_stack)
                        self._style.decorate_pad(c.GetPad(3))

                c.cd(4)
                mg = rt.TMultiGraph("ROCs2","")
                objlist = ['2roc_tmva','2roc_tmva_train','2roc_oldmva_mu','2roc_oldmva_el']
                for el in objlist:
                        mg.Add(self._style.decorate(self._model.get(el)),"c")
                mg.Draw("A")
                if self._style:
                        self._style.decorate_roc_mg(mg)
                        self._style.make_legend(c.GetPad(4),objlist,header='nMtag = 3')
                        self._style.decorate_pad(c.GetPad(4))

                c.cd(5)
                h_stack = rt.THStack("MVAs3","")
                objlist = ['3tmva_b','3tmva_s','3old_b','3old_s']
                for el in objlist:
                        h_stack.Add(self._style.decorate(self._model.get(el)),"hist")
                h_stack.Draw("nostack")
                if self._style:
                        self._style.decorate_stack(h_stack)
                        self._style.decorate_pad(c.GetPad(5))
                        self._style.make_legend(c.GetPad(5),objlist,pos=(0.25,0.65,0.65,0.89))

                c.cd(6)
                mg = rt.TMultiGraph("ROCs3","")
                objlist = ['3roc_tmva','3roc_tmva_train','3roc_oldmva_mu','3roc_oldmva_el']
                for el in objlist:
                        mg.Add(self._style.decorate(self._model.get(el)),"c")
                mg.Draw("A")
                if self._style:
                        self._style.decorate_roc_mg(mg)
                        self._style.make_legend(c.GetPad(6),objlist,header='nMtag #geq 4')
                        self._style.decorate_pad(c.GetPad(6))                        

                if self._style: self._style.decorate_canvas(c)
                c.SaveAs(self.get_outfile_name())
        @log_with()
        def annotate(self,type,config):
                if type == "screen":
                        bright_green_text = "\033[1;32;40m"
                        normal_text = "\033[0;37;40m"
                        print "\n".join(textwrap.wrap(bcolors.OKBLUE+
                                  self._model._annotation.encode('ascii')+
                                  bcolors.ENDC, 120))
                        if os.path.exists(self._outputfolder):
                                shutil.copy2(config,self._outputfolder)
                elif type == "tex":
                        logging.warning("Annotation format: {}. Not implemented yet!".format(type))
                elif type == "md":
                        logging.warning("Annotation format: {}. Not implemented yet!".format(type))
                else:
                        logging.error("Annotation format not recognized: {}".format(type))

def main(arguments):

        # Disable garbage collection for this list of objects
        rt.TCanvas.__init__._creates = False
        rt.TFile.__init__._creates = False
	rt.TH1.__init__._creates = False
	rt.TH2.__init__._creates = False
        rt.THStack.__init__._creates = False
        rt.TGraph.__init__._creates = False
        rt.TMultiGraph.__init__._creates = False
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
        view.set_outputfolder(arguments.dir)
        view.set_outfilename(arguments.outfile)
        view.set_extension(arguments.extension)
        view.draw()
        if arguments.annotation_format:
                view.annotate(arguments.annotation_format,arguments.config_json)

        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('-o', '--outfile', help="Output file")
        parser.add_argument('-e', '--extension', help="Plot file extension (.C, .root, .png, .pdf)", default='png')
        parser.add_argument('--dir', help="Result output directory", default='.')
        parser.add_argument('-j', '--config-json', help="JSON configuration file", required=True)
        parser.add_argument('-a', '--annotation_format', default="screen",\
                            help="Print annotation in given format (screen, tex, md)")
        parser.add_argument('--no-annotation', dest='annotation_format', action='store_false',\
                                                help="Disable annotating")
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
