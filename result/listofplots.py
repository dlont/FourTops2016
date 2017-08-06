try:
    ## the normal way to import from rootplot
    from rootplot.tree2hists import RootTree, Plot
except ImportError:
    ## special import for CMSSW installations of rootplot
    from PhysicsTools.PythonAnalysis.rootplot.tree2hists import RootTree, Plot
from array import array      # to allow making Float_t arrays for ROOT hists
from math import pi
from ROOT import TH1D, TH2F  # import other kinds of hists as neeeded

def lp(treename,filename):
	specific_plots = []
	if 'El' in treename:
		isorangemax=0.15
	elif 'Mu' in treename:
		isorangemax=0.15
		specific_plots = [
		Plot("Muonparam[5]"        , TH1D("leptonNVHits" , ";Lepton Number of valid hits ;entries/bin", 52, -0.5, 50.5)),
		Plot("Muonparam[8]"        , TH1D("leptonNVPixelHits" , ";Lepton Number of valid pixel hits ;entries/bin", 17, -0.5, 15.5)),
		Plot("Muonparam[3]"        , TH1D("leptonchi2" , ";Lepton #chi^{2} ;entries/bin", 15, 0., 15.)),
		Plot("Muonparam[4]"        , TH1D("leptonTrackerLayersWithMeasurement" , ";Lepton # tracker layers with measurement ;entries/bin", 22, -0.5, 20.5)),
		Plot("Muonparam[9]"        , TH1D("leptonMatchedStations" , ";Lepton # of matched tracker stations ;entries/bin", 11, -0.5, 10.5)),
		Plot("Muonparam[6]"        , TH1D("leptond0" , ";Lepton d0 [cm] ;entries/bin", 100, -0.2, 0.2)),
		Plot("Muonparam[7]"        , TH1D("leptonz0" , ";Lepton z0 [cm] ;entries/bin", 100, -2., 2.))
		]
	else:
		raise NameError('Tree name %s is not recognized'%treename)
	
	import listofplots_cards as lpcards
	bdtplot = lpcards.bdtplot
	#if 'Data' in filename: bdtplot = Plot("-666."           , TH1D("bdt"    , ";BDT;entries/bin", 32, -0.6, 1.))
	#if 'Data' in filename: bdtplot = Plot("-666."           , TH1D("bdt"    , ";BDT;entries/bin", 30, -1., 0.5))
	#if 'Data' in filename: bdtplot = Plot("-666."           , TH1D("bdt"    , ";BDT;entries/bin", 50, -1., 1.))
	##if 'Data' in filename: bdtplot = Plot("BDT9and10jetsplit.BDT9and10jetsplit"           , TH1D("bdt"    , ";BDT;entries/bin", 50, -1., 1.))
	#else: bdtplot =  Plot("BDT"           , TH1D("bdt"    , ";BDT;entries/bin", 32, -0.6, 1.))
	#else: bdtplot =  Plot("BDT"           , TH1D("bdt"    , ";BDT;entries/bin", 30, -1.0, 0.5))
	#else: bdtplot =  Plot("BDTninejet.MVAoutput"           , TH1D("bdt"    , ";BDT;entries/bin", 32, -0.6, 1.))
	#else: bdtplot =  Plot("Gradninejet.MVAoutput"           , TH1D("bdt"    , ";BDT;entries/bin", 10, -5., 5.))
	#else: bdtplot =  Plot("BDTjetsplit.MVAoutput"           , TH1D("bdt"    , ";BDT;entries/bin", 30, -1., 0.5))
	#else: bdtplot =  Plot("BDTjetsplit.BDTjetsplit"           , TH1D("bdt"    , ";BDT;entries/bin", 50, -1., 1.))
	#else: bdtplot =  Plot("BDTjetsplit.BDTjetsplit"           , TH1D("bdt"    , ";BDT;entries/bin", 30, -1., 0.5))
	#else: bdtplot =  Plot("BDT9and10jetsplit.BDT9and10jetsplit"           , TH1D("bdt"    , ";BDT;entries/bin", 30, -1., 0.5))
	##else: bdtplot =  Plot("BDT9and10jetsplit.BDT9and10jetsplit"           , TH1D("bdt"    , ";BDT;entries/bin", 50, -1., 1.))

	plots_list = [bdtplot,
	Plot("multitopness"            , TH1D("multitopness"     , "; Topness;entries/bin", 105, -0.7, 0.35)),
	Plot("jetvec[][0]"           , TH1D("jetpt"    , ";jet p_{T} (GeV);entries/bin", 15, 30., 1500.)),
	Plot("jetvec[][1]"           , TH1D("jeteta"    , ";jet #eta;entries/bin", 50, -2.5, 2.5)),
	Plot("jetvec[][2]"           , TH1D("jetphi"    , ";jet #phi;entries/bin", 50, -pi, pi)),
	Plot("jetvec[][3]"           , TH1D("jetcsv"    , ";jet CSVv2;entries/bin", 100, 0., 1.)),
	Plot("1stjetpt"           , TH1D("1stjetpt"    , ";1st jet p_{T} (GeV);entries/bin", 50, 0., 1500.)),
	Plot("2ndjetpt"           , TH1D("2ndjetpt"    , ";2nd jet p_{T} (GeV);entries/bin", 50, 0., 1000.)),
	Plot("5thjetpt"           , TH1D("5thjetpt"    , ";5th jet p_{T} (GeV);entries/bin", 20, 30., 250.)),
	Plot("6thjetpt"           , TH1D("6thjetpt"    , ";6th jet p_{T} (GeV);entries/bin", 20, 30., 200.)),
	Plot("LeptonPt"           , TH1D("leptonpt"    , ";Lepton p_{T} (GeV);entries/bin", 20, 0., 800.)),
	Plot("LeptonEta"           , TH1D("leptoneta"    , ";Lepton #eta ;entries/bin", 50, -2.5, 2.5)),
	Plot("leptonphi"           , TH1D("leptonphi"    , ";Lepton #phi ;entries/bin", 50, -pi, pi)),
	Plot("leptonIso"           , TH1D("leptonIso"    , ";Lepton Isolation ;entries/bin", 25, 0., isorangemax)),
	Plot("nLtags"           , TH1D("nltags"    , ";Number of loose tags;entries/bin", 8, -0.5, 7.5)),
	Plot("nMtags"           , TH1D("nmtags"    , ";Number of medium tags;entries/bin", 4, 1.5, 5.5)),
	Plot("nTtags"           , TH1D("nttags"    , ";Number of tight tags;entries/bin", 5, -0.5, 4.5)),
	Plot("nJets"            , TH1D("njets"     , ";Number of jets;entries/bin", 9, 5.5, 14.5)),
	Plot("HT"           , TH1D("ht"    , ";HT (GeV);entries/bin", 25, 150., 2000.)),
	Plot("HTb"            , TH1D("HTB"     , ";HTB (GeV);entries/bin", 25, 0., 1000.)),
	Plot("HTH"            , TH1D("HTH"     , ";HTH;entries/bin", 100, 0.1, 1.1)),
	Plot("HTRat"            , TH1D("HTRat"     , ";HTRat;entries/bin", 45, 0., 0.45)),
	Plot("HTX"            , TH1D("HTX"     , ";HTX;entries/bin", 20, 0., 3000.)),
	Plot("SumJetMassX"            , TH1D("SumJetMassX"     , ";Sum jet M (GeV);entries/bin", 50, 0., 3500.)),
	Plot("PU"           , TH1D("pu"    , ";Number of prim. v.;entries/bin", 55, -0.5, 54.5)),
	Plot("NjetsW"           , TH1D("njetsw"    , ";p_{T} weighted jet multiplicity;entries/bin", 20, -0.5, 15.5)),
	#Plot("SFlepton"            , TH1D("SFlepton"     , ";Event SF due to leptons;entries/bin", 100, 0., 2.5)),
	#Plot("SFbtag"            , TH1D("SFbtag"     , ";Event SF due to btag;entries/bin", 100, 0., 5.)),
	#Plot("SFbtagUp"            , TH1D("SFbtagUp"     , ";Event SF due to btag (up variation);entries/bin", 100, 0., 2.5)),
	#Plot("SFbtagDown"            , TH1D("SFbtagDown"     , ";Event SF due to btag (down variation);entries/bin", 100, 0., 2.5)),
	#Plot("SFPU"            , TH1D("SFPU"     , ";Event SF due to PU;entries/bin", 100, 0., 5.)),
	Plot("met"            , TH1D("met"     , ";MET (GeV);entries/bin", 40, 0., 400.)),
	#Plot("csvJetcsv1"            , TH1D("csvJetcsv1"     , ";CSV1;entries/bin", 100, 0., 1.)),
	#Plot("csvJetcsv2"            , TH1D("csvJetcsv2"     , ";CSV2;entries/bin", 100, 0., 1.)),
	Plot("csvJetcsv3"            , TH1D("csvJetcsv3"     , ";CSV3;entries/bin", 100, 0., 1.)),
	Plot("csvJetcsv4"            , TH1D("csvJetcsv4"     , ";CSV4;entries/bin", 100, 0., 1.)),
	#Plot("csvJetpt1"            , TH1D("csvJetpt1"     , ";CSV1;entries/bin", 100, 0., 1.)),
	#Plot("csvJetpt2"            , TH1D("csvJetpt2"     , ";CSV2;entries/bin", 100, 0., 1.)),
	#Plot("csvJetpt3"            , TH1D("csvJetpt3"     , ";CSV3;entries/bin", 100, 0., 1.)),
	#Plot("csvJetpt4"            , TH1D("csvJetpt4"     , ";CSV4;entries/bin", 100, 0., 1.))
	]
	plots_list += specific_plots
	return plots_list
