#!/usr/bin/env python

"""
A simple script for mountain range systematics plotting.
"""
__version__ = "1.0"

import os
import sys
import imp
import time
import glob
import shutil
import argparse
import subprocess
import logging
import json
import textwrap
import pprint as pp
from prettytable import  PrettyTable
from prettytable import MSWORD_FRIENDLY
import ROOT as rt
from array import array

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

def make_ratio_histogram(hist_numerator, hist_denominator):
        result = hist_numerator.Clone(hist_numerator.GetName()+'_ratio')
        result.GetYaxis().SetTitle("variation/central -1")
        result.GetYaxis().SetTitleOffset(1.9)
        result.Add(hist_denominator,-1) 
        result.Divide(hist_denominator)
        rt.SetOwnership(result,False)
        return result

class Model(object):
        def __init__(self,configuration):
                self._configuration = configuration
                self._objects = {}
                self._annotation = 'Performance comparision of different MVA discriminants'
                if 'annotation' in self._configuration:
                        self._annotation = self._configuration['annotation']
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
	def decorate_axes(self,hist,json,axes=[]):
		for ax in axes:
			axis = None
			if ax == 'x':			
				axis = hist.GetXaxis()
			if ax == 'y':
				axis = hist.GetYaxis()
			if ax in json:
				for key in json[ax]:
					getattr(axis,key)(json[ax][key])

        @log_with()
        def decorate_histogram(self,hist,json):
                for key in json:
                        getattr(hist,key)(json[key])
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
                        # legend.AddEntry(self._model.get(el),self._json[el]['legend']['name'],self._json[el]['legend']['style'])
                c.cd()
                legend.Draw()
        @log_with()
        def make_legend_from_canvas_config(self,c,canvas_config,**kwargs):
                header=kwargs.get('header',None)
                pos=kwargs.get('pos',(0.01,0.01,0.99,0.1))
                legend = rt.TLegend(*pos)
                legend.SetName("TLeg_"+canvas_config['name'])
                rt.SetOwnership(legend,False)
                legend.SetBorderSize(0)
                legend.SetFillColor(4000)
                if header: legend.SetHeader(header)
                # c.GetListOfPrimitives().Print('all')
                for el in canvas_config["legend"]["entries"]:
                        leg_object = c.GetPrimitive(el+'_mountain_ratio')
                        legend.AddEntry(leg_object,canvas_config[el]['legend_entry']['name'],canvas_config[el]['legend_entry']['option'])
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
                # canvas.SetLeftMargin(1.1)
                # canvas.SetRightMargin(0.1)
                # canvas.SetLogy()
                canvas.Update()

class Serializer(object):
        @log_with()
        def __init__(self,builddir='build'):
                self._buildfolder = builddir
                self._outputfolder = None
                pass
        
        @log_with()
        def set_outputfolder(self,folder):
                self._outputfolder = folder
                if not os.path.exists(folder):
                        os.makedirs(folder)

        @log_with()
        def move_builddir_to_outputfolder(self):
                print self._buildfolder, self._outputfolder, (self._buildfolder and self._outputfolder)
                if self._buildfolder is not None and self._outputfolder is not None:
                        for extension in ['pdf','png','tex']:
                                for file in glob.glob('{}/*.{}'.format(self._buildfolder,extension)):
                                        shutil.move(file, self._outputfolder)

        @log_with()
        def serialize_view(self,View):
                self.move_builddir_to_outputfolder()
                pass
        
        @log_with()
        def serialize_beamer_view(self,View):
                self.move_builddir_to_outputfolder()
                pass

        
        @log_with()
        def serialize_report_view(self,View):
                self.move_builddir_to_outputfolder()
                pass

