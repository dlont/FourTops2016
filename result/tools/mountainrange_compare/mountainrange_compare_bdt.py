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
import tempfile
import pprint as pp
from prettytable import  PrettyTable
from prettytable import MSWORD_FRIENDLY
import ROOT as rt
import numpy as np
import mountainrange.mountainrange_pub_utilities as mr
import autobinning as ab


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

class Model(object):
        def __init__(self,jsondic):
                self._jsondic = jsondic
                self._objects = {}
                self._binning = {}
                self._ob = None
                self._annotation = 'Performance comparision of different MVA discriminants'
                if 'annotation' in self._jsondic:
                        self._annotation = self._jsondic['annotation']
                self.Initialize()

        @log_with()
        def Initialize(self):
                # self._ob = ab.OprimizedBinning(None) # for mass and width variations
                self._ob = ab.EquiProbableBinning()
                self._ob.nbins=10
                pass

        @log_with()
        def get(self,name):
                """
                Factory method
                """
                if name in self._objects:
                        return self._objects[name]
                elif '_longhist' in name:
                        self._objects[name] = self.build_mr_hist(name)
                else:
                        self._objects[name] = self.build_hist(name)
                return self._objects[name]

        @log_with()
        def get_tree(self,filename,treename):
                filenames = filename.split(",")
                chain = rt.TChain(treename)
                for name in filenames:
                        logging.debug(name)
                        chain.Add(name)
                rt.SetOwnership(chain,False)
                return chain

        @log_with()
        def build_mr_hist(self,objname):
            filename = str(self._jsondic[objname]['inputfile'])
            treename = str(self._jsondic[objname]['treename'])
            tree = self.get_tree(filename, treename)
            varname = self._jsondic[objname]['varname']
            baselinecut = self._jsondic[objname]['cut']
            list_of_short_histograms = []
            for extra_cut in self._jsondic[objname]['mrcuts']:
                cut = "&&".join([baselinecut,extra_cut])
                short_hist = self.build_hist_from_cut(objname, tree, varname, cut, True)
                list_of_short_histograms.append(short_hist)
        
            logging.debug("list of short histograms: {}".format(pp.pformat(list_of_short_histograms)))
            nbins = mr.get_total_nbins_from_list(list_of_short_histograms) #modify function interface
            hist_master = rt.TH1F(objname,"",nbins,0.5,float(nbins+0.5))
            hist_master, ignore = mr.fillsingle_from_list(hist_master,list_of_short_histograms)  #modify function interface
            hist_master.Scale(1./hist_master.Integral())
            return hist_master

        @log_with()
        def build_hist_from_cut(self,objname,tree,varname,cut,predefinedhistconfig=False):
                objname += '_{}'.format(next(tempfile._get_candidate_names()))
                if not predefinedhistconfig:
                        min = tree.GetMinimum(varname)
                        max = tree.GetMaximum(varname)
                        nbins = self.get_n_bins_sturges(tree,varname,min,max)
                        drawhistconfig = "({},{},{})".format(nbins,min,max)
                        histexpression = "{}{}".format(objname,drawhistconfig) #e.g h_tttt_BDTA20(25,-1.,1.)
                        logging.debug("Tree draw command: {}".format(histexpression))
                        logging.debug("Tree cut: {}".format(cut))
                        tree.Draw("{}>>{}".format(varname,histexpression),cut)
                        hist = rt.gDirectory.Get(str(objname))
                        hist.Sumw2()
                else:
                        print self._binning
                        print cut.split('&&')
                        h = self._binning['&&'.join(cut.split('&&')[-2:])]['hist'].Clone(objname)
                        histexpression = objname
                        logging.debug("Tree draw command: {}".format(histexpression))
                        logging.debug("Tree cut: {}".format(cut))
                        tree.Draw("{}>>{}".format(varname,histexpression),cut)
                        hist = rt.gDirectory.Get(str(objname))
                        hist.Sumw2()
                        for ibin in range(1,hist.GetNbinsX()+1):
                                hist.SetBinContent(ibin,hist.GetBinContent(ibin)/hist.GetBinWidth(ibin))
                                hist.SetBinError(ibin,hist.GetBinError(ibin)/hist.GetBinWidth(ibin))
                hist = rt.gDirectory.Get(str(objname))
                rt.SetOwnership( hist, False )
                if hist:
                        hist.Scale(1./hist.Integral())
                        return hist

        @log_with()
        def build_hist(self,objname):
                logging.debug(pp.pformat(objname))
                filename = str(self._jsondic[objname]['inputfile'])
                treename = str(self._jsondic[objname]['treename'])
                tree = self.get_tree(filename, treename)
                varname = self._jsondic[objname]['varname']
                min = tree.GetMinimum(varname)
                max = tree.GetMaximum(varname)
                nbins = self.get_n_bins_sturges(tree,varname,min,max)
                drawhistconfig = "({},{},{})".format(nbins,min,max)
                histexpression = "{}{}".format(objname,drawhistconfig) #e.g h_tttt_BDTA20(25,-1.,1.)
                cut = self._jsondic[objname]['cut']  #signal events from tmva tree
                logging.debug("Tree draw command: {}".format(histexpression))
                logging.debug("Tree cut: {}".format(cut))
                tree.Draw("{}>>{}".format(varname,histexpression),cut)
                hist = rt.gDirectory.Get(str(objname))
                rt.SetOwnership( hist, False )
                if hist:
                        hist.Scale(1./hist.Integral())
                        return hist
        @log_with()
        def get_n_bins_scott(self,tree,var,min,max):
                nentries = tree.Draw(var,'','goff')
                vec = tree.GetV1()
                npvec = np.array([vec[i] for i in range(0,nentries)])
                sigma = np.std(npvec)
                bin_width = 3.5*sigma/(nentries)**0.3333333
                nbins = 2*(max - min)/bin_width
                logging.debug('bin width/nbins:{}/{}'.format(bin_width,nbins))
                return int(nbins)

        @log_with()
        def get_n_bins_sturges(self,tree,var,min,max):
                nentries = tree.Draw(var,'','goff')
                nbins = 2*rt.TMath.Log2(nentries)
                bin_width = (max - min)/nbins
                logging.debug('bin width/nbins:{}/{}'.format(bin_width,nbins))
                return int(nbins)

