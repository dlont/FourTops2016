//////////////////////////////////////////////////////////////////////////////
////         Analysis code for search for Four Top Production.            ////
//////////////////////////////////////////////////////////////////////////////

// ttbar @ NLO 13 TeV:                              //ttbar @ NNLO 8 TeV:
//all-had ->679 * .46 = 312.34                      //all-had -> 245.8 * .46 = 113.068
//semi-lep ->679 *.45 = 305.55                      //semi-lep-> 245.8 * .45 = 110.61
//di-lep-> 679* .09 = 61.113                        //di-lep ->  245.8 * .09 = 22.122
#define _USE_MATH_DEFINES
#include "TStyle.h"
#include "TPaveText.h"
#include "TTree.h"
#include "TNtuple.h"
#include "TNtuple.h"
#include <TMatrixDSym.h>
#include <TMatrixDSymEigen.h>
#include <TVectorD.h>
#include <ctime>

#include <cmath>
#include <fstream>
#include <sstream>
#include <sys/stat.h>
#include <errno.h>
#include "TRandom3.h"
#include "TRandom.h"
#include "TProfile.h"
#include <iostream>
#include <map>
#include <cstdlib>

#include <glog/logging.h>

//user code
#include "TopTreeProducer/interface/TRootRun.h"
#include "TopTreeProducer/interface/TRootEvent.h"
#include "TopTreeAnalysisBase/Selection/interface/SelectionTable.h"
//#include "TopTreeAnalysisBase/Selection/interface/FourTopSelectionTable.h"
#include "TopTreeAnalysisBase/Selection/interface/Run2Selection.h"

#include "TopTreeAnalysisBase/Content/interface/AnalysisEnvironment.h"
#include "TopTreeAnalysisBase/Content/interface/Dataset.h"
#include "TopTreeAnalysisBase/Tools/interface/JetTools.h"
#include "TopTreeAnalysisBase/Tools/interface/PlottingTools.h"
#include "TopTreeAnalysisBase/Tools/interface/MultiSamplePlot.h"
#include "TopTreeAnalysisBase/Tools/interface/TTreeLoader.h"
#include "TopTreeAnalysisBase/Tools/interface/AnalysisEnvironmentLoader.h"
#include "TopTreeAnalysisBase/Reconstruction/interface/JetCorrectorParameters.h"
#include "TopTreeAnalysisBase/Reconstruction/interface/JetCorrectionUncertainty.h"
#include "TopTreeAnalysisBase/Reconstruction/interface/MakeBinning.h"
#include "TopTreeAnalysisBase/MCInformation/interface/LumiReWeighting.h"
#include "TopTreeAnalysisBase/MCInformation/interface/JetPartonMatching.h"
#include "TopTreeAnalysisBase/Reconstruction/interface/MEzCalculator.h"
#include "TopTreeAnalysisBase/Tools/interface/LeptonTools.h"
#include "TopTreeAnalysisBase/Tools/interface/SourceDate.h"

#include "TopTreeAnalysisBase/Reconstruction/interface/TTreeObservables.h"

//This header file is taken directly from the BTV wiki. It contains
// to correctly apply an event level Btag SF. It is not yet on CVS
// as I hope to merge the functionality into BTagWeigtTools.h
//#include "TopTreeAnalysisBase/Tools/interface/BTagSFUtil.h"
#include "TopTreeAnalysisBase/Tools/interface/BTagWeightTools.h"
#include "TopTreeAnalysisBase/Tools/interface/BTagCalibrationStandalone.h"

#include "TopTreeAnalysisBase/Tools/interface/JetCombiner.h"
#include "TopTreeAnalysisBase/Tools/interface/MVATrainer.h"
#include "TopTreeAnalysisBase/Tools/interface/MVAComputer.h"
// #include "TopTreeAnalysisBase/Tools/interface/JetTools.h"

#include "TopTreeAnalysisBase/../FourTops/SingleLepAnalysis/interface/CutsTable.h"
#include "TopTreeAnalysisBase/../FourTops/SingleLepAnalysis/interface/HadronicTopReco.h"
#include "TopTreeAnalysisBase/../FourTops/SingleLepAnalysis/interface/EventBDT.h"
#include "TopTreeAnalysisBase/../FourTops/SingleLepAnalysis/interface/Zpeak.h"
#include "TopTreeAnalysisBase/../FourTops/SingleLepAnalysis/interface/Trigger.h"

#include "MakeDirectory.h"

using namespace std;
using namespace TopTree;
using namespace reweight;

