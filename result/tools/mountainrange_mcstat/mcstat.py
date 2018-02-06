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
import mountainrange.mountainrange_pub_utilities as mr

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

                filename = self._jsondic['tttt']['inputfile']
                list_of_short_histograms = []
                for hist in self._jsondic['tttt']['list_of_histograms']:
                        list_of_short_histograms.append(self.get_histogram(filename,hist))
                nbins = mr.get_total_nbins_from_list(list_of_short_histograms)
                hist_master_tttt = rt.TH1F("temp_tttt_master_hist_for_binning","",nbins,0.5,float(nbins+0.5))
                hist_master_tttt, self.stich_bins = mr.fillsingle_from_list(hist_master_tttt,list_of_short_histograms) 
                                
                self.binmapping = mr.binmap(hist_master_tttt)

        @log_with()
        def get_histogram(self,filename,histname):
                f = rt.TFile.Open(filename,'READ')
                rt.SetOwnership(f,False)
                h = f.Get(histname.encode('ascii'))
                rt.SetOwnership(h,False)
                return h

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
        def get(self,name):
                """
                Factory method
                """
                if name in self._objects:
                        return self._objects[name]
                else:
                        self._objects[name] = self.get_stat_err_hist(name)
                return self._objects[name]
        
        @log_with()
        def get_stat_err_hist(self,name):
                filename = self._jsondic[name]['inputfile']

                list_of_short_histograms = []
                for hist in self._jsondic[name]['list_of_histograms']:
                        list_of_short_histograms.append(self.get_histogram(filename,hist))
                
                logging.debug(pp.pformat(list_of_short_histograms))

                nbins = mr.get_total_nbins_from_list(list_of_short_histograms)
                hist_master = rt.TH1F(name,"",nbins,0.5,float(nbins+0.5))
                hist_master, self.stich_bins = mr.fillsingle_from_list(hist_master,list_of_short_histograms) 
                hist_noempty = mr.noemptybins(hist_master, self.binmapping)

                hist_noempty.Divide(hist_noempty)
                hist_noempty.SetName(name)
                return hist_noempty

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
                print name
                # obj.SetLineWidth(2)
                if name in self._json:
                        if 'linecolor' in self._json[name]: obj.SetLineColor(self._json[name]['linecolor'])
                        if 'linestyle' in self._json[name]: obj.SetLineStyle(self._json[name]['linestyle'])
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
			# pass
                        caption = self._json[el]['legend']['name']
                        style = self._json[el]['legend'].get('style',"PE")
                        legend.AddEntry(self._model.get(el),caption,style)
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
                self.style = None
                self._outfilename = 'out'
                self._outfileextension = 'png'
                self._outputfolder = '.'
        @log_with()
        def set_style(self,style):
                self.style = style
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
        def draw_subhist_separators(self,c,stitch_edge_bins,binmapping,labels,hist_template):
                #calculate position of separator vertical lines on mountain range plot
                #without empty bins
                mappedbins = binmapping.keys()
                mappedbins.sort()
                mapped_edge_bins = []
                for edge in stitch_edge_bins:   #for each boundary bin in long histogram
                        mappededge = -1
                        for mb in mappedbins:   #find rightmost nonempty bin before boundary bin
                                if mb <= edge: mappededge = mb
                                else:
                                        mapped_edge_bins.append(mappededge)
                                        break

                #boundary bins on histogram without empty bins
                separator_bins = [binmapping[x] for x in mapped_edge_bins]
                separator_bins.append(hist_template.GetNbinsX())
                logging.debug( "Stitching bins:" )
                logging.debug(pp.pformat( stitch_edge_bins ) )
                logging.debug( "Separator bins:" )
                logging.debug(pp.pformat( separator_bins ) )

                ycoord = self._model._jsondic['ypos']

                c.cd()
                #Draw vertical bars separating different histograms
                ymin = hist_template.GetMinimum()
                ymax = hist_template.GetMaximum()
                xpos_for_labels = [hist_template.GetBinLowEdge(1)]
                for item, isep in enumerate(separator_bins): 
                        xpos_for_labels.append(hist_template.GetBinLowEdge(isep)+hist_template.GetBinWidth(isep))
                        x = xpos_for_labels[item+1]
                        l = rt.TLine(x,ymin,x,ymax); l.SetLineColor(rt.kBlack); l.SetLineWidth(2); l.Draw()

                #Draw labels
                tex = rt.TLatex()
                tex.SetTextSize(0.023)
                tex.SetTextAlign(22)
                tex.SetTextAngle(90)
                print xpos_for_labels
                for item, isep in enumerate(separator_bins):
                        #find center of the stiched histogram
                        x = xpos_for_labels[item]+(xpos_for_labels[item+1]-xpos_for_labels[item])/2.
                        #if label x-cordinate is specified in json config
                        cxmin=rt.gPad.GetLeftMargin()
                        cxmax=1.-rt.gPad.GetRightMargin()
                        xmax = hist_template.GetXaxis().GetXmax()
                        xmin = hist_template.GetXaxis().GetXmin()
                        xndc = cxmin + (x - xmin)/(xmax - xmin) * (cxmax - cxmin)
                        if isinstance(labels,list):
                                if isinstance(labels[item],list) and len(labels[item])>1: xndc = labels[item][1]
                                logging.info('Separator|Label: {} | {} {} {} {}'.format( isep,x,xndc,ycoord,labels[item][0] ) )
                                tex.DrawLatexNDC(xndc,ycoord,labels[item][0])
                c.RedrawAxis()

        @log_with()
        def draw(self):
                c = rt.TCanvas('c','cms',5,45,800,400)
                st = rt.THStack('stack','')
                for ihist, stack_hist in enumerate(self._model._jsondic['stack']):
                        st.Add(self.style.decorate(self._model.get(stack_hist[0])),stack_hist[1])
                st.Draw('nostack')
                st.SetMinimum(0.)
                st.SetMaximum(2.)
                if self.style: self.style.decorate_canvas(c)
                labels = self._model._jsondic['labels']
                self.draw_subhist_separators(c,self._model.stich_bins,self._model.binmapping,\
                labels,st.GetHistogram())
                self.style.make_legend(rt.gPad,['tttt','tt','ttz','tth'],pos=(0.13,0.12,0.15,0.4))
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
        rt.TLine.__init__._creates = False

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
