//////////////////////////////////////////////////////////////////////////////
////         Analysis code for search for Four Top Production.            ////
//////////////////////////////////////////////////////////////////////////////

// ttbar @ NLO 13 TeV:                              //ttbar @ NNLO 8 TeV:
//all-had ->679 * .46 = 312.34                      //all-had -> 245.8 * .46 = 113.068
//semi-lep ->679 *.45 = 305.55                      //semi-lep-> 245.8 * .45 = 110.61
//di-lep-> 679* .09 = 61.113                        //di-lep ->  245.8 * .09 = 22.122
#define _USE_MATH_DEFINES
#include <ctime>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <iostream>
#include <map>
#include <utility>
#include <iterator>

#include <boost/tokenizer.hpp>

#include "TTree.h"

//user code
#include "TopTreeProducer/interface/TRootRun.h"
#include "TopTreeProducer/interface/TRootEvent.h"

#include "TopTreeAnalysisBase/Selection/interface/SelectionTable.h"
#include "TopTreeAnalysisBase/Selection/interface/Run2Selection.h"

#include "TopTreeAnalysisBase/Content/interface/AnalysisEnvironment.h"
#include "TopTreeAnalysisBase/Content/interface/Dataset.h"

#include "TopTreeAnalysisBase/Reconstruction/interface/JetCorrectorParameters.h"
#include "TopTreeAnalysisBase/Reconstruction/interface/JetCorrectionUncertainty.h"

#include "TopTreeAnalysisBase/MCInformation/interface/LumiReWeighting.h"
#include "TopTreeAnalysisBase/MCInformation/interface/JetPartonMatching.h"

#include "TopTreeAnalysisBase/Tools/interface/JetTools.h"
#include "TopTreeAnalysisBase/Tools/interface/TTreeLoader.h"
#include "TopTreeAnalysisBase/Tools/interface/AnalysisEnvironmentLoader.h"
#include "TopTreeAnalysisBase/Tools/interface/LeptonTools.h"
#include "TopTreeAnalysisBase/Tools/interface/SourceDate.h"
#include "TopTreeAnalysisBase/Tools/interface/BTagWeightTools.h"
#include "TopTreeAnalysisBase/Tools/interface/BTagCalibrationStandalone.h"
#include "TopTreeAnalysisBase/Tools/interface/JetCombiner.h"
#include "TopTreeAnalysisBase/Tools/interface/MVATrainer.h"
#include "TopTreeAnalysisBase/Tools/interface/MVAComputer.h"
#include "TopTreeAnalysisBase/Tools/interface/TopologyWorker.h"

#include "BTagSF.h"
#include "CutsTable.h"
#include "HadronicTopReco.h"
#include "EventBDT.h"
#include "Zpeak.h"
#include "Trigger.h"


#include <glog/logging.h>
#include <gflags/gflags.h>
#include "FourTopFlags.h"

#include "Constants.h"

#include "MakeDirectory.h"

#include "Version.h"

#include "FillLeptonArrays.h"
#include "Event.h"
#include "PyAdaBoost.h"

#include "TLorentzVector.h"

using namespace std;
using namespace TopTree;
using namespace reweight;

bool batch =true;

struct HighestCVSBtag
{
    bool operator()( TRootJet* j1, TRootJet* j2 ) const
    {
        return j1->btag_combinedInclusiveSecondaryVertexV2BJetTags() > j2->btag_combinedInclusiveSecondaryVertexV2BJetTags();
    }
};


