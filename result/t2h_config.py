# Configuration file for tree2hists
# Created Nov 14, 2016.
try:
    ## the normal way to import from rootplot
    from rootplot.tree2hists import RootTree, Plot
except ImportError:
    ## special import for CMSSW installations of rootplot
    from PhysicsTools.PythonAnalysis.rootplot.tree2hists import RootTree, Plot
from array import array      # to allow making Float_t arrays for ROOT hists
from math import pi
from ROOT import TH1F, TH2F  # import other kinds of hists as neeeded

list_of_files = [RootTree("Treename", fileName="photons.root", scale=1.0, cuts=""),
                 RootTree("Treename", fileName="photons2.root", scale=1.0, cuts="")]

output_filename = "Hists_photons.root"

cut_for_all_files = "(!TTBit[36] && !TTBit[37] && !TTBit[38] && !TTBit[39] && !vtxIsFake && vtxNdof>4 && abs(vtxZ)<=15)"

# All plots are made for each "cut set".
# A "cut set" is 3 things: folder name to store hists in, string to add to hist titles, and cuts for these hists.
# Let cut_sets = [] to make all plots.
cut_sets = [
    ("barrel15to20", "(|#eta|<1.45, 15<E_{T}<20)", "et>15&&et<20&&abs(eta)<1.45"),
    ("barrel20to30", "(|#eta|<1.45, 20<E_{T}<30)", "et>20&&et<30&&abs(eta)<1.45"),
    ("endcap15to20", "(1.7<|#eta|<2.5, 15<E_{T}<20)", "et>15&&et<20&&abs(eta)>1.7&&abs(eta)<2.5"),
    ("endcap20to30", "(1.7<|#eta|<2.5, 20<E_{T}<30)", "et>20&&et<30&&abs(eta)>1.7&&abs(eta)<2.5")
    ]

# Define histograms to plot
bins_et     = array("f", [15.0, 20.0, 30.0, 50.0, 80.0, 120.0]) # example custom bins
list_of_plots = [
    Plot("et"           , TH1F("pho_et"           , "Lead #gamma: E_{T};E_{T} (GeV);entries/bin", 25, 0.0, 100.0)),
    Plot("eta"          , TH1F("pho_eta"          , "Lead #gamma: #eta;#eta;entries/bin"        , 25, -3.0, 3.0)),
    Plot("et"           , TH1F("pho_et_binned"    , "Lead #gamma: E_{T};E_{T} (GeV);entries/bin", len(bins_et)-1, bins_et)),
    Plot("sigmaIetaIeta", TH1F("pho_sigmaIEtaIEta", "Lead #gamma: #sigma_{i#etai#eta};#sigma_{i#etai#eta};entries/bin",20, 0, 0.06)),
    Plot("metEt/et"     , TH1F("metEt_over_phoEt" , "MET / E_{T}(#gamma);MET/E_{T}(sc);entries/bin"   , 20, 0.0, 3.0)),
    Plot("phi:eta"      , TH2F("phoPhi_vs_phoEta" , "Lead #gamma: #phi vs #eta;#eta;#phi"             , 50, -2.5, 2.5, 18, -pi, pi))
    ]