class Style(object):
        def __init__(self, config_json, model):
                self._json = config_json
                self._model = model
        model = property(None,None)

        @log_with()
        def decorate(self,obj):
                """
                Decorate obeject of the model.
                Assumes Drawable object from ROOT
                """
                name = obj.GetName()
                obj.SetLineWidth(2)
                if name in self._json:
                        if 'linecolor' in self._json[name]: obj.SetLineColor(self._json[name]['linecolor'])
                        if 'linestyle' in self._json[name]: obj.SetLineStyle(self._json[name]['linestyle'])
                return obj
        
        @log_with()
        def decorate_ratio_stack(self, stack, **kwargs):
                stack.GetYaxis().SetTitleOffset(1.1)
                title = kwargs.get('title','')
                xtitle = kwargs.get('xtitle','')
                ytitle = kwargs.get('ytitle','')
                stack.SetTitle(title)
                stack.GetXaxis().SetTitle(xtitle)
                stack.GetYaxis().SetTitle(ytitle)


        @log_with()
        def decorate_stack(self, stack, **kwargs):
                stack.GetYaxis().SetTitleOffset(1.1)
                # stack.GetXaxis().SetLabelSize(.082)
                # stack.GetYaxis().SetLabelSize(.082)
                # stack.GetXaxis().SetTitleSize(.082)
                # stack.GetYaxis().SetTitleSize(.082)
                title = kwargs.get('title','')
                xtitle = kwargs.get('xtitle','')
                ytitle = kwargs.get('ytitle','')
                stack.SetTitle(title)
                stack.GetXaxis().SetTitle(xtitle)
                stack.GetYaxis().SetTitle(ytitle)

        @log_with()
        def decorate_graph(self,mg):
                pass

        @log_with()
        def add_legend_entry(self,legend,entrytitle,entryoption,object=None):
                legend.AddEntry(object,entrytitle,entryoption)
                legend.Draw()
                
        @log_with()
        def make_legend(self,c,objlist,**kwargs):
                header=kwargs.get('header',None)
                pos=kwargs.get('pos',(0.8,0.75,0.99,0.99))
                legend = rt.TLegend(*pos)
                legend.SetName("TLeg_"+c.GetName())
                rt.SetOwnership(legend,False)
                legend.SetBorderSize(0)
                if header: legend.SetHeader(header)
                for el in objlist:
                        legend.AddEntry(self._model.get(el),self._json[el]['legend']['name'],self._json[el]['legend']['style'])
                c.cd()
                legend.Draw()
                return legend

        @log_with()
        def decorate_pad(self, pad, islog):
                pad.SetBottomMargin(0.2)
                pad.SetLeftMargin(0.2)
                pad.SetRightMargin(0.05)
                pad.SetLogy(islog)
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
        def get_outfile_name(self,substring=''):
                for ext in self._outfileextension.split(","):
                        yield '{}/{}{}.{}'.format(self._outputfolder,self._outfilename,substring,ext)

        @log_with()
        def annotate(self,type,config):
                if type == "screen":
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

        @log_with()
        def decorate(self,obj):
                if self._style: return self._style.decorate(obj)
                else: return obj

        @log_with()
        def build_ratio_pad(self, c, ipad, pad, ratio_hist_name):
                c.cd(ipad+1) #root pad numeration starts from 1
                denominator_hist = self._model.get(ratio_hist_name)
                hs = rt.THStack("hsPad{}".format(ipad),"")
                for objname in pad['objects']:
                        ratio_hist = self._model.get(objname).Clone(objname+'_ratio')
                        rt.SetOwnership(ratio_hist,False)
                        ratio_hist.Divide(denominator_hist)
                        hs.Add(ratio_hist,"h")
                hs.Draw("nostack")
                islog=pad.get('islog',False)
                if self._style: 
                        last_histogram_name = hs.GetHists().First().GetName()
                        self._style.decorate_ratio_stack(hs,ytitle='ratio')
                        self._style.decorate_pad(c.GetPad(ipad+1),islog)

        @log_with()
        def build_normal_pad(self, c, ipad, pad):
                c.cd(ipad+1) #root pad numeration starts from 1

                #find optimal binning for objects on the pad
                for cut in self._model._jsondic[pad['objects'][0]]['mrcuts']:
                        self._model._binning[cut]={'nbins':-1,'hist':None}
                        for objname in pad['objects']:
                                filename=self._model._jsondic[objname]['inputfile']
                                treename=self._model._jsondic[objname]['treename']
                                varname=self._model._jsondic[objname]['varname']
                                selection=self._model._jsondic[objname]['cut']
                                tree=self._model.get_tree(filename,treename)
                                nev = tree.Draw(varname,selection+'&&'+cut,'goff')
                                enries_buf = tree.GetVal(0)
                                enries_vec = np.array([enries_buf[i] for i in range(0,nev)])
                                enries_vec.sort()
                                self._model._ob._vec=enries_vec
                                h = self._model._ob.get_histogram(cut)
                                nbins = h.GetNbinsX()
                                if nbins>self._model._binning[cut]['nbins']:
                                        self._model._binning[cut]['nbins']=nbins
                                        self._model._binning[cut]['hist']=h
                                        rt.SetOwnership(h,False)
                        
                #make stack plot with optimized binning
                hs = rt.THStack("hsPad{}".format(ipad),"")
                for objname in pad['objects']:
                        hs.Add(self.decorate(self._model.get(objname)),"h")
                hs.Draw("nostack")
                islog=pad.get('islog',False)
                if self._style: 
                        last_histogram_name = hs.GetHists().First().GetName()
                        self._style.decorate_stack(hs,title=self._model._jsondic[last_histogram_name]['title'])
                        self._style.decorate_pad(c.GetPad(ipad+1),islog)
                        leg = self._style.make_legend(c.GetPad(ipad+1),pad['objects'],pos=(0.1,0.05,0.3,0.25))
                        KSprob = self._model.get(pad['objects'][0]).KolmogorovTest(self._model.get(pad['objects'][1]))
                        # ADprob = self._model.get(pad['objects'][0]).AndersonDarlingTest(self._model.get(pad['objects'][1]))
                        # self._style.add_legend_entry(leg,"KS prob: {}".format(KSprob),"")
                        # self._style.add_legend_entry(leg,"AD prob: {}".format(ADprob),"")
        @log_with()
        def draw(self):

                for canv in self._model._jsondic['canvas']:
                        logging.debug(pp.pformat(canv))
                        name = canv['name']
                        nx,ny = canv.get('nx',1),canv.get('ny',1)
                        c = rt.TCanvas(name,'cms',5,45,800,800)
                        c.Divide(nx,ny)
                        for ipad, pad in enumerate(canv['pads']):
                                if 'ratio_to' not in canv['pads'][ipad]:
                                        self.build_normal_pad(c,ipad,pad)
                                else: 
                                        ratio_hist_name = canv['pads'][ipad]['ratio_to']
                                        self.build_ratio_pad(c,ipad,pad,ratio_hist_name)
                        if self._style: self._style.decorate_canvas(c)
                        for outfilename in self.get_outfile_name('_{}'.format(name)):
                                c.SaveAs(outfilename)
			
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

        model = Model(jsondic)

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
