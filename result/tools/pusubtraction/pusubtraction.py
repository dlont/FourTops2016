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

class Model(object):
        def __init__(self,jsondic):
                self._jsondic = jsondic
                self._objects = {}
                self._annotation = 'Performance comparision of different MVA discriminants'
                if 'annotation' in self._jsondic:
                        self._annotation = self._jsondic['annotation']
                self.Initialize()

        @log_with()
        def Initialize(self):
                pass

        @log_with()
        def get(self,name):
                """
                Factory method
                """
                if name in self._objects:
                        return self._objects[name]
                else:
                        return None #provide factory method implementation here
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
                return obj

        @log_with()
        def decorate_stack(self, stack):
                pass

        @log_with()
        def decorate_graph(self,mg):
                pass

        @log_with()
        def add_legend_entry(self,legend,entrytitle,entryoption,object=None):
                legend.AddEntry(object,entrytitle,entryoption)
                legend.Draw()

        @log_with()
        def make_legend(self,c,**kwargs):
                header=kwargs.get('header',None)
                pos=kwargs.get('pos',(0.8,0.75,0.99,0.99))
                legend = rt.TLegend(*pos)
                legend.SetName("TLeg_"+c.GetName())
                rt.SetOwnership(legend,False)
                legend.SetBorderSize(0)
                if header: legend.SetHeader(header)
                c.cd()
                legend.Draw()
                return legend

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
        def annotate(self,type,config):
                if type == "screen":
                        bright_green_text = "\033[1;32;40m"
                        normal_text = "\033[0;37;40m"
                        print "\n".join(textwrap.wrap(bcolors.OKBLUE+
                                  self._model._annotation.encode('ascii')+
                                  bcolors.ENDC, 120))
                        if os.path.exists(self._outputfolder):
				# Writing JSON data
				with open(self._outputfolder+'/'+os.path.basename(config), 'w') as f:
					json.dump(self._model._jsondic, f, indent=4, sort_keys=True)
                elif type == "tex":
                        logging.warning("Annotation format: {}. Not implemented yet!".format(type))
                elif type == "md":
                        logging.warning("Annotation format: {}. Not implemented yet!".format(type))
                else:
                        logging.error("Annotation format not recognized: {}".format(type))

        @log_with()
        def draw(self):
                c = rt.TCanvas('c','cms',5,45,800,800)

                treename=self._model._jsondic['treename']
                files=self._model._jsondic['inputfile']
                cuts=self._model._jsondic['cuts']
		t = self._model.get_tree(files,treename)

                hpu = None
                t.Draw("0.5*PUIso:min(nJets,10)>>h2dPU(4,6.5,10.6,100,0,15)",cuts)
                hpu=rt.gDirectory.FindObject("h2dPU")
                hpu.SetTitle(";n jets;#sum E_{T}")
                hpu.SetLineColor(rt.kGreen+1)
                hpu.SetMarkerColor(rt.kGreen+1)
                hph = None                
                t.Draw("photonIso:min(nJets,10)>>h2dPhoton(4,6.5,10.6,100,0,15)",cuts)
                hph=rt.gDirectory.FindObject("h2dPhoton")
                hph.SetLineColor(rt.kBlue+1)
                hph.SetMarkerColor(rt.kBlue+1)
                hn = None                                
                t.Draw("neutralHIso:min(nJets,10)>>h2dNeutral(4,6.5,10.6,100,0,15)",cuts)
                hn=rt.gDirectory.FindObject("h2dNeutral")
                hn.SetLineColor(rt.kRed+1)
                hn.SetMarkerColor(rt.kRed+1)

                hpu.Draw("CANDLEX")
                hph.Draw("SAME CANDLEX")
                hn.Draw("SAME CANDLEX")

                leg=self._style.make_legend(c,header="RelIso=0")
                self._style.add_legend_entry(leg,"#sum 0.5E_{T,sub}^{PU}",'l',hpu)
                self._style.add_legend_entry(leg,"#sum E_{T}^{#gamma}",'l',hph)
                self._style.add_legend_entry(leg,"#sum E_{T}^{N}",'l',hn)

                rt.gStyle.SetOptStat(0)

                if self._style: self._style.decorate_canvas(c)
                c.SaveAs(self.get_outfile_name())
			
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
