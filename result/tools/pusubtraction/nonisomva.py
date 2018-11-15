#!/usr/bin/env python

"""
A simple python script template.
"""

import os
import sys
import time
import datetime
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
                self._tf = None
                if 'annotation' in self._jsondic:
                        self._annotation = self._jsondic['annotation']
                self.Initialize()

        @log_with()
        def Initialize(self):
                self.compute_TF()
                pass

        @log_with()
        def compute_TF(self):
                tf_dic = self._jsondic['TF']
                files_data=tf_dic['inputfile_data']
		t_data = self.get_tree(files_data,tf_dic['treename'])
                files_tt=tf_dic['inputfile_tt']
		t_tt = self.get_tree(files_tt,tf_dic['treename'])
                cuts_noniso=tf_dic['cuts_noniso']
                cuts_iso=tf_dic['cuts_iso']
                cuts_inclusiveiso=tf_dic['cuts_inclusiveiso']
                varname = tf_dic['varname']
                eff_lum = tf_dic['eff_lum_tt']

                name = 'TF'

                h_data = None
                t_data.Draw("{}>>{}(25,0,1.25)".format(varname,"ISO_nj6_data"),cuts_inclusiveiso)
                h_data=rt.gDirectory.FindObject("ISO_nj6_data")
                rt.SetOwnership(h_data,False)
                self._objects["ISO_nj6_data"] = h_data
                h_tt = None
                t_tt.Draw("{}>>{}(25,0,1.25)".format(varname,"ISO_nj6_tt"),cuts_inclusiveiso+"*ScaleFactor*SFtrig*GenWeight*{}".format(str(eff_lum)))
                h_tt=rt.gDirectory.FindObject("ISO_nj6_tt")
                h_tt.SetDrawOption("hist")
                rt.SetOwnership(h_tt,False)
                self._objects["ISO_nj6_tt"] = h_tt

                h_data_iso = None
                t_data.Draw("{}>>{}(25,0,1.25)".format(varname,name+"_iso"),cuts_iso)
                h_data_iso=rt.gDirectory.FindObject(name+"_iso")
                rt.SetOwnership(h_data_iso,False)
                self._objects["TF_iso"] = h_data_iso
                # h_data_iso.Print("all")

                h_tt_iso = None
                t_tt.Draw("{}>>{}(25,0,1.25)".format(varname,name+"_iso_tt"),cuts_iso+"*ScaleFactor*SFtrig*GenWeight*{}".format(str(eff_lum)))
                h_tt_iso=rt.gDirectory.FindObject(name+"_iso_tt")
                rt.SetOwnership(h_tt_iso,False)
                self._objects["TF_iso_tt"] = h_tt_iso
                # h_tt_iso.Print("all")

                nonttdata_iso = [h_data_iso.Integral()-h_tt_iso.Integral(),\
                                 rt.TMath.Sqrt(h_data_iso.Integral()+h_tt_iso.Integral())]
                print "data/tt iso: {0:.1f}/{1:.1f}".format(h_data_iso.Integral(),h_tt_iso.Integral())
                print "Non tt data iso: {0:.1f} +/- {1:.2f}".format(nonttdata_iso[0],nonttdata_iso[1])

                h_data_noniso = None
                t_data.Draw("{}>>{}(25,0,1.25)".format(varname,name+"_noniso"),cuts_noniso)
                h_data_noniso=rt.gDirectory.FindObject(name+"_noniso")

                h_tt_noniso = None
                t_tt.Draw("{}>>{}(25,0,1.25)".format(varname,name+"_noniso_tt"),cuts_noniso+"*ScaleFactor*SFtrig*GenWeight*{}".format(str(eff_lum*0.8)))
                h_tt_noniso=rt.gDirectory.FindObject(name+"_noniso_tt")

                nonttdata_noniso = [h_data_noniso.Integral()-h_tt_noniso.Integral(),\
                                    rt.TMath.Sqrt(h_data_noniso.Integral()+h_tt_noniso.Integral())] 
                print "Non tt data noniso: {0:.1f} +/- {1:.2f}".format(nonttdata_noniso[0],nonttdata_noniso[1])

                self._tf = [nonttdata_iso[0]/nonttdata_noniso[0],\
                           nonttdata_iso[0]/nonttdata_noniso[0]*rt.TMath.Sqrt((nonttdata_noniso[1]/nonttdata_noniso[0])**2.+(nonttdata_iso[1]/nonttdata_iso[0])**2.)]
                print 'Transfer factor: {0:.1f} +/- {1:.2f}'.format(self._tf[0],self._tf[1])

        @log_with()
        def get(self,name):
                """
                Factory method
                """
                if name in self._objects:
                        return self._objects[name]
                elif "_iso" in name:
                        self._objects[name] = self.build_iso(name)
                elif "_noniso" in name:
                        self._objects[name] = self.build_noniso(name)
                else:
                        return None #provide factory method implementation here
                return self._objects[name]
        
        @log_with()
        def build_iso(self,name):
                files_data=self._jsondic[name]['inputfile_data']
		t_data = self.get_tree(files_data,self._jsondic[name]['treename'])
                varname = self._jsondic[name]['varname']
                cuts_iso=self._jsondic[name]['cuts']

                h_data_iso = None
                # t_data.Draw("{}>>{}(10,-1,1.)".format(varname,name),cuts_iso)
                eff_lum = self._jsondic[name]['eff_lum_tt']
                t_data.Draw("{}>>{}(10,-1,1.)".format(varname,name),cuts_iso+"*ScaleFactor*SFtrig*GenWeight*{}".format(str(eff_lum)))
                h_data_iso=rt.gDirectory.FindObject(name)
                return h_data_iso
        
        @log_with()
        def build_noniso(self,name):
                files_data=self._jsondic[name]['inputfile_data']
		t_data = self.get_tree(files_data,self._jsondic[name]['treename'])                
                files_tt=self._jsondic[name]['inputfile_tt']
		t_tt = self.get_tree(files_tt,self._jsondic[name]['treename'])
                cuts_noniso=self._jsondic[name]['cuts']
                varname = self._jsondic[name]['varname']                

                h_data_noniso = None
                t_data.Draw("{}>>{}(10,-1,1.)".format(varname,name),cuts_noniso)
                h_data_noniso=rt.gDirectory.FindObject(name)
                # h_data_noniso.Sumw2()

                h_tt_noniso = None
                eff_lum = self._jsondic[name]['eff_lum_tt']
                t_tt.Draw("{}>>{}(10,-1,1.)".format(varname,name+"_tt"),cuts_noniso+"*ScaleFactor*SFtrig*GenWeight*{}".format(str(eff_lum)))
                h_tt_noniso=rt.gDirectory.FindObject(name+"_tt")
                # h_tt_noniso.Sumw2()
                
                #subtract non-iso ttbar contribution from non-iso data
                h_data_noniso.Add(h_tt_noniso,-1.)

                return h_data_noniso

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
                obj.SetLineWidth(2)
                if name in self._json:
                        if 'linecolor' in self._json[name]: obj.SetLineColor(self._json[name]['linecolor'])
                        if 'linestyle' in self._json[name]: obj.SetLineStyle(self._json[name]['linestyle'])
                return obj

        @log_with()
        def decorate_stack(self, stack, **kwargs):
                stack.GetYaxis().SetTitleOffset(1.1)
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
        def add_legend_entry(self,legend,entrytitle,entryoption="",object=None):
                legend.AddEntry(object,entrytitle,entryoption)
                legend.Draw()

        @log_with()
        def make_legend(self,c,objlist,**kwargs):
                header=kwargs.get('header',None)
                pos=kwargs.get('pos',(0.6,0.75,0.99,0.99))
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
                if not folder: folder = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
                self._outputfolder = folder
                if not os.path.exists(folder):
                        os.makedirs(folder)
        @log_with()
        def get_outfile_name(self,substring=''):
                for ext in self._outfileextension.split(","):
                        yield '{}/{}{}.{}'.format(self._outputfolder,self._outfilename,substring,ext)

        @log_with()
        def decorate(self,obj):
                if self._style: return self._style.decorate(obj)
                else: return obj
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
        def build_normal_pad(self, c, ipad, pad):
                c.cd(ipad+1) #root pad numeration starts from 1
                hs = rt.THStack("hsPad{}".format(ipad),"")
                for objname in pad['objects']:
                        hs.Add(self.decorate(self._model.get(objname)))
                hs.Draw("nostack")
                islog=pad.get('islog',False)
                if self._style: 
                        last_histogram_name = hs.GetHists().First().GetName()
                        self._style.decorate_stack(hs,title=self._model._jsondic[last_histogram_name]['title'])
                        self._style.decorate_pad(c.GetPad(ipad+1),islog)
                        leg = None
                        if 'pos' in pad['legend']:
                                leg = self._style.make_legend(c.GetPad(ipad+1),pad['objects'],\
                                header=pad['legend']['header'],\
                                pos=pad['legend']['pos'])
                        else:
                                leg = self._style.make_legend(c.GetPad(ipad+1),pad['objects'],\
                                header=pad['legend']['header'])
                        #find noniso histogram on the pad
                        histname = next((x for x in pad['objects'] if "noniso" in x), None)
                        if histname:
                                h_noniso=self._model.get(histname)
                                n_noniso_events_after_subtraction=h_noniso.Integral()
                                self._style.add_legend_entry(leg,\
                                "N non iso events: {0:.1f} ".format(n_noniso_events_after_subtraction),"")

        @log_with()
        def draw(self):
                rt.gStyle.SetOptStat(0)

                c = rt.TCanvas('c','cms',5,45,800,800)
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