/// MultiSamplePlot
map<string,MultiSamplePlot*> MSPlot;
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
    
    google::InitGoogleLogging(argv[0]);
    
    //Placing arguments in properly typed variables for Dataset creation
    const string dName              = argv[1];
    const string dTitle             = argv[2];
    const int color                 = strtol(argv[4], nullptr, 10);
    const int ls                    = strtol(argv[5], nullptr, 10);
    const int lw                    = strtol(argv[6], nullptr, 10);
    const float normf               = strtod(argv[7], nullptr);
    const float EqLumi              = strtod(argv[8], nullptr);
    const float xSect               = strtod(argv[9], nullptr);
    const float PreselEff           = strtod(argv[10], nullptr);
    string fileName                 = argv[11];    
    const int startEvent            = batch ? 0 : strtol(argv[argc-2], nullptr, 10);
    const int endEvent              = batch ? -1 : strtol(argv[argc-1], nullptr, 10);
    string inputChannel;

    int lenOfFileName = fileName.length();
    char numberOfRootFile = fileName.at(lenOfFileName-6); //to find number of root file before .root
    char numberOfRootFile1 = fileName.at(lenOfFileName-7); //to find number of root file before .root
    char numberOfRootFile2 = fileName.at(lenOfFileName-8); //to find number of root file before .root

    cout<<"!! number of root file"<<numberOfRootFile<<endl;


    vector<string> vecfileNames;
    cout<<"argc: "<<argc<<endl;
        for(int args = 0; args < argc; args++)
        {
            cout<<args<<"  : "<<argv[args]<<endl;
        }

    if (batch){
        //Checking Passed Arguments to ensure proper execution of MACRO
        inputChannel       = argv[argc-1];
        cout<<"Input channel: "<<inputChannel<<endl;


        if(argc < 12)
        {
            std::cerr << "INVALID INPUT FROM XMLFILE.  CHECK XML IMPUT FROM SCRIPT.  " << argc << " ARGUMENTS HAVE BEEN PASSED." << std::endl;
            return 1;
        }

        for(int args = 11; args < argc-1; args++) 
        {
            vecfileNames.push_back(argv[args]);
        }        
    }
    else{  //ie. running locally 

        //Checking Passed Arguments to ensure proper execution of MACRO
        if(argc < 14)
        {
            std::cerr << "INVALID INPUT FROM XMLFILE.  CHECK XML IMPUT FROM SCRIPT.  " << argc << " ARGUMENTS HAVE BEEN PASSED." << std::endl;
            return 1;
        }

        for(int args = 11; args < argc-2; args++)
        {
            vecfileNames.push_back(argv[args]);
        }
    }

    cout << "---Dataset accepted from command line---" << endl;
    cout << "Dataset Name: " << dName << endl;
    cout << "Dataset Title: " << dTitle << endl;
    cout << "Dataset color: " << color << endl;
    cout << "Dataset ls: " << ls << endl;
    cout << "Dataset lw: " << lw << endl;
    cout << "Dataset normf: " << normf << endl;
    cout << "Dataset EqLumi: " << EqLumi << endl;
    cout << "Dataset xSect: " << xSect << endl;
    cout << "Dataset File Name: " << vecfileNames[0] << endl;
    cout << "Beginning Event: " << startEvent << endl;
    cout << "Ending Event: " << endEvent << endl;
    cout << "----------------------------------------" << endl;
    for(int vecfiles=0; vecfiles<vecfileNames.size(); vecfiles++){
        cout<<"vecfile names: "<<vecfiles<<" : "<<vecfileNames[vecfiles]<<endl;
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
    
    postfix = postfix + "_" + numberOfRootFile2 + numberOfRootFile1 + numberOfRootFile;
    clock_t start = clock();

    cout << "*************************************************************" << endl;
    cout << " Beginning of the program for the FourTop search ! "           << endl;
    cout << "*************************************************************" << endl;


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
    bool bTagReweight      = false;
    bool bTagCSVReweight   = false;
    bool bLeptonSF         = false;
    bool debug             = false;
    bool applyJER          = false;
    bool applyJEC          = false;
    bool JERNom            = false;
    bool JERUp             = false;
    bool JERDown           = false;
    bool JESUp             = false;
    bool JESDown           = false;
    bool fillingbTagHistos = false;
    string MVAmethod       = "BDT"; // MVAmethod to be used to get the good jet combi calculation (not for training! this is chosen in the jetcombiner class)
    float Luminosity       = 2628.0 ; //pb^-1 shown is C+D, D only is 2094.08809124; silverJson
    //bool split_ttbar     = false;

    if (batch && inputChannel.find("Mu")!=string::npos){
        Muon = true;
        Electron = false;
    }
    if (batch && inputChannel.find("El")!=string::npos){
        Muon = false;
        Electron = true;
    }
    if(Muon && SingleLepton){
        cout<<" ***** USING SINGLE MUON CHANNEL  ******"<<endl;
        channelpostfix = "_Mu";
    }
    else if(Electron && SingleLepton){
        cout<<" ***** Using SINGLE ELECTRON CHANNEL *****"<<endl;
        channelpostfix = "_El";
    }
    else    {
        cerr<<"Correct Channel not selected."<<endl;
        exit(1);
    }

    /////////////////////////////////
    //  Set up AnalysisEnvironment //
    /////////////////////////////////

    AnalysisEnvironment anaEnv;
    cout<<" - Creating environment ..."<<endl;
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
    vector < Dataset* > datasets;    cout << " - Creating Dataset ..." << endl;
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
        bTagCalib = new BTagCalibration("CSVv2","../TopTreeAnalysisBase/Calibrations/BTagging/CSVv2_76X_combToMujets.csv");
        bTagReader = new BTagCalibrationReader(bTagCalib,BTagEntry::OP_MEDIUM,"mujets","central"); //mujets
        bTagReaderUp = new BTagCalibrationReader(bTagCalib,BTagEntry::OP_MEDIUM,"mujets","up"); //mujets
        bTagReaderDown = new BTagCalibrationReader(bTagCalib,BTagEntry::OP_MEDIUM,"mujets","down"); //mujets

        if(fillingbTagHistos) {
            if (Muon) {
                btwt = new BTagWeightTools(bTagReader,"HistosPtEta_"+dataSetName+ numberOfRootFile2 + numberOfRootFile1 + numberOfRootFile+"_Mu.root",false,30,500,2.4);
                btwtUp = new BTagWeightTools(bTagReaderUp,"HistosPtEta_"+dataSetName+ numberOfRootFile2 + numberOfRootFile1 + numberOfRootFile+"_Mu_Up.root",false,30,500,2.4);
                btwtDown = new BTagWeightTools(bTagReaderDown,"HistosPtEta_"+dataSetName+ numberOfRootFile2 + numberOfRootFile1 + numberOfRootFile+"_Mu_Down.root",false,30,500,2.4);
            }
            else if (Electron) {
                btwt = new BTagWeightTools(bTagReader,"HistosPtEta_"+dataSetName+ numberOfRootFile2 + numberOfRootFile1 + numberOfRootFile+"_El.root",false,30,500,2.4);
                btwtUp = new BTagWeightTools(bTagReaderUp,"HistosPtEta_"+dataSetName+ numberOfRootFile2 + numberOfRootFile1 + numberOfRootFile+"_El_Up.root",false,30,500,2.4);
                btwtDown = new BTagWeightTools(bTagReaderDown,"HistosPtEta_"+dataSetName+ numberOfRootFile2 + numberOfRootFile1 + numberOfRootFile+"_El_Down.root",false,30,500,2.4);
            }
        }    
        else {
            btwt = new BTagWeightTools(bTagReader,"histos/Histo_powheg_76X.root",false,30,500,2.4); 
            btwtUp = new BTagWeightTools(bTagReaderUp,"histos/Histo_powheg_76X.root",false,30,500,2.4); 
            btwtDown = new BTagWeightTools(bTagReaderDown,"histos/Histo_powheg_76X.root",false,30,500,2.4); 
        }
    }

    if(bTagCSVReweight && !isData){
        // BTagCalibration calib_csvv2("csvv2", "../TopTreeAnalysisBase/Calibrations/BTagging/ttH_BTV_CSVv2_13TeV_2015D_20151120.csv");
        BTagCalibration calib_csvv2("csvv2", "../TopTreeAnalysisBase/Calibrations/BTagging/CSVv2_76X_combToMujets.csv");
        reader_csvv2 = new BTagCalibrationReader(&calib_csvv2, // calibration instance
              BTagEntry::OP_RESHAPING, // operating point
              "iterativefit", // measurement type
              "central"); // systematics type
    }

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
            // cout<<"ID: "<<muonSFWeightID_TT<<" Iso: "<<muonSFWeightIso_TT<<"  TrigC: "<<muonSFWeightTrigC_TT<<" TrigD1: "<< muonSFWeightTrigD1_TT<<" TrigD2: "<< muonSFWeightTrigD2_TT<<endl;
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
    cout << " Initialized Eventcomputer_ for event_level BDT" << endl;

    /////////////////////////////////////////////////
    ////                 Trigger                  ///
    /////////////////////////////////////////////////
    Trigger* trigger = new Trigger(Muon, Electron);
    trigger->bookTriggers();

    /////////////////////////////////////////////////
    //             Get Luminosity for data         //
    /////////////////////////////////////////////////

    cout <<"found sample with equivalent lumi "<<  theDataset->EquivalentLumi() <<endl;
    if(dataSetName.find("Data") != string::npos || dataSetName.find("data")!=string::npos || dataSetName.find("DATA")!=string::npos)
    {
        Luminosity = theDataset->EquivalentLumi();      cout <<"found DATA sample with equivalent lumi "<<  theDataset->EquivalentLumi() <<endl;
    }
    cout << "Rescaling to an integrated luminosity of "<< Luminosity <<" pb^-1" << endl;

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
    cout << " - Variable declaration ..." << endl;
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

    ///////////////////////////////////////////////////////
    //               MultiSample plots                   //
    ///////////////////////////////////////////////////////

    MSPlot["NbOfVertices"]          = new MultiSamplePlot(datasets, "NbOfVertices", 60, 0, 60, "Nb. of vertices");
    //Muons
    MSPlot["MuonPt"]                = new MultiSamplePlot(datasets, "MuonPt", 30, 0, 300, "PT_{#mu}");
    MSPlot["leptonIso"]             = new MultiSamplePlot(datasets, "LeptonIso", 10, 0, 0.25, "RelIso");    
    //Electrons
    MSPlot["ElectronRelIsolation"]  = new MultiSamplePlot(datasets, "ElectronRelIsolation", 10, 0, .25, "RelIso");
    //B-tagging discriminators
    MSPlot["BdiscBJetCand_CSV"]     = new MultiSamplePlot(datasets, "BdiscBJetCand_CSV", 20, 0, 1, "CSV b-disc.");
    MSPlot["NbOfSelectedBJets"]     = new MultiSamplePlot(datasets, "NbOfSelectedBJets", 8, 0, 8, "Nb. of tags");
    MSPlot["HTb_SelectedJets"]      = new MultiSamplePlot(datasets, "HTb_SelectedJets", 50, 0, 1500, "HTb");    
    //Jets
    MSPlot["JetEta"]                = new MultiSamplePlot(datasets, "JetEta", 40,-4, 4, "Jet #eta");
    MSPlot["JetpT"]                 = new MultiSamplePlot(datasets, "JetpT", 100, 0, 400, "Jet p_{T}");
    MSPlot["HT_SelectedJets"]       = new MultiSamplePlot(datasets, "HT_SelectedJets", 30, 0, 1500, "HT");
    MSPlot["HTRat"]                 = new MultiSamplePlot(datasets, "HTRat", 50, 0, 20, "HTRat");
    MSPlot["5thJetPt"]              = new MultiSamplePlot(datasets, "5thJetPt", 60, 0, 400, "PT_{jet}");
    MSPlot["6thJetPt"]              = new MultiSamplePlot(datasets, "6thJetPt", 60, 0, 400, "PT_{jet}");
    
    MSPlot["MET"]                   = new MultiSamplePlot(datasets, "MET", 70, 0, 700, "MET");
    MSPlot["NbOfBadTrijets"]        = new MultiSamplePlot(datasets, "NbOfBadTriJets", 150, 0, 150, "Nb. of Bad Combs");

    MSPlot["TriJetMass_Matched"]    = new MultiSamplePlot(datasets, "TriJetMassMatched", 100, 0, 1000, "m_{bjj}");
    MSPlot["TriJetMass_UnMatched"]  = new MultiSamplePlot(datasets, "TriJetMassUnMatched", 100, 0, 1000, "m_{bjj}");

    MSPlot["MVA2TriJetMass"]        = new MultiSamplePlot(datasets, "MVA2TriJetMass", 75, 0, 500, "m_{bjj}");
    MSPlot["MVA1TriJetMassMatched"] = new MultiSamplePlot(datasets, "MVA1TriJetMassMatched", 75, 0, 500, "m_{bjj}");


    /////////////////////////////////////////////////
    //                 Cuts table                  //
    /////////////////////////////////////////////////
