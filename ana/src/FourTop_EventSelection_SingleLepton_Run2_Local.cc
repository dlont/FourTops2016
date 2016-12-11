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

#include "CutsTable.h"
#include "HadronicTopReco.h"
#include "EventBDT.h"
#include "Zpeak.h"
#include "Trigger.h"


#include <glog/logging.h>
#include <gflags/gflags.h>
#include "FourTopFlags.h"

#include "MakeDirectory.h"

#include "Version.h"

#include "Event.h"

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
    const int color                     = FLAGS_dataset_color;
    const int ls                        = FLAGS_dataset_linestyle;
    const int lw                        = FLAGS_dataset_linewidth;
    const double normf                  = FLAGS_dataset_norm_factor;
    const double EqLumi                 = FLAGS_dataset_eq_lumi;
    const double xSect                  = FLAGS_dataset_cross_section;
    const double PreselEff              = FLAGS_dataset_preselection_eff;
    const std::string inputChannel      = FLAGS_fourtops_channel;
    const int startEvent                = batch ? 0 : 0;
    const int endEvent                  = batch ? -1 : -1;

    std::vector<std::string> vecfileNames;
    boost::char_separator<char> sep(",");
    boost::tokenizer<boost::char_separator<char>> tokens(FLAGS_input_files, sep);
    for (const auto& t : tokens) {
        vecfileNames.push_back(t);
    }
    
    std::cout<<"!! number of root file: "<<jobid<<std::endl;


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
    int postTrig = 0;
    int ndefs =0;
    int negWeights = 0;
    float weightCount = 0.0;
    int eventCount = 0;
    float scalefactorbtageff, mistagfactor;
    string dataSetName = "";
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

    bool SingleLepton      = true;
    bool Muon              = false;
    bool Electron          = false;
    bool HadTopOn          = true;
    bool EventBDTOn        = true;
    bool TrainMVA          = false; // If false, the previously trained MVA will be used to calculate stuff
    bool bx25              = true;
    bool bTagReweight      = true;
    bool bTagCSVReweight   = false;
    bool bLeptonSF         = false;
    bool debug             = false;
    bool applyJER          = true;
    bool applyJEC          = true;
    bool JERNom            = true;
    bool JERUp             = false;
    bool JERDown           = false;
    bool JESUp             = false;
    bool JESDown           = false;
    bool fillingbTagHistos = false;
    std::string MVAmethod       = "BDT";
    float Luminosity       = 2628.0 ; //pb^-1 shown is C+D, D only is 2094.08809124; silverJson
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
    anaEnv.METCollection = "PFMET_slimmedMETs";
    anaEnv.MuonCollection = "Muons_slimmedMuons";
    anaEnv.ElectronCollection = "Electrons_slimmedElectrons";
    anaEnv.GenJetCollection   = "GenJets_slimmedGenJets";
    // anaEnv.TrackMETCollection = "";
    // anaEnv.GenEventCollection = "GenEvent";
    anaEnv.NPGenEventCollection = "NPGenEvent";
    anaEnv.MCParticlesCollection = "MCParticles";
    anaEnv.loadFatJetCollection = false;
    anaEnv.loadGenJetCollection = true;
    // anaEnv.loadGenEventCollection = false;
    anaEnv.loadNPGenEventCollection = false;
    anaEnv.loadMCParticles = true;
    // anaEnv.loadTrackMETCollection = false;
    anaEnv.JetType = 2;
    anaEnv.METType = 2;

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
    BTagCalibrationReader * reader_csvv2; //for csv reshaping 

    BTagWeightTools *btwt;
    BTagWeightTools *btwtUp;
    BTagWeightTools *btwtDown;
    bool isData = false;
    if(dataSetName.find("Data")!=string::npos){
        isData = true;
    }

    if(bTagReweight && dataSetName.find("Data")==string::npos){
        //Btag documentation : http://mon.iihe.ac.be/~smoortga/TopTrees/BTagSF/BTaggingSF_inTopTrees.pdf //v2 or _v2
        bTagCalib = new BTagCalibration("CSVv2","../TopTreeAnalysisBase/Calibrations/BTagging/CSVv2_80X_ichep_incl_ChangedTo_mujets.csv");
        bTagReader = new BTagCalibrationReader(bTagCalib,BTagEntry::OP_MEDIUM,"mujets","central"); //mujets
        bTagReaderUp = new BTagCalibrationReader(bTagCalib,BTagEntry::OP_MEDIUM,"mujets","up"); //mujets
        bTagReaderDown = new BTagCalibrationReader(bTagCalib,BTagEntry::OP_MEDIUM,"mujets","down"); //mujets

//        TFile fBtagEffHist_central("histos/Histo_powheg_76X.root");
//        TFile fBtagEffHist_down("histos/Histo_powheg_76X_Down.root");
//        TFile fBtagEffHist_up("histos/Histo_powheg_76X_Up.root");
        if(fillingbTagHistos) {
            if (Muon) {
                btwt = new BTagWeightTools(bTagReader,"HistosPtEta_"+dataSetName+ jobid+"_Mu.root",false,30,500,2.4);
                btwtUp = new BTagWeightTools(bTagReaderUp,"HistosPtEta_"+dataSetName+ jobid+"_Mu_Up.root",false,30,500,2.4);
                btwtDown = new BTagWeightTools(bTagReaderDown,"HistosPtEta_"+dataSetName+ jobid+"_Mu_Down.root",false,30,500,2.4);
            }
            else if (Electron) {
                btwt = new BTagWeightTools(bTagReader,"HistosPtEta_"+dataSetName+ jobid+"_El.root",false,30,500,2.4);
                btwtUp = new BTagWeightTools(bTagReaderUp,"HistosPtEta_"+dataSetName+ jobid+"_El_Up.root",false,30,500,2.4);
                btwtDown = new BTagWeightTools(bTagReaderDown,"HistosPtEta_"+dataSetName+ jobid+"_El_Down.root",false,30,500,2.4);
            }
        }    
        else {
            btwt = new BTagWeightTools(bTagReader,"histos/Histo_powheg_76X.root",false,30,500,2.4); 
            btwtUp = new BTagWeightTools(bTagReaderUp,"histos/Histo_powheg_76X_Down.root",false,30,500,2.4); 
            btwtDown = new BTagWeightTools(bTagReaderDown,"histos/Histo_powheg_76X_Up.root",false,30,500,2.4); 
        }
    }

    if(bTagCSVReweight && !isData){
        // BTagCalibration calib_csvv2("csvv2", "../TopTreeAnalysisBase/Calibrations/BTagging/ttH_BTV_CSVv2_13TeV_2015D_20151120.csv");
        BTagCalibration calib_csvv2("csvv2", "../TopTreeAnalysisBase/Calibrations/BTagging/CSVv2_80X_ichep_incl_ChangedTo_mujets.csv");
        reader_csvv2 = new BTagCalibrationReader(&calib_csvv2, // calibration instance
              BTagEntry::OP_RESHAPING, // operating point
              "iterativefit", // measurement type
              "central"); // systematics type
    }
