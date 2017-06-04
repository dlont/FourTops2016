try:
    ## the normal way to import from rootplot
    from rootplot.tree2hists import RootTree, Plot
except ImportError:
    ## special import for CMSSW installations of rootplot
    from PhysicsTools.PythonAnalysis.rootplot.tree2hists import RootTree, Plot
from array import array      # to allow making Float_t arrays for ROOT hists
from math import pi
from ROOT import TH1D, TH2F  # import other kinds of hists as neeeded

#bdtplot =  Plot("BDT"           , TH1D("bdt"    , ";BDT;entries/bin", 17, -0.6, 1.))
#bdtplot =  Plot("bdt_paper"           , TH1D("bdt"    , ";BDT;entries/bin", 17, -0.6, 1.))
bdtplot =  Plot("BDTninejet.MVAoutput"           , TH1D("bdt"    , ";BDT;entries/bin", 32, -0.6, 1.))
#bdtplot =  Plot("Gradninejet.MVAoutput"           , TH1D("bdt"    , ";BDT;entries/bin", 10, -5., 5.))
lp = [bdtplot]
