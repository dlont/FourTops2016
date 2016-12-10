try:
    ## the normal way to import from rootplot
    from rootplot.tree2hists import RootTree, Plot
except ImportError:
    ## special import for CMSSW installations of rootplot
    from PhysicsTools.PythonAnalysis.rootplot.tree2hists import RootTree, Plot
from array import array      # to allow making Float_t arrays for ROOT hists
from math import pi
from ROOT import TH1F, TH2F  # import other kinds of hists as neeeded

lp = [
    Plot("BDT"           , TH1F("bdt"    , ";BDT;entries/bin", 100, -0.6, 1.)),
    Plot("HT"           , TH1F("ht"    , ";HT (GeV);entries/bin", 185, 150., 2000.)),
    Plot("PU"           , TH1F("pu"    , ";Number of prim. v.;entries/bin", 55, -0.5, 54.5)),
    Plot("LeptonPt"           , TH1F("leptonpt"    , ";p_{T} (GeV);entries/bin", 100, 0., 1000.)),
    Plot("LeptonEta"           , TH1F("leptoneta"    , ";#eta ;entries/bin", 100, -2.5, 2.5)),
    Plot("nLtags"           , TH1F("nltags"    , ";Number of loose tags;entries/bin", 11, -0.5, 10.5)),
    Plot("nMtags"           , TH1F("nmtags"    , ";Number of medium tags;entries/bin", 11, -0.5, 10.5)),
    Plot("nTtags"           , TH1F("nttags"    , ";Number of tight tags;entries/bin", 8, -0.5, 7.5)),
    Plot("nJets"            , TH1F("njets"     , ";Number of jets;entries/bin", 15, 3.5, 18.5))
    ]
