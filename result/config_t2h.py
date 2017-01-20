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

list_of_files = [RootTree(str(tree_name), fileName=inputfile, scale=scalefactor, cuts="")]

cut_for_all_files = ""

# All plots are made for each "cut set".
# A "cut set" is 3 things: folder name to store hists in, string to add to hist titles, and cuts for these hists.
# Let cut_sets = [] to make all plots.
cut_sets = [
    ("allSF", "", "ScaleFactor"),
    ("allSF_NJ6", "Njet=6", "(nJets==6)*ScaleFactor"),
    ("allSF_NJ7", "Njet=7", "(nJets==7)*ScaleFactor"),
    ("allSF_NJ8", "Njet=8", "(nJets==8)*ScaleFactor"),
    ("allSF_NJ9", "Njet=9", "(nJets==9)*ScaleFactor"),
    ("allSF_NJ10+", "Njet>9", "(nJets>9)*ScaleFactor"),
    ("PU", "", "SFPU"),
    ("PUup", "", "SFPU_up"),
    ("PUdown", "", "SFPU_down"),
    ("btagSF", "", "SFbtag"),
    ("leptonSF", "", "SFlepton"),
    ("noSF", "", ""),
    ("weight1", "", "weight1*ScaleFactor"),
    ("weight2", "", "weight2*ScaleFactor"),
    ("weight3", "", "weight3*ScaleFactor"),
    ("weight4", "", "weight4*ScaleFactor"),
    ("weight5", "", "weight5*ScaleFactor"),
    ("weight7", "", "weight7*ScaleFactor"),
    ("weight1_NJ6", "Njet=6", "(nJets==6) *weight1*ScaleFactor"),
    ("weight2_NJ7", "Njet=7", "(nJets==7) *weight2*ScaleFactor"),
    ("weight3_NJ8", "Njet=8", "(nJets==8) *weight3*ScaleFactor"),
    ("weight4_NJ9", "Njet=9", "(nJets==9) *weight4*ScaleFactor"),
    ("weight5_NJ10+", "Njet>9", "(nJets>9)*weight5*ScaleFactor")
#    (weight7"barrel15to20", "(|#eta|<1.45weight7, 15<E_{T}<20)", "et>15&&et<20&&abs(eta)<1.45"),
#    ("barrel20to30", "(|#eta|<1.45, 20<E_{T}<30)", "et>20&&et<30&&abs(eta)<1.45"),
#    ("endcap15to20", "(1.7<|#eta|<2.5, 15<E_{T}<20)", "et>15&&et<20&&abs(eta)>1.7&&abs(eta)<2.5"),
#    ("endcap20to30", "(1.7<|#eta|<2.5, 20<E_{T}<30)", "et>20&&et<30&&abs(eta)>1.7&&abs(eta)<2.5")
    ]

# Define histograms to plot
bins_et     = array("f", [15.0, 20.0, 30.0, 50.0, 80.0, 120.0]) # example custom bins
from listofplots import lp
list_of_plots = lp
