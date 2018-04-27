#!/usr/bin/env python

"""
A simple python script template.
"""

import os,sys,inspect
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
import numpy as np
import pandas as pd

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir+'/mountainrange_compare') 
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
                self._ob = ab.EquiProbableBinning() #optimized binning provide
                self._binning = {}                  #map of bins for each object
                self._annotation = 'Performance comparision of different MVA discriminants'
                if 'annotation' in self._jsondic:
                        self._annotation = self._jsondic['annotation']
                self.Initialize()

        @log_with()
        def Initialize(self):
                self.binning_init()
                self.make_table()
                pass

        @log_with()
        def make_table(self):

                eff_lumi = self._jsondic.get('eff_lumi_tt',1.)

                list_df = []
                list_df_eff = []
                list_df_nbins = []
                for row in self._jsondic['tables']['rows_names']:
                        nentries = [self.get(name).GetEntries() for name in self._jsondic['tables'][row]['nentries']]
                        nbins = [self._jsondic['binning'][name]['nbins'] for name in self._jsondic['tables'][row]['nbins']]
                        list_df.append(pd.DataFrame([nentries],columns=self._jsondic['tables']['columns_names'],index=[row]))
                        list_df_eff.append(pd.DataFrame([[entr*eff_lumi for entr in nentries]],columns=self._jsondic['tables']['columns_names'],index=[row]))
                        list_df_nbins.append(pd.DataFrame([nbins],columns=self._jsondic['tables']['columns_names'],index=[row]))

                df = pd.concat(list_df)
                df_eff = pd.concat(list_df_eff)
                df_nbins = pd.concat(list_df_nbins)

                print "tt mc n entries"
                print df
                print "tt observed prediction"
                print df_eff
                print "Number of bins"
                print df_nbins
                print "tt prediction N observed per bin"
                print df_eff.div(df_nbins)
                print "tt mc stat unc"                
                print df.div(df_nbins).apply(lambda x: 1./np.sqrt(x))

        @log_with()
        def binning_init(self):
                #build histogram prototypes for predefined binning
                for name, binning in self._jsondic['binning'].iteritems():
                        print '{}\n{}\n{}'.format(30*'=',name,30*'=')
                        nbins = binning.get('nbins',1)
                        filename=binning['inputfile']
                        treename=binning['treename']
                        varname=binning['varname']
                        cut=binning['cut']
                        tree=self.get_tree(filename,treename)
                        nev = tree.Draw(varname,cut,'goff')
                        enries_buf = tree.GetVal(0)
                        enries_vec = np.array([enries_buf[i] for i in range(0,nev)])
                        enries_vec.sort()
                        self._ob._vec=enries_vec
                        self._ob.nbins=nbins
                        self._ob.xmin=-1.
                        self._ob.xmax=1.
                        h = self._ob.get_histogram(name)
                        rt.SetOwnership(h,False)
                        self._binning[name]={'nbins':nbins,'hist':h}

        @log_with()
        def get(self,name):
                """
                Factory method
                """
                if name in self._objects:
                        return self._objects[name]
                else:
                        if 'uniform' in name:
                                self._objects[name] = self.build_hist_uniform(name)
                        elif 'optimized' in name:
                                self._objects[name] = self.build_hist_optimized(name)
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
                        h = self._binning[cut.split('&&')[-1]]['hist'].Clone(objname)
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
        def build_hist_optimized(self,objname):
                logging.debug(pp.pformat(objname))
                filename = str(self._jsondic[objname]['inputfile'])
                treename = str(self._jsondic[objname]['treename'])
                tree = self.get_tree(filename, treename)
                varname = self._jsondic[objname]['varname']
                cut = self._jsondic[objname]['cut']  #signal events from tmva tree
                binning_hist_name = self._jsondic[objname]['binning']
                hist = self._binning[binning_hist_name]['hist'].Clone(str(objname))
                logging.debug("Tree draw command: "+"{}>>{}".format(varname,str(objname)))
                logging.debug("Tree cut: {}".format(cut))
                tree.Draw("{}>>{}".format(varname,str(objname)),cut,'goff')
                hist = rt.gDirectory.Get(str(objname))
                rt.SetOwnership( hist, False )
                for ibin in range(1,hist.GetNbinsX()+1):
                        hist.SetBinContent(ibin,hist.GetBinContent(ibin)/hist.GetBinWidth(ibin))
                        hist.SetBinError(ibin,hist.GetBinError(ibin)/hist.GetBinWidth(ibin))
                return hist

        @log_with()
        def build_hist_uniform(self,objname):
                logging.debug(pp.pformat(objname))
                filename = str(self._jsondic[objname]['inputfile'])
                treename = str(self._jsondic[objname]['treename'])
                tree = self.get_tree(filename, treename)
                varname = self._jsondic[objname]['varname']
                min = -1.0
                max = 1.0
                nbins = 50
                drawhistconfig = "({},{},{})".format(nbins,min,max)
                histexpression = "{}{}".format(objname,drawhistconfig) #e.g h_tttt_BDTA20(25,-1.,1.)
                cut = self._jsondic[objname]['cut']  #signal events from tmva tree
                logging.debug("Tree draw command: {}".format(histexpression))
                logging.debug("Tree cut: {}".format(cut))
                tree.Draw("{}>>{}".format(varname,histexpression),cut,'goff')
                hist = rt.gDirectory.Get(str(objname))
                rt.SetOwnership( hist, False )
                for ibin in range(1,hist.GetNbinsX()+1):
                        hist.SetBinContent(ibin,hist.GetBinContent(ibin)/hist.GetBinWidth(ibin))
                        hist.SetBinError(ibin,hist.GetBinError(ibin)/hist.GetBinWidth(ibin))
                return hist

        @log_with()
        def build_hist(self,objname):
                logging.debug(pp.pformat(objname))
                filename = str(self._jsondic[objname]['inputfile'])
                treename = str(self._jsondic[objname]['treename'])
                tree = self.get_tree(filename, treename)
                varname = self._jsondic[objname]['varname']
                min = -1.0
                max = 1.0
                nbins = 50 if 'optimiz' in objname else 20
                drawhistconfig = "({},{},{})".format(nbins,min,max)
                histexpression = "{}{}".format(objname,drawhistconfig) #e.g h_tttt_BDTA20(25,-1.,1.)
                cut = self._jsondic[objname]['cut']  #signal events from tmva tree
                logging.debug("Tree draw command: {}".format(histexpression))
                logging.debug("Tree cut: {}".format(cut))
                tree.Draw("{}>>{}".format(varname,histexpression),cut,'goff')
                hist = rt.gDirectory.Get(str(objname))
                rt.SetOwnership( hist, False )
                if hist:
                        hist.Scale(1./hist.Integral())
                        return hist
                else:
                        print "Error: no histogram: ", str(objname)
                        sys.exit(1)

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
                linewidth = self._json[obj.GetName()].get('linewidth',2)
                linecolor = self._json[obj.GetName()].get('linecolor',rt.kBlue)
                linestyle = self._json[obj.GetName()].get('linestyle',1)
                obj.SetLineWidth(linewidth)
                obj.SetLineColor(linecolor)
                obj.SetLineStyle(linestyle)
                return obj

        @log_with()
        def decorate_stack(self, stack):
                pass

        @log_with()
        def decorate_graph(self,mg):
                pass

        @log_with()
        def make_legend(self,c,objlist,**kwargs):
                header=kwargs.get('header',None)
                pos=kwargs.get('pos',(0.11,0.11,0.5,0.5))
                legend = rt.TLegend(*pos)
                legend.SetName("TLeg_"+c.GetName())
                rt.SetOwnership(legend,False)
                legend.SetBorderSize(0)
                if header: legend.SetHeader(header)
                for el in objlist:
			pass
                        # legend.AddEntry(self.model.get(el),self._json[el]['legend']['name'],self._json[el]['legend']['style'])
                c.cd()
                legend.Draw()

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
                self.model = None
                self._style = None
                self._outfilename = 'out'
                self._outfileextension = 'png'
                self._outputfolder = '.'
        @log_with()
        def set_style(self,style):
                self._style = style
        @log_with()
        def set_model(self,model):
                self.model = model
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
                        bright_green_text = "\033[1;32;40m"
                        normal_text = "\033[0;37;40m"
                        print "\n".join(textwrap.wrap(bcolors.OKBLUE+
                                  self.model._annotation.encode('ascii')+
                                  bcolors.ENDC, 120))
                        if os.path.exists(self._outputfolder):
				# Writing JSON data
				with open(self._outputfolder+'/'+os.path.basename(config), 'w') as f:
					json.dump(self.model._jsondic, f, indent=4, sort_keys=True)
                elif type == "tex":
                        logging.warning("Annotation format: {}. Not implemented yet!".format(type))
                elif type == "md":
                        logging.warning("Annotation format: {}. Not implemented yet!".format(type))
                else:
                        logging.error("Annotation format not recognized: {}".format(type))

        @log_with()
        def decorate(self,object):
                return self._style.decorate(object)

        @log_with()
        def build_normal_pad(self, c, ipad, pad):
                c.cd(ipad+1) #root pad numeration starts from 1

                #make stack plot with optimized binning
                hs = rt.THStack("hsPad{}".format(ipad),"")
                for objname in pad['objects']:
                        hs.Add(self.decorate(self.model.get(objname)),"h")
                hs.Draw("nostack")
                islog=pad.get('islog',False)
                if self._style: 
                        last_histogram_name = hs.GetHists().First().GetName()
                        # self._style.decorate_stack(hs,title=self.model._jsondic[last_histogram_name]['title'])
                        self._style.decorate_pad(c.GetPad(ipad+1),islog)
        
        @log_with()
        def build_ratio_pad(self, c, ipad, pad):
                c.cd(ipad+1) #root pad numeration starts from 1
                hs_rat = rt.THStack("hsPad_rat{}".format(ipad),"")
                for objname in pad['objects']:
                        hist_ratio_clone = self.model.get(objname).Clone(objname+'_rat')
                        hist_ratio_clone.Divide(hist_ratio_clone)
                        hs_rat.Add(hist_ratio_clone,"h")
                hs_rat.Draw("nostack")
                if self._style: 
                        hs.Print()
                        last_histogram_name = hs.GetHists().First().GetName()
                        # self._style.decorate_stack(hs,title=self.model._jsondic[last_histogram_name]['title'])
                        self._style.decorate_pad(c.GetPad(ipad+1),islog)

        @log_with()
        def draw(self):
                for canv in self.model._jsondic['canvas']:
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
	
	jsondic['command']=' '.join(sys.argv)
        if arguments.annotation_format:
                view.annotate(arguments.annotation_format,arguments.config_json)

        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('-o', '--outfile', help="Output file")
        parser.add_argument('-e', '--extension', help="Plot file extension (.C, .root, .png, .pdf)", default='png,pdf')
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
