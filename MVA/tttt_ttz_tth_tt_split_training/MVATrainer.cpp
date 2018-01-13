/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/*
 * File:   MVATrainer.cpp
 * Author: iihe
 *
 * Created on May 9, 2016, 11:37 PM
 */

#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <utility>

#include "TChain.h"
#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TObjString.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TPluginManager.h"

#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>
#include <boost/program_options.hpp>
#include <boost/tokenizer.hpp>
#include <boost/filesystem.hpp>

//Changing to these include paths for compatibility with ROOT v5.34
#include "TMVA/Factory.h"
#include "TMVA/Tools.h"
#include "TMVA/Config.h"

#include "BookMethods.hpp"

namespace pt = boost::property_tree;
namespace fs = boost::filesystem;

using namespace boost::program_options;
using namespace std;

namespace bcolors{
    string HEADER =     "\033[95m";
    string OKBLUE =     "\033[94m";
    string OKGREEN =    "\033[92m";
    string WARNING =    "\033[93m";
    string FAIL =       "\033[91m";
    string ENDC =       "\033[0m";
    string BOLD =       "\033[1m";
    string UNDERLINE =  "\033[4m";
};

// JSON root
pt::ptree root;

//Global map for different TMVA Methods
extern "C" std::map<std::string,bool> Use; //definde in BookMethod.cpp