//    std::exit(EXIT_SUCCESS);
    /////////////////////////////////////////////////
    //                   Lepton SF                 //
    /////////////////////////////////////////////////
    MuonSFWeight* muonSFWeightID_TT;   
    MuonSFWeight* muonSFWeightIso_TT;
    MuonSFWeight* muonSFWeightTrigC_TT;
    MuonSFWeight* muonSFWeightTrigD1_TT;
    MuonSFWeight* muonSFWeightTrigD2_TT;


    ElectronSFWeight* electronSFWeight; 
    if(bLeptonSF){
        if(Muon){ 
            // muonSFWeight = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/Muon_SF_TopEA.root","SF_totErr",false,false);  OLD SF WEIGHT
            muonSFWeightID_TT = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/MuonID_Z_RunBCD_prompt80X_7p65.root", "MC_NUM_TightIDandIPCut_DEN_genTracks_PAR_pt_spliteta_bin1/abseta_pt_ratio", true, false, false);
            muonSFWeightIso_TT = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/MuonIso_Z_RunBCD_prompt80X_7p65.root", "MC_NUM_TightRelIso_DEN_TightID_PAR_pt_spliteta_bin1/abseta_pt_ratio", true, false, false);  // Tight RelIso, Tight ID
            muonSFWeightTrigC_TT = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/SingleMuonTrigger_Z_RunBCD_prompt80X_7p65.root", "IsoMu22_OR_IsoTkMu22_PtEtaBins_Run273158_to_274093/efficienciesDATA/abseta_PLOT_pt_bin0_&_Tight2012_pass_&_tag_IsoMu22_pass_DATA", true, false, false);
            muonSFWeightTrigD1_TT = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/SingleMuonTrigger_Z_RunBCD_prompt80X_7p65.root", "IsoMu22_OR_IsoTkMu22_PtEtaBins_Run273158_to_274093/efficienciesDATA/abseta_PLOT_pt_bin0_&_Tight2012_pass_&_tag_IsoMu22_pass_DATA", true, false, false);
            muonSFWeightTrigD2_TT = new MuonSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/MuonSF/SingleMuonTrigger_Z_RunBCD_prompt80X_7p65.root", "IsoMu22_OR_IsoTkMu22_PtEtaBins_Run273158_to_274093/efficienciesDATA/abseta_PLOT_pt_bin0_&_Tight2012_pass_&_tag_IsoMu22_pass_DATA", true, false, false);
        }
        else if(Electron){
            electronSFWeight = new ElectronSFWeight("../TopTreeAnalysisBase/Calibrations/LeptonSF/ElectronSF/egammaEffi.txt_SF2D_GsfTrackingEff.root","EGamma_SF2D",false,false);    
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
    //             Get Luminosity for data         //
    /////////////////////////////////////////////////

    std::cout <<"found sample with equivalent lumi "<<  theDataset->EquivalentLumi() <<std::endl;
    if(dataSetName.find("Data") != string::npos || dataSetName.find("data")!=string::npos || dataSetName.find("DATA")!=string::npos)
    {
        Luminosity = theDataset->EquivalentLumi();      std::cout <<"found DATA sample with equivalent lumi "<<  theDataset->EquivalentLumi() <<std::endl;
    }
    std::cout << "Rescaling to an integrated luminosity of "<< Luminosity <<" pb^-1" << std::endl;

    /////////////////////////////////////////////////
    //                Top Reco MVA                 //
    /////////////////////////////////////////////////
    HadronicTopReco *hadronicTopReco;
    if(HadTopOn){
        hadronicTopReco = new HadronicTopReco(nullptr, Muon, Electron, TrainMVA, datasets, MVAmethod, debug, Luminosity);
    }
    /////////////////////////////////////////////////
    //            vectors of objects               //
    /////////////////////////////////////////////////
    std::cout << " - Variable declaration ..." << std::endl;
    vector < TRootVertex* >   vertex;
    vector < TRootMuon* >     init_muons;
    vector < TRootElectron* > init_electrons;
    vector < TRootJet* >      init_jets;
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

    LumiWeights = LumiReWeighting("../TopTreeAnalysisBase/Calibrations/PileUpReweighting/pileup_MC_RunIISpring16MiniAODv2-Asympt.root", "../TopTreeAnalysisBase/Calibrations/PileUpReweighting/pileup_2016Data80X_Run273158-276811Cert.root", "pileup", "pileup");    
    LumiWeights_up = LumiReWeighting("../TopTreeAnalysisBase/Calibrations/PileUpReweighting/pileup_MC_RunIISpring16MiniAODv2-Asympt.root", "../TopTreeAnalysisBase/Calibrations/PileUpReweighting/pileup_2016Data80X_Run273158-276811Cert.root", "pileup", "pileup");    
    LumiWeights_down = LumiReWeighting("../TopTreeAnalysisBase/Calibrations/PileUpReweighting/pileup_MC_RunIISpring16MiniAODv2-Asympt.root", "../TopTreeAnalysisBase/Calibrations/PileUpReweighting/pileup_2016Data80X_Run273158-276811Cert.root", "pileup", "pileup");    

    ///////////////////////////////////////////
    ///  Initialise Jet Energy Corrections  ///
    ///////////////////////////////////////////
    
    vector<JetCorrectorParameters> vCorrParam;
    string pathCalJEC = "../TopTreeAnalysisBase/Calibrations/JECFiles/Spring16_25nsV6/";

    if(isData)
    {
        JetCorrectorParameters *L1JetCorPar = new JetCorrectorParameters(pathCalJEC+"Spring16_25nsV6_DATA_L1FastJet_AK4PFchs.txt");
        vCorrParam.push_back(*L1JetCorPar);
        JetCorrectorParameters *L2JetCorPar = new JetCorrectorParameters(pathCalJEC+"Spring16_25nsV6_DATA_L2Relative_AK4PFchs.txt");
        vCorrParam.push_back(*L2JetCorPar);
        JetCorrectorParameters *L3JetCorPar = new JetCorrectorParameters(pathCalJEC+"Spring16_25nsV6_DATA_L3Absolute_AK4PFchs.txt");
        vCorrParam.push_back(*L3JetCorPar);
        JetCorrectorParameters *L2L3ResJetCorPar = new JetCorrectorParameters(pathCalJEC+"Spring16_25nsV6_DATA_L2L3Residual_AK4PFchs.txt");
        vCorrParam.push_back(*L2L3ResJetCorPar);
    }
    else
    {
        JetCorrectorParameters *L1JetCorPar = new JetCorrectorParameters(pathCalJEC+"Spring16_25nsV6_MC_L1FastJet_AK4PFchs.txt");
        vCorrParam.push_back(*L1JetCorPar);
        JetCorrectorParameters *L2JetCorPar = new JetCorrectorParameters(pathCalJEC+"Spring16_25nsV6_MC_L2Relative_AK4PFchs.txt");
        vCorrParam.push_back(*L2JetCorPar);
        JetCorrectorParameters *L3JetCorPar = new JetCorrectorParameters(pathCalJEC+"Spring16_25nsV6_MC_L3Absolute_AK4PFchs.txt");
        vCorrParam.push_back(*L3JetCorPar);
    }
    JetCorrectionUncertainty *jecUnc = new JetCorrectionUncertainty(pathCalJEC+"Spring16_25nsV6_MC_Uncertainty_AK4PFchs.txt");

    JetTools *jetTools = new JetTools(vCorrParam, jecUnc, true); //true means redo also L1

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
        //                 nlo or bx25?                //
        /////////////////////////////////////////////////
        bool nlo = true;
        dataSetName = datasets[d]->Name();

        if(dataSetName.find("JERDown")!=string::npos){
            JERDown=true;
        }
        else if(dataSetName.find("JERUp")!=string::npos){
            JERUp=true;
        }
        else{
            JERNom=true;
        }

        if(dataSetName.find("JESDown")!=string::npos){
            JESDown=true;
        }
        else if(dataSetName.find("JESUp")!=string::npos){
            JESUp=true;
        }    

        if(dataSetName.find("bx50") != std::string::npos) bx25 = false;
        else bx25 = true;
        if(bx25) std::cout << "Dataset with 25ns Bunch Spacing!" <<std::endl;
        else std::cout << "Dataset with 50ns Bunch Spacing!" <<std::endl;

        if(dataSetName.find("NLO") != std::string::npos || dataSetName.find("nlo") !=std::string::npos) nlo = true;
        else nlo = false;
        if(nlo) std::cout << "NLO Dataset!" <<std::endl;
        else std::cout << "LO Dataset!" << std::endl;

        ///////////////////////////////////////////////////////
        //      Setup Date string and nTuple for output      //
        ///////////////////////////////////////////////////////

        SourceDate *strdate = new SourceDate();
        string date_str = strdate->ReturnDateStr();

        /////////////////////////////////////////////////
        //               Craneen setup                 //
        /////////////////////////////////////////////////
        string channel_dir = "output/Craneens"+channelpostfix;
        string date_dir = channel_dir+"/Craneens" + date_str +"/";
        int mkdirstatus = mkdir_p(channel_dir.c_str());
        mkdirstatus = mkdir_p(date_dir.c_str());
        LOG(INFO) << "created dirs";
        string Ntuptitle   = "Craneen_" + channelpostfix;
        
        string Ntupname    = "output/Craneens" + channelpostfix + "/Craneens" + date_str + "/Craneen_" + dataSetName + postfix + ".root";     
        TFile * tupfile    = new TFile(Ntupname.c_str(),"RECREATE");
        TTree * tup        = new TTree(Ntuptitle.c_str(), Ntuptitle.c_str());
        Event myEvent;
        myEvent.makeBranches(tup);

        LOG(INFO) << "Output Craneens File: " << Ntupname ;

	TTree * booktup      = new TTree("bookkeeping", "bookkeeping");
	long long runId = 0;			booktup -> Branch("Runnr",&runId,"Runnr/I");
	long long evId  = 0;			booktup -> Branch("Eventnr",&evId,"Evnr/I");
	long long lumBlkId = 0;			booktup -> Branch("Lumisec",&lumBlkId,"Lumisec/I");
	std::string tag = GIT_TAG; 		booktup -> Branch("Tag",&tag);
  

        ////////////////////////////////////////////////////////////
        //       Define object containers and initalisations      //
        ////////////////////////////////////////////////////////////

        float BDTScore, MHT, MHTSig, STJet,leptoneta, leptonpt, leptonphi, electronpt, electroneta, bjetpt, EventMass, EventMassX, SumJetMass, SumJetMassX, H, HX;
        float HTHi, HTRat, HT, HTX, HTH, HTXHX, sumpx_X, sumpy_X, sumpz_X, sume_X, sumpx, sumpy, sumpz, sume, jetpt, PTBalTopEventX, PTBalTopSumJetX, PTBalTopMuMet;     
        int itrigger = -1, previousRun = -1;
        int currentRun;           
        vector<TRootElectron*> selectedElectrons;
        vector<TRootPFJet*>    selectedOrigJets; //all original jets before jet lepton cleaning
        vector<TRootPFJet*>    selectedJets; //all jets after jet lepton cleaning
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
        if (dataSetName.find("Data")!=string::npos || dataSetName.find("data")!=string::npos || dataSetName.find("DATA")!=string::npos) TrainMVA=false;

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

        for (long long ievt = event_start; ievt < end_d; ievt++)
        {
            LOG(INFO) <<"START OF EVENT LOOP";

            BDTScore= -99999.0, MHT = 0., MHTSig = 0.,leptoneta = 0., leptonpt =0., electronpt=0., electroneta=0., bjetpt =0., STJet = 0.;
            EventMass =0., EventMassX =0., SumJetMass = 0., SumJetMassX=0., HTHi =0., HTRat = 0;  H = 0., HX =0., HT = 0., HTX = 0.;
            HTH=0.,HTXHX=0., sumpx_X = 0., sumpy_X= 0., sumpz_X =0., sume_X= 0. , sumpx =0., sumpy=0., sumpz=0., sume=0., jetpt =0.;
            PTBalTopEventX = 0., PTBalTopSumJetX =0.;

            unsigned long ievt_d = ievt;

            if(ievt%1000 == 0)
            {
                std::cout<<"Processing the "<<ievt<<"th event, time = "<< ((double)clock() - start) / CLOCKS_PER_SEC 
                << " ("<<100*(ievt-0)/(ending-0)<<"%)"<<flush<<"\r"<<std::endl;
            }

            float scaleFactor = 1.;  // scale factor for the event
            bool trigged = false;  // Disabling the HLT requirement
            LOG(INFO) <<"Load Event";
            event = treeLoader.LoadEvent (ievt, vertex, init_muons, init_electrons, init_jets, mets, debug);
            if (dataSetName.find("Data")==string::npos) {
                genjets = treeLoader.LoadGenJet(ievt,false);
            }

            ///////////////////////////////////////////
            //      Set up for miniAOD weights       //
            ///////////////////////////////////////////

            currentRun  = event->runId(); 
            LOG(INFO) <<"got run ID";

            runId    = event->runId(); 
	    evId     = event->eventId();
	    lumBlkId = event->lumiBlockId();
	    booktup -> Fill();
   
            datasets[d]->eventTree()->LoadTree(ievt); 
            LOG(INFO) <<"load tree";

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
                if(JERNom) jetTools->correctJetJER(init_jets, genjets, mets[0], "nominal", false);
                else if(JERDown) jetTools->correctJetJER(init_jets, genjets, mets[0], "minus", false);
                else if (JERUp) jetTools->correctJetJER(init_jets, genjets, mets[0], "plus", false);
                /// Example how to apply JES systematics
            }


            if(JESDown) jetTools->correctJetJESUnc(init_jets, "minus", 1);
            else if(JESUp) jetTools->correctJetJESUnc(init_jets, "plus", 1);


            if (applyJEC)   ///should this have  && dataSetName.find("Data")==string::npos
            {
                jetTools->correctJets(init_jets, event->fixedGridRhoFastjetAll(), isData);
            }

            ///////////////////////////////////////////////////////////
            //           Object definitions for selection            //
            ///////////////////////////////////////////////////////////
            Run2Selection r2selection(init_jets, init_muons, init_electrons, mets);

            int nMu = 0, nEl = 0, nLooseMu = 0, nLooseEl = 0; //number of (loose) muons/electrons

            LOG(INFO) <<"Get jets";
            selectedOrigJets                                    = r2selection.GetSelectedJets();                                        
            if(Electron){
                LOG(INFO) <<"Get Loose Muons";
                selectedMuons                                       = r2selection.GetSelectedMuons(10, 2.5, 0.25, "Loose", "Spring15"); 
                nMu = selectedMuons.size();
                LOG(INFO) <<"Get Tight Electrons";                                                                                          
                selectedOrigElectrons                               = r2selection.GetSelectedElectrons(30, 2.1, "Tight", "Spring16_80X", true, false); 
                LOG(INFO) <<"Get Loose Electrons";
                selectedOrigExtraElectrons                          = r2selection.GetSelectedElectrons(15, 2.5, "Veto", "Spring16_80X", true, false); 
            }
            else if(Muon){
                LOG(INFO) <<"Get Tight Muons";
                selectedMuons                                       = r2selection.GetSelectedMuons(26, 2.1, 0.15, "Tight", "Spring15"); 
                nMu = selectedMuons.size(); //Number of Muons in Event
                selectedOrigElectrons                                   = r2selection.GetSelectedElectrons(15, 2.5, "Veto", "Spring16_80X", true, false);
                LOG(INFO) <<"Get Loose Electrons";    
                selectedExtraMuons                                  = r2selection.GetSelectedMuons(10, 2.5, 0.25, "Loose", "Spring15"); 
                LOG(INFO) <<"Get Loose Muons";
                nLooseMu = selectedExtraMuons.size();   //Number of loose muons      
            }

            //remove electrons between 1.4442 and 1.5660
            selectedElectrons.clear();
            for(int e_iter=0; e_iter<selectedOrigElectrons.size();e_iter++){
                if(selectedOrigElectrons[e_iter]->Eta()<=1.4442 || selectedOrigElectrons[e_iter]->Eta()>=1.5660){
                    selectedElectrons.push_back(selectedOrigElectrons[e_iter]);
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
            //std::cout<<nMu<<"<--nmu  nEl-->"<<nEl<<std::endl;
            if(Muon && nMu>0){
                for (int origJets=0; origJets<selectedOrigJets.size(); origJets++){
                    if(selectedOrigJets[origJets]->Pt()<30) std::cout<<selectedOrigJets[origJets]->Pt()<<std::endl;
                    if(selectedOrigJets[origJets]->DeltaR(*selectedMuons[0])>0.4){
                        selectedJets.push_back(selectedOrigJets[origJets]);
                    }                    
                }
            }
            else if(Electron && nEl>0){
                for (int origJets=0; origJets<selectedOrigJets.size(); origJets++){
                    if(selectedOrigJets[origJets]->DeltaR(*selectedElectrons[0])>0.4){
                        selectedJets.push_back(selectedOrigJets[origJets]);
                    }                       
                }
            }
            else selectedJets = selectedOrigJets;

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
                if (selectedJets[seljet]->btag_combinedInclusiveSecondaryVertexV2BJetTags() > 0.46   ) //0.605
                {
                    selectedLBJets.push_back(selectedJets[seljet]);
                    if (selectedJets[seljet]->btag_combinedInclusiveSecondaryVertexV2BJetTags() > 0.80) //0.890
                    {
                        HTb += selectedJets[seljet]->Pt();
                        selectedMBJets.push_back(selectedJets[seljet]);
                        if (selectedJets[seljet]->btag_combinedInclusiveSecondaryVertexV2BJetTags() > 0.935) //0.970
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

            ///////////////////////////////////////////
            //     Apply primary vertex selection    //
            ///////////////////////////////////////////

            bool isGoodPV = r2selection.isPVSelected(vertex, 4, 24., 2);
            LOG(INFO) <<"PrimaryVertexBit: " << isGoodPV << " TriggerBit: " << trigged;

            /////////////////////////////////
            //        Trigger              //
            /////////////////////////////////
            float normfactor = datasets[d]->NormFactor();
//            treeLoader.ListTriggers(currentRun,0);
            trigger->checkAvail(currentRun, datasets, d, &treeLoader, event, treenumber);
            trigged = trigger->checkIfFired(currentRun, datasets, d);
 
            /////////////////////////////////
            //       Primary vertex        //
            /////////////////////////////////
            //Filling Histogram of the number of vertices before Event Selection
            if (!isGoodPV) continue; // Check that there is a good Primary Vertex

            /////////////////////////////////
            //        Trigger              //
            /////////////////////////////////            
            preTrig++;
            if (!trigged)          continue;  //If an HLT condition is not present, skip this event in the loop.       
            postTrig++; 


            /////////////////////////////////////////////////
            //               Pu reweighting                //
            /////////////////////////////////////////////////

            float lumiWeight, lumiWeight_up, lumiWeight_down;
            if(dataSetName.find("Data") !=string::npos || dataSetName.find("data") != string::npos || dataSetName.find("DATA") != string::npos)
            {
                lumiWeight=1;
                lumiWeight_up=1;
                lumiWeight_down=1;
            }
            else{
                // lumiWeight = LumiWeights.ITweight( vertex.size() ); 
//                lumiWeight = LumiWeights.ITweight( (int)event->nTruePU());
//                lumiWeight_up = LumiWeights_up.ITweight( (int)event->nTruePU()); 
//                lumiWeight_down = LumiWeights_down.ITweight( (int)event->nTruePU()); 
                lumiWeight = 1.;
                lumiWeight_up = 1.; 
                lumiWeight_down = 1.; 
 
                
            }
            scaleFactor = scaleFactor * lumiWeight;


            /////////////////////////////////////////////////
            //                    bTag SF                  //
            /////////////////////////////////////////////////

            float bTagEff(-1);
            float bTagEffUp(-1);
            float bTagEffDown(-1);
            if(fillingbTagHistos){
                if(bTagReweight && dataSetName.find("Data")==string::npos){
                //get btag weight info
                    for(int jetbtag = 0; jetbtag<selectedJets.size(); jetbtag++){
                        float jetpt = selectedJets[jetbtag]->Pt();
                        float jeteta = selectedJets[jetbtag]->Eta();
                        float jetdisc = selectedJets[jetbtag]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                        BTagEntry::JetFlavor jflav;
                        int jetpartonflav = std::abs(selectedJets[jetbtag]->partonFlavour());
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
                    btwtUp->FillMCEfficiencyHistos(selectedJets); 
                    btwtDown->FillMCEfficiencyHistos(selectedJets); 

                }
            }

            LOG(INFO)<<"getMCEventWeight for btag";
            float btagWeight = 1;
            float btagWeightUp = 1;
            float btagWeightDown = 1;
            if(bTagReweight && dataSetName.find("Data")==string::npos){
                if(!fillingbTagHistos){
                    btagWeight =  btwt->getMCEventWeight(selectedJets, false);
                    btagWeightUp =  btwtUp->getMCEventWeight(selectedJets, false);
                    btagWeightDown =  btwtDown->getMCEventWeight(selectedJets, false);
                }
                
                LOG(INFO)<<"btag weight "<<btagWeight<<"  btag weight Up "<<btagWeightUp<<"   btag weight Down "<<btagWeightDown;
            }
            ////csv discriminator reweighting

            if(bTagCSVReweight && !isData){
            //get btag weight info
                for(int jetbtag = 0; jetbtag<selectedJets.size(); jetbtag++){
                    float jetpt = selectedJets[jetbtag]->Pt();
                    float jeteta = selectedJets[jetbtag]->Eta();
                    float jetdisc = selectedJets[jetbtag]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                    BTagEntry::JetFlavor jflav;
                    int jetpartonflav = std::abs(selectedJets[jetbtag]->partonFlavour());
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
                    bTagEff = reader_csvv2->eval(jflav, jeteta, jetpt, jetdisc);   
                    btagWeight*=bTagEff;
             
                    LOG(INFO)<<"btag efficiency = "<<bTagEff;       
                }      


            }
            scaleFactor*=btagWeight; 


            /////////////////////////////////////////////////
            //                   Lepton SF                 //
            /////////////////////////////////////////////////

            float fleptonSF = 1;
            if(bLeptonSF){ ///lepton SF for ID and ISO
                if(Muon && nMu>0){
                    fleptonSF = muonSFWeightID_TT->at(selectedMuons[0]->Eta(), selectedMuons[0]->Pt(), 0) * muonSFWeightIso_TT->at(selectedMuons[0]->Eta(), selectedMuons[0]->Pt(), 0);
                }
                else if(Electron && nEl>0){
                    fleptonSF = electronSFWeight->at(selectedElectrons[0]->Eta(),selectedElectrons[0]->Pt(),0);
                }
            }

            float trigSFC = 1;
            float trigSFD1 = 1;
            float trigSFD2 = 1;
            float trigSFTot = 1;
            if(bLeptonSF){ //lepton SF for trigger
                if(dataSetName.find("Data")==string::npos && Muon && nMu>0){
                    trigSFC = muonSFWeightTrigC_TT->at(selectedMuons[0]->Eta(), selectedMuons[0]->Pt(), 0);
                    trigSFD1 = muonSFWeightTrigD1_TT->at(selectedMuons[0]->Eta(), selectedMuons[0]->Pt(), 0);
                    trigSFD2 = muonSFWeightTrigD2_TT->at(selectedMuons[0]->Eta(), selectedMuons[0]->Pt(), 0);       
                    trigSFTot =( (trigSFC*17.2) + (trigSFD1*947.544) + (trigSFD2*1681.2) )/Luminosity;  
                }
                fleptonSF*=trigSFTot;
            }

            LOG(INFO)<<"lepton SF:  "<<fleptonSF;
            if(dataSetName.find("Data")==string::npos)   scaleFactor *= fleptonSF;


            /////////////////////////////////
            //        Gen weights          //
            /////////////////////////////////

            double weight_0 = 1; //nominal
            double weight_1 = 1, weight_2 = 1, weight_3 = 1, weight_4 = 1, weight_5 = 1, weight_6 = 1, weight_7 = 1, weight_8 = 1;

            if(dataSetName.find("Data")==string::npos){
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
                }
                else if (event->getWeight(1001)!= -9999){
                    weight_0 = (event->getWeight(1001))/(abs(event->originalXWGTUP()));  
                    weight_1 = (event->getWeight(1002))/(abs(event->originalXWGTUP()));                
                    weight_2 = (event->getWeight(1003))/(abs(event->originalXWGTUP()));                
                    weight_3 = (event->getWeight(1004))/(abs(event->originalXWGTUP()));                
                    weight_4 = (event->getWeight(1005))/(abs(event->originalXWGTUP()));                
                    weight_5 = (event->getWeight(1006))/(abs(event->originalXWGTUP()));                
                    weight_6 = (event->getWeight(1007))/(abs(event->originalXWGTUP()));                
                    weight_7 = (event->getWeight(1008))/(abs(event->originalXWGTUP()));                
                    weight_8 = (event->getWeight(1009))/(abs(event->originalXWGTUP()));                    
                }
            }

            /////////////////////////////////////////////////
            //            neg weights counter              //
            /////////////////////////////////////////////////

            if(weight_0 < 0.0)
            {
                //scaleFactor *= -1.0;  //Taking into account negative weights in NLO Monte Carlo
                negWeights++;
            }

            //Apply the lepton, jet, btag and HT & MET selections

            LOG(INFO)<<"Number of Muons = "<< nMu <<"    electrons =  "  <<nEl<<"     Jets = "<< selectedJets.size()   <<" loose BJets = "<<  nLtags   <<
                "  MuonChannel = "<<Muon<<" Electron Channel"<<Electron;

            ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //                                                                                 Baseline Event selection                                                                      //
            ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if (Muon)
            {   
                if  (  (!( nMu == 1 && nEl == 0 && nLooseMu == 1 && nJets>=6 && nMtags >=0)) )continue; // Muon Channel Selection
            }
            else if(Electron){
                if  (  !( nMu == 0 && nEl == 1 && nLooseEl == 1 && nJets>=6 && nMtags >=0)) continue; // Electron Channel Selection
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
            vector<TRootMCParticle*> mcParticles_flav;
            // TRootGenEvent* genEvt_flav = 0;
            if(dataSetName.find("TTJets")!=string::npos){
                // genEvt_flav = treeLoader.LoadGenEvent(ievt,false);
                treeLoader.LoadMCEvent(ievt, 0, mcParticles_flav,false);
                for(unsigned int p=0; p<mcParticles_flav.size(); p++) {
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
            LOG(INFO)<<"TMVA mass reco";
            sort(selectedJets.begin(),selectedJets.end(),HighestCVSBtag());
            float csvJetcsv1 = 1, csvJetcsv2 = 1, csvJetcsv3 =1, csvJetcsv4 =1;

            if (selectedJets.size()>4){
                csvJetcsv1 = selectedJets[0]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                csvJetcsv2 = selectedJets[1]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                csvJetcsv3 = selectedJets[2]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                csvJetcsv4 = selectedJets[3]->btag_combinedInclusiveSecondaryVertexV2BJetTags();                
            }
            // std::cout<<"csv: "<<csvJetcsv1<<std::endl;

            if (HadTopOn){
                hadronicTopReco->SetCollections(selectedJets, selectedMuons, selectedElectrons, scaleFactor);
            }

            if(HadTopOn){
                if(!TrainMVA){ //if not training, but computing 
                    hadronicTopReco->Compute1st(d, selectedJets, datasets);
                    hadronicTopReco->Compute2nd(d, selectedJets, datasets);
                    diTopness = hadronicTopReco->ReturnDiTopness();
                    SumJetMassX = hadronicTopReco->ReturnSumJetMassX();
                    HTX = hadronicTopReco->ReturnHTX();// std::cout<<"HTX: "<<HTX<<std::endl;
                }
//                hadronicTopReco->FillDiagnosticPlots(fout, d, selectedJets, datasets);
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
                float relisomu = (selectedMuons[0]->chargedHadronIso(4) + max( 0.0, selectedMuons[0]->neutralHadronIso(4) + selectedMuons[0]->photonIso(4) - 0.) ) / selectedMuons[0]->Pt();
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

            for (Int_t seljet1 =0; seljet1 < selectedJets.size(); seljet1++ )
            {

                //Event-level variables
                jetpt = selectedJets[seljet1]->Pt();
                HT = HT + jetpt;
                H = H +  selectedJets[seljet1]->P();
                if (seljet1 > 4  )  HTHi +=  selectedJets[seljet1]->Pt();
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

            //////////////////////
            // Jets Based Plots //
            //////////////////////

            float met = mets[0]->Et();

            LOG(INFO)<<"lepton vars";
            ////////////////////////////////////////////
            //              Get lepton pt             //
            ////////////////////////////////////////////
            float selectedLeptonPt = 0 ;
            if(Muon&&selectedMuons.size()>0){
                selectedLeptonPt = selectedMuons[0]->Pt();
                leptoneta = selectedMuons[0]->Eta();
                leptonphi = selectedMuons[0]->Phi();                
            }
            else if(Electron&&selectedElectrons.size()>0){
                selectedLeptonPt = selectedElectrons[0]->Pt();
                leptoneta = selectedElectrons[0]->Eta();
                leptonphi = selectedElectrons[0]->Phi();
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


            BDTScore = 0 ;
            if(EventBDTOn){
                eventBDT->computeBDTScore();
                BDTScore = eventBDT->returnBDTScore();
            }

            ////////////////////////////////////////////
            //       Return variables for ntup        //
            ////////////////////////////////////////////
            if (selectedMBJets.size()>0){
                bjetpt = selectedMBJets[0]->Pt();
            }
            float firstjetpt = selectedJets[0]->Pt();
            float secondjetpt = selectedJets[1]->Pt();
            float nvertices = vertex.size();
            float angletoplep = 0;
            float angletop1top2 = 0;
            if(HadTopOn){
                angletop1top2 = hadronicTopReco->ReturnAnglet1t2();
                angletoplep = hadronicTopReco->ReturnAngletoplep();                
            }
            float nOrigJets = (float)selectedOrigJets.size();
            float jet5and6Pt = jet5Pt+jet6Pt;
            double vals[63] = {BDTScore,nJets,nOrigJets,nLtags,nMtags,nTtags,HT,selectedLeptonPt,leptoneta,bjetpt,HT2M,HTb,HTH,HTRat,HTX,SumJetMassX,diTopness,numOfbb,numOfcc,numOfll,ttbar_flav,scaleFactor,fleptonSF,btagWeight,btagWeightUp,btagWeightDown,lumiWeight,lumiWeight_up,lumiWeight_down,nvertices,normfactor,Luminosity,weight_0,weight_1,weight_2,weight_3,weight_4,weight_5,weight_6,weight_7,weight_8,met,angletop1top2,angletoplep,firstjetpt,secondjetpt,leptonIso,leptonphi,chargedHIso,neutralHIso,photonIso,PUIso,jet5Pt,jet6Pt,jet5and6Pt, csvJetcsv1, csvJetcsv2, csvJetcsv3, csvJetcsv4, csvJetpt1, csvJetpt2, csvJetpt3, csvJetpt4};
            myEvent.fill(vals);
            tupfile->cd();
            tup->Fill();

        } //End Loop on Events
        std::cout<<"Write files"<<std::endl;
        tupfile->cd();
        tup->Write();
	booktup->Write();
        tupfile->Close();


        std::cout <<"n events passed  =  "<<passed <<std::endl;
        std::cout <<"n events with negative weights = "<<negWeights << std::endl;
        std::cout << "Event Count: " << eventCount << std::endl;
        std::cout << "Weight Count: " << weightCount << std::endl;
        //important: free memory
        treeLoader.UnLoadDataset();
//            MLoutput.close();

    } //End Loop on Datasets

    /////////////
    // Writing //
    /////////////

    std::cout << " - Writing outputs to the files ..." << std::endl;

    if(fillingbTagHistos && bTagReweight && dataSetName.find("Data")==string::npos){
        delete btwt;
        delete btwtDown;
        delete btwtUp;
    }    

    std::cout<<"TRIGGGG"<<std::endl;

    std::cout<<"preTrig: "<<preTrig<<"   postTrig: "<<postTrig<<std::endl;
    std::cout<<"********"<<std::endl;
    if(postTrig>0){
        std::cout<<"negative weight NormFactor: "<< ( (postTrig - (2*negWeights))/postTrig )<<std::endl;
    }

    delete trigger;

    if (HadTopOn){
        //if(TrainMVA)jetCombiner->Write(foutmva, true, pathPNGJetCombi.c_str());
//        hadronicTopReco->WriteDiagnosticPlots(fout, pathPNG);
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