class View(object):
        @log_with()
        def __init__(self):
                self.model = None
                self._style = None
                self._outfilename = 'out'
                self._outfileextension = 'png'
                self._outputfolder = 'build'
        @log_with()
        def set_style(self,style):
                self._style = style
        @log_with()
        def set_model(self,model):
                self.model = model
        @log_with()
        def set_builddir(self,folder):
                self._outputfolder = folder
                if not os.path.exists(folder):
                        os.makedirs(folder)
        @log_with()
        def set_outfilename(self,filename):
                if filename: self._outfilename = filename
        @log_with()
        def set_extension(self,extension):
                self._outfileextension = extension
        @log_with()
        def get_outfile_name(self,substring=''):
                for ext in self._outfileextension.split(","):
                        yield '{}/{}{}.{}'.format(self._outputfolder,self._outfilename,substring,ext)

        @log_with()
        def annotate(self,type):
                if type == "screen":
                        bright_green_text = "\033[1;32;40m"
                        normal_text = "\033[0;37;40m"
                        print "\n".join(textwrap.wrap(bcolors.OKBLUE+
                                  self.model._annotation.encode('ascii')+
                                  bcolors.ENDC, 120))
                elif type == "tex":
                        logging.warning("Annotation format: {}. Not implemented yet!".format(type))
                elif type == "md":
                        logging.warning("Annotation format: {}. Not implemented yet!".format(type))
                else:
                        logging.error("Annotation format not recognized: {}".format(type))

        @log_with()
        def save_config(self, config):
                if os.path.exists(self._outputfolder):
                        # Writing configuration data
                        if "_cff.py" in config: 
				with open(self._outputfolder+'/'+os.path.basename(config), 'w') as f:
                                        serialized_config_str = pp.pformat(self.model._configuration)
                                        serialized_config_str = 'config='+serialized_config_str
                                        f.write(serialized_config_str)
                        elif ".json" in config: 
                                with open(self._outputfolder+'/'+os.path.basename(config), 'w') as f:
                                        json.dump(self.model._configuration, f, indent=4, sort_keys=True)

        @log_with()
        def save(self,serializer):
                serializer.serialize_view(self)

        @log_with()
        def build_canvas(self,canvas_config):
                c = None
                logging.debug(canvas_config)
                if canvas_config['type'] == '3x1_ratio_leg_bottom':
                        c = rt.TCanvas('c','cms',5,45,800,600)
                        c.Divide(1,3)
                        # top_pad_width + middle_pad_width + legend_pad_width = 1
                        top_pad_width    = 0.55
                        middle_pad_width = 0.25
                        legend_pad_width = 0.2
                        
                        for ipad in range(1,4): # [1;4)
                                c.cd(ipad)
                                rt.gPad.SetPad("pad_1_"+str(ipad),"",0.01,0.01,0.99,0.99)
                                # rt.gPad.SetFrameFillColor(0)
                                rt.gPad.SetFillColor(0)
                                rt.gPad.SetFillStyle(4000)
                                rt.gPad.SetLeftMargin(0.2)
                                if ipad == 1:  # top pad 
                                        rt.gPad.SetBottomMargin(1-top_pad_width)
                                if ipad == 2:  # ratio pad
                                        rt.gPad.SetTopMargin(top_pad_width)
                                        rt.gPad.SetBottomMargin(legend_pad_width)
                                if ipad == 3:  # legend pad
                                        rt.gPad.SetTopMargin(top_pad_width+middle_pad_width)
                        
                        distrib_title = "btag;BDT;N entries"
			labels = canvas_config['separators']['labels']
			conf = {"ypos":canvas_config['separators']['ypos'],"size":canvas_config['separators']['size']}
                        rootfile = rt.TFile(canvas_config['central']['type']['infile'],"READ")
                        list_hists_in_file_central = canvas_config['central']['type']['subhistograms']
                        hist_central,nbins,nonemptybin_map,stitch_edge_bins = mr.fillnonemptysingle_from_list( distrib_title, rootfile, list_hists_in_file_central, 'central')
			xbins = stitch_edge_bins; xbins.insert(0,0.); xbins = [el - 0.5 for el in xbins];			
			xbins = array('d',xbins)
			if canvas_config['central']['type']['algorithm'] == 'from_file_norm':
				hist_central=hist_central.Rebin(len(xbins)-1, hist_central.GetName(), xbins)
			if canvas_config['central']['type']['algorithm'] == 'from_file_norm_nj':
				hist_central=hist_central.Rebin(len(xbins)-1, hist_central.GetName(), xbins)
				hist_central.Rebin(3)
                        pad1 = c.cd(1)
                        rt.gPad.SetLogy()
			rt.gPad.Update()
			if 'axes' in canvas_config['central']:
				self._style.decorate_axes(hist_central,canvas_config['central']['axes'],axes=['y'])
                        if 'style' in canvas_config['central']:
				self._style.decorate_histogram(hist_central,canvas_config['central']['style']); hist_central.Draw("hist e")
                        c.cd(2)
                        hist_ratio_central = make_ratio_histogram(hist_central,   hist_central)
                        hist_ratio_central.Draw("hist")
                        hist_ratio_central.SetAxisRange(canvas_config['ratios']['yrange'][0],canvas_config['ratios']['yrange'][1],"Y")
			if 'axes' in canvas_config['central']:
				self._style.decorate_axes(hist_ratio_central,canvas_config['central']['axes'],axes=['x'])
                        rt.SetOwnership(hist_central,False)
                        for template in canvas_config['templates']:
                                rootfile = rt.TFile(canvas_config[template]['type']['infile'],"READ")
                                list_hists_in_file = canvas_config[template]['type']['subhistograms']
                                logging.debug(template)
                                logging.debug(rootfile)
                                logging.debug(list_hists_in_file)
                                hist,temp_nbins,temp_nonemptybin_map,stitch_edge_bins = mr.fillnonemptysingle_from_list( distrib_title, rootfile, list_hists_in_file, template)
				if canvas_config['central']['type']['algorithm'] == 'from_file_norm':
					hist = hist.Rebin(len(xbins)-1, hist.GetName(), xbins)
				if canvas_config['central']['type']['algorithm'] == 'from_file_norm_nj':
					hist = hist.Rebin(len(xbins)-1, hist.GetName(), xbins)
					hist.Rebin(3)
                                rt.SetOwnership(hist,False)
                                c.cd(1)
				if 'style' in canvas_config[template]:
                                	self._style.decorate_histogram(hist,canvas_config[template]['style']); 
				hist.Draw("hist same")
                                c.cd(2)
                                hist_ratio   = make_ratio_histogram(hist,   hist_central)
				#mr.draw_subhist_separators(rt.gPad,stitch_edge_bins,nonemptybin_map,labels,conf,hist_ratio)
				if 'style_ratio' in canvas_config[template]:
                                	self._style.decorate_histogram(hist_ratio,canvas_config[template]['style_ratio']); hist_ratio.Draw("hist same")
				else:
                                	self._style.decorate_histogram(hist_ratio,canvas_config[template]['style']); hist_ratio.Draw("hist same")
	
			c.cd(1)
			if 'from_file_norm' in canvas_config['central']['type']['algorithm']:
				mr.draw_subhist_labels(rt.gPad,labels,conf,hist_central)
			elif canvas_config['central']['type']['algorithm'] == 'from_file':
				mr.draw_subhist_separators(rt.gPad,stitch_edge_bins,nonemptybin_map,labels,conf,hist_central)
                        c.cd(2)
                        leg = self._style.make_legend_from_canvas_config(rt.gPad,canvas_config)
                        c.cd(3)
                        leg.SetFillStyle(4000)
                        leg.SetBorderSize(0)
                        leg.SetNColumns(len(canvas_config['legend']['entries'])/2)
                        leg.Draw()
                else:
                        raise RuntimeError(bcolors.FAIL+"Canvas TYPE:{0} for CANVAS:{1} is not recognized".format(canvas_config['type'],canvas_config['name'])+bcolors.ENDC)

                return c
        @log_with()
        def draw(self):
                
                rt.gStyle.SetOptStat(0)
                print bcolors.HEADER+"Drawing systematics templates"+bcolors.ENDC

                # read canvas from config and build them
                list_of_canvas = self.model._configuration['canvas']
                for canvas_label in list_of_canvas:
                        canvas_config = self.model._configuration.get(canvas_label,None)
                        if canvas_config is None: 
                                raise RuntimeError(bcolors.FAIL+"Cannot retrieve configuration for CANVAS:{0}".format(canvas_label)+bcolors.ENDC)
                        c = self.build_canvas(canvas_config)

                        if self._style: self._style.decorate_canvas(c)
                        for output_file_name in self.get_outfile_name(canvas_config['name']):
                                c.SaveAs(output_file_name)
			