// For more info on the options used for preparing the Train and Testsamples, see section 3.1.4 of the TMVA manual
int main(int argc, char** argv) {
    std::vector<std::tuple<const std::string,const std::string,double>> vBckgFiles;
    std::vector<std::tuple<const std::string,const std::string,double>> vSigFiles;
    std::string outputdirName;
    std::string jsonconfigName;
    bool noAnnotate;

    // Parse command line arguments
    try {
      options_description desc{"Options",160};
      desc.add_options()
        ("help,h", "Help screen")
        ("dir", value<string>()->default_value("."),"Output directory")
        ("no-annotate", value<bool>()->default_value(false),"Disable annotation")
        ("json,j", value<string>(),"JSON configuration file")
        ("background_craneens", value<string>(), "List of coma separated background craneen files")
        ("signal_craneens", value<string>(), "List of coma separated signal craneen files")
        ("tree_name", value<string>(),"Input tree name");

      variables_map vm;
      store(parse_command_line(argc, argv, desc), vm);
      notify(vm);

      if (vm.count("help")) {
        std::cout << desc << '\n';
        exit(0);
      }
      if (vm.count("no-annotate")) {
        noAnnotate = vm["no-annotate"].as<bool>();
        if (!noAnnotate) std::cout << "Annotation switched on" << endl;
      }
      if (vm.count("background_craneens")) {
        const boost::char_separator<char> sep(",");
        boost::tokenizer<boost::char_separator<char>> tokens(vm["background_craneens"].as<string>(), sep);

        unsigned int i = 0;
        cout << "Background craneens:" << endl;
        for (const auto& t : tokens) {
            cout << i++ << ":\t" << t << endl;
            vBckgFiles.push_back(std::make_tuple(t,"Craneen__Mu",1.));
        }
      }
      if (vm.count("signal_craneens")) {
        const boost::char_separator<char> sep(",");
        boost::tokenizer<boost::char_separator<char>> tokens(vm["signal_craneens"].as<string>(), sep);

        unsigned int i = 0;
        cout << "Signal craneens:" << endl;
        for (const auto& t : tokens) {
            cout << i++ << ":\t" << t << endl;
            vSigFiles.push_back(std::make_tuple(t,"Craneen__Mu",1.));
        }
      }
      if (vm.count("dir")) {
        outputdirName = vm["dir"].as<string>();
      }
      if (vm.count("json")) {
        // Load the json file in this ptree
        jsonconfigName = vm["json"].as<string>();
        cout << "Config file: " << jsonconfigName << endl;
        pt::read_json(vm["json"].as<string>(), root);
        unsigned int i = 0;
        for (pt::ptree::value_type &element : root.get_child("background")) {
                auto fName = element.second.get<std::string>("filename");
                auto tName = element.second.get<std::string>("treename");
                auto w = element.second.get<double>("weight");
                auto p = std::make_tuple(fName,tName,w);
                cout << i <<":\t" << fName << "\t" << w << endl;
                vBckgFiles.push_back(p);
        }
        i = 0;
        for (pt::ptree::value_type &element : root.get_child("signal")) {
                auto fName = element.second.get<std::string>("filename");
                auto tName = element.second.get<std::string>("treename");
                auto w = element.second.get<double>("weight");
                auto p = std::make_tuple(fName,tName,w);
                cout << i <<":\t" << fName << "\t" << w << endl;
                vSigFiles.push_back(p);
        }
      }
    }
    catch (const error &ex)
    {
      std::cerr << ex.what() << '\n';
    }

    SwitchTrainMethods();

  std::string dirname = outputdirName+"/"+"MVA/weights";
  if (!fs::exists(dirname)) {
    std::cout << "Creating output folder: " << dirname << endl;
    fs::create_directories(dirname);
  }
	(TMVA::gConfig().GetIONames()).fWeightFileDir = dirname.c_str();

	//std::cout << "dirname changed?" << std::endl;

  std::string OutputMVAWeights = "TMVA";
  std::string OutputRootFile = outputdirName+"/"+"TMVA.root";
  TFile *outFile = new TFile(OutputRootFile.c_str(),"RECREATE");
//  std::string factoryOptions( "!V:!Silent:Transformations=I;D;P;G,D:!Color:!DrawProgressBar");
  std::string factoryOptions( "!V:!Silent:Transformations=I:Color:DrawProgressBar");
  auto factory = new TMVA::Factory( OutputMVAWeights.c_str(), outFile, factoryOptions );


  // global event weights per tree (see below for setting event-wise weights)
  Double_t signalWeight     = 1.0;
  Double_t backgroundWeight = 1.0;

  // ====== register trees ====================================================

  for(const auto& bgFile: vBckgFiles) {
    auto inFile = TFile::Open(std::get<0>(bgFile).c_str(), "READ");
    if (!inFile) {
        std::cerr << "Can't read input file: " << std::get<0>(bgFile) << endl;
        std::exit(1);
    }
    auto TreeB = static_cast<TTree*>(inFile->Get(std::get<1>(bgFile).c_str()));
    if (!TreeB) {
        std::cerr << "There is no tree : " << std::get<1>(bgFile) << endl;
        std::exit(1);
    }
    backgroundWeight = std::get<2>(bgFile);
    factory->AddBackgroundTree( TreeB, backgroundWeight );
  }

  for(const auto& sigFile: vSigFiles) {
    auto inFile = TFile::Open(std::get<0>(sigFile).c_str(), "READ");
    if (!inFile) {
        std::cerr << "Can't read input file: " << std::get<0>(sigFile) << endl;
        std::exit(1);
    }
    auto TreeS = static_cast<TTree*>(inFile->Get(std::get<1>(sigFile).c_str()));
    if (!TreeS) {
        std::cerr << "There is no tree : " << std::get<1>(sigFile) << endl;
        std::exit(1);
    }
    signalWeight = std::get<2>(sigFile);
    factory->AddSignalTree    ( TreeS,     signalWeight     );
  }

  // This would set individual event weights (the variables defined in the
  // expression need to exist in the original TTree)
  //    for signal    : factory->SetSignalWeightExpression("weight1*weight2");
  //    for background: factory->SetBackgroundWeightExpression("weight1*weight2");

factory->SetSignalWeightExpression("GenWeight");
factory->SetBackgroundWeightExpression("GenWeight");

factory->AddVariable( "nMtags", "nMtags", "units", 'I' );
factory->AddVariable( "nJets", "nJets", "units", 'I' );
factory->AddVariable( "multitopness", "Multitopness", "units", 'F' );
factory->AddVariable( "HTb", "HT of selected b jets", "units", 'F' );
factory->AddVariable( "HTH", "HT/H", "units", 'F' );
factory->AddVariable( "jetvec[9][0]", "lepton p_T", "units", 'F' );
factory->AddVariable( "LeptonPt", "lepton p_T", "units", 'F' );
factory->AddVariable( "SumJetMassX", "Inv. mass of reduced hadronic system", "units", 'F' );
factory->AddVariable( "HTX", "HTX", "units", 'F' );
factory->AddVariable( "csvJetcsv1", "1st highest csv", "units", 'F' );
factory->AddVariable( "csvJetcsv2", "2nd highest csv", "units", 'F' );
factory->AddVariable( "csvJetcsv3", "third highest csv", "units", 'F' );
factory->AddVariable( "csvJetcsv4", "fourth highest csv", "units", 'F' );
factory->AddVariable( "csvJetpt1", "highest p_T jet csv", "units", 'F' );
factory->AddVariable( "csvJetpt2", "2nd highest p_T jet csv", "units", 'F' );
factory->AddVariable( "csvJetpt3", "third highest p_T jet csv", "units", 'F' );
factory->AddVariable( "csvJetpt4", "fourth highest p_T jet csv", "units", 'F' );
factory->AddVariable( "1stjetpt", "leading jet p_T", "units", 'F' );
factory->AddVariable( "2ndjetpt", "second leading jet p_T", "units", 'F' );
factory->AddVariable( "5thjetpt", "fifth leading jet p_T", "units", 'F' );
factory->AddVariable( "6thjetpt", "sixth leading jet p_T", "units", 'F' );
// factory->AddVariable( "angletop1top2", "Angle between two hadronic tops", "units", 'F' ); // this variable is constant?
// factory->AddVariable( "angletoplep", "Angle between hadronic top and lepton", "units", 'F' ); //this variable is constant?

// You can add so-called "Spectator variables", which are not used in the MVA training,
// but will appear in the final "TestTree" produced by TMVA. This TestTree will contain the
// input variables, the response values of all trained MVAs, and the spectator variables
factory->AddSpectator( "nJets := nJets",  "jet multiplicity", "units", 'F' );
factory->AddSpectator( "nMtags := nMtags",  "b tags multiplicity", "units", 'F' );
factory->AddSpectator( "GenWeight := GenWeight",  "ME weight", "units", 'F' );

  int nTrainS=50000, nTestS=50000, nTrainB=150000, nTestB=150000;

  std::string CutsS{"nJets>=10"};
  std::string CutsB{"nJets>=10"};            //Example cut => "abs(var1)<0.5 && abs(var2-0.5)<1";

  std::string SplitMode;        //SplitMode: Random, Alternate and Block

  //Setting al the int's to 0 will split the sample in two parts for training and testing

  std::stringstream nTRS, nTS, nTRB, nTB;
  nTRS << nTrainS; nTS << nTestS;
  nTRB << nTrainB; nTB << nTestB;

  std::string trainLine = "";//"nTrain_Signal="+nTRS.str()+":nTest_Signal="+nTS.str();
  //trainLine += ":nTrain_Background="+nTRB.str()+":nTest_Background="+nTB.str();

  if (SplitMode == "") {
     trainLine += ":SplitMode=Random:NormMode=NumEvents:!V";
  } else {
    trainLine += ":SplitMode="+SplitMode+":NormMode=NumEvents:!V";
  }

  // tell the factory to use all remaining events in the trees after training for testing:
  factory->PrepareTrainingAndTestTree( TCut(CutsS.c_str()), TCut(CutsB.c_str()),trainLine.c_str());

   // ---- Book MVA methods
   //
   // please lookup the various method configuration options in the corresponding cxx files, eg:
   // src/MethoCuts.cxx, etc, or here: http://tmva.sourceforge.net/optionRef.html
   // it is possible to preset ranges in the option string in which the cut optimisation should be done:
   // "...:CutRangeMin[2]=-1:CutRangeMax[2]=1"...", where [2] is the third input variable


  bookMethods(factory, Use);

   // ---- Now you can tell the factory to train, test, and evaluate the MVAs

   // Train MVAs using the set of training events
   cout << "train it" << endl;
   factory->TrainAllMethodsForClassification();

   // ---- Evaluate all MVAs using the set of test events
   cout << "test it" << endl;
   factory->TestAllMethods();

   // ----- Evaluate and compare performance of all configured MVAs
   cout << "evaluate it" << endl;
   factory->EvaluateAllMethods();

   // --------------------------------------------------------------

   // Save the output
   outFile->Close();

   std::cout << "==> Wrote root file: " << outFile->GetName() << std::endl;
   // --------------------------------------------------------------

   delete factory;

   //Write annotation
   if(!noAnnotate && !jsonconfigName.empty()) {
     //copy config file if any
     if(fs::exists(jsonconfigName)) {
        try {
          fs::copy(jsonconfigName,outputdirName+"/"+jsonconfigName);
        } catch (const std::exception &ex) {
          std::cerr << ex.what() << '\n' << endl;
        }
        std::string msg = bcolors::OKBLUE +
                          root.get<std::string>("annotation") +
                          bcolors::ENDC;
        std::cout << msg << std::endl;
     }
   }

  cout << "done!" << endl;

    return 0;
}