int main (int argc, char *argv[])
{
    
    gflags::SetVersionString(META_INFO);
    gflags::ParseCommandLineFlags(&argc, &argv, false);
    google::InitGoogleLogging(argv[0]);
    
    
    //Placing arguments in properly typed variables for Dataset creation
    const std::string jobid             = FLAGS_jobid;
    const std::string dName             = FLAGS_dataset_name;
    const std::string dTitle            = FLAGS_dataset_title;
    const bool is_local_out             = FLAGS_is_local_output;
    const int color                     = FLAGS_dataset_color;
    const int ls                        = FLAGS_dataset_linestyle;
    const int lw                        = FLAGS_dataset_linewidth;
    const double normf                  = FLAGS_dataset_norm_factor;
    const double EqLumi                 = FLAGS_dataset_eq_lumi;
    const double xSect                  = FLAGS_dataset_cross_section;
    const double PreselEff              = FLAGS_dataset_preselection_eff;
    const std::string inputChannel      = FLAGS_fourtops_channel;
    const int startEvent                = batch ? 0 : 0;
    const int endEvent                  = FLAGS_nevents;

    std::vector<std::string> vecfileNames;
    boost::char_separator<char> sep(",");
    boost::tokenizer<boost::char_separator<char>> tokens(FLAGS_input_files, sep);
    for (const auto& t : tokens) {
        vecfileNames.push_back(t);
    }
    
    std::cout<<"OUTPUT root file suffix: "<<jobid<<std::endl;


    std::cout<<"argc: "<<argc<<std::endl;
        for(int args = 0; args < argc; args++)
        {
            std::cout<<args<<"  : "<<argv[args]<<std::endl;
        }

    std::cout << "---Dataset accepted from command line---" << std::endl;
    std::cout << "Dataset Name: " << dName << std::endl;
    std::cout << "Dataset Title: " << dTitle << std::endl;
    std::cout << "Dataset color: " << color << std::endl;
    std::cout << "Dataset ls: " << ls << std::endl;
    std::cout << "Dataset lw: " << lw << std::endl;
    std::cout << "Dataset normf: " << normf << std::endl;
    std::cout << "Dataset EqLumi: " << EqLumi << std::endl;
    std::cout << "Dataset xSect: " << xSect << std::endl;
    std::cout << "Dataset File Name: " << vecfileNames[0] << std::endl;
    std::cout << "JET corrections JEC/JER: " << FLAGS_fourtops_jes <<'/'<< FLAGS_fourtops_jer << std::endl;
    std::cout << "Beginning Event: " << startEvent << std::endl;
    std::cout << "Ending Event: " << endEvent << std::endl;
    std::cout << "----------------------------------------" << std::endl;
    for(int vecfiles=0; vecfiles<vecfileNames.size(); vecfiles++){
        std::cout<<"vecfile names: "<<vecfiles<<" : "<<vecfileNames[vecfiles]<<std::endl;
    }
//    ofstream eventlist;
//    eventlist.open ("interesting_events_mu2.txt");

    int passed = 0;
    int preTrig = 0;
    double postTrig = 0;
    int ndefs =0;
    double negWeights = 0, negWeightsPretrig = 0;
    float weightCount = 0.0;
    int eventCount = 0;
    float scalefactorbtageff, mistagfactor;
    string dataSetName = dName;
    string channelpostfix = "";
    string postfix = "_Run2_TopTree_Study"; // to relabel the names of the output file
    
    postfix = postfix + "_" + jobid;
    clock_t start = clock();

    std::cout << "*************************************************************" << std::endl;
    std::cout << " Beginning of the program for the FourTop search ! "           << std::endl;
    std::cout << "*************************************************************" << std::endl;


    ///////////////////////////////////////
    //      Configuration                //
    ///////////////////////////////////////

    bool HadTopOn          = true;		// Enable hadronic top decay finder (trijet bdt)
    bool EventBDTOn        = true;		// Enable event-level tttt discriminant
    bool TrainMVA          = false; // If false, the previously trained MVA will be used to calculate stuff
    bool bTagReweight      = FLAGS_fourtops_btagregular;	// Enable btag SF. btagging reweighting approach: regular btag reweighting
    bool bTagCSVReweight   = FLAGS_fourtops_btagcsvrs;		// Enable btag SF. btagging reweighting approach: csv discriminant reshaping
    bool bTopPt            = FLAGS_fourtops_toprew;		// Enable top transverse momentum reweighting
    bool bLeptonSF         = true;				// Enable lepton SF
    bool debug             = false;				// Verbosity flags used in some classes
    bool applyJER          = true;				// Enable jet energy resolution stochastic smearing
    bool applyJEC          = true;				// Enable jet energy correction
    bool JERUp             = isJERUp();				// JER systematics variation
    bool JERDown           = isJERDown();			// JER systematics variation
    bool JESUp             = isJESUp();				// JES systematics variation
    bool JESDown           = isJESDown();			// JES systematics variation
    bool fillingbTagHistos = false;				// Enable filling of btagging efficiency histograms required for btagging reweighting

    auto electron_id = electronID();				// Switch from VID to cutbased electron ID for e.g. QCD bg estimation
    std::string MVAmethod       = "BDT";			// Top hadronic decays reconstruction MVA method (only "BDT" is supported)


    std::transform(dataSetName.begin(), dataSetName.end(), dataSetName.begin(), ::tolower); // make dataset name lowecase

    // Data VS MC switch (used for corrections/reweighting)
    bool isData = false;
    if(dataSetName.find("data")!=string::npos){
        isData = true;
    }

    // Channel ID flags
    const bool SingleLepton      = true;		// Always true in single lepton analysis

    // Mutually exclusive channel flags
    bool Muon              = false;			// Single electon channel
    bool Electron          = false;			// Single muon channel
    if (batch && inputChannel.find("Mu")!=string::npos){
        Muon = true;
        Electron = false;
    }
    if (batch && inputChannel.find("El")!=string::npos){
        Muon = false;
        Electron = true;
    }
    if(Muon && SingleLepton){
        std::cout<<" ***** USING SINGLE MUON CHANNEL  ******"<<std::endl;
        channelpostfix = "_Mu";
    }
    else if(Electron && SingleLepton){
        std::cout<<" ***** Using SINGLE ELECTRON CHANNEL *****"<<std::endl;
        channelpostfix = "_El";
    }
    else    {
        cerr<<"Correct Channel not selected."<<std::endl;
        exit(1);
    }

    /////////////////////////////////
    //  Set up AnalysisEnvironment //
    /////////////////////////////////

    AnalysisEnvironment anaEnv;
    std::cout<<" - Creating environment ..."<<std::endl;
    anaEnv.PrimaryVertexCollection = "PrimaryVertex";
    anaEnv.JetCollection = "PFJets_slimmedJets";
    anaEnv.FatJetCollection = "FatJets_slimmedJetsAK8";
    //if(isData) anaEnv.METCollection = "PFMET_slimmedMETsMuEGClean";
    anaEnv.METCollection = "PFMET_slimmedMETs"; 
    anaEnv.MuonCollection = "Muons_slimmedMuons";
    anaEnv.ElectronCollection = "Electrons_selectedElectrons";
    anaEnv.GenJetCollection   = "GenJets_slimmedGenJets";
    anaEnv.NPGenEventCollection = "NPGenEvent";
    anaEnv.MCParticlesCollection = "MCParticles";
    anaEnv.loadFatJetCollection = false;
    anaEnv.loadGenJetCollection = true;
    anaEnv.loadNPGenEventCollection = false;
    anaEnv.loadMCParticles = true;
    anaEnv.JetType = 2;
    anaEnv.METType = 2;

    //////////////////////////////////////////////////
    //            PyMVA initialization              //
    //////////////////////////////////////////////////
    std::string path7="MVA/Freyas/noNjetsW/BDTAdaBoost_njets7_40_2.p";
    std::string path8="MVA/Freyas/noNjetsW/BDTAdaBoost_njets8_400_2.p";
    std::string path9="MVA/Freyas/noNjetsW/BDTAdaBoost_njets9_400_2.p";
    std::string path10="MVA/Freyas/noNjetsW/BDTAdaBoost_njets10_400_2.p";
    PyAdaBoost pyada7(path7);
    PyAdaBoost pyada8(path8);
    PyAdaBoost pyada9(path9);
    PyAdaBoost pyada10(path10);

    ///////////////////////////////////////////
    //            Load datasets              //
    ///////////////////////////////////////////

    TTreeLoader treeLoader;
    vector < Dataset* > datasets;    std::cout << " - Creating Dataset ..." << std::endl;
    Dataset* theDataset = new Dataset(dName, dTitle, true, color, ls, lw, normf, xSect, vecfileNames);
    theDataset->SetEquivalentLuminosity(EqLumi);
    datasets.push_back(theDataset);
    dataSetName = theDataset->Name();

    //////////////////////////////////////////////////////
    //     bTag calibration reader and weight tools     //
    //////////////////////////////////////////////////////

    BTagCalibration * bTagCalib;   
    BTagCalibrationReader * bTagReader;
    BTagCalibrationReader * bTagReaderUp;
    BTagCalibrationReader * bTagReaderDown;

    BTagWeightTools *btwt;
    BTagWeightTools *btwtUp;
    BTagWeightTools *btwtDown;
    
    BTagSF* csvrsw;

    
    ///////////////////////////////////////////////////////
    //      Setup Date string and nTuple for output      //
    ///////////////////////////////////////////////////////

    SourceDate *strdate = new SourceDate();
    string date_str = strdate->ReturnDateStr();
    
    std::string channel_dirhist = "output/histo"+channelpostfix;
    std::string date_dirhist = channel_dirhist+"/histo" + date_str +"/";
    int mkdirstatushist = mkdir_p(date_dirhist.c_str());

    TFile* btagEffHistFile_central = nullptr;
    TFile* btagEffHistFile_up = nullptr;
    TFile* btagEffHistFile_down = nullptr;
    if(bTagReweight && !isData ){
        //Btag documentation : http://mon.iihe.ac.be/~smoortga/TopTrees/BTagSF/BTaggingSF_inTopTrees.pdf //v2 or _v2
        bTagCalib = new BTagCalibration("CSVv2","../TopTreeAnalysisBase/Calibrations/BTagging/CSVv2Moriond17_2017_1_26_BtoH.csv");
//        bTagCalib = new BTagCalibration("csvv2", "../TopTreeAnalysisBase/Calibrations/BTagging/CSVv2_80X_ichep_incl_ChangedTo_mujets.csv");
        bTagReader = new BTagCalibrationReader(bTagCalib,BTagEntry::OP_MEDIUM,"mujets","central"); //mujets
        bTagReaderUp = new BTagCalibrationReader(bTagCalib,BTagEntry::OP_MEDIUM,"mujets","up"); //mujets
        bTagReaderDown = new BTagCalibrationReader(bTagCalib,BTagEntry::OP_MEDIUM,"mujets","down"); //mujets

        if(fillingbTagHistos) {
            if (Muon) {
                std::string filename = date_dirhist+"HistosPtEta_"+dataSetName+ jobid+"_Mu.root";
                btagEffHistFile_central  = TFile::Open(filename.c_str(),"UPDATE");
//                filename = "HistosPtEta_"+dataSetName+ jobid+"_Mu_Up.root";
//                btagEffHistFile_up  = TFile::Open(filename.c_str(),"UPDATE");
//                filename = "HistosPtEta_"+dataSetName+ jobid+"_Mu_Down.root";
//                btagEffHistFile_down = TFile::Open(filename.c_str(),"UPDATE");
            }
            else if (Electron) {
                std::string filename = date_dirhist+"HistosPtEta_"+dataSetName+ jobid+"_El.root";
                btagEffHistFile_central  = TFile::Open(filename.c_str(),"UPDATE");
//                filename = "HistosPtEta_"+dataSetName+ jobid+"_El_Up.root";
//                btagEffHistFile_up  = TFile::Open(filename.c_str(),"UPDATE");
//                filename = "HistosPtEta_"+dataSetName+ jobid+"_El_Down.root";
//                btagEffHistFile_down = TFile::Open(filename.c_str(),"UPDATE");
            }
            btwt = new BTagWeightTools(bTagReader,btagEffHistFile_central,30,500,2.4,false);
//            btwtUp = new BTagWeightTools(bTagReaderUp,btagEffHistFile_up,30,500,2.4,false);
//            btwtDown = new BTagWeightTools(bTagReaderDown,btagEffHistFile_down,30,500,2.4,false);
        }    
        else {
            btagEffHistFile_central  = TFile::Open("histos/Hist_powheg_80X.root");
//            btagEffHistFile_central  = TFile::Open("histos/Histo_powheg_76X.root");
//            btagEffHistFile_up  = TFile::Open("histos/Histo_powheg_76X_Down.root","UPDATE");
//            btagEffHistFile_down = TFile::Open("histos/Histo_powheg_76X_Up.root","UPDATE");

            btwt = new BTagWeightTools(bTagReader,btagEffHistFile_central,30,500,2.4,false); 
            btwtUp = new BTagWeightTools(bTagReaderUp,btagEffHistFile_central,30,500,2.4,false); 
            btwtDown = new BTagWeightTools(bTagReaderDown,btagEffHistFile_central,30,500,2.4,false); 
        }
    }

    if(bTagCSVReweight && !isData){
        // BTagCalibration calib_csvv2("csvv2", "../TopTreeAnalysisBase/Calibrations/BTagging/ttH_BTV_CSVv2_13TeV_2015D_20151120.csv");
//        BTagCalibration calib_csvv2("csvv2", "../TopTreeAnalysisBase/Calibrations/BTagging/CSVv2_80X_ichep_incl_ChangedTo_mujets.csv");
        BTagCalibration calib_csvv2("csvv2", "../TopTreeAnalysisBase/Calibrations/BTagging/CSVv2Moriond17_2017_1_26_BtoH.csv"); //TTAB default
        csvrsw = new BTagSF(&calib_csvv2);
    }
//    std::exit(EXIT_SUCCESS);
    /////////////////////////////////////////////////
    //                   Lepton SF                 //
    /////////////////////////////////////////////////
    MuonSFWeight* muonSFWeightID_BCDEF;   
    MuonSFWeight* muonSFWeightID_GH;   
    MuonSFWeight* muonSFWeightIso_BCDEF;
    MuonSFWeight* muonSFWeightIso_GH;
    MuonSFWeight* muonSFWeightTrig_BCDEF;
    MuonSFWeight* muonSFWeightTrig_GH;
    
    TFile *muontrackfile = new TFile("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/Tracking_EfficienciesAndSF_BCDEFGH.root","read");
    TGraph* h_muonSFWeightTrack = static_cast<TGraph*>( muontrackfile->Get("ratio_eff_eta3_dr030e030_corr")->Clone() );//Tracking efficiency as function of eta

    
    ElectronSFWeight* electronSFWeightReco; 
    ElectronSFWeight* electronSFWeightIDISO; 
    ElectronSFWeight* electronSFWeightTrig_BCDEF; 
    ElectronSFWeight* electronSFWeightTrig_GH;
    ElectronSFWeight* electronSFWeightTrig;
    

    // Set up lepton scale factors if lepton corrections are switched on
    // Different datataking periods in 2016 have different correction factors
    // Since MC doesn't know about run dependence of detector performance 
    // luminosity weighted average is used as the correction factor applied to MC
    if(bLeptonSF){
        if(Muon){
            muonSFWeightID_BCDEF = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/MuonID_EfficienciesAndSF_BCDEF.root", "MC_NUM_TightID_DEN_genTracks_PAR_pt_eta/abseta_pt_ratio", true, false, false);
            //muonSFWeightID_BCDEF = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/MuonID_EfficienciesAndSF_BCDEF.root", "MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta/abseta_pt_ratio", true, false, false);
            muonSFWeightID_GH = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/MuonID_EfficienciesAndSF_GH.root", "MC_NUM_TightID_DEN_genTracks_PAR_pt_eta/abseta_pt_ratio", true, false, false);
            //muonSFWeightID_GH = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/MuonID_EfficienciesAndSF_GH.root", "MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta/abseta_pt_ratio", true, false, false);
            muonSFWeightIso_BCDEF = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/MuonIso_EfficienciesAndSF_BCDEF.root", "TightISO_TightID_pt_eta/abseta_pt_ratio", true, false, false);  // Tight RelIso, Tight ID
            //muonSFWeightIso_BCDEF = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/MuonIso_EfficienciesAndSF_BCDEF.root", "TightISO_MediumID_pt_eta/abseta_pt_ratio", true, false, false);  // Tight RelIso, Tight ID
            muonSFWeightIso_GH = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/MuonIso_EfficienciesAndSF_GH.root", "TightISO_TightID_pt_eta/abseta_pt_ratio", true, false, false);  // Tight RelIso, Tight ID
            //muonSFWeightIso_GH = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/MuonIso_EfficienciesAndSF_GH.root", "TightISO_MediumID_pt_eta/abseta_pt_ratio", true, false, false);  // Tight RelIso, Tight ID
            muonSFWeightTrig_BCDEF = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/SingleMuonTrigger_EfficienciesAndSF_RunsBCDEF.root", "IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio", true, false, false);
            muonSFWeightTrig_GH = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/SingleMuonTrigger_EfficienciesAndSF_RunsGH.root", "IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio", true, false, false);
        }
        else if(Electron){
            electronSFWeightReco = new ElectronSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/ElectronSF/20170413/egammaEffi.txt_EGM2D_reco_20170413.root","EGamma_SF2D",true,false,false,true);    
            electronSFWeightIDISO = new ElectronSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/ElectronSF/20170413/egammaEffi.txt_EGM2D_IDcutbTight_20170413.root","EGamma_SF2D",true,false,false);    
            electronSFWeightTrig_BCDEF = new ElectronSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/ElectronSF/Moriond17/TriggerSF_Run2016BCDEF_v2.root","Ele32_eta2p1_WPTight_Gsf_swappedAxes",true,false,false);
            electronSFWeightTrig_GH = new ElectronSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/ElectronSF/Moriond17/TriggerSF_Run2016GH_v2.root","Ele32_eta2p1_WPTight_Gsf_swappedAxes",true,false,false);
            electronSFWeightTrig = new ElectronSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/ElectronSF/SF_HLT_Ele32_eta2p1.root","SF",true,false,false);
        }
    }
    /////////////////////////////////////////////////
    ////                Event BDT                 ///
    /////////////////////////////////////////////////

    EventBDT* eventBDT;
    if (EventBDTOn){
        HadTopOn = true;
        eventBDT = new EventBDT();
        eventBDT->initaliseEventComp();
    }
    std::cout << " Initialized Eventcomputer_ for event_level BDT" << std::endl;

    /////////////////////////////////////////////////
    ////                 Trigger                  ///
    /////////////////////////////////////////////////
    Trigger* trigger = new Trigger(Muon, Electron);
    trigger->bookTriggers();

    /////////////////////////////////////////////////
    //                Top Reco MVA                 //
    /////////////////////////////////////////////////
    HadronicTopReco *hadronicTopReco;
    if(HadTopOn){
        string rootFileName ("~/t2016/output/train"+channelpostfix+"/Train"+postfix+"_"+dName+".root"); //eg. FourTop_Run2_TopTree_Study_Data_Mu.root
	TFile *fout = nullptr;
        if (TrainMVA) fout = new TFile (rootFileName.c_str(), "RECREATE");
        hadronicTopReco = new HadronicTopReco(fout, Muon, Electron, TrainMVA, datasets, MVAmethod, debug, 1.);
    }
    /////////////////////////////////////////////////
    //            vectors of objects               //
    /////////////////////////////////////////////////
    std::cout << " - Variable declaration ..." << std::endl;
    vector < TRootVertex* >   vertex;
    vector < TRootMuon* >     init_muons;
    vector < TRootElectron* > init_electrons;
    vector < TRootJet* >      init_jets;
    vector < TRootJet* >      init_uncor_jets;
    vector < TRootMET* >      mets;
    vector < TRootGenJet* > genjets;

    /////////////////////////////////////////////////
    //              Global variable                //
    /////////////////////////////////////////////////
    TRootEvent* event = 0;
    TRootRun *runInfos = new TRootRun();

    /////////////////////////////////////////////////
    //                 Cuts table                  //
    /////////////////////////////////////////////////
//    CutsTable *cutsTable = new CutsTable(Muon, Electron);
//    cutsTable->AddSelections();
//    cutsTable->CreateTable(datasets, Luminosity);

    /////////////////////////////////////////////////
    //               Pu reweighting                //
    /////////////////////////////////////////////////
    std::cout<<"Getting lumi weights"<<std::endl;
    LumiReWeighting LumiWeights;
    LumiReWeighting LumiWeights_up;
    LumiReWeighting LumiWeights_down;

    LumiWeights = LumiReWeighting("../TopTreeAnalysisBase/Calibrations/PileUpReweighting/MCPileup_Summer16.root", "../TopTreeAnalysisBase/Calibrations/PileUpReweighting/pileup_2016Data80X_Run271036-284044Cert__Full2016DataSet.root", "pileup", "pileup");    // nominal SF
    LumiWeights_up = LumiReWeighting("../TopTreeAnalysisBase/Calibrations/PileUpReweighting/MCPileup_Summer16.root", "../TopTreeAnalysisBase/Calibrations/PileUpReweighting/pileup_2016Data80X_Run271036-284044Cert__Full2016DataSet_sysPlus.root", "pileup", "pileup");    // upward variation
    LumiWeights_down = LumiReWeighting("../TopTreeAnalysisBase/Calibrations/PileUpReweighting/MCPileup_Summer16.root", "../TopTreeAnalysisBase/Calibrations/PileUpReweighting/pileup_2016Data80X_Run271036-284044Cert__Full2016DataSet_sysMinus.root", "pileup", "pileup");    //downward variation
     
    ///////////////////////////////////////////
    ///  Initialise Jet Energy Corrections  ///
    ///////////////////////////////////////////
    
    //////////////////////////////////////////////////
    // Jet corrections are run dependent
    // In addition there are flavour dependent jet correction uncertainties
    // Since 2016 doesn't have dedicated flavour dependent uncertainties, 
    // Run 1 values were used
    ///////////////////////////////////////////////
    vector<JetCorrectorParameters> vCorrParam;
    string pathCalJEC = "../TopTreeAnalysisBase/Calibrations/JECFiles/";

    JetCorrectionUncertainty *jecUnc = nullptr;

    using sharedJetCorrectionUncertainty = shared_ptr<JetCorrectionUncertainty>;
    sharedJetCorrectionUncertainty jecUnc_Gluon(nullptr);
    sharedJetCorrectionUncertainty jecUnc_Quark(nullptr);
    sharedJetCorrectionUncertainty jecUnc_Charm(nullptr);
    sharedJetCorrectionUncertainty jecUnc_Bottom(nullptr);

    if(dName.find("Run2016B")!=string::npos || dName.find("Run2016C")!=string::npos || dName.find("Run2016D")!=string::npos)
    {
	    JetCorrectorParameters *L1JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016BCDV4_DATA/Summer16_23Sep2016BCDV4_DATA_L1FastJet_AK4PFchs.txt");
	    vCorrParam.push_back(*L1JetCorPar);
	    JetCorrectorParameters *L2JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016BCDV4_DATA/Summer16_23Sep2016BCDV4_DATA_L2Relative_AK4PFchs.txt");
	    vCorrParam.push_back(*L2JetCorPar);
	    JetCorrectorParameters *L3JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016BCDV4_DATA/Summer16_23Sep2016BCDV4_DATA_L3Absolute_AK4PFchs.txt");
	    vCorrParam.push_back(*L3JetCorPar);
	    JetCorrectorParameters *L2L3ResJetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016BCDV4_DATA/Summer16_23Sep2016BCDV4_DATA_L2L3Residual_AK4PFchs.txt");
	    vCorrParam.push_back(*L2L3ResJetCorPar);
	    jecUnc = new JetCorrectionUncertainty(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016BCDV4_DATA/Summer16_23Sep2016BCDV4_DATA_Uncertainty_AK4PFchs.txt");
    }
    else if(dName.find("Run2016E")!=string::npos || dName.find("Data_Run2016F")!=string::npos)
    {
	    JetCorrectorParameters *L1JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016EFV4_DATA/Summer16_23Sep2016EFV4_DATA_L1FastJet_AK4PFchs.txt");
	    vCorrParam.push_back(*L1JetCorPar);
	    JetCorrectorParameters *L2JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016EFV4_DATA/Summer16_23Sep2016EFV4_DATA_L2Relative_AK4PFchs.txt");
	    vCorrParam.push_back(*L2JetCorPar);
	    JetCorrectorParameters *L3JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016EFV4_DATA/Summer16_23Sep2016EFV4_DATA_L3Absolute_AK4PFchs.txt");
	    vCorrParam.push_back(*L3JetCorPar);
	    JetCorrectorParameters *L2L3ResJetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016EFV4_DATA/Summer16_23Sep2016EFV4_DATA_L2L3Residual_AK4PFchs.txt");
	    vCorrParam.push_back(*L2L3ResJetCorPar);
	    jecUnc = new JetCorrectionUncertainty(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016EFV4_DATA/Summer16_23Sep2016EFV4_DATA_Uncertainty_AK4PFchs.txt");
    }
    else if(dName.find("Run2016G")!=string::npos)
    {
	    JetCorrectorParameters *L1JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016GV4_DATA/Summer16_23Sep2016GV4_DATA_L1FastJet_AK4PFchs.txt");
	    vCorrParam.push_back(*L1JetCorPar);
	    JetCorrectorParameters *L2JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016GV4_DATA/Summer16_23Sep2016GV4_DATA_L2Relative_AK4PFchs.txt");
	    vCorrParam.push_back(*L2JetCorPar);
	    JetCorrectorParameters *L3JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016GV4_DATA/Summer16_23Sep2016GV4_DATA_L3Absolute_AK4PFchs.txt");
	    vCorrParam.push_back(*L3JetCorPar);
	    JetCorrectorParameters *L2L3ResJetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016GV4_DATA/Summer16_23Sep2016GV4_DATA_L2L3Residual_AK4PFchs.txt");
	    vCorrParam.push_back(*L2L3ResJetCorPar);
	    jecUnc = new JetCorrectionUncertainty(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016GV4_DATA/Summer16_23Sep2016GV4_DATA_Uncertainty_AK4PFchs.txt");
    }
    else if(dName.find("Run2016H")!=string::npos)
    {
	    JetCorrectorParameters *L1JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L1FastJet_AK4PFchs.txt");
	    vCorrParam.push_back(*L1JetCorPar);
	    JetCorrectorParameters *L2JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L2Relative_AK4PFchs.txt");
	    vCorrParam.push_back(*L2JetCorPar);
	    JetCorrectorParameters *L3JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L3Absolute_AK4PFchs.txt");
	    vCorrParam.push_back(*L3JetCorPar);
	    JetCorrectorParameters *L2L3ResJetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L2L3Residual_AK4PFchs.txt");
	    vCorrParam.push_back(*L2L3ResJetCorPar);
	    jecUnc = new JetCorrectionUncertainty(pathCalJEC+"/Summer16_23Sep2016V4_DATA/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_Uncertainty_AK4PFchs.txt");
    }
    else
    {
        JetCorrectorParameters *L1JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_L1FastJet_AK4PFchs.txt");
        vCorrParam.push_back(*L1JetCorPar);
        JetCorrectorParameters *L2JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_L2Relative_AK4PFchs.txt");
        vCorrParam.push_back(*L2JetCorPar);
        JetCorrectorParameters *L3JetCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_L3Absolute_AK4PFchs.txt");
        vCorrParam.push_back(*L3JetCorPar);

	const std::string uncSourceType = JESSource();
	if ( uncSourceType.compare("central") == 0 || uncSourceType.compare("Total_down") == 0 || uncSourceType.compare("Total_up") == 0 ) {
        	jecUnc = new JetCorrectionUncertainty(pathCalJEC+"/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_Uncertainty_AK4PFchs.txt");
   		DLOG(INFO)<<"DEBUG:Total ";
	} else if (uncSourceType.compare("SubTotalScale_up") == 0 || uncSourceType.compare("SubTotalScale_down") == 0) {
		JetCorrectorParameters *MCUncCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_UncertaintySources_AK4PFchs.txt","SubTotalScale");
        	jecUnc = new JetCorrectionUncertainty(*MCUncCorPar);
   		DLOG(INFO)<<"DEBUG:SubTotalScale";
	} else if (uncSourceType.compare("SubTotalPt_up") == 0 || uncSourceType.compare("SubTotalPt_down") == 0) {
		JetCorrectorParameters *MCUncCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_UncertaintySources_AK4PFchs.txt","SubTotalPt");
                jecUnc = new JetCorrectionUncertainty(*MCUncCorPar);
   		DLOG(INFO)<<"DEBUG:SubTotalPt";
	} else if (uncSourceType.compare("SubTotalRelative_up") == 0 || uncSourceType.compare("SubTotalRelative_down") == 0) {
		JetCorrectorParameters *MCUncCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_UncertaintySources_AK4PFchs.txt","SubTotalRelative");
                jecUnc = new JetCorrectionUncertainty(*MCUncCorPar);
   		DLOG(INFO)<<"DEBUG:SubTotalRelative";
	} else if (uncSourceType.compare("SubTotalPileUp_up") == 0 || uncSourceType.compare("SubTotalPileUp_down") == 0) {
		JetCorrectorParameters *MCUncCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_UncertaintySources_AK4PFchs.txt","SubTotalPileUp");
                jecUnc = new JetCorrectionUncertainty(*MCUncCorPar);
   		DLOG(INFO)<<"DEBUG:SubTotalPileUp";
    } else if (uncSourceType.compare("SubTotalTimePtEta_up") == 0 || uncSourceType.compare("SubTotalTimePtEta_down") == 0) {
        JetCorrectorParameters *MCUncCorPar = new JetCorrectorParameters(pathCalJEC+"/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_UncertaintySources_AK4PFchs.txt","TimePtEta");
                jecUnc = new JetCorrectionUncertainty(*MCUncCorPar);
   		DLOG(INFO)<<"DEBUG:SubTotalTimePtEta";
	} else if (uncSourceType.compare("SubTotalFlavor_up") == 0 || uncSourceType.compare("SubTotalFlavor_down") == 0) {
		auto MCUncCorParG = make_shared<JetCorrectorParameters>(pathCalJEC+"/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_UncertaintySources_AK4PFchs.txt","FlavorPureGluon");
            	jecUnc_Gluon = make_shared<JetCorrectionUncertainty>(*MCUncCorParG);
            	auto MCUncCorParQ = make_shared<JetCorrectorParameters>(pathCalJEC+"/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_UncertaintySources_AK4PFchs.txt","FlavorPureQuark");
            	jecUnc_Quark = make_shared<JetCorrectionUncertainty>(*MCUncCorParQ);
            	auto MCUncCorParC = make_shared<JetCorrectorParameters>(pathCalJEC+"/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_UncertaintySources_AK4PFchs.txt","FlavorPureCharm");
            	jecUnc_Charm = make_shared<JetCorrectionUncertainty>(*MCUncCorParC);
            	auto MCUncCorParB = make_shared<JetCorrectorParameters>(pathCalJEC+"/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_UncertaintySources_AK4PFchs.txt","FlavorPureBottom");
            	jecUnc_Bottom = make_shared<JetCorrectionUncertainty>(*MCUncCorParB);
            	jecUnc = new JetCorrectionUncertainty(pathCalJEC+"/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_Uncertainty_AK4PFchs.txt");
	}
    }
    JetTools *jetTools = new JetTools(vCorrParam, jecUnc, true); //true means redo also L1
    auto jetTools_G = make_shared<JetTools>(vCorrParam, jecUnc_Gluon.get(), true); //true means redo also L1
    auto jetTools_Q = make_shared<JetTools>(vCorrParam, jecUnc_Quark.get(), true); //true means redo also L1
    auto jetTools_C = make_shared<JetTools>(vCorrParam, jecUnc_Charm.get(), true); //true means redo also L1
    auto jetTools_B = make_shared<JetTools>(vCorrParam, jecUnc_Bottom.get(), true); //true means redo also L1


    /////////////////////////////////////////////////////////////////////////////////////////////////
    //                                                                                             //
    //                                      Loop on datasets                                       //
    //                                                                                             //
    /////////////////////////////////////////////////////////////////////////////////////////////////
    std::cout << " - Loop over datasets ... " << datasets.size () << " datasets !" << std::endl;
    for (unsigned int d = 0; d < datasets.size(); d++)
    {
        std::cout<<"Load Dataset"<<std::endl;    
        treeLoader.LoadDataset (datasets[d], anaEnv);  //open files and load dataset
        string previousFilename2 = "";
        string currentfilename2 = "";

        /////////////////////////////////////////////////
        //               Craneen setup                 //
        /////////////////////////////////////////////////

	// By default batch processing at T2_BE_IIHE localgrid is assumed,
	// therefore output craneens are saved to /scratch space of the worker node
	// and transfered to /pnfs upon completion

        string Ntupname    = "/scratch/$PBS_JOBID/Craneen_" + dataSetName + postfix + ".root"; 
	if (is_local_out) {	// if output to the user home folder is requested (typically for tests)
        	string channel_dir = "output/Craneens"+channelpostfix;
        	string date_dir = channel_dir+"/Craneens" + date_str +"/";
        	int mkdirstatus = mkdir_p(channel_dir.c_str());			//make "output/Craneens_Mu(El) folder if does not exist 
        	mkdirstatus = mkdir_p(date_dir.c_str());			//make output/Craneens_Mu(El)/Craneensdd_mm_yyyy/ folder if does not exist
        	LOG(INFO) << "created dirs";					//
		Ntupname    = "output/Craneens" + channelpostfix + "/Craneens" + date_str + "/Craneen_" + dataSetName + postfix + ".root";    //for /user output
	}
        std::cout << "Output Craneens File: " << Ntupname << std::endl;
        auto tupfile    = make_shared<TFile>(Ntupname.c_str(),"RECREATE");
        const string Ntuptitle   = "Craneen_" + channelpostfix;
        TTree * tup        = new TTree(Ntuptitle.c_str(), Ntuptitle.c_str());	// Craneen__* tree
        Event myEvent;								// Structure aggregating Craneen leaves
        myEvent.makeBranches(tup);						// Book Craneen branches

	// Book trigger leaves
	cout << "checking triggers: " << endl;
	// trigger variables
	std::array<Int_t,200> triggers_container;
	for(int iter_trig=0; iter_trig< (isData?trigger->triggerListData.size():trigger->triggerListMC.size()) && iter_trig<200; iter_trig++){
		TString trigname;
		if (isData) trigname = trigger->triggerListData[iter_trig];
		if (!isData) trigname = trigger->triggerListMC[iter_trig];
		trigname.ReplaceAll("_v*","");
		trigname.ReplaceAll("_v1","");
		trigname.ReplaceAll("_v2","");
		trigname.ReplaceAll("_v3","");
		trigname.ReplaceAll("_v4","");
		trigname.ReplaceAll("_v5","");
		trigname.ReplaceAll("_v6","");
		trigname.ReplaceAll("_v7","");
		trigname.ReplaceAll("_v8","");
		trigname.ReplaceAll("_v9","");
		trigname.ReplaceAll("_v10","");
		trigname.ReplaceAll("_v11","");
		trigname.ReplaceAll("_v12","");
		TString branchname = trigname+"/I";
		std::cout << "adding trigger to trees " << trigname << " mapped to element " << iter_trig << " " << branchname << std::endl;
		tup->Branch(trigname,&(triggers_container[iter_trig]),branchname);
	}
    	long long runId = 0;			tup -> Branch("Runnr",&runId,"Runnr/L");
	long long evId  = 0;			tup -> Branch("Eventnr",&evId,"Evnr/L");
	long long lumBlkId = 0;			tup -> Branch("Lumisec",&lumBlkId,"Lumisec/L");
	int genFilter = 0;			tup -> Branch("GenFilter",&genFilter,"GenFilter/I");

	std::vector<TLorentzVector> tup_genJets;
	std::vector<TLorentzVector> tup_genLeptons;
	tup -> Branch("genJets",&tup_genJets);
	tup -> Branch("genLeptons",&tup_genLeptons);

    LOG(INFO) << "Output Craneens File: " << Ntupname ;

    ///////////////////////////////////////////////////////////
    // tag tree with code version info
    ///////////////////////////////////////////////////////////
    auto sh_tagtup = std::make_shared<TTree>("tag", "tag");
	std::string tag = META_INFO; 		sh_tagtup -> Branch("Tag",&tag);
    sh_tagtup->Fill();
    sh_tagtup->Write();

    //////////////////////////////////////////////////////////
    // bookkeeping tree for mc luminosity normalization
    //////////////////////////////////////////////////////////

	TTree * booktup = new TTree("bookkeeping", "bookkeeping");
    long long nPV = 0;			booktup -> Branch("nPV",&nPV,"nPV/I");
    double    genweight = 0.;	booktup -> Branch("Genweight",&genweight,"Genweight/D");
        // long long genttxtype = -999;		booktup -> Branch("Genttxtype",&genttxtype,"Genttxtype/I");
        // long long nleptons = -999;		booktup -> Branch("nleptons",&nleptons,"nleptons/I");
        // long long ngenjets = -999;		booktup -> Branch("nGenjets",&ngenjets,"nGenjets/I");
        // long long nbjetsfid = -999;		booktup -> Branch("nbjetsfid",&nbjetsfid,"nbjetsfid/I");
        // long long nbjetsful = -999;		booktup -> Branch("nbjetsful",&nbjetsful,"nbjetsful/I");
        // long long ngenjets20 = -999;		booktup -> Branch("nGenjets20",&ngenjets20,"nGenjets20/I");
        // long long ngenjets20Eta25 = -999;	booktup -> Branch("nGenjets20Eta25",&ngenjets20Eta25,"nGenjets20Eta25/I");
	//booktup -> Branch("genJets",&tup_genJets);
	//booktup -> Branch("genLeptons",&tup_genLeptons);

  
	////////////////////////////////////////////////////////////////
	//	Histograms for b fake and efficiency study	      //
	////////////////////////////////////////////////////////////////
	//
	map<string,shared_ptr<TH1D>> histo1D_my;
	histo1D_my["h_fakeb_jetmult"] 		= make_shared<TH1D>("h_fakeb_jetmult","N wrongly matched b genjets",4,6.5,10.5);
	histo1D_my["h_effb_jetmult"] 		= make_shared<TH1D>("h_effb_jetmult","N correctly matched b genjets",4,6.5,10.5);
	histo1D_my["h_totb_jetmult"] 		= make_shared<TH1D>("h_totb_jetmult","N total b genjets",4,6.5,10.5);

	const int NofPtBins = 20;
	const double PtMin = 30.;
	const double PtMax = 500.;
	const int NofEtaBins = 4;
	map<string,shared_ptr<TH2D>> histo2D_my;
	histo2D_my["h_fakeb_jetmult_pt"] 	= make_shared<TH2D>("h_fakeb_jetmult_pt","N wrongly matched b genjets",NofPtBins,PtMin,PtMax,4,6.5,10.5);
	histo2D_my["h_effb_jetmult_pt"]		= make_shared<TH2D>("h_effb_jetmult_pt","N correctly matched b genjets",NofPtBins,PtMin,PtMax,4,6.5,10.5);
	histo2D_my["h_totb_jetmult_pt"]		= make_shared<TH2D>("h_totb_jetmult_pt","N total b genjets",NofPtBins,PtMin,PtMax,4,6.5,10.5);
	histo2D_my["h_fakeb_eta_pt"] 		= make_shared<TH2D>("h_fakeb_eta_pt","N wrongly matched b genjets",25,-2.5,2.5,NofPtBins,PtMin,PtMax);
	histo2D_my["h_effb_eta_pt"] 		= make_shared<TH2D>("h_effb_eta_pt","N correctly matched b genjets",25,-2.5,2.5,NofPtBins,PtMin,PtMax);
	histo2D_my["h_totb_eta_pt"] 		= make_shared<TH2D>("h_totb_eta_pt","N total b genjets",25,-2.5,2.5,NofPtBins,PtMin,PtMax);

	//Like in Btag weight tools
        map<string,shared_ptr<TH2F>> histo2D_btwt;
	histo2D_btwt["BtaggedJets"] 		= make_shared<TH2F>("BtaggedJets", "Total number of btagged jets", NofPtBins, PtMin, PtMax, NofEtaBins, 0, 2.4);
  	histo2D_btwt["BtaggedBJets"] 		= make_shared<TH2F>("BtaggedBJets", "Total number of btagged b-jets", NofPtBins, PtMin, PtMax, NofEtaBins, 0, 2.4);
	histo2D_btwt["BtaggedCJets"] 		= make_shared<TH2F>("BtaggedCJets", "Total number of btagged c-jets", NofPtBins, PtMin, PtMax, NofEtaBins, 0, 2.4);
	histo2D_btwt["BtaggedLightJets"]    = make_shared<TH2F>("BtaggedLightJets", "Total number of btagged light jets", NofPtBins, PtMin, PtMax, NofEtaBins, 0, 2.4);
	histo2D_btwt["TotalNofBJets"] 		= make_shared<TH2F>("TotalNofBJets", "Total number of b-jets", NofPtBins, PtMin, PtMax, NofEtaBins, 0, 2.4);
	histo2D_btwt["TotalNofCJets"] 		= make_shared<TH2F>("TotalNofCJets", "Total number of c-jets", NofPtBins, PtMin, PtMax, NofEtaBins, 0, 2.4);
	histo2D_btwt["TotalNofLightJets"] 	= make_shared<TH2F>("TotalNofLightJets", "Total number of light jets", NofPtBins, PtMin, PtMax, NofEtaBins, 0, 2.4);

  
	////////////////////////////////////////////////////////////////
	//	Histograms for 	cutflow table                         //
	////////////////////////////////////////////////////////////////
	//
	map<string,shared_ptr<TH1>> histo_cutflow;
	const int NofCuts = 10;
	const char* cutLabels[NofCuts] = {"Total", "Good PV", "SL triggers", "Event cleaning", "One lepton", "Jet multiplicity", "N_{tags}^{m}>2", "Lepton iso.", "HT>500", "MET>50"};
	map<string,int> cut2binID;
	histo_cutflow["cutflow"]             = make_shared<TH1D>("cutflow", "Total number of events passing the cut. SF included. Lumi weight not included.", 
								 NofCuts, 0.5, NofCuts+0.5);
	for (int iCut=0; iCut<NofCuts; ++iCut) {
		cut2binID[cutLabels[iCut]] = iCut+1;
		histo_cutflow["cutflow"]->GetXaxis()->SetBinLabel(cut2binID.at(cutLabels[iCut]),cutLabels[iCut]);
	}


        ////////////////////////////////////////////////////////////
        //       Define object containers and initalisations      //
        ////////////////////////////////////////////////////////////

        float BDTScore, BDTScore1, MHT, MHTSig, STJet, leptonvalidhits, leptoneta, leptonpt, leptonphi, electronpt, electroneta, bjetpt, EventMass, EventMassX, SumJetMass, SumJetMassX, H, HX;
        float HTHi, HTRat, HT, HTX, HTH, HTXHX, sumpx_X, sumpy_X, sumpz_X, sume_X, sumpx, sumpy, sumpz, sume, jetpt, PTBalTopEventX, PTBalTopSumJetX, PTBalTopMuMet;     
        int itrigger = -1, previousRun = -1;
        int currentRun;           
        vector<TRootElectron*> selectedElectrons;
        vector<TRootPFJet*>    selectedOrigJets; //all original jets before jet lepton cleaning
        vector<TRootPFJet*>    selectedOrigUncorJets; //all original jets before jet lepton cleaning
        vector<TRootPFJet*>    selectedJets; //all jets after jet lepton cleaning
        vector<TRootPFJet*>    selectedUncorJets; //all jets after jet lepton cleaning
        vector<TRootPFJet*>    selectedJets2; //after removal of 2 highest CSVL btags
        vector<TRootPFJet*>    selectedpreJECJERJets;

        vector<TRootMuon*>     selectedMuons;
        vector<TRootElectron*> selectedExtraElectrons;
        vector<TRootElectron*> selectedOrigElectrons;
        vector<TRootElectron*> selectedOrigExtraElectrons;

        vector<TRootMuon*>     selectedExtraMuons;
        selectedElectrons.reserve(10);
        selectedMuons.reserve(10);
        vector<TRootPFJet*>      selectedJets2ndPass;
        vector<TRootPFJet*>      selectedJets3rdPass;
        vector<TRootPFJet*>      MVASelJets1;
        vector<TRootJet*>      selectedLBJets; //CSVL btags
        vector<TRootJet*>      selectedMBJets; //CSVM btags
        vector<TRootJet*>      selectedTBJets; //CSVT btags
        vector<TRootJet*>      selectedLightJets;
        int iFile2 = -1;
        datasets[d]->runTree()->SetBranchStatus("runInfos*",1);
        datasets[d]->runTree()->SetBranchAddress("runInfos",&runInfos);
        if (isData) TrainMVA=false;

        //////////////////////////////////////////////////////////
        //                  Load Topology worker                //
        //////////////////////////////////////////////////////////  tools for getting event variables based on the topology
        
        TopologyWorker* topologyW = new TopologyWorker(false);

        ///////////////////////////////////////////////////////////
        //             Get # of events to run over               //
        ///////////////////////////////////////////////////////////

        // int start = 0;
        long long ending = datasets[d]->NofEvtsToRunOver();    std::cout <<"Number of events in full dataset = "<<  ending  <<std::endl;
        long long event_start = startEvent; //set start of for loop to input startEvent
        long long end_d = ending; //initialise end of for loop to end of dataset

        if(endEvent <ending && endEvent>0 ) end_d = endEvent; // if the input endEvent is less than total events in dataset (and greater than 0), set max of for loop to endEvent
        
        std::cout <<"Will run over "<<  end_d<< " events..."<<std::endl;    
        std::cout <<"Starting event = = = = "<< event_start  << std::endl;

        ////////////////////////////////////////////////////////////////////////////////
        //                                 Loop on events                             //
        ////////////////////////////////////////////////////////////////////////////////
	
        auto printjetdata = [](const TRootJet* j) {std::cout << j->Pt() << " " << j->Eta() << " " << j->partonFlavour() << std::endl;};

        for (long long ievt = event_start; ievt < end_d; ievt++)
        {
            LOG(INFO) <<"START OF EVENT LOOP";

            BDTScore= -99999.0, BDTScore1=-99999.0, MHT = 0., MHTSig = 0., leptonvalidhits = 0., leptoneta = 0., leptonpt =0., electronpt=0., electroneta=0., bjetpt =0., STJet = 0.;
            EventMass =0., EventMassX =0., SumJetMass = 0., SumJetMassX=0., HTHi =0., HTRat = 0;  H = 0., HX =0., HT = 0., HTX = 0.;
            HTH=0.,HTXHX=0., sumpx_X = 0., sumpy_X= 0., sumpz_X =0., sume_X= 0. , sumpx =0., sumpy=0., sumpz=0., sume=0., jetpt =0.;
            PTBalTopEventX = 0., PTBalTopSumJetX =0.;

            unsigned long ievt_d = ievt;

            if(ievt%1000 == 0)
            {
                std::cout<<"Processing the "<<ievt<<"th event, time = "<< ((double)clock() - start) / CLOCKS_PER_SEC 
                << " ("<<100*(ievt-0)/(ending-0)<<"%)"<<flush<<"\r"<<std::endl;
            }

            double scaleFactor = 1.;  // scale factor for the event
            bool trigged = false;  // Disabling the HLT requirement
            LOG(INFO) <<"Load Event";
            event = treeLoader.LoadEvent (ievt, vertex, init_muons, init_electrons, init_jets, mets, debug);
	    init_uncor_jets.clear();
	    for( auto j: init_jets ) {
		init_uncor_jets.push_back(new TRootPFJet(*(static_cast<TRootPFJet*>(j))));
	    }
	    
            if (!isData) {
                genjets = treeLoader.LoadGenJet(ievt,false);
            }

            vector<TRootMCParticle*> mcParticles_flav;
            treeLoader.LoadMCEvent(ievt, 0, mcParticles_flav,false);

            ///////////////////////////////////////////
            //      Set up for miniAOD weights       //
            ///////////////////////////////////////////

            datasets[d]->eventTree()->LoadTree(ievt); 
            LOG(INFO) <<"load tree";

            currentRun  = event->runId(); 
            LOG(INFO) <<"got run ID";

            runId    = event->runId(); 
            evId     = event->eventId();
            lumBlkId = event->lumiBlockId();
            nPV      = event->nTruePU();
            if(!isData){
            genweight=1.0;
		    if (event->getWeight(1)!= -9999) { genweight = (event->getWeight(1))/(abs(event->originalXWGTUP())); } 
		    if (event->getWeight(1001)!= -9999) { genweight = (event->getWeight(1001))/(abs(event->originalXWGTUP())); }
	    } else {
            genweight = 1.0;
        }
	    histo_cutflow["cutflow"]->Fill(cut2binID.at("Total"),genweight);

        // genttxtype = event->getgenTTX_id();
	    // ngenjets = genjets.size();   
	    // ngenjets20 = std::count_if( std::begin(genjets), std::end(genjets), [](TRootGenJet* jet){return (jet->Pt()>20);} );   
	
	    // auto top16010_fidpscuts = [](TRootGenJet* jet){return ( jet->Pt()>20&&fabs(jet->Eta())<2.5); };
	    // ngenjets20Eta25 = std::count_if( std::begin(genjets), std::end(genjets), top16010_fidpscuts );   

	    // auto top16010b_fidpscuts = [](TRootGenJet* jet){return (jet->Pt()>20 && fabs(jet->Eta())<2.5 && fabs(jet->type()) == 5); };
	    // nbjetsfid = std::count_if( std::begin(genjets), std::end(genjets), top16010b_fidpscuts); 
	    //// auto top16010b_fidpscuts = [](TRootMCParticle* p){return ( p->Pt()>20&&fabs(p->Eta())<2.5)&&fabs(p->type())==5&&p->isLastCopy();};
	    ////nbjetsfid = std::count_if( std::begin(mcParticles_flav), std::end(mcParticles_flav), top16010b_fidpscuts); 
	    // auto top16010b_fulpscuts = [](TRootGenJet* jet){return jet->Pt()>20&&fabs(jet->type())==5;};
	    // nbjetsful = std::count_if( std::begin(genjets), std::end(genjets), top16010b_fulpscuts); 
	    //auto top16010b_fulpscuts = [](TRootMCParticle* p){return p->Pt()>20&&fabs(p->type())==5&&p->isLastCopy();};
	    //nbjetsful = std::count_if( std::begin(mcParticles_flav), std::end(mcParticles_flav), top16010b_fulpscuts); 

	    // auto top16010_fidleptons = [](TRootMCParticle* p){return (fabs(p->type())==11 || fabs(p->type())==13) && p->Pt()>20 && fabs(p->Eta())<2.4 &&
								    //   p->isLastCopy() && fabs(p->grannyType())==6; };
		    // nleptons = std::count_if( std::begin(mcParticles_flav), std::end(mcParticles_flav), top16010_fidleptons );

	    auto push_genlepton2lorentz = [&tup_genLeptons](TRootMCParticle* p){
		if ( (((p->status()==1) && ( fabs(p->type())==11 || fabs(p->type())==13)) || ( p->status()==2 && fabs(p->type())==15 )) && fabs(p->grannyType())==6) 
			tup_genLeptons.emplace_back(p->Px(),p->Py(),p->Pz(),p->E());
		else ;
	    };
	    tup_genLeptons.clear();
	    //std::for_each( std::begin(mcParticles_flav), std::end(mcParticles_flav), push_genlepton2lorentz);

	    auto push_genjet2lorentz = [&tup_genJets](TRootGenJet* jet){
		tup_genJets.emplace_back(TLorentzVector(jet->Px(),jet->Py(),jet->Pz(),jet->E()));
	    };
	    //std::for_each( std::begin(genjets), std::end(genjets), push_genjet2lorentz );

	    //double HT=0.;
	    //for (auto genjet: genjets ) {
	    //    if (genjet->Pt()>30 && abs(genjet->Eta())<2.4) HT+=genjet->Pt();
	    //}
	    //cout << "EventID: " << event->eventId() << " genHT: " << HT << endl;

	    booktup -> Fill();
	    tup_genJets.clear();
	    tup_genLeptons.clear();
   
            int treenumber = datasets[d]->eventTree()->GetTreeNumber(); 
            currentfilename2 = datasets[d]->eventTree()->GetFile()->GetName();
            if(previousFilename2 != currentfilename2){
                previousFilename2 = currentfilename2;
                iFile2++;
                std::cout<<"got tree number: "<<treenumber<<std::endl;
                std::cout<<"File changed!!!! => iFile2 = "<<iFile2 << " new file is " << datasets[d]->eventTree()->GetFile()->GetName() << " in sample " << datasets[d]->Name() << std::endl;
            }
            //////////////////////////////////////
            ///  Jet Energy Scale Corrections  ///
            //////////////////////////////////////
            if (applyJER && !isData)
            {
                if(JERDown)      jetTools->correctJetJER(init_jets, genjets, mets[0], "minus", false);
                else if(JERUp)   jetTools->correctJetJER(init_jets, genjets, mets[0], "plus", false);
                else {
			jetTools->correctJetJER(init_jets, genjets, mets[0], "nominal", false);
			jetTools->correctJetJER(init_uncor_jets, genjets, mets[0], "nominal", false);
		}
                /// Example how to apply JES systematics
            }
		//std::cout << "Before correction" << std::endl;
		//for_each( std::begin(init_jets), std::end(init_jets), printjetdata);

	    if(JESSource().find("SubTotalFlavor")==string::npos){		//If regular jet correction
            	if(JESDown) jetTools->correctJetJESUnc(init_jets, "minus", 1);
            	if(JESUp) jetTools->correctJetJESUnc(init_jets, "plus", 1);
	    } else {
		if(JESDown) {
		    for(auto jet: init_jets){
                    	if(abs(jet->partonFlavour())==5) jetTools_B->correctJetJESUnc(jet, "minus", 1);
                    	if(abs(jet->partonFlavour())==4) jetTools_C->correctJetJESUnc(jet, "minus", 1);
                    	if(abs(jet->partonFlavour())==21 || jet->partonFlavour()==0) jetTools_G->correctJetJESUnc(jet, "minus", 1);
                    	if(abs(jet->partonFlavour())>0 && abs(jet->partonFlavour())<4) jetTools_Q->correctJetJESUnc(jet, "minus", 1);
		    }
		}
		if(JESUp) {
		    for(auto jet: init_jets){
                    	if(abs(jet->partonFlavour())==5) jetTools_B->correctJetJESUnc(jet, "plus", 1);
                    	if(abs(jet->partonFlavour())==4) jetTools_C->correctJetJESUnc(jet, "plus", 1);
                    	if(abs(jet->partonFlavour())==21 || jet->partonFlavour()==0) jetTools_G->correctJetJESUnc(jet, "plus", 1);
                    	if(abs(jet->partonFlavour())>0 && abs(jet->partonFlavour())<4) jetTools_Q->correctJetJESUnc(jet, "plus", 1);
		    }
		}
	    }
		//std::cout << "After correction" << std::endl;
		//for_each( std::begin(init_jets), std::end(init_jets), printjetdata);


            if (applyJEC)   ///should this have  && dataSetName.find("Data")==string::npos
            {
                jetTools->correctJets(init_jets, event->fixedGridRhoFastjetAll(), isData);
                jetTools->correctJets(init_uncor_jets, event->fixedGridRhoFastjetAll(), isData);
            }

            ///////////////////////////////////////////////////////////
            //           Object definitions for selection            //
            ///////////////////////////////////////////////////////////
            Run2Selection r2selection(init_jets, init_muons, init_electrons, mets);
            Run2Selection r2uncor_selection(init_uncor_jets, init_muons, init_electrons, mets);
		//std::cout << "Init After correction" << std::endl;
		//for_each( std::begin(init_jets), std::end(init_jets), printjetdata);
		//std::cout << "Init Before correction" << std::endl;
		//for_each( std::begin(init_uncor_jets), std::end(init_uncor_jets), printjetdata);

            int nMu = 0, nEl = 0, nLooseMu = 0, nLooseEl = 0; //number of (loose) muons/electrons

            LOG(INFO) <<"Get jets";
            //selectedOrigJets                                    = r2selection.GetSelectedJets(25.,2.4,true,"Loose");                                        
            selectedOrigJets                                    = r2selection.GetSelectedJets(30.,2.4,true,"Loose");                                        
            selectedOrigUncorJets                                    = r2uncor_selection.GetSelectedJets(30.,2.4,true,"Loose");                                        
            if(Electron){
                LOG(INFO) <<"Get Loose Muons";
                selectedMuons                                       = r2selection.GetSelectedMuons(10, 2.5, 0.25, "Loose", "Summer16"); 
                nMu = selectedMuons.size();
                LOG(INFO) <<"Get Tight Electrons";                                                                                          
		switch (electron_id) {
			case ElectronID::VIDbased: selectedOrigElectrons = r2selection.GetSelectedElectrons(35, 2.4, "Tight", "Spring16_80X", true, true); 
						   break;
			case ElectronID::CUTbased: selectedOrigElectrons = r2selection.GetSelectedElectrons(35, 2.4, "Tight", "Spring16_80X", true, false);
        					   vector<TRootElectron*> selectedFakeTightOrigElectrons = r2selection.GetSelectedElectrons(35, 2.4, "FakeTight", "Spring16_80X", true, false);
						   selectedOrigElectrons.insert(selectedOrigElectrons.end(),
										std::make_move_iterator(selectedFakeTightOrigElectrons.begin()),
										std::make_move_iterator(selectedFakeTightOrigElectrons.end()));
						   break;
		}
                LOG(INFO) <<"Get Loose Electrons";
                selectedOrigExtraElectrons                          = r2selection.GetSelectedElectrons(15, 2.5, "Veto", "Spring16_80X", true, true); 
            }
            else if(Muon){
                LOG(INFO) <<"Get Tight Muons";
		selectedMuons                                       = r2selection.GetSelectedMuons(35, 2.4, 100., "Tight", "Summer16");
                //selectedMuons                                       = r2selection.GetSelectedMuons(26, 2.1, 1000.0, "Tight", "Summer16"); 
                //LOG(INFO) <<"Get Medium Muons";
                //selectedMuons                                       = r2selection.GetSelectedMuons(26, 2.1, 0.15, "Medium", "Summer16"); 
                nMu = selectedMuons.size(); //Number of Muons in Event
                selectedOrigElectrons                                   = r2selection.GetSelectedElectrons(15, 2.5, "Veto", "Spring16_80X", true, true);
                LOG(INFO) <<"Get Loose Electrons";    
                selectedExtraMuons                                  = r2selection.GetSelectedMuons(10, 2.5, 0.25, "Loose", "Summer16"); 
                LOG(INFO) <<"Get Loose Muons";
                nLooseMu = selectedExtraMuons.size();   //Number of loose muons      
            }

            //remove electrons between 1.4442 and 1.5660
            auto bCrackVeto = false;
            selectedElectrons.clear();
            for(int e_iter=0; e_iter<selectedOrigElectrons.size();e_iter++){
                if(selectedOrigElectrons[e_iter]->Eta()<=1.4442 || selectedOrigElectrons[e_iter]->Eta()>=1.5660){
                    selectedElectrons.push_back(selectedOrigElectrons[e_iter]);
		    bCrackVeto = false;
                } else {
		    bCrackVeto = true;
                }
            }
            nEl = selectedElectrons.size(); //Number of Electrons in Event   

            selectedExtraElectrons.clear();
            if(Electron){
                for(int e_iter=0; e_iter<selectedOrigExtraElectrons.size();e_iter++){
                    if(selectedOrigExtraElectrons[e_iter]->Eta()<=1.4442 || selectedOrigExtraElectrons[e_iter]->Eta()>=1.5660){
                        selectedExtraElectrons.push_back(selectedOrigExtraElectrons[e_iter]);
                    }
                }
                nLooseEl = selectedExtraElectrons.size(); //Number of loose electrons
            }

            /////////////////////////////////////////////////
            //            Jet lepton cleaning              //
            /////////////////////////////////////////////////
            selectedJets.clear();
            selectedUncorJets.clear();
            //std::cout<<nMu<<"<--nmu  nEl-->"<<nEl<<std::endl;
            if(Muon && nMu>0){
                for (int origJets=0; origJets<selectedOrigJets.size(); origJets++){
                    if(selectedOrigJets[origJets]->DeltaR(*selectedMuons[0])>0.4){
                        selectedJets.push_back(selectedOrigJets[origJets]);
                    }                    
                }
                for (int origJets=0; origJets<selectedOrigUncorJets.size(); origJets++){
                    if(selectedOrigUncorJets[origJets]->DeltaR(*selectedMuons[0])>0.4){
                        selectedUncorJets.push_back(selectedOrigUncorJets[origJets]);
                    }                    
                }
            }
            else if(Electron && nEl>0){
                for (int origJets=0; origJets<selectedOrigJets.size(); origJets++){
                    if(selectedOrigJets[origJets]->DeltaR(*selectedElectrons[0])>0.4){
                        selectedJets.push_back(selectedOrigJets[origJets]);
                    }                       
                }
                for (int origJets=0; origJets<selectedOrigUncorJets.size(); origJets++){
                    if(selectedOrigUncorJets[origJets]->DeltaR(*selectedElectrons[0])>0.4){
                        selectedUncorJets.push_back(selectedOrigUncorJets[origJets]);
                    }                    
                }
            }
            else {
		selectedJets = selectedOrigJets;
		selectedUncorJets = selectedOrigUncorJets;
	    }

	    //auto printPtBtag = [](const TRootPFJet* jet){
	    //    cout << setw(10) << jet->Pt() << setw(10) << jet->btag_combinedInclusiveSecondaryVertexV2BJetTags() << endl;
	    //};
	    //std::for_each(selectedJets.begin(), selectedJets.end(), printPtBtag);
	    //auto noLightsBelow30 = [](const TRootPFJet* jet) {
	    //    bool result = false;
            //    if (jet -> btag_combinedInclusiveSecondaryVertexV2BJetTags() < 0.8484 && jet -> Pt() < 30.) result = true;
            //    return result;
	    //};
	    //selectedJets.erase( std::remove_if( selectedJets.begin(), selectedJets.end(), noLightsBelow30 ), selectedJets.end() );

            ///////////////////////////////////////////////////////////////////////////////////
            // Preselection looping over Jet Collection                                      //
            // Summing HT and calculating leading, lagging, and ratio for Selected and BJets //
            ///////////////////////////////////////////////////////////////////////////////////

            selectedLBJets.clear();
            selectedMBJets.clear();
            selectedTBJets.clear();
            selectedLightJets.clear();

            float HTb = 0.;  //calculate assigning loose, medium and tight tags
            for (Int_t seljet =0; seljet < selectedJets.size(); seljet++ )
            {
                if (selectedJets[seljet]->btag_combinedInclusiveSecondaryVertexV2BJetTags() >  0.5426    ) //0.605
                {
                    selectedLBJets.push_back(selectedJets[seljet]);
                    if (selectedJets[seljet]->btag_combinedInclusiveSecondaryVertexV2BJetTags() > 0.8484 ) //0.890
                    {
                        HTb += selectedJets[seljet]->Pt();
                        selectedMBJets.push_back(selectedJets[seljet]);
                        if (selectedJets[seljet]->btag_combinedInclusiveSecondaryVertexV2BJetTags() > 0.9535 ) //0.970
                        {
                            selectedTBJets.push_back(selectedJets[seljet]);
                        }
                    }
                }
                else
                {
                    selectedLightJets.push_back(selectedJets[seljet]);
                }
            }

	    //auto jetPtSelector = [](TRootJet* jet){ 
	    //    if (jet->btag_combinedInclusiveSecondaryVertexV2BJetTags() <= 0.8484 && jet->Pt()<30. ) return true; 
	    //    else return false;
	    //};
	    //selectedJets.erase(std::remove_if(selectedJets.begin(),selectedJets.end(),jetPtSelector),selectedJets.end());

            float nJets = selectedJets.size(); //Number of Jets in Event
            float nLtags = selectedLBJets.size(); //Number of CSVL tags in Event (includes jets that pass CSVM & CSVT)
            float nMtags = selectedMBJets.size(); //Number of CSVM tags in Event (includes jets that pass CSVT)
            float nTtags = selectedTBJets.size(); //Number of CSVT tags in Event 
            float nLights=selectedLightJets.size();


            //htrat leading lagging calculation
            float temp_HT = 0.;
            float HT_leading = 0.;
            float HT_lagging = 0.;
            float HTRat = 0;
            for (Int_t seljet0 =0; seljet0 < selectedJets.size(); seljet0++ ){
                temp_HT += selectedJets[seljet0]->Pt();
                if (seljet0 < 4){
                    HT_leading += selectedJets[seljet0]->Pt();
                }else{
                    HT_lagging += selectedJets[seljet0]->Pt();
                }
            }

            //HTRat = HT_leading/HT_lagging;

            
            /////////////////////////////////
            //        Gen weights          //
            /////////////////////////////////

            double weight_0 = 1; //nominal
            double weight_1 = 1, weight_2 = 1, weight_3 = 1, weight_4 = 1, weight_5 = 1, weight_6 = 1, weight_7 = 1, weight_8 = 1;
            double weight_hdamp_up = 1., weight_hdamp_dw = 1.;
	    double weight_ct10 = 1., weight_mmht14 = 1.;
            double weight_nnpdf[101]; std::fill_n( weight_nnpdf, 101, -99.);
            auto ttXtype =  -1; // ttbb, ttcc, ttx event type
	    auto ttXrew  = 1., ttXrew_up = 1., ttXrew_down = 1.;  // heavy-flavour reweighting factor

            if(!isData){
                ttXtype = event->getgenTTX_id();
		if(dataSetName.find("TTJets")!=string::npos || 
           dataSetName.find("TTFSRS")!=string::npos || 
           dataSetName.find("TTISR")!=string::npos || 
           dataSetName.find("TTUE")!=string::npos || 
           dataSetName.find("TTCR")!=string::npos || 
           dataSetName.find("TTHdamp")!=string::npos || 
           dataSetName.find("TTScale")!=string::npos){
			if (ttXtype % 100 > 50) {
				ttXrew  = 1.;	
                                ttXrew_up = 1.35;
                                ttXrew_down = 0.65;
				//ttXrew  = 4.0/3.2;	//see TOP-16-10 for cross sections
                        	//ttXrew_up = (4.0 + 0.6 + 1.3) / (3.2 - 0.4);
                        	//ttXrew_down = (4.0 - 0.6 - 1.3) / (3.2 + 0.4);

			}
			if (ttXtype % 100 == 0) {	//see https://twiki.cern.ch/twiki/bin/view/CMSPublic/GenHFHadronMatcher#Event_categorization_example_2
				//ttXrew  = 184./257.;				//0.716
				//ttXrew_up = (184. + 6. + 33.) / (257. - 26.);	//0.965
				//ttXrew_down = (184. - 6. - 33.) / (257. + 26.);	//0.512
			}
			scaleFactor *= ttXrew;
		}
		
                if(event->getWeight(1)!= -9999){
                    weight_0 = (event->getWeight(1))/(abs(event->originalXWGTUP()));  
                    weight_1 = (event->getWeight(2))/(abs(event->originalXWGTUP()));                
                    weight_2 = (event->getWeight(3))/(abs(event->originalXWGTUP()));                
                    weight_3 = (event->getWeight(4))/(abs(event->originalXWGTUP()));                
                    weight_4 = (event->getWeight(5))/(abs(event->originalXWGTUP()));                
                    weight_5 = (event->getWeight(6))/(abs(event->originalXWGTUP()));                
                    weight_6 = (event->getWeight(7))/(abs(event->originalXWGTUP()));                
                    weight_7 = (event->getWeight(8))/(abs(event->originalXWGTUP()));                
                    weight_8 = (event->getWeight(9))/(abs(event->originalXWGTUP()));                    
            } else if (event->getWeight(1001)!= -9999){
                    weight_0 = (event->getWeight(1001))/(abs(event->originalXWGTUP()));  
                    weight_1 = (event->getWeight(1002))/(abs(event->originalXWGTUP()));                
                    weight_2 = (event->getWeight(1003))/(abs(event->originalXWGTUP()));                
                    weight_3 = (event->getWeight(1004))/(abs(event->originalXWGTUP()));                
                    weight_4 = (event->getWeight(1005))/(abs(event->originalXWGTUP()));                
                    weight_5 = (event->getWeight(1006))/(abs(event->originalXWGTUP()));                
                    weight_6 = (event->getWeight(1007))/(abs(event->originalXWGTUP()));                
                    weight_7 = (event->getWeight(1008))/(abs(event->originalXWGTUP()));                
                    weight_8 = (event->getWeight(1009))/(abs(event->originalXWGTUP()));                    
		    if (dataSetName.find("tttt")!=string::npos) {
			weight_6 = weight_5;
			weight_8 = weight_7;
		    }
                }

		DLOG(INFO) << "GEN weights:" << setw(10) << weight_0 << setw(10) << weight_1 << setw(10) << weight_2 << setw(10) << weight_3
					     << setw(10) << weight_4 << setw(10) << weight_5 << setw(10) << weight_6 << setw(10) << weight_7
					     << setw(10) << weight_8 << endl;
		// hdamp variation
		if (event->getWeight(1001)!= -9999) {
			weight_hdamp_up = event->getWeight(5019)/fabs(event->originalXWGTUP());
			weight_hdamp_dw = event->getWeight(5010)/fabs(event->originalXWGTUP());
			DLOG(INFO) << "hdamp w(up)= " << weight_hdamp_up << "\t" << "hdamp w(down)= " << weight_hdamp_dw;
		}
		// pdf envelope variations (NNPDF30, CT10, MMHT14)
		if (event->getWeight(1001)!= -9999) {
			if(dataSetName.find("TTJets")!=string::npos ||
                dataSetName.find("TTFSRS")!=string::npos || 
                dataSetName.find("TTISR")!=string::npos || 
                dataSetName.find("TTUE")!=string::npos || 
                dataSetName.find("TTCR")!=string::npos || 
                dataSetName.find("TTHdamp")!=string::npos || 
                dataSetName.find("TTScale")!=string::npos){
				auto min_weight_nnpdf30=99999.;
				auto max_weight_nnpdf30=-99999.;
				int index = 0;
				for (unsigned int weight_id=2001; weight_id<=2100; weight_id++) {
					auto temp = event->getWeight(weight_id)/fabs(event->originalXWGTUP());
					weight_nnpdf[index++]=temp;
				}
				std::stringstream debug_nnpdf_weights;
				for (index=0;index<=100;index++) debug_nnpdf_weights << index << ":" << weight_nnpdf[index] << " ";
				DLOG(INFO) << "w(nnpdf)= " << debug_nnpdf_weights.str();
				//auto min_weight_ct10=99999.;
				//auto max_weight_ct10=-99999.;
				//for (unsigned int weight_id=3001; weight_id<=3057; weight_id++) {
				//	auto temp = event->getWeight(weight_id)/fabs(event->originalXWGTUP());
				//	if (temp < min_weight_ct10) min_weight_ct10 = temp;
				//	if (temp > max_weight_ct10) max_weight_ct10 = temp;
				//}
				//auto min_weight_mmht14=99999.;
				//auto max_weight_mmht14=-99999.;
				//for (unsigned int weight_id=4001; weight_id<=4051; weight_id++) {
				//	auto temp = event->getWeight(weight_id)/fabs(event->originalXWGTUP());
				//	if (temp < min_weight_mmht14) min_weight_mmht14 = temp;
				//	if (temp > max_weight_mmht14) max_weight_mmht14 = temp;
				//}
				weight_ct10   = event->getWeight(3001)/fabs(event->originalXWGTUP());
				weight_mmht14 = event->getWeight(4001)/fabs(event->originalXWGTUP());
				DLOG(INFO) << "w(ct10)= " << weight_ct10 << "\t" << "w(mmht14)= " << weight_mmht14;
			}
		}
            }

            ///////////////////////////////////////////
            //     Apply primary vertex selection    //
            ///////////////////////////////////////////

            bool isGoodPV = r2selection.isPVSelected(vertex, 4, 24., 2);
            LOG(INFO) <<"PrimaryVertexBit: " << isGoodPV << " TriggerBit: " << trigged;

            /////////////////////////////////
            //        Trigger              //
            /////////////////////////////////
            float normfactor = datasets[d]->NormFactor();
            //treeLoader.ListTriggers(currentRun,0);
            trigger->checkAvail(currentRun, datasets, d, &treeLoader, event, treenumber);
            trigged = trigger->checkIfFired(currentRun, datasets, d);
 
            /////////////////////////////////
            //       Primary vertex        //
            /////////////////////////////////
            //Filling Histogram of the number of vertices before Event Selection
            if (!isGoodPV) {
		for( auto j: init_uncor_jets ) delete j;
		continue; // Check that there is a good Primary Vertex
	    }
	    histo_cutflow["cutflow"]->Fill(cut2binID.at("Good PV"),genweight*scaleFactor);
            /////////////////////////////////
            //        Trigger              //
            /////////////////////////////////            
            preTrig+=1.;
            if(weight_0 < 0.0)
            {
                //scaleFactor *= -1.0;  //Taking into account negative weights in NLO Monte Carlo
                negWeightsPretrig+=1.;
            }
            
            if (!trigged) {
		 for( auto j: init_uncor_jets ) delete j;
	         continue;  //If an HLT condition is not present, skip this event in the loop.       
	    }
	    histo_cutflow["cutflow"]->Fill(cut2binID.at("SL triggers"),genweight*scaleFactor);
	    triggers_container.fill(0);
	    for(int iter_trig=0; iter_trig< ((isData?trigger->triggerListData.size():trigger->triggerListMC.size())) && iter_trig<200; iter_trig++){
		    if (isData) triggers_container[iter_trig] = trigger->triggermapData.find(trigger->triggerListData[iter_trig])->second.second;
		    if (!isData) triggers_container[iter_trig] = trigger->triggermapMC.find(trigger->triggerListMC[iter_trig])->second.second;
	    }

            postTrig+=1.; 
            /////////////////////////////////////////////////
            //            neg weights counter              //
            /////////////////////////////////////////////////
            if(weight_0 < 0.0)
            {
                //scaleFactor *= -1.0;  //Taking into account negative weights in NLO Monte Carlo
                negWeights+=1.;
            }


            /////////////////////////////////////////////////
            //               Pu reweighting                //
            /////////////////////////////////////////////////

            float lumiWeight = 1., lumiWeight_up = 1., lumiWeight_down = 1.;
            if (!isData) {
                lumiWeight = LumiWeights.ITweight( (int)event->nTruePU());
                lumiWeight_up = LumiWeights_up.ITweight( (int)event->nTruePU()); 
                lumiWeight_down = LumiWeights_down.ITweight( (int)event->nTruePU()); 
                
                LOG(INFO)<<"Lumi weight "<<lumiWeight<<"  Lumi weight Up "<<lumiWeight_up<<"   Lumi weight Down "<<lumiWeight_down;
		scaleFactor = scaleFactor * lumiWeight;
            }
	


            /////////////////////////////////////////////////
            //                    bTag SF                  //
            /////////////////////////////////////////////////

            float bTagEff(-1);
            float bTagEffUp(-1);
            float bTagEffDown(-1);
            if(fillingbTagHistos){
                if(bTagReweight && !isData){
                //get btag weight info
                    for(int jetbtag = 0; jetbtag<selectedJets.size(); jetbtag++){
                        float jetpt = selectedJets[jetbtag]->Pt();
                        float jeteta = selectedJets[jetbtag]->Eta();
                        float jetdisc = selectedJets[jetbtag]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                        BTagEntry::JetFlavor jflav;
                        int jetpartonflav = std::abs(selectedJets[jetbtag]->hadronFlavour());
                        LOG(INFO)<<"parton flavour: "<<jetpartonflav<<"  jet eta: "<<jeteta<<" jet pt: "<<jetpt<<"  jet disc: "<<jetdisc;
                        if(jetpartonflav == 5){
                            jflav = BTagEntry::FLAV_B;
                        }
                        else if(jetpartonflav == 4){
                            jflav = BTagEntry::FLAV_C;
                        }
                        else{
                            jflav = BTagEntry::FLAV_UDSG;
                        }
                        bTagEff = bTagReader->eval(jflav, jeteta, jetpt, jetdisc);    
                        bTagEffUp = bTagReaderUp->eval(jflav, jeteta, jetpt, jetdisc);                     
                        bTagEffDown = bTagReaderDown->eval(jflav, jeteta, jetpt, jetdisc);                     
                 
                        LOG(INFO)<<"btag efficiency = "<<bTagEff;       
                    }      
                    btwt->FillMCEfficiencyHistos(selectedJets); 
//                    btwtUp->FillMCEfficiencyHistos(selectedJets); 
//                    btwtDown->FillMCEfficiencyHistos(selectedJets); 

                }
            }

            LOG(INFO)<<"getMCEventWeight for btag";
            float btagWeight = 1;
            float btagWeightUp = 1;
            float btagWeightDown = 1;
            if(bTagReweight && !isData){
                if(!fillingbTagHistos){
                    btagWeight =  btwt->getMCEventWeight(selectedJets, false);
                    btagWeightUp =  btwtUp->getMCEventWeight(selectedJets, false);
                    btagWeightDown =  btwtDown->getMCEventWeight(selectedJets, false);
                }
                
                DLOG(INFO)<<"btag weight "<<btagWeight<<"  btag weight Up "<<btagWeightUp<<"   btag weight Down "<<btagWeightDown;
            }
            ////csv discriminator reweighting
            
            std::map<string,double> csvrsweights;
            if(bTagCSVReweight && !isData) {
            //get btag weight info
                if(!fillingbTagHistos){
                    csvrsweights = csvrsw->getSFs(selectedJets);
		    if (JESUp || JESDown) csvrsweights = csvrsw->getSFs(selectedUncorJets);
		
		    //std::cout << "Before correction" << std::endl;
		    //for_each( std::begin(selectedUncorJets), std::end(selectedUncorJets), printjetdata);
		    //std::cout << "After correction" << std::endl;
		    //for_each( std::begin(selectedJets), std::end(selectedJets), printjetdata);

                    for(auto el: csvrsweights) DLOG(INFO) << "CSVRS:" << std::setw(10) << el.first << std::setw(10) << el.second ;
                }      
            }
            if( bTagCSVReweight && !isData ) scaleFactor*=csvrsweights.find("nominal")->second;


            /////////////////////////////////////////////////
            //                   Lepton SF                 //
            /////////////////////////////////////////////////

            float fleptonSF = 1;
            if(bLeptonSF && !isData){ ///lepton SF for ID and ISO
                if(Muon && nMu>0){
                    auto W_MuonIsoSF_BCDEF = muonSFWeightIso_BCDEF->at(selectedMuons[0]->Eta(), selectedMuons[0]->Pt(), 0)*Constant::lum_RunsBCDEF;
                    auto W_MuonIsoSF_GH    = muonSFWeightIso_GH->at(selectedMuons[0]->Eta(), selectedMuons[0]->Pt(), 0)*Constant::lum_RunsGH;
                    auto muISOSF =(W_MuonIsoSF_BCDEF + W_MuonIsoSF_GH)/(Constant::lum_RunsGH+Constant::lum_RunsBCDEF);
                    DLOG(INFO)<<"Muon ISO SF:  "<< muISOSF;
                    
                    auto W_MuonIDSF_BCDEF = muonSFWeightID_BCDEF->at(selectedMuons[0]->Eta(), selectedMuons[0]->Pt(), 0)*Constant::lum_RunsBCDEF;
                    auto W_MuonIDSF_GH    = muonSFWeightID_GH->at(selectedMuons[0]->Eta(), selectedMuons[0]->Pt(), 0)*Constant::lum_RunsGH;
                    auto muIDSF =(W_MuonIDSF_BCDEF + W_MuonIDSF_GH)/(Constant::lum_RunsGH+Constant::lum_RunsBCDEF);
                    DLOG(INFO)<<"Muon ID SF:  "<< muIDSF;
                    
                    auto MuonTrackSF = h_muonSFWeightTrack->Eval(selectedMuons[0]->Eta());
                    
                    fleptonSF = muIDSF * muISOSF * MuonTrackSF;
                }
                else if(Electron && nEl>0){
                    auto eleTrkSF = electronSFWeightReco->at(selectedElectrons[0]->superClusterEta(),selectedElectrons[0]->Pt(),0);
                    DLOG(INFO)<<"Electron Tracking SF:  "<< eleTrkSF;
                    auto eleIDISOSF = electronSFWeightIDISO->at(selectedElectrons[0]->superClusterEta(),selectedElectrons[0]->Pt(),0);
                    DLOG(INFO)<<"Electron ID ISO SF:  "<< eleIDISOSF;
                    fleptonSF = eleTrkSF *  eleIDISOSF;
                }
            }

            double trigSFTot = 1.;
            if(bLeptonSF && !isData){ //lepton SF for trigger
                if(Muon && nMu>0){
                    auto W_MuonTrigSF_BCDEF =  muonSFWeightTrig_BCDEF->at(selectedMuons[0]->Eta(), selectedMuons[0]->Pt(), 0)*Constant::lum_RunsBCDEF;
                    auto W_MuonTrigSF_GH    =  muonSFWeightTrig_GH->at(selectedMuons[0]->Eta(), selectedMuons[0]->Pt(), 0)*Constant::lum_RunsGH;
                    trigSFTot          =  (W_MuonTrigSF_BCDEF + W_MuonTrigSF_GH)/(Constant::lum_RunsGH+Constant::lum_RunsBCDEF);
                    DLOG(INFO)<<"Muon Trigger SF:  "<< trigSFTot;
                } else if(Electron && nEl>0) {
                    auto eleTRIGSF_BCDEF = electronSFWeightTrig_BCDEF->at(selectedElectrons[0]->superClusterEta(),selectedElectrons[0]->Pt(),0)*Constant::lum_RunsBCDEF;
                    auto eleTRIGSF_GH = electronSFWeightTrig_GH->at(selectedElectrons[0]->superClusterEta(),selectedElectrons[0]->Pt(),0)*Constant::lum_RunsGH;
                    auto eleTRIGSF = electronSFWeightTrig->at(selectedElectrons[0]->superClusterEta(),selectedElectrons[0]->Pt(),0);
                    trigSFTot = (eleTRIGSF_BCDEF + eleTRIGSF_GH)/(Constant::lum_RunsGH+Constant::lum_RunsBCDEF);
		    trigSFTot = eleTRIGSF;
                    DLOG(INFO)<<"Electron Trigger SF:  "<< trigSFTot;
                }
                //fleptonSF*=trigSFTot;
            }

            LOG(INFO)<<"lepton SF:  "<<fleptonSF;
            if(!isData)   scaleFactor *= fleptonSF;

            //Apply the lepton, jet, btag and HT & MET selections

            LOG(INFO)<<"Number of Muons = "<< nMu <<"    electrons =  "  <<nEl<<"     Jets = "<< selectedJets.size()   <<" loose BJets = "<<  nLtags   <<
                "  MuonChannel = "<<Muon<<" Electron Channel"<<Electron;

            ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //                                                                                 Baseline Event selection                                                                      //
            ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//            //Event cleaning filters
	    auto HBHEnoise = event->getHBHENoiseFilter();
	    auto HBHEIso = event->getHBHENoiseIsoFilter();
	    auto CSCTight = event->getglobalTightHalo2016Filter();
	    auto EcalDead = event->getEcalDeadCellTriggerPrimitiveFilter();
	    auto badchan   = event-> getBadChCandFilter();
	    auto badmu = event-> getBadPFMuonFilter();
	    if (!HBHEnoise) {
		for( auto j: init_uncor_jets ) delete j;
		continue;
	    }
	    if (!HBHEIso) {
		for( auto j: init_uncor_jets ) delete j;
		continue;
	    }
	    if (!CSCTight) {
		for( auto j: init_uncor_jets ) delete j;
		continue;
	    }
            if (!EcalDead) {
		for( auto j: init_uncor_jets ) delete j;
		continue;
	    }
	    if (!badchan) {
		for( auto j: init_uncor_jets ) delete j;
		continue;
	    }
	    if (!badmu) {
		for( auto j: init_uncor_jets ) delete j;
		continue;
	    }

	    histo_cutflow["cutflow"]->Fill(cut2binID.at("Event cleaning"),genweight*trigSFTot*scaleFactor);

            if (Muon)
            {   
                if  (  !( nMu == 1 && nEl == 0 && nLooseMu == 1 && !bCrackVeto && fabs(selectedMuons[0]->Eta())<2.1 ) ) {
			for( auto j: init_uncor_jets ) delete j;
			continue; // Muon Channel Selection
		}
		histo_cutflow["cutflow"]->Fill(cut2binID.at("One lepton"),genweight*trigSFTot*scaleFactor);
		if  (  !( nJets>=7 ) ) {
			for( auto j: init_uncor_jets ) delete j;
			continue; // Muon Channel jet multiplicity Selection
		}
		histo_cutflow["cutflow"]->Fill(cut2binID.at("Jet multiplicity"),genweight*trigSFTot*scaleFactor);
		if  (  !( nMtags >=2 ) ) {
			for( auto j: init_uncor_jets ) delete j;
			continue; // Muon Channel b tag multiplicity Selection
		}
		histo_cutflow["cutflow"]->Fill(cut2binID.at("N_{tags}^{m}>2"),genweight*trigSFTot*scaleFactor);
            }
            else if(Electron){
                if  (  !( nMu == 0 && nEl == 1 && nLooseEl == 1 && fabs(selectedElectrons[0]->Eta())<2.1) ) {
			for( auto j: init_uncor_jets ) delete j;
			continue; // Electron Channel Selection
		}
		histo_cutflow["cutflow"]->Fill(cut2binID.at("One lepton"),genweight*trigSFTot*scaleFactor);
                if  (  !( nJets>=8 ) ) {
			for( auto j: init_uncor_jets ) delete j;
			continue; // Electron Channel Selection
		}
		histo_cutflow["cutflow"]->Fill(cut2binID.at("Jet multiplicity"),genweight*trigSFTot*scaleFactor);
                if  (  !( nMtags >=2 ) ) {
			for( auto j: init_uncor_jets ) delete j;
			continue; // Electron Channel Selection
		}
		histo_cutflow["cutflow"]->Fill(cut2binID.at("N_{tags}^{m}>2"),genweight*trigSFTot*scaleFactor);
            }
            else{
                cerr<<"Correct Channel not selected."<<std::endl;
                exit(1);
            }
            LOG(INFO)<<"after baseline"<<std::endl;
            weightCount += scaleFactor;
            eventCount++;
            LOG(INFO)<<"Selection Passed."<<std::endl;
            passed++;
            /////////////////////////////////////////////////
            //            ttbb reweighting                 //
            /////////////////////////////////////////////////
            float numOfbb = 0;
            float numOfcc = 0;
            float numOfll = 0;
            float ttbar_flav = -1;
            double fTopPtReWeightsf = 1.;
            double fTopPtReWeightsfUp = 1.;
            double fTopPtReWeightsfDown = 1.;
            // TRootGenEvent* genEvt_flav = 0;
            if(dataSetName.find("TTJets")!=string::npos ||
                dataSetName.find("TTFSRS")!=string::npos || 
                dataSetName.find("TTISR")!=string::npos || 
                dataSetName.find("TTUE")!=string::npos || 
                dataSetName.find("TTCR")!=string::npos || 
                dataSetName.find("TTHdamp")!=string::npos || 
                dataSetName.find("TTScale")!=string::npos){
                // genEvt_flav = treeLoader.LoadGenEvent(ievt,false);
                // treeLoader.LoadMCEvent(ievt, 0, mcParticles_flav,false);
                
                auto fAntitopPtsf = 1., fTopPtsf = 1.;
                auto fAntitopPtsfUp = 1., fTopPtsfUp = 1.;
                auto fAntitopPtsfDown = 1., fTopPtsfDown = 1.;
                for(unsigned int p=0; p<mcParticles_flav.size(); p++) {
                    //Calculating event weight according to the TopPtReweighing: https://twiki.cern.ch/twiki/bin/view/CMS/TopPtReweighting
                    if(bTopPt)
                    {
                        if(mcParticles_flav[p]->type() == 6 && mcParticles_flav[p]->isLastCopy() )
                        {
                            fTopPtsf  = TMath::Exp(0.0615-0.0005*mcParticles_flav[p]->Pt());
                            fTopPtsfUp  = TMath::Exp((6.15024e-02+3.24328e-02)-(5.17833e-04 - 1.72690e-04)*mcParticles_flav[p]->Pt());
                            fTopPtsfDown  = TMath::Exp((6.15024e-02-3.24328e-02)-(5.17833e-04 + 1.72690e-04)*mcParticles_flav[p]->Pt());
                        }
                        else if(mcParticles_flav[p]->type() == -6 && mcParticles_flav[p]->isLastCopy() )
                        {
                            fAntitopPtsf  = TMath::Exp(0.0615-0.0005*mcParticles_flav[p]->Pt());
                            fAntitopPtsfUp  = TMath::Exp((6.15024e-02+3.24328e-02)-(5.17833e-04 - 1.72690e-04)*mcParticles_flav[p]->Pt());
                            fAntitopPtsfDown  = TMath::Exp((6.15024e-02-3.24328e-02)-(5.17833e-04 + 1.72690e-04)*mcParticles_flav[p]->Pt());
                        }
                    }
                    //std::cout<<"status: "<<mcParticles_flav[p]->status()<<"  id: "<<mcParticles_flav[p]->type()<<" mother: "<<mcParticles_flav[p]->motherType()<<std::endl;
                    if(mcParticles_flav[p]->status()<30 && mcParticles_flav[p]->status()>20 && abs(mcParticles_flav[p]->motherType())!=6){

                        if (abs(mcParticles_flav[p]->type())==5)
                        {
                            // ttbar_flav=2;
                            numOfbb++;  
                        }
                        
                        else if (abs(mcParticles_flav[p]->type())==4 && abs(mcParticles_flav[p]->motherType())!=5 && abs(mcParticles_flav[p]->motherType())!=24)
                        {
                            // ttbar_flav=1;
                            numOfcc++; 
                        }
                        
                        else if (abs(mcParticles_flav[p]->type())<4){
                            // ttbar_flav=1;
                            numOfll++; 
                        }
                    }

                }
		fTopPtReWeightsf = TMath::Sqrt(fTopPtsf*fAntitopPtsf);
		fTopPtReWeightsfUp = TMath::Sqrt(fTopPtsfUp*fAntitopPtsfUp);
		fTopPtReWeightsfDown = TMath::Sqrt(fTopPtsfDown*fAntitopPtsfDown);
		DLOG(INFO) << "Top reweighting (top/anti-top/comb): " << setw(10) << fTopPtsf << setw(10) << fAntitopPtsf << setw(10) << fTopPtReWeightsf;
		scaleFactor *= fTopPtReWeightsf;
            } 

            if(numOfbb>=2){
                ttbar_flav = 2;
            }
            else if(numOfcc>=2){
                ttbar_flav = 1;
            }
            else{
                ttbar_flav = 0;
            }


            //////////////////////////////////////////
            //     TMVA for mass Reconstruction     //
            //////////////////////////////////////////
            float diTopness = 0;
	    float triTopness = 0;
            LOG(INFO)<<"TMVA mass reco";
            sort(selectedJets.begin(),selectedJets.end(),HighestCVSBtag());
            float csvJetcsv1 = 1, csvJetcsv2 = 1, csvJetcsv3 =1, csvJetcsv4 =1;

            if (selectedJets.size()>4){
		const int njets = selectedJets.size();
		std::vector<double> csvArray(njets);
		for (int ijet=0; ijet<njets; ++ijet) csvArray[ijet] = selectedJets[ijet]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
		std::sort(csvArray.begin(), csvArray.end());
		std::reverse(csvArray.begin(), csvArray.end());
                csvJetcsv1 = csvArray[0];
                csvJetcsv2 = csvArray[1];
                csvJetcsv3 = csvArray[2];
                csvJetcsv4 = csvArray[3];                
            }
            // std::cout<<"csv: "<<csvJetcsv1<<std::endl;

            if (HadTopOn){
                hadronicTopReco->SetCollections(selectedJets, selectedMuons, selectedElectrons, scaleFactor);
            }

	    double MT1 = 0., MW1 = 0.,  MT2 = 0., MW2 = 0., MT3 = 0., MW3 = 0.;
        double trj1st[3][6]; std::fill( &trj1st[0][0], &trj1st[0][0]+sizeof(trj1st)/sizeof(trj1st[0][0]), -10.);
        double trj2nd[3][6]; std::fill( &trj2nd[0][0], &trj2nd[0][0]+sizeof(trj2nd)/sizeof(trj2nd[0][0]), -10.);
        double trj3rd[3][6]; std::fill( &trj3rd[0][0], &trj3rd[0][0]+sizeof(trj3rd)/sizeof(trj3rd[0][0]), -10.);
        
            if(HadTopOn){
                if(!TrainMVA){ //if not training, but computing 
                    hadronicTopReco->Compute1st(d, selectedJets, datasets);
                    hadronicTopReco->Compute2nd(d, selectedJets, datasets);
                    diTopness = hadronicTopReco->ReturnDiTopness();
                    SumJetMassX = hadronicTopReco->ReturnSumJetMassX();
                    HTX = hadronicTopReco->ReturnHTX();// std::cout<<"HTX: "<<HTX<<std::endl;

		    std::vector<unsigned int> selectedTrijetIDs1st = hadronicTopReco->MVAvals1.second;
		    TLorentzVector TLVTop1(0.,0.,0.,0.);
		    TLorentzVector TLVW1(0.,0.,0.,0.);
		    for (auto jetId: selectedTrijetIDs1st) TLVTop1 += (*selectedJets[jetId]);
		    for (auto jetId: {selectedTrijetIDs1st[0], selectedTrijetIDs1st[1]}) TLVW1 += (*selectedJets[jetId]); 
		    MT1 = TLVTop1.M(); MW1 =  TLVW1.M();
		    DLOG(INFO) << "MT1,MW1: " << setw(10) << MT1 << setw(10) << MW1;

            // Fill first trijet combination
            int ijet = 0;
            for (auto jetId: {selectedTrijetIDs1st[0], selectedTrijetIDs1st[1], selectedTrijetIDs1st[2]}){
                trj1st[ijet][0]=selectedJets[jetId]->Pt();
                trj1st[ijet][1]=selectedJets[jetId]->Eta();
                trj1st[ijet][2]=selectedJets[jetId]->Phi();
                trj1st[ijet][3]=selectedJets[jetId]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                trj1st[ijet][4]=selectedJets[jetId]->E();
                trj1st[ijet][5]=hadronicTopReco->MVAvals1.first;
                ijet++;
            }

		    std::vector<unsigned int> selectedTrijetIDs2nd = hadronicTopReco->MVAvals2ndPass.second;
		    TLorentzVector TLVTop2(0.,0.,0.,0.);
		    TLorentzVector TLVW2(0.,0.,0.,0.);
		    for (auto jetId: selectedTrijetIDs2nd) {
			TLVTop2 += (*selectedJets[jetId]);
		}
		    for (auto jetId: {selectedTrijetIDs2nd[0], selectedTrijetIDs2nd[1]}) TLVW2 += (*selectedJets[jetId]); 
		    MT2 = TLVTop2.M(); MW2 =  TLVW2.M();
		    DLOG(INFO) << "MT2,MW2: " << setw(10) << MT2 << setw(10) << MW2;

            // Fill second trijet combination
            ijet = 0;
            for (auto jetId: {selectedTrijetIDs2nd[0], selectedTrijetIDs2nd[1], selectedTrijetIDs2nd[2]}){
                trj2nd[ijet][0]=selectedJets[jetId]->Pt();
                trj2nd[ijet][1]=selectedJets[jetId]->Eta();
                trj2nd[ijet][2]=selectedJets[jetId]->Phi();
                trj2nd[ijet][3]=selectedJets[jetId]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                trj2nd[ijet][4]=selectedJets[jetId]->E();
                trj2nd[ijet][5]=hadronicTopReco->MVAvals2ndPass.first;
                ijet++;
            }

		    if (selectedJets.size()>=10) {
                hadronicTopReco->Compute3rd(d, selectedJets, datasets);
                triTopness = hadronicTopReco->ReturnTriTopness();
                std::vector<unsigned int> selectedTrijetIDs3rd = hadronicTopReco->MVAvals3rdPass.second;
                TLorentzVector TLVTop3(0.,0.,0.,0.);
                TLorentzVector TLVW3(0.,0.,0.,0.);
                for (auto jetId: selectedTrijetIDs2nd) TLVTop3 += (*selectedJets[jetId]);
                for (auto jetId: {selectedTrijetIDs3rd[0], selectedTrijetIDs3rd[1]}) TLVW3 += (*selectedJets[jetId]); 
                MT3 = TLVTop3.M(); MW3 =  TLVW3.M();
                DLOG(INFO) << "tritopness,MT3,MW3: " << nJets << setw(20) << triTopness << setw(20) << MT3 << setw(20) << MW3;

                // Fill third trijet combination
                ijet = 0;
                for (auto jetId: {selectedTrijetIDs3rd[0], selectedTrijetIDs3rd[1], selectedTrijetIDs3rd[2]}){
                    trj3rd[ijet][0]=selectedJets[jetId]->Pt();
                    trj3rd[ijet][1]=selectedJets[jetId]->Eta();
                    trj3rd[ijet][2]=selectedJets[jetId]->Phi();
                    trj3rd[ijet][3]=selectedJets[jetId]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                    trj3rd[ijet][4]=selectedJets[jetId]->E();
                    trj3rd[ijet][5]=hadronicTopReco->MVAvals3rdPass.first;
                    ijet++;
                }
		    }
                } else { // if training hadronic top decay reconstruction
                    hadronicTopReco->SetMCParticles(mcParticles_flav);
                    hadronicTopReco->Train(d, selectedJets, datasets);
                }
            }

            //std::cout<<"SumJetMassX: "<<SumJetMassX<<std::endl;
            ///////////////////////////////////
            // Filling histograms / plotting //
            ///////////////////////////////////
            LOG(INFO)<<"Plots";

            //////////////////////
            // Muon Based Plots //
            //////////////////////
            float leptonIso=0;
            float chargedHIso = 0;
            float neutralHIso = 0;
            float photonIso = 0;
            float PUIso = 0;
            for (Int_t selmu =0; selmu < selectedMuons.size(); selmu++ )
            {
                float relisomu = (selectedMuons[0]->chargedHadronIso(4) + max( 0.0, selectedMuons[0]->neutralHadronIso(4) + selectedMuons[0]->photonIso(4) - 0.5*selectedMuons[0]->puChargedHadronIso(4)) ) / selectedMuons[0]->Pt();
                chargedHIso = selectedMuons[0]->chargedHadronIso(4);
                neutralHIso = selectedMuons[0]->neutralHadronIso(4);
                photonIso = selectedMuons[0]->photonIso(4);
                PUIso = selectedMuons[0]->puChargedHadronIso(4);


                if(Muon){
                    leptonIso =relisomu;
                }
            }

            //////////////////////////
            // Electron Based Plots //
            //////////////////////////

            for (Int_t selel =0; selel < selectedElectrons.size(); selel++ )
            {
                float reliso = selectedElectrons[selel]->relPfIso(4, 0.5);

                if (Electron){
                    leptonIso = reliso;
                }
            }


            ////////////////////////////////////////////
            //       calculating HT rat and HTH       //
            ////////////////////////////////////////////
            LOG(INFO)<<"HT rat and HTH";
            HT = 0;
            float HT1M2L=0, H1M2L=0, HTbjets=0, HT2M=0, H2M=0, HT2L2J=0;
            sort(selectedJets.begin(),selectedJets.end(),HighestPt()); //order Jets wrt Pt for tuple output

	    vector<TLorentzVector> TLVjetholder;
            for (Int_t seljet1 =0; seljet1 < selectedJets.size(); seljet1++ )
            {

                //Event-level variables
                jetpt = selectedJets[seljet1]->Pt();
                HT = HT + jetpt;
                H = H +  selectedJets[seljet1]->P();
                if (seljet1 > 4  )  HTHi +=  selectedJets[seljet1]->Pt();
		TLVjetholder.push_back(*selectedJets[seljet1]);
            }

            float csvJetpt1 = 1, csvJetpt2 = 1, csvJetpt3 =1, csvJetpt4 =1;

            if (selectedJets.size()>4){
                csvJetpt1 = selectedJets[0]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                csvJetpt2 = selectedJets[1]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                csvJetpt3 = selectedJets[2]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                csvJetpt4 = selectedJets[3]->btag_combinedInclusiveSecondaryVertexV2BJetTags();                
            }

            HTH = HT/H;
            HTRat = HTHi/HT;

            ////////////////////////////////////////////
            //        Topological variables           //
            ////////////////////////////////////////////
	    topologyW->setPartList(TLVjetholder, TLVjetholder);
	    float fSphericity = topologyW->get_sphericity();
	    float fOblateness = topologyW->oblateness();
	    float fAplanarity = topologyW->get_aplanarity();
	    float fh10 = topologyW->get_h10();
	    float fh20 = topologyW->get_h20();
	    float fh30 = topologyW->get_h30();
	    float fh40 = topologyW->get_h40();
	    float fh50 = topologyW->get_h50();
	    float fh60 = topologyW->get_h60();
	    float fht = topologyW->get_ht();
	    float fht3 = topologyW->get_ht3();
	    float fet0 = topologyW->get_et0();
	    float fsqrts = topologyW->get_sqrts();
	    float fnjetW = topologyW->get_njetW(); //125

	    float fet56 = topologyW->get_et56(); 
	    float fcentrality = topologyW->get_centrality();

            //////////////////////
            // Jets Based Plots //
            //////////////////////

            float met = mets[0]->Et();

	    if  ( Muon && leptonIso < 0.15 ) { 
		    histo_cutflow["cutflow"]->Fill(cut2binID.at("Lepton iso."),genweight*trigSFTot*scaleFactor);
		    if  ( HT>500 ) {
			    histo_cutflow["cutflow"]->Fill(cut2binID.at("HT>500"),genweight*trigSFTot*scaleFactor);
			    if  ( met>50 ) {
				    histo_cutflow["cutflow"]->Fill(cut2binID.at("MET>50"),genweight*trigSFTot*scaleFactor);
			    }
		    }
	    } else if ( Electron ) {
		    histo_cutflow["cutflow"]->Fill(cut2binID.at("Lepton iso."),genweight*trigSFTot*scaleFactor);
		    if  ( HT>500 ) {
			    histo_cutflow["cutflow"]->Fill(cut2binID.at("HT>500"),genweight*trigSFTot*scaleFactor);
			    if  ( met>50 ) {
				    histo_cutflow["cutflow"]->Fill(cut2binID.at("MET>50"),genweight*trigSFTot*scaleFactor);
			    }
		    }
	    }

            LOG(INFO)<<"lepton vars";
            ////////////////////////////////////////////
            //              Get lepton pt             //
            ////////////////////////////////////////////
            float selectedLeptonPt = 0 ;
            if(Muon&&selectedMuons.size()>0){
                selectedLeptonPt = selectedMuons[0]->Pt();
                leptoneta = selectedMuons[0]->Eta();
                leptonphi = selectedMuons[0]->Phi();                
                leptonvalidhits = selectedMuons[0]->nofValidHits();
            }
            else if(Electron&&selectedElectrons.size()>0){
                selectedLeptonPt = selectedElectrons[0]->Pt();
                leptoneta = selectedElectrons[0]->Eta();
                leptonphi = selectedElectrons[0]->Phi();
                leptonvalidhits = selectedElectrons[0]->trackNValidHits();
            }


            ////////////////////////////////////////////
            //       Fill BDT & compute score         //
            ////////////////////////////////////////////
            LOG(INFO)<<"event BDT computer";
            float jet5Pt = 0;
            float jet6Pt = 0;
            if (EventBDTOn){
                if (nJets>5){
                    jet5Pt =  selectedJets[4]->Pt();
                    jet6Pt = selectedJets[5]->Pt();
                }
                eventBDT->fillVariables(diTopness, selectedLeptonPt, leptoneta, HTH, HTRat, HTb, nLtags, nMtags, nTtags, nJets, jet5Pt, jet6Pt);
            }           

            float firstjetpt = selectedJets[0]->Pt();
            float secondjetpt = selectedJets[1]->Pt();

            BDTScore = 0 ;
            BDTScore1 = 0 ;
            if(EventBDTOn){
                eventBDT->computeBDTScore();
                BDTScore = eventBDT->returnBDTScore();
                std::vector<float> input{diTopness, HTb, HTH, selectedLeptonPt, SumJetMassX, HTX, 
                          	      csvJetcsv3, csvJetcsv4, firstjetpt, secondjetpt,
                          	      jet5Pt, jet6Pt, 0.0, 0.0, 
                                  csvJetpt3, csvJetpt4};
                if (nJets<=7) BDTScore1 = pyada7.getMVA(input);
                if (nJets==8) BDTScore1 = pyada8.getMVA(input);
                if (nJets==9) BDTScore1 = pyada9.getMVA(input);
                if (nJets>=10) BDTScore1 = pyada10.getMVA(input);
            }

            ////////////////////////////////////////////
            //       Return variables for ntup        //
            ////////////////////////////////////////////
            if (selectedMBJets.size()>0){
                bjetpt = selectedMBJets[0]->Pt();
            }
            float nvertices = vertex.size();
            float angletoplep = 0;
            float angletop1top2 = 0;
            if(HadTopOn){
                angletop1top2 = hadronicTopReco->ReturnAnglet1t2();
                angletoplep = hadronicTopReco->ReturnAngletoplep();                
            }
            float nOrigJets = (float)selectedOrigJets.size();
            float jet5and6Pt = jet5Pt+jet6Pt;
            bool electronVFIDflag = false; //TODO: fill correct VF ID information in
            double vals[74] = {BDTScore,nJets,nOrigJets,nLtags,nMtags,nTtags,
            HT,selectedLeptonPt,leptoneta,bjetpt,HT2M,HTb,HTH,HTRat,HTX,
            SumJetMassX,diTopness,numOfbb,numOfcc,numOfll,ttbar_flav,
            scaleFactor,fleptonSF,btagWeight,btagWeightUp,btagWeightDown,
            lumiWeight,lumiWeight_up,lumiWeight_down,nvertices,normfactor,
            weight_0,weight_1,weight_2,weight_3,weight_4,weight_5,weight_6,weight_7,weight_8,
            met,angletop1top2,angletoplep,firstjetpt,secondjetpt,leptonIso,leptonphi,
            chargedHIso,neutralHIso,photonIso,PUIso,jet5Pt,jet6Pt,jet5and6Pt, 
            csvJetcsv1,csvJetcsv2,csvJetcsv3,csvJetcsv4,csvJetpt1,csvJetpt2,csvJetpt3,csvJetpt4,fTopPtReWeightsf,ttXtype,ttXrew,
	        trigSFTot,fnjetW, MT1, MT2, MT3, MW1, MW2, MW3, BDTScore1};

//		std::cout << "Interesting event: " << setw(20) << runId << ":" << lumBlkId << ":" << evId << " " << BDTScore << setw(20) << nJets 
//			  << " " << nMtags << " " << HT << " " << fnjetW << std::endl;
            
            double csvrs[] = {
                    csvrsweights.find("nominal")->second,
                    csvrsweights.find("JESUp")->second,          csvrsweights.find("JESDown")->second,
                    csvrsweights.find("LFUp")->second,           csvrsweights.find("LFDown")->second,
                    csvrsweights.find("HFUp")->second,           csvrsweights.find("HFDown")->second,
                    csvrsweights.find("CSVHFStats1Up")->second,  csvrsweights.find("CSVHFStats1Down")->second,
                    csvrsweights.find("CSVHFStats2Up")->second,  csvrsweights.find("CSVHFStats2Down")->second,
                    csvrsweights.find("CSVLFStats1Up")->second,  csvrsweights.find("CSVLFStats1Down")->second,
                    csvrsweights.find("CSVLFStats2Up")->second,  csvrsweights.find("CSVLFStats2Down")->second,
                    csvrsweights.find("CSVCFErr1Up")->second,    csvrsweights.find("CSVCFErr1Down")->second,
                    csvrsweights.find("CSVCFErr2Up")->second,    csvrsweights.find("CSVCFErr2Down")->second
            };
            double w[] = {weight_0,weight_1,weight_2,weight_3,weight_4,weight_6,weight_6,weight_8,weight_8};    //replace extreme variations by good
            double hdampw[] = {weight_hdamp_dw, weight_hdamp_up};
            double pdfw[]   = {weight_ct10, weight_mmht14};
            double ttxrew[]   = {ttXrew_up, ttXrew_down};
            double topptrew[]   = {fTopPtReWeightsf,fTopPtReWeightsfUp,fTopPtReWeightsfDown};
            double jetvec[30][5];
            for (auto jet=0; jet<nJets; ++jet){
                jetvec[jet][0] = selectedJets[jet]->Pt();
                jetvec[jet][1] = selectedJets[jet]->Eta();
                jetvec[jet][2] = selectedJets[jet]->Phi();
                jetvec[jet][3] = selectedJets[jet]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                jetvec[jet][4] = selectedJets[jet]->E();
            }
	    double electron[20]; std::fill_n( electron, 20, -10.);
	    double muon[20];	 std::fill_n( muon, 20, -10.);
	    if(Muon) FillMuonParams(selectedMuons[0],muon);
	    if(Electron) FillElectronParams(selectedElectrons[0],electron);
            myEvent.fill_electronVFID(electronVFIDflag);
            myEvent.fill(vals,jetvec,electron,muon,nJets,w,csvrs,hdampw,pdfw,weight_nnpdf,ttxrew,topptrew,
                         trj1st, trj2nd, trj3rd);
        // if (nJets < 10)
            // std::cout << trj3rd[0][4] << " " << trj3rd[1][4] << " " << trj3rd[2][4] << std::endl;

	    tup_genLeptons.clear();
	    std::for_each( std::begin(mcParticles_flav), std::end(mcParticles_flav), push_genlepton2lorentz);

	    tup_genJets.clear();
	    std::for_each( std::begin(genjets), std::end(genjets), push_genjet2lorentz );

	    auto genHT=0.;
	    auto NgenJets=0;
	    genFilter = 0;
	    for ( const auto& jet: tup_genJets ) {
		if ( jet.Pt()>30. && fabs(jet.Eta())<2.4 ) genHT += jet.Pt();
		if ( jet.Pt()>30. ) ++NgenJets;
	    }
	    if ( tup_genLeptons.size() >= 1 && genHT>500 && NgenJets>=9) genFilter = 1;

            tupfile->cd();
            tup->Fill();
	    tup_genJets.clear();
	    tup_genLeptons.clear();

	    for( auto j: init_uncor_jets ) delete j;

	    //////////////////////////////////////////////////////////////////////////////////////////////
	    // Find matching pairs of jets for different kinds of efficiency histograms		   //
	    //////////////////////////////////////////////////////////////////////////////////////////////
	    int nCorMatch = 0;
	    int nFakeMatch = 0;
	    int nTotMatch = 0;

	    using pair_genJetPFJet = pair<TRootGenJet*,TRootPFJet*>;
	    vector< pair_genJetPFJet > matched_jets;
	    auto dist_dR = [](TRootGenJet* g, TRootPFJet* j) {
	    	return TMath::Sqrt(TMath::Power(g->Eta() - j->Eta(),2) + TMath::Power(g->Phi() - j->Phi(),2));
	    };
	    for(const auto& genjet: genjets) { 
	    	for(const auto& selectedjet: selectedJets) {
	    		auto dR = dist_dR(genjet,selectedjet);
	    		if (dR < 0.4) {
	    			matched_jets.emplace_back( make_pair(genjet,selectedjet) );
	    			if (fabs(selectedjet->hadronFlavour())==5 && selectedjet->btag_combinedInclusiveSecondaryVertexV2BJetTags()>0.9535) nCorMatch++;
	    			if (fabs(selectedjet->hadronFlavour())!=5 && selectedjet->btag_combinedInclusiveSecondaryVertexV2BJetTags()>0.9535) nFakeMatch++;
	    			if (selectedjet->btag_combinedInclusiveSecondaryVertexV2BJetTags()>0.9535) nTotMatch++;
	    		}
	    	}
	    }
	    for (const auto& genjet_seljet_pair: matched_jets) {
		auto flav = abs(genjet_seljet_pair.second->hadronFlavour());
		auto btagValue = genjet_seljet_pair.second->btag_combinedInclusiveSecondaryVertexV2BJetTags();
		if (flav == 5 && btagValue>0.9535 ) {
			histo1D_my["h_effb_jetmult"]->Fill(nJets>10?10.:nJets);
			histo2D_my["h_effb_jetmult_pt"]->Fill(nJets>10?10.:nJets, genjet_seljet_pair.second->Pt());
			histo2D_my["h_effb_eta_pt"]->Fill(genjet_seljet_pair.second->Eta(), genjet_seljet_pair.second->Pt());
		}
		if (flav != 5 && btagValue>0.9535 ) {
			histo1D_my["h_fakeb_jetmult"]->Fill(nJets>10?10.:nJets);
			histo2D_my["h_fakeb_jetmult_pt"]->Fill(nJets>10?10.:nJets, genjet_seljet_pair.second->Pt());
			histo2D_my["h_fakeb_eta_pt"]->Fill(genjet_seljet_pair.second->Eta(), genjet_seljet_pair.second->Pt());
		}
		if (btagValue>0.9535) {
			histo1D_my["h_totb_jetmult"]->Fill(nJets>10?10.:nJets); 
			histo2D_my["h_totb_jetmult_pt"]->Fill(nJets>10?10.:nJets, genjet_seljet_pair.second->Pt());
			histo2D_my["h_totb_eta_pt"]->Fill(genjet_seljet_pair.second->Eta(), genjet_seljet_pair.second->Pt());
		}
	    }

	    for(const auto& selectedjet: selectedJets) {
		int  flav = abs(selectedjet->hadronFlavour());
		auto btagValue = selectedjet->btag_combinedInclusiveSecondaryVertexV2BJetTags();
		auto localPt = selectedjet->Pt();
                auto localEta = selectedjet->Eta();
		if (localPt >= PtMax) localPt = PtMax-1;
                if (localEta >= 2.4) localEta = 2.4-0.01;
                if (flav == 5) 			histo2D_btwt["TotalNofBJets"]->Fill(localPt,localEta); //b-jet
                else if (flav == 4) 		histo2D_btwt["TotalNofCJets"]->Fill(localPt,localEta); //c-jet
                else if (flav == 0) 		histo2D_btwt["TotalNofLightJets"]->Fill(localPt,localEta); //light
                else 				histo2D_btwt["TotalNofLightJets"]->Fill(localPt,localEta); //assume light
		if (btagValue > 0.9535) {
						histo2D_btwt["BtaggedJets"]->Fill(localPt,localEta);
			if (flav == 5) 		histo2D_btwt["BtaggedBJets"]->Fill(localPt,localEta); //b-jet
			else if (flav == 4) 	histo2D_btwt["BtaggedCJets"]->Fill(localPt,localEta); //c-jet
			else if (flav == 0) 	histo2D_btwt["BtaggedLightJets"]->Fill(localPt,localEta);//light
			else 			histo2D_btwt["BtaggedLightJets"]->Fill(localPt,localEta);//assume light
		}
	    }

        } //End Loop on Events


	tupfile->cd();
	auto btagHistDir = tupfile->mkdir("btag");
	btagHistDir->cd();
	for (const auto& el: histo1D_my) el.second->Write();
	for (const auto& el: histo2D_my) el.second->Write();
	for (const auto& el: histo2D_btwt) el.second->Write();

	// Cutflow histograms
	tupfile->cd();
	auto cutflowHistDir = tupfile->mkdir("cutflow");
	cutflowHistDir->cd();
	for (const auto& el: histo_cutflow) el.second->Write();

        std::cout<<"Write files"<<std::endl;
        tupfile->cd();
        tup->Write();
	booktup->Write();
        tupfile->Close();


        std::cout <<"n events passed  =  "<<passed <<std::endl;
        std::cout <<"n events with negative weights = "<<negWeights << std::endl;
        std::cout <<"n events with negative weights pretrig= "<<negWeightsPretrig << std::endl;
        std::cout << "Event Count: " << eventCount << std::endl;
        std::cout << "Weight Count: " << weightCount << std::endl;
	std::cout << "Output Craneen: " << Ntupname << std::endl;
        //important: free memory
        treeLoader.UnLoadDataset();
//            MLoutput.close();

    } //End Loop on Datasets

    /////////////
    // Writing //
    /////////////

    std::cout << " - Writing outputs to the files ..." << std::endl;

    if(bTagReweight && !isData){

        delete btwt;
//        delete btwtDown;
//        delete btwtUp;
        
//        btagEffHistFile_central->Write();
//        btagEffHistFile_up->Write();
//        btagEffHistFile_down->Write();
        btagEffHistFile_central->Close();
//        btagEffHistFile_up->Close();
//        btagEffHistFile_down->Close();
        delete btagEffHistFile_central;
//        delete btagEffHistFile_up;
//        delete btagEffHistFile_down;
    }    

    std::cout<<"TRIGGGG"<<std::endl;

    std::cout<<"preTrig: "<<preTrig<<"   postTrig: "<<postTrig<<std::endl;
    std::cout<<"********"<<std::endl;
    if(postTrig>0){
        std::cout<<"negative weight NormFactor (posttrig): "<< ( (postTrig - (2*negWeights))/postTrig )<<std::endl;
    }
    if(preTrig>0){
        std::cout<<"negative weight NormFactor (pretrig): "<< ( (preTrig - (2*negWeightsPretrig))/preTrig )<<std::endl;
    }

    delete trigger;

    if (HadTopOn){
        //if(TrainMVA)jetCombiner->Write(foutmva, true, pathPNGJetCombi.c_str());
        delete hadronicTopReco;        
    }
    if(EventBDTOn){
        delete eventBDT;
    }

    if(jetTools) delete jetTools;
    std::cout << "It took us " << ((double)clock() - start) / CLOCKS_PER_SEC << " to run the program" << std::endl;
    std::cout << "********************************************" << std::endl;
    std::cout << "           End of the program !!            " << std::endl;
    std::cout << "********************************************" << std::endl;
    
    return 0;
}
