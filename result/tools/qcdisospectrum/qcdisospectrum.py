#!/usr/bin/env python

"""
A simple python script template.
"""

import os
import sys
import imp
import time
import shutil
import array
import argparse
import subprocess
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

BUILDDIR='build'

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

def all_hists_integral(hist_list):
        integral = 0
        for hist in hist_list:
                integral += hist.Integral()
        return integral

class Datasets(object):
        def __init__(self,craneens):
                self.chains = {}
                for name,tup in craneens.iteritems():
                        ch = rt.TChain(tup[0])                  # tree name
                        ch.Add(tup[1])                          # files
                        self.chains[name]=(ch,tup[2])           # eff. lumi.

@log_with()
def move_to_destination(artifacts,destination_dir):
        subprocess.call(["mv",artifacts,destination_dir])

@log_with()
def copy_to_destination(artifacts,destination_dir):
        subprocess.call(["cp","-a",artifacts,destination_dir])

class Model(object):
        def __init__(self,configuration):
                self._configuration = configuration
                self._objects = {}
                self._annotation = 'Performance comparision of different MVA discriminants'
                if 'annotation' in self._configuration:
                        self._annotation = self._configuration['annotation']

                self.craneens = None
                self.Initialize()
                self.iso_cut=self._configuration['iso_cut']
                self.str_iso_cut='{}'.format(self.iso_cut)
                self.str_iso_cut_epsilon='{}'.format(self.iso_cut*1.0001)
        @log_with()
        def Initialize(self):
                self.craneens = Datasets(self._configuration['inputfiles'])
                pass

        @log_with()
        def get(self,name):
                """
                Factory method
                """
                if name in self._objects:
                        return self._objects[name]
                elif 'lowiso' in name:
                        self._objects[name] = self.get_h_lowiso(name)
                elif 'highiso' in name:
                        self._objects[name] = self.get_h_highiso(name)
                else:
                        logging.error("Cannot retrive model object: {0}".format(name))
                        return None #provide factory method implementation here
                return self._objects[name]

        @log_with()
        def get_h_lowiso(self,name):
                bins_edges =  array.array('f',[0.,self.iso_cut,self.iso_cut*2.0])
                h = rt.TH1D(name,'Iso;;',len(bins_edges)-1,bins_edges)
                h.Sumw2()
                rt.SetOwnership(h,False)
                observable = self._configuration['observable']
                cuts = str()
                chains = self.craneens.chains
                for key in chains:
                        draw_command = '{0}>>+{1}'.format(observable,name)
                        cuts = '('+self._configuration['cuts']+' && leptonIso<'+self.str_iso_cut+')*'+str(chains[key][1])
                        chains[key][0].Draw(draw_command,cuts)
                        logging.info(draw_command)
                        logging.info(cuts)
                h.Print('all')
                return h

        @log_with()
        def get_h_highiso(self,name):
                bins_edges =  array.array('f',[0.,self.iso_cut,self.iso_cut*2.0])
                h = rt.TH1D(name,'NonIso inc. overflow;;',len(bins_edges)-1,bins_edges)
                h.Sumw2()
                rt.SetOwnership(h,False)
                observable = self._configuration['observable']
                cuts = str()
                chains = self.craneens.chains
                for key in chains:
                        draw_command = '(({0}>='.format(observable)+self.str_iso_cut+')?'+self.str_iso_cut_epsilon+':{0})>>+{1}'.format(observable,name)
                        cuts = '('+self._configuration['cuts']+' && leptonIso>='+self.str_iso_cut+')*'+str(chains[key][1])
                        chains[key][0].Draw(draw_command,cuts)
                        logging.info(draw_command)
                        logging.info(cuts)
                h.Print('all')
                return h
                

