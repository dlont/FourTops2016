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

inputfile=str(sys.argv[2])
output_filename=str(sys.argv[3])
tree_name=str(sys.argv[4])
scalefactor=float(sys.argv[5])

print 'Using input file: ' + inputfile
print 'Output file: ' + inputfile

tthftype = ''
if 'TTll' in output_filename:
	tthftype = '&& ((ttxType%100) < 40)'
if 'TTbb' in output_filename:
	tthftype = '&& ((ttxType%100) >= 51)'
if 'TTcc' in output_filename:
	tthftype = '&& ((ttxType%100) >= 41 && (ttxType%100) < 50)'
print 'tthftype cut=',tthftype

trigger_cuts = ''
if 'Mu' in tree_name:
	trigger_cuts = "((HLT_IsoMu24==1||HLT_IsoTkMu24==1) && nJets>6 && met > 50)"
	#trigger_cuts = "(HLT_PFHT400_SixJet30_DoubleBTagCSV_p056==1)"
	#trigger_cuts = "(HLT_Mu15_IsoVVVL_BTagCSV_p067_PFHT400==1)"
elif 'El' in tree_name:
	#trigger_cuts = "((HLT_Ele32_eta2p1_WPTight_Gsf==1) && HT > 450 && met > 50)"
	trigger_cuts = "((HLT_Ele32_eta2p1_WPTight_Gsf==1) && nJets>7 && HT > 450 && met > 50)"
	#trigger_cuts = "(HLT_PFHT400_SixJet30_DoubleBTagCSV_p056==1)"
	#trigger_cuts = "(HLT_Ele15_IsoVVVL_PFHT350_PFMET50==1)"
list_of_files = [RootTree(str(tree_name), fileName=inputfile, scale=scalefactor, cuts="")]

cut_for_all_files = ""

# All plots are made for each "cut set".
# A "cut set" is 3 things: folder name to store hists in, string to add to hist titles, and cuts for these hists.
# Let cut_sets = [] to make all plots.
cut_sets = [
    ("allSF", "", "({1} {0})*ScaleFactor*SFtrig*GenWeight".format(tthftype,trigger_cuts)),
    ("6J2M", "Njet=6, nMtags=2",   "(nJets==6 && nMtags==2 {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("6J3M", "Njet=6, nMtags=3",   "(nJets==6 && nMtags==3 {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("6J4M", "Njet=6, nMtags=4",   "(nJets==6 && nMtags>=4 {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("7J2M", "Njet=7, nMtags=2",   "(nJets==7 && nMtags==2 {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("7J3M", "Njet=7, nMtags=3",   "(nJets==7 && nMtags==3 {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("7J4M", "Njet=7, nMtags=4",   "(nJets==7 && nMtags>=4 {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("8J2M", "Njet=8, nMtags=2",   "(nJets==8 && nMtags==2 {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("8J3M", "Njet=8, nMtags=3",   "(nJets==8 && nMtags==3 {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("8J4M", "Njet=8, nMtags=4",   "(nJets==8 && nMtags>=4 {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("9J2M", "Njet=9, nMtags=2",   "(nJets==9 && nMtags==2 {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("9J3M", "Njet=9, nMtags=3",   "(nJets==9 && nMtags==3 {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("9J4M", "Njet=9, nMtags=4",   "(nJets==9 && nMtags>=4 {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("10J2M", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2  {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("10J3M", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3  {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("10J4M", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4  {0})*ScaleFactor*SFtrig*GenWeight*{1}".format(tthftype,trigger_cuts)),
    #("PU", "", "SFPU"),
    #("PUup", "", "SFPU_up"),
    #("PUdown", "", "SFPU_down"),
    #("btagSF", "", "SFbtag"),
    #("leptonSF", "", "SFlepton"),
    #("toprew", "", "toprew"),
    #("csvrs", "", "csvrsw[0]"),
    #("noSF", "", ""),
    ("weight1", "", "(abs(weight1)*ScaleFactor*SFtrig {0})*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("weight2", "", "(abs(weight2)*ScaleFactor*SFtrig {0})*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("weight3", "", "(abs(weight3)*ScaleFactor*SFtrig {0})*GenWeight*{1}".format(tthftype,trigger_cuts)),
    ("weight4", "", "(abs(weight4)*ScaleFactor*SFtrig {0})*GenWeight*{1}".format(tthftype,trigger_cuts)),
    #("weight5", "", "(abs(weight5)*ScaleFactor*SFtrig)*GenWeight*"+trigger_cuts), 
    ("weight6", "", "(abs(weight6)*ScaleFactor*SFtrig {0})*GenWeight*{1}".format(tthftype,trigger_cuts)), 
    #("weight7", "", "(abs(weight7)*ScaleFactor*SFtrig)*GenWeight*"+trigger_cuts), 
    ("weight8", "", "(abs(weight8)*ScaleFactor*SFtrig {0})*GenWeight*{1}".format(tthftype,trigger_cuts)), 
#    (weight7"barrel15to20", "(|#eta|<1.45weight7, 15<E_{T}<20)", "et>15&&et<20&&abs(eta)<1.45"),
#    ("barrel20to30", "(|#eta|<1.45, 20<E_{T}<30)", "et>20&&et<30&&abs(eta)<1.45"),
#    ("endcap15to20", "(1.7<|#eta|<2.5, 15<E_{T}<20)", "et>15&&et<20&&abs(eta)>1.7&&abs(eta)<2.5"),
#    ("endcap20to30", "(1.7<|#eta|<2.5, 20<E_{T}<30)", "et>20&&et<30&&abs(eta)>1.7&&abs(eta)<2.5")
    ]

# Define histograms to plot
bins_et     = array("f", [15.0, 20.0, 30.0, 50.0, 80.0, 120.0]) # example custom bins
from listofplots import lp
list_of_plots = lp(tree_name,inputfile)
