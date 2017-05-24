try:
    ## the normal way to import from rootplot
    from rootplot.tree2hists import RootTree, Plot
except ImportError:
    ## special import for CMSSW installations of rootplot
    from PhysicsTools.PythonAnalysis.rootplot.tree2hists import RootTree, Plot
from array import array      # to allow making Float_t arrays for ROOT hists
from math import pi
from ROOT import TH1D, TH2F  # import other kinds of hists as neeeded

lp = [
    Plot("BDT"           , TH1D("bdt"    , ";BDT;entries/bin", 17, -0.6, 1.))
    #Plot("bdt_paper"           , TH1D("bdt"    , ";BDT;entries/bin", 17, -0.6, 1.))
    ]
