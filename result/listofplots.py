try:
    ## the normal way to import from rootplot
    from rootplot.tree2hists import RootTree, Plot
except ImportError:
    ## special import for CMSSW installations of rootplot
    from PhysicsTools.PythonAnalysis.rootplot.tree2hists import RootTree, Plot
from array import array      # to allow making Float_t arrays for ROOT hists
from math import pi
from ROOT import TH1D, TH2F  # import other kinds of hists as neeeded

def lp(treename):
	if 'El' in treename:
		isorangemax=0.15
	elif 'Mu' in treename:
		isorangemax=0.5
	else:
		raise NameError('Tree name %s is not recognized'%treename)
	plots_list = [
	Plot("BDT"           , TH1D("bdt"    , ";BDT;entries/bin", 17, -0.6, 1.)),
	Plot("multitopness"            , TH1D("multitopness"     , "; Topness;entries/bin", 100, -1.1, 0.3)),
	Plot("jetvec[][0]"           , TH1D("jetpt"    , ";jet p_{T} (GeV);entries/bin", 15, 30., 1500.)),
	Plot("jetvec[][1]"           , TH1D("jeteta"    , ";jet #eta;entries/bin", 50, -2.5, 2.5)),
	Plot("jetvec[][2]"           , TH1D("jetphi"    , ";jet #phi;entries/bin", 50, -pi, pi)),
	Plot("jetvec[][3]"           , TH1D("jetcsv"    , ";jet CSVv2;entries/bin", 100, 0., 1.)),
	#Plot("1stjetpt"           , TH1D("1stjetpt"    , ";1st jet p_{T} (GeV);entries/bin", 50, 0., 1500.)),
	#Plot("2ndjetpt"           , TH1D("2ndjetpt"    , ";2nd jet p_{T} (GeV);entries/bin", 50, 0., 1000.)),
	Plot("5thjetpt"           , TH1D("5thjetpt"    , ";5th jet p_{T} (GeV);entries/bin", 20, 30., 250.)),
	Plot("6thjetpt"           , TH1D("6thjetpt"    , ";6th jet p_{T} (GeV);entries/bin", 20, 30., 200.)),
	Plot("LeptonPt"           , TH1D("leptonpt"    , ";Lepton p_{T} (GeV);entries/bin", 20, 0., 800.)),
	Plot("LeptonEta"           , TH1D("leptoneta"    , ";Lepton #eta ;entries/bin", 50, -2.5, 2.5)),
	Plot("leptonphi"           , TH1D("leptonphi"    , ";Lepton #phi ;entries/bin", 50, -pi, pi)),
	Plot("leptonIso"           , TH1D("leptonIso"    , ";Lepton Isolation ;entries/bin", 25, 0., isorangemax)),
	Plot("nLtags"           , TH1D("nltags"    , ";Number of loose tags;entries/bin", 8, -0.5, 7.5)),
	Plot("nMtags"           , TH1D("nmtags"    , ";Number of medium tags;entries/bin", 8, -0.5, 7.5)),
	Plot("nTtags"           , TH1D("nttags"    , ";Number of tight tags;entries/bin", 6, -0.5, 5.5)),
	Plot("nJets"            , TH1D("njets"     , ";Number of jets;entries/bin", 9, 5.5, 14.5)),
	Plot("HT"           , TH1D("ht"    , ";HT (GeV);entries/bin", 25, 150., 2000.)),
	Plot("HTb"            , TH1D("HTB"     , ";HTB (GeV);entries/bin", 25, 0., 1000.)),
	Plot("HTH"            , TH1D("HTH"     , ";HTH;entries/bin", 100, 0.1, 1.1)),
	Plot("HTRat"            , TH1D("HTRat"     , ";HTRat;entries/bin", 45, 0., 0.45)),
	Plot("HTX"            , TH1D("HTX"     , ";HTX;entries/bin", 20, 0., 3000.)),
	Plot("SumJetMassX"            , TH1D("SumJetMassX"     , ";Sum jet M (GeV);entries/bin", 50, 0., 3500.)),
	Plot("PU"           , TH1D("pu"    , ";Number of prim. v.;entries/bin", 55, -0.5, 54.5)),
	#Plot("SFlepton"            , TH1D("SFlepton"     , ";Event SF due to leptons;entries/bin", 100, 0., 2.5)),
	#Plot("SFbtag"            , TH1D("SFbtag"     , ";Event SF due to btag;entries/bin", 100, 0., 5.)),
	#Plot("SFbtagUp"            , TH1D("SFbtagUp"     , ";Event SF due to btag (up variation);entries/bin", 100, 0., 2.5)),
	#Plot("SFbtagDown"            , TH1D("SFbtagDown"     , ";Event SF due to btag (down variation);entries/bin", 100, 0., 2.5)),
	#Plot("SFPU"            , TH1D("SFPU"     , ";Event SF due to PU;entries/bin", 100, 0., 5.)),
	Plot("met"            , TH1D("met"     , ";MET (GeV);entries/bin", 50, 0., 800.)),
	#Plot("csvJetcsv1"            , TH1D("csvJetcsv1"     , ";CSV1;entries/bin", 100, 0., 1.)),
	#Plot("csvJetcsv2"            , TH1D("csvJetcsv2"     , ";CSV2;entries/bin", 100, 0., 1.)),
	#Plot("csvJetcsv3"            , TH1D("csvJetcsv3"     , ";CSV3;entries/bin", 100, 0., 1.)),
	#Plot("csvJetcsv4"            , TH1D("csvJetcsv4"     , ";CSV4;entries/bin", 100, 0., 1.)),
	#Plot("csvJetpt1"            , TH1D("csvJetpt1"     , ";CSV1;entries/bin", 100, 0., 1.)),
	#Plot("csvJetpt2"            , TH1D("csvJetpt2"     , ";CSV2;entries/bin", 100, 0., 1.)),
	#Plot("csvJetpt3"            , TH1D("csvJetpt3"     , ";CSV3;entries/bin", 100, 0., 1.)),
	#Plot("csvJetpt4"            , TH1D("csvJetpt4"     , ";CSV4;entries/bin", 100, 0., 1.))
	]
	return plots_list