//    CutsTable *cutsTable = new CutsTable(Muon, Electron);
//    cutsTable->AddSelections();
//    cutsTable->CreateTable(datasets, Luminosity);

    /////////////////////////////////////////////////
    //               Pu reweighting                //
    /////////////////////////////////////////////////
    cout<<"Getting lumi weights"<<endl;
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
    cout << " - Loop over datasets ... " << datasets.size () << " datasets !" << endl;
    for (unsigned int d = 0; d < datasets.size(); d++)
    {
        cout<<"Load Dataset"<<endl;    
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

//        ofstream MLoutput;
//        MLoutput.open(("MLvariables"+dataSetName+ numberOfRootFile2 + numberOfRootFile1 + numberOfRootFile+".csv").c_str());

        if(dataSetName.find("bx50") != std::string::npos) bx25 = false;
        else bx25 = true;
        if(bx25) cout << "Dataset with 25ns Bunch Spacing!" <<endl;
        else cout << "Dataset with 50ns Bunch Spacing!" <<endl;

        if(dataSetName.find("NLO") != std::string::npos || dataSetName.find("nlo") !=std::string::npos) nlo = true;
        else nlo = false;
        if(nlo) cout << "NLO Dataset!" <<endl;
        else cout << "LO Dataset!" << endl;

        ///////////////////////////////////////////////////////
        //      Setup Date string and nTuple for output      //
        ///////////////////////////////////////////////////////

        SourceDate *strdate = new SourceDate();
        string date_str = strdate->ReturnDateStr();
        if(debug)cout<<"date print"<<endl;

        /////////////////////////////////////////////////
        //               Craneen setup                 //
        /////////////////////////////////////////////////
        string channel_dir = "output/Craneens"+channelpostfix;
        string date_dir = channel_dir+"/Craneens" + date_str +"/";
        int mkdirstatus = mkdir_p(channel_dir.c_str());
        mkdirstatus = mkdir_p(date_dir.c_str());
        if(debug)cout<<"created dirs"<<endl;
        string Ntuptitle   = "Craneen_" + channelpostfix;
        
        string Ntupname    = "output/Craneens" + channelpostfix + "/Craneens" + date_str + "/Craneen_" + dataSetName + postfix + ".root";     
        TFile * tupfile    = new TFile(Ntupname.c_str(),"RECREATE");
        TNtuple * tup      = new TNtuple(Ntuptitle.c_str(), Ntuptitle.c_str(), "BDT:nJets:NOrigJets:nLtags:nMtags:nTtags:HT:LeptonPt:LeptonEta:LeadingBJetPt:HT2M:HTb:HTH:HTRat:HTX:SumJetMassX:multitopness:nbb:ncc:nll:ttbar_flav:ScaleFactor:SFlepton:SFbtag:SFbtagUp:SFbtagDown:SFPU:SFPU_up:SFPU_down:PU:NormFactor:Luminosity:GenWeight:weight1:weight2:weight3:weight4:weight5:weight6:weight7:weight8:met:angletop1top2:angletoplep:1stjetpt:2ndjetpt:leptonIso:leptonphi:chargedHIso:neutralHIso:photonIso:PUIso:5thjetpt:6thjetpt:jet5and6pt:csvJetcsv1:csvJetcsv2:csvJetcsv3:csvJetcsv4:csvJetpt1:csvJetpt2:csvJetpt3:csvJetpt4");
        LOG(INFO) << "Output Craneens File: " << Ntupname ;
        // string Ntup4j0bname    = "Craneens" + channelpostfix + "/Craneens" + date_str + "/Craneen_4j0b_" + dataSetName + postfix + ".root";     
        // TFile * tup4j0bfile    = new TFile(Ntupname.c_str(),"RECREATE");
        // TNtuple * tup4j0b      = new TNtuple(Ntuptitle.c_str(), Ntuptitle.c_str(), "BDT:nJets:NOrigJets:nLtags:nMtags:nTtags:HT:LeptonPt:LeptonEta:LeadingBJetPt:HT2M:HTb:HTH:HTRat:multitopness:nbb:ncc:nll:ttbar_flav:ScaleFactor:SFlepton:SFbtag:SFPU:PU:NormFactor:Luminosity:GenWeight:weight1:weight2:weight3:weight4:weight5:weight6:weight7:weight8:met:angletop1top2:angletoplep:1stjetpt:2ndjetpt:leptonIso:leptonphi:chargedHIso:neutralHIso:photonIso:PUIso");
        

//        string Ntupjetname = "output/Craneens" + channelpostfix + "/Craneens" + date_str + "/CraneenJets_" + dataSetName + postfix + ".root";
//        TFile * tupjetfile = new TFile(Ntupjetname.c_str(),"RECREATE");
//        TNtuple * tupjet   = new TNtuple(Ntuptitle.c_str(),Ntuptitle.c_str(), "jetpT:csvDisc:jeteta:jetphi:jetLeptDR:ScaleFactor:NormFactor:Luminosity:SFlepton:SFbtag:SFPU:GenWeight");
        
//        string NtupZname   = "output/Craneens" + channelpostfix + "/Craneens" + date_str + "/CraneenZ_" + dataSetName + postfix + ".root";
//        TFile * tupZfile   = new TFile(NtupZname.c_str(),"RECREATE");
//        TNtuple * tupZ     = new TNtuple(Ntuptitle.c_str(),Ntuptitle.c_str(), "invMassll:ScaleFactor:NormFactor:Luminosity");
//        if(debug)cout<<"created craneens"<<endl;

//        string NtupCutsname = "output/Craneens" + channelpostfix + "/Craneens" + date_str + "/CraneenCuts_" + dataSetName + postfix + ".root";
//        TFile * tupCutfile   = new TFile(NtupCutsname.c_str(),"RECREATE");

        // string elTuptitle = "Craneen_" + channelpostfix + "_ElecID";
        // string muTuptitle = "Craneen_" + channelpostfix + "_MuonID";
        // string jetTuptitle = "Craneen_" + channelpostfix + "_JetID";
//        string cutTuptitle = "output/Craneen_" + channelpostfix + "_CutFlow";
        // TNtuple * eltup = new TNtuple(elTuptitle.c_str(),elTuptitle.c_str(),"ScaleFactor:NormFactor:Luminosity:ElSuperclusterEta:Elfull5x5:EldEdatIn:EldPhiIn:ElhOverE:ElRelIso:ElEmP:Eld0:Eldz:ElMissingHits:ElE:ElP");
        // TNtuple * mutup = new TNtuple(muTuptitle.c_str(),muTuptitle.c_str(),"ScaleFactor:NormFactor:Luminosity:MuPt:MuEta:MuRelIso");
        // TNtuple * jettup = new TNtuple(jetTuptitle.c_str(),jetTuptitle.c_str(),"ScaleFactor:NormFactor:Luminosity:NHF:NEMF:nConstituents:CHF:CMultiplicity:CEMF");
//        TNtuple * cuttup = new TNtuple(cutTuptitle.c_str(),cutTuptitle.c_str(),"ScaleFactor:NormFactor:Luminosity:trigger:isGoodPV:Lep1:Lep2:nJets:nTags:HT");


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
        unsigned long long ending = datasets[d]->NofEvtsToRunOver();    cout <<"Number of events in full dataset = "<<  ending  <<endl;
        int event_start = startEvent; //set start of for loop to input startEvent
        double end_d = ending; //initialise end of for loop to end of dataset

        if(endEvent <ending && endEvent>0 ) end_d = endEvent; // if the input endEvent is less than total events in dataset (and greater than 0), set max of for loop to endEvent
        
        cout <<"Will run over "<<  end_d<< " events..."<<endl;    
        cout <<"Starting event = = = = "<< event_start  << endl;

        ////////////////////////////////////////////////////////////////////////////////
        //                                 Loop on events                             //
        ////////////////////////////////////////////////////////////////////////////////

        for (unsigned int ievt = event_start; ievt < end_d; ievt++)
        {
            if(debug) cout<<"START OF EVENT LOOP"<<endl;
            BDTScore= -99999.0, MHT = 0., MHTSig = 0.,leptoneta = 0., leptonpt =0., electronpt=0., electroneta=0., bjetpt =0., STJet = 0.;
            EventMass =0., EventMassX =0., SumJetMass = 0., SumJetMassX=0., HTHi =0., HTRat = 0;  H = 0., HX =0., HT = 0., HTX = 0.;
            HTH=0.,HTXHX=0., sumpx_X = 0., sumpy_X= 0., sumpz_X =0., sume_X= 0. , sumpx =0., sumpy=0., sumpz=0., sume=0., jetpt =0.;
            PTBalTopEventX = 0., PTBalTopSumJetX =0.;

            double ievt_d = ievt;

            if(ievt%1000 == 0)
            {
                std::cout<<"Processing the "<<ievt<<"th event, time = "<< ((double)clock() - start) / CLOCKS_PER_SEC 
                << " ("<<100*(ievt-0)/(ending-0)<<"%)"<<flush<<"\r"<<endl;
            }

            float scaleFactor = 1.;  // scale factor for the event
            bool trigged = false;  // Disabling the HLT requirement
            if(debug) cout<<"before tree load"<<endl;
            event = treeLoader.LoadEvent (ievt, vertex, init_muons, init_electrons, init_jets, mets, debug);      if(debug)cout<<"after tree load"<<endl; //load event
            if (dataSetName.find("Data")==string::npos) {
                // cout<<"getting gen jets"<<endl;
                genjets = treeLoader.LoadGenJet(ievt,false);
            //sort(genjets.begin(),genjets.end(),HighestPt()); // HighestPt() is included from the Selection class
            }
            // cout<<"macro genjets: "<<genjets.size()<<endl;
            float rho = event->fixedGridRhoFastjetAll();        if (debug)cout <<"Rho: " << rho <<endl;


            ///////////////////////////////////////////
            //      Set up for miniAOD weights       //
            ///////////////////////////////////////////

            currentRun = event->runId(); if(debug) cout<<"got run ID"<<endl;
            datasets[d]->eventTree()->LoadTree(ievt); if(debug) cout<<"load tree"<<endl;
            int treenumber = datasets[d]->eventTree()->GetTreeNumber(); 
            // cout<<"treenumber: "<< treenumber<<endl;
            currentfilename2 = datasets[d]->eventTree()->GetFile()->GetName();
            if(previousFilename2 != currentfilename2){
                previousFilename2 = currentfilename2;
                iFile2++;
                cout<<"got tree number: "<<treenumber<<endl;
                cout<<"File changed!!!! => iFile2 = "<<iFile2 << " new file is " << datasets[d]->eventTree()->GetFile()->GetName() << " in sample " << datasets[d]->Name() << endl;
            }

            //int rBytes = datasets[d]->runTree()->GetEntry(treenumber);  if(debug) cout<<"get entry with treenumber"<<endl;

            //////////////////////////////////////
            ///  Jet Energy Scale Corrections  ///
            //////////////////////////////////////

            // cout<<"before JER smearing"<<endl;
            // for(int jj=0; jj<init_jets.size();jj++){
            //     cout<<jj<<" jet pt : "<<init_jets[jj]->Pt()<<endl;
            // }

            if (applyJER && !isData)
            {
                if(JERNom) jetTools->correctJetJER(init_jets, genjets, mets[0], "nominal", false);
                else if(JERDown) jetTools->correctJetJER(init_jets, genjets, mets[0], "minus", false);
                else if (JERUp) jetTools->correctJetJER(init_jets, genjets, mets[0], "plus", false);
                /// Example how to apply JES systematics

                // cout << "JER smeared!!! " << endl;
            }
            // cout<<"after JER smearing" <<endl;

            // for(int jj=0; jj<init_jets.size();jj++){
            //     cout<<jj<<" jet pt : "<<init_jets[jj]->Pt()<<endl;
            // }

            if(JESDown) jetTools->correctJetJESUnc(init_jets, "minus", 1);
            else if(JESUp) jetTools->correctJetJESUnc(init_jets, "plus", 1);


            if (applyJEC)   ///should this have  && dataSetName.find("Data")==string::npos
            {
                // cout<<"apply JEC"<<endl;
                jetTools->correctJets(init_jets, event->fixedGridRhoFastjetAll(), isData);
            }

            ///////////////////////////////////////////////////////////
            //           Object definitions for selection            //
            ///////////////////////////////////////////////////////////
            Run2Selection r2selection(init_jets, init_muons, init_electrons, mets);

            int nMu = 0, nEl = 0, nLooseMu = 0, nLooseEl = 0; //number of (loose) muons/electrons

            if(Electron){
                                                                                                                                           
                selectedOrigJets                                    = r2selection.GetSelectedJets(); if (debug)cout<<"Getting Jets"<<endl; // ApplyJetId
                                                                                                                                            
                selectedMuons                                       = r2selection.GetSelectedMuons(10, 2.5, 0.25, "Loose", "Spring15"); if (debug)cout<<"Getting Loose Muons"<<endl;
                nMu = selectedMuons.size(); //Number of Muons in Event
                                                                                                                                            
                selectedOrigElectrons                                   = r2selection.GetSelectedElectrons(30, 2.1, "Tight", "Spring16_80X", true); if (debug)cout<<"Getting Tight Electrons"<<endl; // VBTF ID       
                                                                                                                                            
                selectedOrigExtraElectrons                              = r2selection.GetSelectedElectrons(15, 2.5, "Veto", "Spring16_80X", true); if (debug)cout<<"Getting Loose Electrons"<<endl;

            }
            else if(Muon){
                                                                                                                                           
                selectedOrigJets                                    = r2selection.GetSelectedJets();  if (debug)cout<<"Getting Jets"<<endl; // ApplyJetId
                                                                                                                                            
                selectedMuons                                       = r2selection.GetSelectedMuons(26, 2.1, 0.15, "Tight", "Spring15"); if (debug)cout<<"Getting Tight Muons"<<endl;
                nMu = selectedMuons.size(); //Number of Muons in Event
                                                                                                                                            
                selectedOrigElectrons                                   = r2selection.GetSelectedElectrons(15, 2.5, "Veto", "Spring16_80X", true); if (debug)cout<<"Getting Loose Electrons"<<endl; // VBTF ID    
                                                                                                                                            
                selectedExtraMuons                                  = r2selection.GetSelectedMuons(10, 2.5, 0.25, "Loose", "Spring15"); if (debug)cout<<"Getting Loose Muons"<<endl;
                nLooseMu = selectedExtraMuons.size();   //Number of loose muons      
            }
            //if(nEl>0) cout<<"nEl: "<<nEl<<endl;

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
             // cout<<"nel: "<<nEl<<"  nLooseEl: "<<nLooseEl<<"  origel: "<<selectedOrigElectrons.size()<<"  origextra el: "<<selectedOrigExtraElectrons.size()<<endl;
            }

            /////////////////////////////////////////////////
            //            Jet lepton cleaning              //
            /////////////////////////////////////////////////
            selectedJets.clear();
            //cout<<nMu<<"<--nmu  nEl-->"<<nEl<<endl;
            if(Muon && nMu>0){
                for (int origJets=0; origJets<selectedOrigJets.size(); origJets++){
                    if(selectedOrigJets[origJets]->Pt()<30) cout<<selectedOrigJets[origJets]->Pt()<<endl;
                    //cout<<"DR: "<< selectedOrigJets[origJets]->DeltaR(*selectedMuons[0])<<endl;
                    if(selectedOrigJets[origJets]->DeltaR(*selectedMuons[0])>0.4){
                        selectedJets.push_back(selectedOrigJets[origJets]);
                    }                    
                }
            }
            else if(Electron && nEl>0){
                for (int origJets=0; origJets<selectedOrigJets.size(); origJets++){
                    //cout<<"DR: "<< selectedOrigJets[origJets]->DeltaR(*selectedMuons[0])<<endl;
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
            if (debug)	cout <<"PrimaryVertexBit: " << isGoodPV << " TriggerBit: " << trigged <<endl;
            if (debug) cin.get();


            /////////////////////////////////
            //        Trigger              //
            /////////////////////////////////
            float normfactor = datasets[d]->NormFactor();

            // cout<<"!!CHECK AVAIL!!"<<endl;
            trigger->checkAvail(currentRun, datasets, d, &treeLoader, event, treenumber);
            // cout<<"!!CHECK FIRED!!"<<endl;

            trigged = trigger->checkIfFired(currentRun, datasets, d);
            // trigged=true;
//            tupCutfile->cd();
            //cutsTable->FillTable(d, normfactor, Luminosity, isGoodPV, trigged, scaleFactor, nMu, nLooseMu, nEl, nLooseEl, nJets, nLtags, nMtags, nTtags, cuttup);   if(debug) cout<<"cuts table filled"<<endl;
 
            /////////////////////////////////
            //       Primary vertex        //
            /////////////////////////////////
            //Filling Histogram of the number of vertices before Event Selection
            MSPlot["NbOfVertices"]->Fill(vertex.size(), datasets[d], true, Luminosity*scaleFactor);
            if (!isGoodPV) continue; // Check that there is a good Primary Vertex

            /////////////////////////////////
            //        Trigger              //
            /////////////////////////////////            
            preTrig++;
            if (debug)cout<<"triggered? Y/N?  "<< trigged  <<endl;
            //if(dataSetName.find("Data") != string::npos || dataSetName.find("data") != string::npos || dataSetName.find("DATA") != string::npos){
            if (!trigged)          continue;  //If an HLT condition is not present, skip this event in the loop.       
            //}
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
            // if(lumiWeight<0.2)     cout<<"PU:  "<<(int)event->nTruePU()<<"    LUMI WEIGHT   :   "<<lumiWeight<<" ! "<<endl;
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
                        if(debug) cout<<"parton flavour: "<<jetpartonflav<<"  jet eta: "<<jeteta<<" jet pt: "<<jetpt<<"  jet disc: "<<jetdisc<<endl;
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
                 
                        if(debug)cout<<"btag efficiency = "<<bTagEff<<endl;       
                    }      
                    btwt->FillMCEfficiencyHistos(selectedJets); 
                    btwtUp->FillMCEfficiencyHistos(selectedJets); 
                    btwtDown->FillMCEfficiencyHistos(selectedJets); 

                }
            }

            if (debug) cout<<"getMCEventWeight for btag"<<endl;
            float btagWeight = 1;
            float btagWeightUp = 1;
            float btagWeightDown = 1;
            if(bTagReweight && dataSetName.find("Data")==string::npos){
                if(!fillingbTagHistos){
                    btagWeight =  btwt->getMCEventWeight(selectedJets, false);
                    btagWeightUp =  btwtUp->getMCEventWeight(selectedJets, false);
                    btagWeightDown =  btwtDown->getMCEventWeight(selectedJets, false);
                }
                
                if(debug) cout<<"btag weight "<<btagWeight<<"  btag weight Up "<<btagWeightUp<<"   btag weight Down "<<btagWeightDown<<endl;
            }
            // if(ievt<1000)
            // {
            //     cout<<"btagweight: "<<btagWeight<<endl;
            // }

            ////csv discriminator reweighting
            // float TotalCSVbtagweight=1;
            if(bTagCSVReweight && !isData){
            //get btag weight info
                for(int jetbtag = 0; jetbtag<selectedJets.size(); jetbtag++){
                    float jetpt = selectedJets[jetbtag]->Pt();
                    float jeteta = selectedJets[jetbtag]->Eta();
                    float jetdisc = selectedJets[jetbtag]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                    BTagEntry::JetFlavor jflav;
                    int jetpartonflav = std::abs(selectedJets[jetbtag]->partonFlavour());
                    if(debug) cout<<"parton flavour: "<<jetpartonflav<<"  jet eta: "<<jeteta<<" jet pt: "<<jetpt<<"  jet disc: "<<jetdisc<<endl;
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
                    // cout<<bTagEff<<endl;
                    btagWeight*=bTagEff;
             
                    if(debug)cout<<"btag efficiency = "<<bTagEff<<endl;       
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

            if(debug) cout<<"lepton SF:  "<<fleptonSF<<endl;
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
                // else {
                //     cout<<endl;
                //     cout<<"no weights found"<<endl;
                //     cout<<endl;
                // }
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

            if (debug)  cout<<"Number of Muons = "<< nMu <<"    electrons =  "  <<nEl<<"     Jets = "<< selectedJets.size()   <<" loose BJets = "<<  nLtags   <<
                "  MuonChannel = "<<Muon<<" Electron Channel"<<Electron<<endl;

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
                cerr<<"Correct Channel not selected."<<endl;
                exit(1);
            }
            if(debug) cout<<"after baseline"<<endl;
            weightCount += scaleFactor;
            eventCount++;
            if(debug)
            {
                cout<<"Selection Passed."<<endl;
                cin.get();
            }
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
                    //cout<<"status: "<<mcParticles_flav[p]->status()<<"  id: "<<mcParticles_flav[p]->type()<<" mother: "<<mcParticles_flav[p]->motherType()<<endl;
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
            if (debug) cout<<"TMVA mass reco"<<endl;
            sort(selectedJets.begin(),selectedJets.end(),HighestCVSBtag());
            float csvJetcsv1 = 1, csvJetcsv2 = 1, csvJetcsv3 =1, csvJetcsv4 =1;

            if (selectedJets.size()>4){
                csvJetcsv1 = selectedJets[0]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                csvJetcsv2 = selectedJets[1]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                csvJetcsv3 = selectedJets[2]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                csvJetcsv4 = selectedJets[3]->btag_combinedInclusiveSecondaryVertexV2BJetTags();                
            }
            // cout<<"csv: "<<csvJetcsv1<<endl;

            if (HadTopOn){
                hadronicTopReco->SetCollections(selectedJets, selectedMuons, selectedElectrons, scaleFactor);
            }

            if(HadTopOn){
                if(!TrainMVA){ //if not training, but computing 
                    hadronicTopReco->Compute1st(d, selectedJets, datasets);
                    hadronicTopReco->Compute2nd(d, selectedJets, datasets);
                    diTopness = hadronicTopReco->ReturnDiTopness();
                    SumJetMassX = hadronicTopReco->ReturnSumJetMassX();
                    HTX = hadronicTopReco->ReturnHTX();// cout<<"HTX: "<<HTX<<endl;
                }
//                hadronicTopReco->FillDiagnosticPlots(fout, d, selectedJets, datasets);
            }

            //cout<<"SumJetMassX: "<<SumJetMassX<<endl;
            ///////////////////////////////////
            // Filling histograms / plotting //
            ///////////////////////////////////
            if (debug) cout<<"Plots"<<endl;

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

                
                MSPlot["leptonIso"]->Fill(relisomu, datasets[d], true, Luminosity*scaleFactor);
                MSPlot["MuonPt"]->Fill(selectedMuons[selmu]->Pt(), datasets[d], true, Luminosity*scaleFactor);
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
                MSPlot["ElectronRelIsolation"]->Fill(reliso, datasets[d], true, Luminosity*scaleFactor);
                if (Electron){
                    leptonIso = reliso;
                }
            }


            ////////////////////////////////////////////
            //       calculating HT rat and HTH       //
            ////////////////////////////////////////////
            if (debug) cout<<"HT rat and HTH"<<endl;
            HT = 0;
            float HT1M2L=0, H1M2L=0, HTbjets=0, HT2M=0, H2M=0, HT2L2J=0;
            sort(selectedJets.begin(),selectedJets.end(),HighestPt()); //order Jets wrt Pt for tuple output
            // tupCutfile->cd();
            for (Int_t seljet1 =0; seljet1 < selectedJets.size(); seljet1++ )
            {
                MSPlot["BdiscBJetCand_CSV"]->Fill(selectedJets[seljet1]->btag_combinedInclusiveSecondaryVertexV2BJetTags(),datasets[d], true, Luminosity*scaleFactor);
                MSPlot["JetEta"]->Fill(selectedJets[seljet1]->Eta() , datasets[d], true, Luminosity*scaleFactor);
                //Event-level variables
                jetpt = selectedJets[seljet1]->Pt();
                HT = HT + jetpt;
                H = H +  selectedJets[seljet1]->P();
                if (seljet1 > 4  )  HTHi +=  selectedJets[seljet1]->Pt();
                // jettup->Fill(scaleFactor,normfactor,Luminosity,selectedJets[seljet1]->neutralHadronEnergyFraction(),selectedJets[seljet1]->neutralEmEnergyFraction(),selectedJets[seljet1]->nConstituents(),selectedJets[seljet1]->chargedHadronEnergyFraction(),selectedJets[seljet1]->chargedMultiplicity(),selectedJets[seljet1]->chargedEmEnergyFraction());

            }

            float csvJetpt1 = 1, csvJetpt2 = 1, csvJetpt3 =1, csvJetpt4 =1;

            if (selectedJets.size()>4){
                csvJetpt1 = selectedJets[0]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                csvJetpt2 = selectedJets[1]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                csvJetpt3 = selectedJets[2]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
                csvJetpt4 = selectedJets[3]->btag_combinedInclusiveSecondaryVertexV2BJetTags();                
            }
            // cout<<"pt : "<<csvJetpt1<<endl;
            HTH = HT/H;
            HTRat = HTHi/HT;

            //////////////////////
            // Jets Based Plots //
            //////////////////////
            MSPlot["HTb_SelectedJets"]->Fill(HTb, datasets[d], true, Luminosity*scaleFactor);
            MSPlot["HTRat"]->Fill(HTRat, datasets[d], true, Luminosity*scaleFactor);
            MSPlot["NbOfSelectedBJets"]->Fill(selectedMBJets.size(), datasets[d], true, Luminosity*scaleFactor);
            float met = mets[0]->Et();
            MSPlot["MET"]->Fill(mets[0]->Et(), datasets[d], true, Luminosity*scaleFactor);

            if(nJets>5){
                MSPlot["5thJetPt"]->Fill(selectedJets[4]->Pt(), datasets[d], true, Luminosity*scaleFactor);
                MSPlot["6thJetPt"]->Fill(selectedJets[5]->Pt(), datasets[d], true, Luminosity*scaleFactor);
            }

            MSPlot["HT_SelectedJets"]->Fill(HT, datasets[d], true, Luminosity*scaleFactor);


            if(debug) cout<<"lepton vars"<<endl;
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
            //    Jet variables + jet craneen         //
            ////////////////////////////////////////////