class Style(object):
        def __init__(self, config_json, model):
                self._json = config_json
                self._model = model
        model = property(None,None)

        @log_with()
        def decorate(self,obj):
                """
                Decorate object of the model.
                Assumes Drawable object from ROOT
                """
                name = obj.GetName()
                return obj

        @log_with()
        def decorate_stack(self, stack):
                stack.GetYaxis().SetTitleOffset(1.5)
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
                        # legend.AddEntry(self._model.get(el),self._json[el]['legend']['name'],self._json[el]['legend']['style'])
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
                canvas.SetLeftMargin(0.2)
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
                        yield '{}{}.{}'.format(self._outfilename,substring,ext)

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
				with open(BUILDDIR+'/'+os.path.basename(config), 'w') as f:
                                        serialized_config_str = pp.pformat(self.model._configuration)
                                        serialized_config_str = 'config='+serialized_config_str
                                        f.write(serialized_config_str)
                        elif ".json" in config: 
                                with open(BUILDDIR+'/'+os.path.basename(config), 'w') as f:
                                        json.dump(self.model._configuration, f, indent=4, sort_keys=True)

        @log_with()
        def draw(self):
                c = rt.TCanvas("c","cms",5,45,800,800)
                if self._style: self._style.decorate_canvas(c)

                h_lowiso = self.model.get('hist_lowiso')
                h_lowiso.SetFillColor(rt.kRed)
                h_highiso = self.model.get('hist_highiso')
                h_highiso.SetFillColor(rt.kBlue)

                total_integral = all_hists_integral([h_lowiso,h_highiso])
                # h_lowiso.Scale(1.0/total_integral)
                # h_highiso.Scale(1.0/total_integral)

                st = rt.THStack('st','Simulation (nJets>=8 && nMtags>=2 && HT>500 && met > 50 && LeptonPt>35.);RelIso;#frac{1}{N}#frac{dN}{dRelIso}')
                st.Add(h_lowiso,'hist E0')
                st.Add(h_highiso,'hist E0')
                st.Draw('nostack')
                if self._style: self._style.decorate_stack(st)

                leg = c.BuildLegend(0.25,0.75,0.5,0.85)
                iso_hist_unc = (h_lowiso.GetBinError(1)/h_lowiso.GetBinContent(1))**2.0
                noniso_hist_unc = (h_highiso.GetBinError(2)/h_highiso.GetBinContent(2))**2.0
                tf = h_lowiso.Integral()/h_highiso.Integral()
                tf_unc = rt.TMath.Sqrt(iso_hist_unc+noniso_hist_unc)*tf
                print h_lowiso.GetBinError(1), h_lowiso.GetBinContent(1)
                print h_highiso.GetBinError(2), h_highiso.GetBinContent(2)
                print tf, rt.TMath.Sqrt(iso_hist_unc+noniso_hist_unc)
                leg.AddEntry(rt.TObject(),"TF={0:.2f}#pm{1:.2f}".format(tf,tf_unc))

                self.set_outfilename(self.model._configuration['fig_name'])
                self.set_extension(self.model._configuration['fig_ext'])

                for output_file_name in self.get_outfile_name():
                        c.SaveAs(BUILDDIR+'/{}'.format(output_file_name))

class LatexReportView(View):
        @log_with()
        def __init__(self):
                self.limits=None
                pass

        @log_with()
        def Init(self):
                pass

        @log_with()
        def draw(self):
                self.Init()
                copy_to_destination("latex",BUILDDIR)
                copy_to_destination("resources",BUILDDIR)
                View.draw(self) #output figures are saved to ./build by default
                for output_file_name in self.get_outfile_name():
                        copy_to_destination(BUILDDIR+'/{}'.format(output_file_name),BUILDDIR+'/resources') #copy to resources to be visible from tex
                print self.model._configuration
                for artifact in self.model._configuration['latex']['artifacts']:
                       with open(BUILDDIR+'/{}'.format(artifact['name']),'w') as f:
                               f.write(artifact['content'])
                pdflatex_command = ["pdflatex", "-interaction=nonstop", "-output-directory=.", self.model._configuration['latex']['main']]
                print ' '.join(pdflatex_command)
                subprocess.call(pdflatex_command, cwd=BUILDDIR)


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

        model = Model(configuration)

        style = Style(configuration,model)

        view = None
        if configuration['mode'] == 'beamer':
                print "beamer option is not implemented!"
                # view = LatexBeamerView()
        elif configuration['mode'] == 'report':
                view = LatexReportView()
        else:
                view = View()
        view.set_model(model)
        view.set_style(style)
        view.set_outputfolder(arguments.dir)
        view.draw()
	#Move output artifacts to destination folder
        # pdf_file_name = self.model._configuration['latex']['main']
        # pdf_file_name.replace('tex','pdf')
        # subprocess.call(["cp","-a",pdf_file_name,self._outputfolder])
        # for figure_file_name in self.get_outfile_name():
        #         subprocess.call(["cp","-a",figure_file_name,self._outputfolder])

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
        parser.add_argument('-o', '--outfile', help="Output file")
        parser.add_argument('-e', '--extension', help="Plot file extension (.C, .root, .png, .pdf)", default='png')
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
