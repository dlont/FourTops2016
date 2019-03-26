#!/usr/bin/python

import argparse, json, logging
import sys, re
import pprint

import ROOT
from ROOT import TFile, TTree
from ROOT import TCanvas, TH1, TH2, TProfile, TColor
from ROOT import TGraph, TGraphAsymmErrors, TMultiGraph
from ROOT import TF1
from ROOT import gROOT, gDirectory, gStyle, gPad
from ROOT import gStyle, gPad, TLegend, TAxis
from ROOT import SetOwnership

import tdrstyle 

logger = 0

gcSaver = []

def applyFigureStyle(obj,dic):
    '''
    Apply style to drawable object like Histograms or Graphs. ROOT API specific.
    Example dictionary: {"SetMarkerColor":ROOT.kBlue, "SetMarkerSize":2, "SetMarkerStyle":20}
    '''
    logger.debug('Started')
    for element_command, style in dic.iteritems():
        logger.debug('Apply command: %s.%s(%s)' % (obj,element_command, style))
        getattr(obj, element_command)(style)
    logger.debug('Finished')
    
def setBinLabels(axis,dic):
    '''
    dic provides the binID:Label mapping 
    '''
    
class comparisonFac:
    '''
    Class provides human-readable comparison of multiple limit points
    either in graphical or table format.
    
    result_format: supported options ("pdf","png","eps","C","tex")
    currently "tex" is a stub.
    '''
    def __init__(self,result_format,outfilename='limitComparison'):
        logger.debug('Started')
        logger.debug('Finished')
        
    def addPoint(self,point):
        logger.debug('Started')
        self.points_list.append(point)
        logger.debug('Finished')
    
    def getResult(self):
        logger.debug('Started')
        logger.debug('Finished')
    
    def getObservedGraph(self,style_dic):
        '''
        Retrive graph with observed limit points.
        Assumes "obs" key in input JSON object
        '''
        pass
    
    def getExpectedGraph(self,style_dic):
        '''
        Retrive graph with expected limit points and uncertainties.
        Assumes "exp_(16.0,50.0,84.0)" keys in input JSON object
        '''
        pass
    
    def getGraph(self,type,style_dic):
        pass
    
    def getPlot(self):
        '''
        Retrive ROOT canvas with comparison plot
        '''
        logger.debug('Started')
#        mg = TMultiGraph()
#        
#        grExpected_style_dic = {'SetMarkerColor':ROOT.kBlue, 'SetFillColor':ROOT.kWhite, 'SetMarkerSize':2, 'SetMarkerStyle':20, 'SetName':"Expected"}
#        grExpected = self.getGraph('Exp', grExpected_style_dic)
#        mg.Add(grExpected,"p")
#        grObserved_style_dic = {'SetMarkerColor':ROOT.kRed, 'SetFillColor':ROOT.kWhite, 'SetMarkerSize':2, 'SetMarkerStyle':20, 'SetName':"Observed"}
#        grObserved = self.getGraph('Obs', grObserved_style_dic)
#        #mg.Add(grObserved,"p")
#        
#        canvas = TCanvas('canvas', 'CMS')
#        gcSaver.append(canvas)
#        
#        mg.Draw('A')
#        mg.GetYaxis().SetTitle("Asymptotic CL_{S} upper limit (#sigma/#sigma_{SM})")
#        axis = mg.GetXaxis()
#        binID_list = [(axis.FindBin(grExpected.GetX()[ipoint]),str('fit%s'%ipoint)) for ipoint in 
#                            range(0,grExpected.GetN())]
#        axis_labels = dict((binID, label) for (binID, label) in binID_list)
#        setBinLabels(mg.GetXaxis(),axis_labels)
#        
#        canvas.BuildLegend()
#        tdrstyle.cmsPrel(-1., 13., False)
#        
#        canvas.Print(self.outfilename+'.'+self.result_format)
        logger.debug('Finished')
    
    def getTable(self):
        '''
        Retrive LaTeX table with limit comparison
        '''
        logger.debug('Started')
        logger.debug('Finished')
        pass

