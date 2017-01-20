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
    Plot("BDT"           , TH1D("bdt"    , ";BDT;entries/bin", 100, -0.6, 1.)),
    Plot("HT"           , TH1D("ht"    , ";HT (GeV);entries/bin", 185, 150., 2000.)),
    Plot("PU"           , TH1D("pu"    , ";Number of prim. v.;entries/bin", 55, -0.5, 54.5)),
    Plot("1stjetpt"           , TH1D("1stjetpt"    , ";1st jet p_{T} (GeV);entries/bin", 100, 0., 2000.)),
    Plot("2ndjetpt"           , TH1D("2ndjetpt"    , ";2nd jet p_{T} (GeV);entries/bin", 100, 0., 2000.)),
    Plot("5thjetpt"           , TH1D("5thjetpt"    , ";5th jet p_{T} (GeV);entries/bin", 100, 0., 350.)),
    Plot("6thjetpt"           , TH1D("6thjetpt"    , ";6th jet p_{T} (GeV);entries/bin", 100, 0., 250.)),
    Plot("LeptonPt"           , TH1D("leptonpt"    , ";Lepton p_{T} (GeV);entries/bin", 100, 0., 1000.)),
    Plot("LeptonEta"           , TH1D("leptoneta"    , ";Lepton #eta ;entries/bin", 100, -2.5, 2.5)),
    Plot("leptonphi"           , TH1D("leptonphi"    , ";Lepton #eta ;entries/bin", 100, -pi, pi)),
    Plot("leptonIso"           , TH1D("leptonIso"    , ";Lepton Isolation ;entries/bin", 100, 0., 0.5)),
    Plot("nLtags"           , TH1D("nltags"    , ";Number of loose tags;entries/bin", 11, -0.5, 10.5)),
    Plot("nMtags"           , TH1D("nmtags"    , ";Number of medium tags;entries/bin", 11, -0.5, 10.5)),
    Plot("nTtags"           , TH1D("nttags"    , ";Number of tight tags;entries/bin", 8, -0.5, 7.5)),
    Plot("nJets"            , TH1D("njets"     , ";Number of jets;entries/bin", 15, 3.5, 18.5)),
    Plot("HTb"            , TH1D("HTB"     , ";HTB (GeV);entries/bin", 100, 0., 2000.)),
    Plot("HTH"            , TH1D("HTH"     , ";HTH;entries/bin", 100, 0., 1.)),
    Plot("HTRat"            , TH1D("HTRat"     , ";HTRat;entries/bin", 100, 0., 0.5)),
    Plot("HTX"            , TH1D("HTX"     , ";HTX;entries/bin", 100, 0., 3000.)),
    Plot("SumJetMassX"            , TH1D("SumJetMassX"     , ";Sum jet M (GeV);entries/bin", 100, 0., 6000.)),
    Plot("multitopness"            , TH1D("multitopness"     , "; Topness;entries/bin", 100, -1.1, 0.3)),
    Plot("SFlepton"            , TH1D("SFlepton"     , ";Event SF due to leptons;entries/bin", 100, 0., 2.5)),
    Plot("SFbtag"            , TH1D("SFbtag"     , ";Event SF due to btag;entries/bin", 100, 0., 2.5)),
    Plot("SFbtagUp"            , TH1D("SFbtagUp"     , ";Event SF due to btag (up variation);entries/bin", 100, 0., 2.5)),
    Plot("SFbtagDown"            , TH1D("SFbtagDown"     , ";Event SF due to btag (down variation);entries/bin", 100, 0., 2.5)),
    Plot("SFPU"            , TH1D("SFPU"     , ";Event SF due to PU;entries/bin", 100, 0., 5.)),
    Plot("met"            , TH1D("met"     , ";MET (GeV);entries/bin", 100, 0., 1000.)),
    Plot("csvJetcsv1"            , TH1D("csvJetcsv1"     , ";CSV1;entries/bin", 100, 0., 1.)),
    Plot("csvJetcsv2"            , TH1D("csvJetcsv2"     , ";CSV2;entries/bin", 100, 0., 1.)),
    Plot("csvJetcsv3"            , TH1D("csvJetcsv3"     , ";CSV3;entries/bin", 100, 0., 1.)),
    Plot("csvJetcsv4"            , TH1D("csvJetcsv4"     , ";CSV4;entries/bin", 100, 0., 1.)),
    Plot("csvJetpt1"            , TH1D("csvJetpt1"     , ";CSV1;entries/bin", 100, 0., 1.)),
    Plot("csvJetpt2"            , TH1D("csvJetpt2"     , ";CSV2;entries/bin", 100, 0., 1.)),
    Plot("csvJetpt3"            , TH1D("csvJetpt3"     , ";CSV3;entries/bin", 100, 0., 1.)),
    Plot("csvJetpt4"            , TH1D("csvJetpt4"     , ";CSV4;entries/bin", 100, 0., 1.))
    ]
