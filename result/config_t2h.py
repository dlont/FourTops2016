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
    ("6J2M", "Njet=6, nMtags=2", "(nJets==6 && nMtags==2)*ScaleFactor"),
    ("6J3M", "Njet=6, nMtags=3", "(nJets==6 && nMtags==3)*ScaleFactor"),
    ("6J4M", "Njet=6, nMtags=4", "(nJets==6 && nMtags==4)*ScaleFactor"),
    ("7J2M", "Njet=7, nMtags=2", "(nJets==7 && nMtags==2)*ScaleFactor"),
    ("7J3M", "Njet=7, nMtags=3", "(nJets==7 && nMtags==3)*ScaleFactor"),
    ("7J4M", "Njet=7, nMtags=4", "(nJets==7 && nMtags==4)*ScaleFactor"),
    ("8J2M", "Njet=8, nMtags=2", "(nJets==8 && nMtags==2)*ScaleFactor"),
    ("8J3M", "Njet=8, nMtags=3", "(nJets==8 && nMtags==3)*ScaleFactor"),
    ("8J4M", "Njet=8, nMtags=4", "(nJets==8 && nMtags==4)*ScaleFactor"),
    ("9J2M", "Njet=9+, nMtags=2", "(nJets>=9 && nMtags==2)*ScaleFactor"),
    ("9J3M", "Njet=9+, nMtags=3", "(nJets>=9 && nMtags==3)*ScaleFactor"),
    ("9J4M", "Njet=9+, nMtags=4", "(nJets>=9 && nMtags==4)*ScaleFactor"),
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
    ("weight1_6J2M", "Njet=6, nMtags=2", "(nJets==6 && nMtags==2)*ScaleFactor*weight1"),
    ("weight2_6J2M", "Njet=6, nMtags=2", "(nJets==6 && nMtags==2)*ScaleFactor*weight2"),
    ("weight3_6J2M", "Njet=6, nMtags=2", "(nJets==6 && nMtags==2)*ScaleFactor*weight3"),
    ("weight4_6J2M", "Njet=6, nMtags=2", "(nJets==6 && nMtags==2)*ScaleFactor*weight4"),
    ("weight5_6J2M", "Njet=6, nMtags=2", "(nJets==6 && nMtags==2)*ScaleFactor*weight5"),
    ("weight7_6J2M", "Njet=6, nMtags=2", "(nJets==6 && nMtags==2)*ScaleFactor*weight7"),
    ("weight1_6J3M", "Njet=6, nMtags=3", "(nJets==6 && nMtags==3)*ScaleFactor*weight1"),
    ("weight2_6J3M", "Njet=6, nMtags=3", "(nJets==6 && nMtags==3)*ScaleFactor*weight2"),
    ("weight3_6J3M", "Njet=6, nMtags=3", "(nJets==6 && nMtags==3)*ScaleFactor*weight3"),
    ("weight4_6J3M", "Njet=6, nMtags=3", "(nJets==6 && nMtags==3)*ScaleFactor*weight4"),
    ("weight5_6J3M", "Njet=6, nMtags=3", "(nJets==6 && nMtags==3)*ScaleFactor*weight5"),
    ("weight7_6J3M", "Njet=6, nMtags=3", "(nJets==6 && nMtags==3)*ScaleFactor*weight7"),
    ("weight1_6J4M", "Njet=6, nMtags=4", "(nJets==6 && nMtags==4)*ScaleFactor*weight1"),
    ("weight2_6J4M", "Njet=6, nMtags=4", "(nJets==6 && nMtags==4)*ScaleFactor*weight2"),
    ("weight3_6J4M", "Njet=6, nMtags=4", "(nJets==6 && nMtags==4)*ScaleFactor*weight3"),
    ("weight4_6J4M", "Njet=6, nMtags=4", "(nJets==6 && nMtags==4)*ScaleFactor*weight4"),
    ("weight5_6J4M", "Njet=6, nMtags=4", "(nJets==6 && nMtags==4)*ScaleFactor*weight5"),
    ("weight7_6J4M", "Njet=6, nMtags=4", "(nJets==6 && nMtags==4)*ScaleFactor*weight7"),
    ("weight1_7J2M", "Njet=7, nMtags=2", "(nJets==7 && nMtags==2)*ScaleFactor*weight1"),
    ("weight2_7J2M", "Njet=7, nMtags=2", "(nJets==7 && nMtags==2)*ScaleFactor*weight2"),
    ("weight3_7J2M", "Njet=7, nMtags=2", "(nJets==7 && nMtags==2)*ScaleFactor*weight3"),
    ("weight4_7J2M", "Njet=7, nMtags=2", "(nJets==7 && nMtags==2)*ScaleFactor*weight4"),
    ("weight5_7J2M", "Njet=7, nMtags=2", "(nJets==7 && nMtags==2)*ScaleFactor*weight5"),
    ("weight7_7J2M", "Njet=7, nMtags=2", "(nJets==7 && nMtags==2)*ScaleFactor*weight7"),
    ("weight1_7J3M", "Njet=7, nMtags=3", "(nJets==7 && nMtags==3)*ScaleFactor*weight1"),
    ("weight2_7J3M", "Njet=7, nMtags=3", "(nJets==7 && nMtags==3)*ScaleFactor*weight2"),
    ("weight3_7J3M", "Njet=7, nMtags=3", "(nJets==7 && nMtags==3)*ScaleFactor*weight3"),
    ("weight4_7J3M", "Njet=7, nMtags=3", "(nJets==7 && nMtags==3)*ScaleFactor*weight4"),
    ("weight5_7J3M", "Njet=7, nMtags=3", "(nJets==7 && nMtags==3)*ScaleFactor*weight5"),
    ("weight7_7J3M", "Njet=7, nMtags=3", "(nJets==7 && nMtags==3)*ScaleFactor*weight7"),
    ("weight1_7J4M", "Njet=7, nMtags=4", "(nJets==7 && nMtags==4)*ScaleFactor*weight1"),
    ("weight2_7J4M", "Njet=7, nMtags=4", "(nJets==7 && nMtags==4)*ScaleFactor*weight2"),
    ("weight3_7J4M", "Njet=7, nMtags=4", "(nJets==7 && nMtags==4)*ScaleFactor*weight3"),
    ("weight4_7J4M", "Njet=7, nMtags=4", "(nJets==7 && nMtags==4)*ScaleFactor*weight4"),
    ("weight5_7J4M", "Njet=7, nMtags=4", "(nJets==7 && nMtags==4)*ScaleFactor*weight5"),
    ("weight7_7J4M", "Njet=7, nMtags=4", "(nJets==7 && nMtags==4)*ScaleFactor*weight7"),
    ("weight1_8J2M", "Njet=8, nMtags=2", "(nJets==8 && nMtags==2)*ScaleFactor*weight1"),
    ("weight2_8J2M", "Njet=8, nMtags=2", "(nJets==8 && nMtags==2)*ScaleFactor*weight2"),
    ("weight3_8J2M", "Njet=8, nMtags=2", "(nJets==8 && nMtags==2)*ScaleFactor*weight3"),
    ("weight4_8J2M", "Njet=8, nMtags=2", "(nJets==8 && nMtags==2)*ScaleFactor*weight4"),
    ("weight5_8J2M", "Njet=8, nMtags=2", "(nJets==8 && nMtags==2)*ScaleFactor*weight5"),
    ("weight7_8J2M", "Njet=8, nMtags=2", "(nJets==8 && nMtags==2)*ScaleFactor*weight7"),
    ("weight1_8J3M", "Njet=8, nMtags=3", "(nJets==8 && nMtags==3)*ScaleFactor*weight1"),
    ("weight2_8J3M", "Njet=8, nMtags=3", "(nJets==8 && nMtags==3)*ScaleFactor*weight2"),
    ("weight3_8J3M", "Njet=8, nMtags=3", "(nJets==8 && nMtags==3)*ScaleFactor*weight3"),
    ("weight4_8J3M", "Njet=8, nMtags=3", "(nJets==8 && nMtags==3)*ScaleFactor*weight4"),
    ("weight5_8J3M", "Njet=8, nMtags=3", "(nJets==8 && nMtags==3)*ScaleFactor*weight5"),
    ("weight7_8J3M", "Njet=8, nMtags=3", "(nJets==8 && nMtags==3)*ScaleFactor*weight7"),
    ("weight1_8J4M", "Njet=8, nMtags=4", "(nJets==8 && nMtags==4)*ScaleFactor*weight1"),
    ("weight2_8J4M", "Njet=8, nMtags=4", "(nJets==8 && nMtags==4)*ScaleFactor*weight2"),
    ("weight3_8J4M", "Njet=8, nMtags=4", "(nJets==8 && nMtags==4)*ScaleFactor*weight3"),
    ("weight4_8J4M", "Njet=8, nMtags=4", "(nJets==8 && nMtags==4)*ScaleFactor*weight4"),
    ("weight5_8J4M", "Njet=8, nMtags=4", "(nJets==8 && nMtags==4)*ScaleFactor*weight5"),
    ("weight7_8J4M", "Njet=8, nMtags=4", "(nJets==8 && nMtags==4)*ScaleFactor*weight7"),
    ("weight1_9J2M", "Njet=9+, nMtags=2", "(nJets>=9 && nMtags==2)*ScaleFactor*weight1"),
    ("weight2_9J2M", "Njet=9+, nMtags=2", "(nJets>=9 && nMtags==2)*ScaleFactor*weight2"),
    ("weight3_9J2M", "Njet=9+, nMtags=2", "(nJets>=9 && nMtags==2)*ScaleFactor*weight3"),
    ("weight4_9J2M", "Njet=9+, nMtags=2", "(nJets>=9 && nMtags==2)*ScaleFactor*weight4"),
    ("weight5_9J2M", "Njet=9+, nMtags=2", "(nJets>=9 && nMtags==2)*ScaleFactor*weight5"),
    ("weight7_9J2M", "Njet=9+, nMtags=2", "(nJets>=9 && nMtags==2)*ScaleFactor*weight7"),
    ("weight1_9J3M", "Njet=9+, nMtags=3", "(nJets>=9 && nMtags==3)*ScaleFactor*weight1"),
    ("weight2_9J3M", "Njet=9+, nMtags=3", "(nJets>=9 && nMtags==3)*ScaleFactor*weight2"),
    ("weight3_9J3M", "Njet=9+, nMtags=3", "(nJets>=9 && nMtags==3)*ScaleFactor*weight3"),
    ("weight4_9J3M", "Njet=9+, nMtags=3", "(nJets>=9 && nMtags==3)*ScaleFactor*weight4"),
    ("weight5_9J3M", "Njet=9+, nMtags=3", "(nJets>=9 && nMtags==3)*ScaleFactor*weight5"),
    ("weight7_9J3M", "Njet=9+, nMtags=3", "(nJets>=9 && nMtags==3)*ScaleFactor*weight7"),
    ("weight1_9J4M", "Njet=9+, nMtags=4", "(nJets>=9 && nMtags==4)*ScaleFactor*weight1"),
    ("weight2_9J4M", "Njet=9+, nMtags=4", "(nJets>=9 && nMtags==4)*ScaleFactor*weight2"),
    ("weight3_9J4M", "Njet=9+, nMtags=4", "(nJets>=9 && nMtags==4)*ScaleFactor*weight3"),
    ("weight4_9J4M", "Njet=9+, nMtags=4", "(nJets>=9 && nMtags==4)*ScaleFactor*weight4"),
    ("weight5_9J4M", "Njet=9+, nMtags=4", "(nJets>=9 && nMtags==4)*ScaleFactor*weight5"),
    ("weight7_9J4M", "Njet=9+, nMtags=4", "(nJets>=9 && nMtags==4)*ScaleFactor*weight7")
#    (weight7"barrel15to20", "(|#eta|<1.45weight7, 15<E_{T}<20)", "et>15&&et<20&&abs(eta)<1.45"),
#    ("barrel20to30", "(|#eta|<1.45, 20<E_{T}<30)", "et>20&&et<30&&abs(eta)<1.45"),
#    ("endcap15to20", "(1.7<|#eta|<2.5, 15<E_{T}<20)", "et>15&&et<20&&abs(eta)>1.7&&abs(eta)<2.5"),
#    ("endcap20to30", "(1.7<|#eta|<2.5, 20<E_{T}<30)", "et>20&&et<30&&abs(eta)>1.7&&abs(eta)<2.5")
    ]

# Define histograms to plot
bins_et     = array("f", [15.0, 20.0, 30.0, 50.0, 80.0, 120.0]) # example custom bins
from listofplots import lp
list_of_plots = lp