def getGraph(filename,style_dic):
        gr = TGraph(filename)
        applyFigureStyle(gr,style_dic)
        return gr
    
def decorateSecondAxis(canvas,gr):
    '''
    Add second axis indicating number of sigma deviations
    '''
    from ROOT import TGaxis
    logger.debug('Started')
    canvas.cd()

    rightmax = 1.1*gr.GetMaximum()
    axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),
                  ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),
                  0,rightmax,510,"+L");
    axis.SetLineColor(ROOT.kRed);
    axis.SetLabelColor(ROOT.kRed);
    axis.Draw();
    logger.debug('Finished')
    
def decorateGraph(gr,settings):
    gr.GetYaxis().SetTitle(settings["yaxistitle"])
    gr.GetXaxis().SetTitle(settings["xaxistitle"])
    
def compare(input_files,st_json_filename):
    '''
    make figure or table with limit comparison
    '''
    logger.debug('Started')
    logger.info('Input files:')
    for idx, filename in enumerate(input_files):
        logger.info('file '+str(idx)+": "+filename)
        
    logger.info('Reading settings JSON...')
    with open(st_json_filename) as json_file:
        settings = json.load(json_file)
    
    logger.debug('Creating canvas')
    canvas = TCanvas('c',settings["canvastitle"],5,45,800,800)
    canvas.SetLogy(settings["islogy"])
    mg = TMultiGraph()
    filename = [s for s in input_files if "prefit" in s]
    grPrefit = getGraph(filename[0],{"SetMarkerColor":ROOT.kBlue, "SetMarkerSize":2, "SetMarkerStyle":20})
    logger.info('prefit file: '+filename[0])
    mg.Add(grPrefit,"p")
    filename = [s for s in input_files if "postfit" in s]
    grPostfit = getGraph(filename[0],{"SetMarkerColor":ROOT.kRed, "SetMarkerSize":2, "SetMarkerStyle":20})
    logger.info('postfit file: '+filename[0])
    mg.Add(grPostfit,"p")
    
    mg.Draw('A')
    decorateGraph(mg, settings)
    decorateSecondAxis(canvas,mg)
    
    canvas.SaveAs(settings["output_filename"]+'.'+settings["output_format"])
    logger.debug('Finished')

def main(argv):
    global logger
    TH1.AddDirectory(False);
    
    #setup logger
    logformat = '[%(filename)s:%(lineno)s:%(levelname)s - %(funcName)20s() ] %(message)s'
    logging.basicConfig(format=logformat, level=logging.WARNING)
    logger = logging.getLogger()
    
    #setup command-line parser
    parser = argparse.ArgumentParser(description='Compare multiple limits in the same plot.',
                    add_help=False)
    parser.add_argument('-u', '--usage', action='help', help='show this help message and exit')
#    parser.add_argument('-o','--outfile', help='output file name without extension', required=True)
    parser.add_argument('-l','--loglevel', help='verbosity threshold: DEBUG, INFO, WARNING, ERROR', required=False)
#    parser.add_argument('-f','--fmt', help='comprison output format: pdf,png,eps,C,tex', required=False)
    parser.add_argument('-s','--settings', help='JSON with canvas settings', required=True)
    parser.add_argument('input_files', metavar='INPUT', type=str, nargs='+',
                    help='plaint text files with points definitions')
                        
    args = parser.parse_args()
    
    #modify logging message severity
    if args.loglevel is not None:
        numeric_level = getattr(logging, args.loglevel.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % args.loglevel)
        logger.setLevel(numeric_level)
    
    #make comparison
    logger.debug('Started')
    compare(args.input_files,args.settings)
    logger.debug('Finished')
    
if __name__ == "__main__":
   main(sys.argv)
