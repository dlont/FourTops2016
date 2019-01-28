# Configuration file for tree2hists
# Created Nov 13, 2016.
try:
    ## the normal way to import from rootplot
    from rootplot.tree2hists import RootTree, Plot
except ImportError:
    ## special import for CMSSW installations of rootplot
    from PhysicsTools.PythonAnalysis.rootplot.tree2hists import RootTree, Plot
from array import array      # to allow making Float_t arrays for ROOT hists
from math import pi
from ROOT import TH1F, TH2F  # import other kinds of hists as neeeded
import sys
from triggercuts import trgcuts

inputfile=str(sys.argv[2])
output_filename=str(sys.argv[3])
tree_name=str(sys.argv[4])
scalefactor=float(sys.argv[5])
target=str(sys.argv[6])

print 'Using input file: ' + inputfile
print 'Output file: ' + output_filename
print 'Input tree name: ' + tree_name

tthftype = ''
if 'TTll' in output_filename:
	tthftype = '&& ((ttxType%100) < 40)'
if 'TTbb' in output_filename:
	tthftype = '&& ((ttxType%100) >= 51)'
if 'TTcc' in output_filename:
	tthftype = '&& ((ttxType%100) >= 41 && (ttxType%100) < 50)'
print 'tthftype cut=',tthftype

trigger_cuts = None

# Selection cuts change depending on the name of input Craneen file in order to properly include gen filtered samples
add_filter_flag = True if '_TTJets_' in inputfile else False
if add_filter_flag: trigger_cuts = trgcuts(tree_name) + '&&(GenFilter==0)'
else: trigger_cuts = trgcuts(tree_name)

list_of_files = [RootTree(str(tree_name), fileName=inputfile, scale=scalefactor, cuts="")]

cut_for_all_files = ""

# All plots are made for each "cut set".
# A "cut set" is 3 things: folder name to store hists in, string to add to hist titles, and cuts for these hists.
# Let cut_sets = [] to make all plots.
search_scheme = '9J4M,10J4M'
from centralweight import centralweight
cut_sets = [
    ("allSF", "", "({1} {0})*{2}".format(tthftype,trigger_cuts,centralweight)),
    ("6J2M", "Njet=6, nMtags=2",   "(nJets==6 && nMtags==2 {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
    ("6J3M", "Njet=6, nMtags=3",   "(nJets==6 && nMtags==3 {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
    ("6J4M", "Njet=6, nMtags=4",   "(nJets==6 && nMtags>=4 {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
    ("7J2M", "Njet=7, nMtags=2",   "(nJets==7 && nMtags==2 {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
    ("7J3M", "Njet=7, nMtags=3",   "(nJets==7 && nMtags==3 {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
    ("7J4M", "Njet=7, nMtags=4",   "(nJets==7 && nMtags>=4 {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
    ("8J2M", "Njet=8, nMtags=2",   "(nJets==8 && nMtags==2 {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
    ("8J3M", "Njet=8, nMtags=3",   "(nJets==8 && nMtags==3 {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
    ("8J4M", "Njet=8, nMtags=4",   "(nJets==8 && nMtags>=4 {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
    ("9J2M", "Njet=9, nMtags=2",   "(nJets==9 && nMtags==2 {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
    ("10J2M", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2  {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
    #("PU", "", "SFPU"),
    #("PUup", "", "SFPU_up"),
    #("PUdown", "", "SFPU_down"),
    #("btagSF", "", "SFbtag"),
    #("leptonSF", "", "SFlepton"),
    #("toprew", "", "toprew"),
    #("csvrs", "", "csvrsw[0]"),
    ("noSF", "", "{1}{0} ".format(tthftype,trigger_cuts)),
    ("PuLepSF", "", "ScaleFactor*GenWeight*({1}{0})".format(tthftype,trigger_cuts)),
    ("PuLepTrigSF", "", "ScaleFactor*GenWeight*SFtrig*({1}{0})".format(tthftype,trigger_cuts)),
    ("weight1", "", "(abs(weight1)*{2} {0})*{1}".format(tthftype,trigger_cuts,centralweight)),
    ("weight2", "", "(abs(weight2)*{2} {0})*{1}".format(tthftype,trigger_cuts,centralweight)),
    ("weight3", "", "(abs(weight3)*{2} {0})*{1}".format(tthftype,trigger_cuts,centralweight)),
    ("weight4", "", "(abs(weight4)*{2} {0})*{1}".format(tthftype,trigger_cuts,centralweight)),
    #("weight5", "", "(abs(weight5)*ScaleFactor*SFtrig)*GenWeight*"+trigger_cuts,centralweight), 
    ("weight6", "", "(abs(weight6)*{2} {0})*{1}".format(tthftype,trigger_cuts,centralweight)), 
    #("weight7", "", "(abs(weight7)*ScaleFactor*SFtrig)*GenWeight*"+trigger_cuts,centralweight), 
    ("weight8", "", "(abs(weight8)*{2} {0})*{1}".format(tthftype,trigger_cuts,centralweight)), 
    ]
if search_scheme == '9J3M,10J3M':
    cut_sets += [
        ("9J3M", "Njet=9, nMtags=3",   "(nJets==9 && nMtags>=3 {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
        ("10J3M", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3  {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
    ]
elif search_scheme == '9J4M,10J4M':
    cut_sets += [
        ("9J3M", "Njet=9, nMtags=3",   "(nJets==9 && nMtags==3 {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
        ("10J3M", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3  {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
        ("9J4M", "Njet=9, nMtags=3",   "(nJets==9 && nMtags>=4 {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
        ("10J4M", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=4  {0} && {1})*{2}".format(tthftype,trigger_cuts,centralweight)),
    ]

print "Target variable: ", target
from listofplots import lp
#from listofplots_single_plot import lp
#from listofplots_coarse import lp
list_of_plots = lp(tree_name,inputfile,target)

from custombinning import custom_binning