class LatexBeamerView(View):
        @log_with()
        def __init__(self):
                self.limits=None
                pass

        @log_with()
        def Init(self):
                pass

        @log_with()
        def save(self,serializer):
                serializer.serialize_beamer_view(self)

        @log_with()
        def draw(self):
                self.Init()
		View.draw(self)
                print self.model._configuration
                subprocess.call(["pdflatex", "-interaction=nonstopmode", "-output-directory={}".format(self._outputfolder), 
                                 self.model._configuration['latex_main']])

class LatexReportView(View):
        @log_with()
        def __init__(self):
                self.limits=None
                pass

        @log_with()
        def Init(self):
                pass


        @log_with()
        def save(self,serializer):
                serializer.serialize_report_view(self)

        @log_with()
        def draw(self):
                self.Init()
		View.draw(self)
                print self.model._configuration
                # subprocess.call(["pdflatex", "-interaction=nonstopmode", "-output-directory={}".format(self._outputfolder),
                                #  self.model._configuration['latex_main']])
		
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
        configuration = None
	if ".json" in arguments.config:
        	with open(arguments.config) as json_data:
                	configuration = json.load(json_data)
                	logging.debug(pp.pformat(configuration))
	elif "_cff.py" in arguments.config:
                configuration_module = imp.load_source('my_config', arguments.config)
		configuration = configuration_module.config
		logging.debug(pp.pformat(configuration))
        else: raise RuntimeError(bcolors.FAIL+"Configuration file format {} is not recognized".format(arguments.config)+bcolors.ENDC)

        model = Model(configuration)

        style = Style(configuration,model)

        view = None
        if configuration['mode'] == 'beamer':
                print "beamer option is not implemented!"
                view = LatexBeamerView()
        elif configuration['mode'] == 'report':
                print "report option is not implemented!"
                view = LatexReportView()
        else:
                view = View()
        view.set_model(model)
        view.set_style(style)
        view.set_builddir(arguments.builddir)
        view.set_outfilename(arguments.outfile)
        view.set_extension(arguments.extension)
        view.draw()
        # serializer = Serializer(builddir=arguments.builddir)
        # serializer.set_outputfolder(arguments.dir)
        # view.save(serializer)
	
	configuration['command']=' '.join(sys.argv)
        if arguments.annotation_format:
                view.annotate(arguments.annotation_format)
                view.save_config(arguments.config)

        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)
        parser.add_argument('-o', '--outfile', help="Output file", default='test')
        parser.add_argument('-e', '--extension', help="Plot file extension (.C, .root, .png, .pdf)", default='png')
        parser.add_argument('--builddir', help="Build directory", default='build')
        parser.add_argument('--dir', help="Result output directory", default='.')
        parser.add_argument('-c', '--config', help=".json or _cff.py configuration file", required=True)
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