//            tupjetfile->cd();
//            for (Int_t seljet1 =0; seljet1 < selectedJets.size(); seljet1++ )
//            {
//                float jeteta = selectedJets[seljet1]->Eta();
//                float jetphi = selectedJets[seljet1]->Phi();
//                float csvDisc = selectedJets[seljet1]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
//                float jetpT = selectedJets[seljet1]->Pt();
//                float jetLepDR = 0;
//                if (Muon){
//                    jetLepDR = selectedJets[seljet1]->DeltaR(*selectedMuons[0]);
//                }
//                else if (Electron){
//                    jetLepDR = selectedJets[seljet1]->DeltaR(*selectedElectrons[0]);
//                }
//                float jetvals[12] = {jetpT,csvDisc,jeteta,jetphi,jetLepDR,scaleFactor,normfactor,Luminosity, fleptonSF, btagWeight, lumiWeight, weight_0};//SFlepton:SFbtag:SFPU:GenWeight
//                tupjet->Fill(jetvals);
//            }


            ////////////////////////////////////////////
            //       Fill BDT & compute score         //
            ////////////////////////////////////////////
            if(debug) cout<<"event BDT computer"<<endl;
            float jet5Pt = 0;
            float jet6Pt = 0;
            if (EventBDTOn){
                if (nJets>5){
                    jet5Pt =  selectedJets[4]->Pt();
                    jet6Pt = selectedJets[5]->Pt();
                    //cout<<"5thjetpt "<<jet5Pt<<"  jet6pt: "<<jet6Pt<<endl;
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
            float vals[63] = {BDTScore,nJets,nOrigJets,nLtags,nMtags,nTtags,HT,selectedLeptonPt,leptoneta,bjetpt,HT2M,HTb,HTH,HTRat,HTX,SumJetMassX,diTopness,numOfbb,numOfcc,numOfll,ttbar_flav,scaleFactor,fleptonSF,btagWeight,btagWeightUp,btagWeightDown,lumiWeight,lumiWeight_up,lumiWeight_down,nvertices,normfactor,Luminosity,weight_0,weight_1,weight_2,weight_3,weight_4,weight_5,weight_6,weight_7,weight_8,met,angletop1top2,angletoplep,firstjetpt,secondjetpt,leptonIso,leptonphi,chargedHIso,neutralHIso,photonIso,PUIso,jet5Pt,jet6Pt,jet5and6Pt, csvJetcsv1, csvJetcsv2, csvJetcsv3, csvJetcsv4, csvJetpt1, csvJetpt2, csvJetpt3, csvJetpt4};
            tupfile->cd();
            tup->Fill(vals);
            // tupCutfile->cd();
            // if(Electron) eltup->Fill(scaleFactor,normfactor,Luminosity,selectedElectrons[0]->superClusterEta(),selectedElectrons[0]->sigmaIEtaIEta_full5x5(),fabs(selectedElectrons[0]->deltaEtaIn()),fabs(selectedElectrons[0]->deltaPhiIn()),selectedElectrons[0]->hadronicOverEm(),selectedElectrons[0]->relPfIso(3, 0.5),selectedElectrons[0]->ioEmIoP(),fabs(selectedElectrons[0]->d0()),fabs(selectedElectrons[0]->dz()),selectedElectrons[0]->missingHits(),selectedElectrons[0]->E(),selectedElectrons[0]->P());
            // if(Muon) mutup->Fill(scaleFactor,normfactor,Luminosity,leptonpt,leptoneta,selectedMuons[0]->relPfIso(4, 0.5));
        } //End Loop on Events
        cout<<"Write files"<<endl;
        tupfile->cd();
        tup->Write();
        tupfile->Close();

//        tupCutfile->cd();
//        cuttup->Write();
        // eltup->Write();
        // mutup->Write();
        // jettup->Write();
//        tupCutfile->Close();

//        tupjetfile->cd();
//        tupjet->Write();
//        tupjetfile->Close();

//        tupZfile->cd();
//        tupZ->Write();
//        tupZfile->Close();
        cout <<"n events passed  =  "<<passed <<endl;
        cout <<"n events with negative weights = "<<negWeights << endl;
        cout << "Event Count: " << eventCount << endl;
        cout << "Weight Count: " << weightCount << endl;
        //important: free memory
        treeLoader.UnLoadDataset();
//            MLoutput.close();

    } //End Loop on Datasets

    /////////////
    // Writing //
    /////////////

    cout << " - Writing outputs to the files ..." << endl;

    if(fillingbTagHistos && bTagReweight && dataSetName.find("Data")==string::npos){
        delete btwt;
        delete btwtDown;
        delete btwtUp;
    }    

    cout<<"TRIGGGG"<<endl;

    cout<<"preTrig: "<<preTrig<<"   postTrig: "<<postTrig<<endl;
    cout<<"********"<<endl;
    if(postTrig>0){
        cout<<"negative weight NormFactor: "<< ( (postTrig - (2*negWeights))/postTrig )<<endl;
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

    cout << "It took us " << ((double)clock() - start) / CLOCKS_PER_SEC << " to run the program" << endl;
    cout << "********************************************" << endl;
    cout << "           End of the program !!            " << endl;
    cout << "********************************************" << endl;
    
    return 0;
}
