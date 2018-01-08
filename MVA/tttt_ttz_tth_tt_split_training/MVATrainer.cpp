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

#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <vector>

#include "TChain.h"
#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TObjString.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TPluginManager.h"

#include <boost/program_options.hpp>
#include <boost/tokenizer.hpp>

//Changing to these include paths for compatibility with ROOT v5.34
#include "TMVA/Factory.h"
#include "TMVA/Tools.h"
#include "TMVA/Config.h"

#include "BookMethods.hpp"

using namespace boost::program_options;
using namespace std;

//---------------------------------------------------------------
  // default MVA methods to be trained + tested

  std::map<std::string,bool> Use;
  void SwitchTrainMethods()
  {
      Use["BDTA10"]            = true;
      Use["BDTA20"]            = true;
      Use["BDTA30"]            = true;
      Use["BDTA40"]            = true;
      Use["BDTA50"]            = true;
      Use["BDTA100"]           = true;
      Use["BDTA200"]           = true;
      Use["BDTA500"]           = true;
      // ------------------------------
      Use["BDTASIG10"]            = true;
      Use["BDTASIG20"]            = true;
      Use["BDTASIG30"]            = true;
      Use["BDTASIG40"]            = true;
      Use["BDTASIG50"]            = true;
      Use["BDTASIG100"]           = true;
      Use["BDTASIG200"]           = true;
      Use["BDTASIG500"]           = true;
      // ------------------------------
      Use["BDTG10"]            = true;
      Use["BDTG20"]            = true;
      Use["BDTG30"]            = true;
      Use["BDTG40"]            = true;
      Use["BDTG50"]            = true;
      Use["BDTG100"]           = true;
      Use["BDTG200"]           = true;
      Use["BDTG500"]           = true;
      // ------------------------------
      Use["BDTGSIG10"]            = true;
      Use["BDTGSIG20"]            = true;
      Use["BDTGSIG30"]            = true;
      Use["BDTGSIG40"]            = true;
      Use["BDTGSIG50"]            = true;
      Use["BDTGSIG100"]           = true;
      Use["BDTGSIG200"]           = true;
      Use["BDTGSIG500"]           = true;
      // ------------------------------
      return;
  }
/*
 *
 */
// For more info on the options used for preparing the Train and Testsamples, see section 3.1.4 of the TMVA manual
int main(int argc, char** argv) {
    std::vector<std::string> vBckgFileNames;
    std::vector<std::string> vSigFileNames;
    std::string treeName;
    try {
      options_description desc{"Options",160};
      desc.add_options()
        ("help,h", "Help screen")
        ("background_craneens", value<string>()->default_value("Craneen_TTJets_powheg_Run2_TopTree_Study.root"), "List of coma separated background craneen files")
        ("signal_craneens", value<string>()->default_value("Craneen_ttttNLO_Run2_TopTree_Study.root"), "List of coma separated signal craneen files")
        ("tree_name", value<string>()->default_value("Craneen__Mu"),"Input tree name");

      variables_map vm;
      store(parse_command_line(argc, argv, desc), vm);
      notify(vm);

      if (vm.count("help")) {
        std::cout << desc << '\n';
        exit(0);
      }
      if (vm.count("background_craneens")) {
        const boost::char_separator<char> sep(",");
        boost::tokenizer<boost::char_separator<char>> tokens(vm["background_craneens"].as<string>(), sep);

        unsigned int i = 0;
        cout << "Background craneens:" << endl;
        for (const auto& t : tokens) {
            cout << i++ << ":\t" << t << endl;
            vBckgFileNames.push_back(t);
        }
      }
      if (vm.count("signal_craneens")) {
        const boost::char_separator<char> sep(",");
        boost::tokenizer<boost::char_separator<char>> tokens(vm["signal_craneens"].as<string>(), sep);

        unsigned int i = 0;
        cout << "Signal craneens:" << endl;
        for (const auto& t : tokens) {
            cout << i++ << ":\t" << t << endl;
            vSigFileNames.push_back(t);
        }
      }
      if (vm.count("tree_name")) {
        treeName = vm["tree_name"].as<string>();
      }
    }
    catch (const error &ex)
    {
      std::cerr << ex.what() << '\n';
    }

    SwitchTrainMethods();

  std::string dirname = "MVA/weights";
	(TMVA::gConfig().GetIONames()).fWeightFileDir = dirname.c_str();

	//std::cout << "dirname changed?" << std::endl;

  std::string OutputMVAWeights = "TMVA";
  std::string OutputRootFile = "TMVA.root";
  TFile *outFile = new TFile(OutputRootFile.c_str(),"RECREATE");
//  std::string factoryOptions( "!V:!Silent:Transformations=I;D;P;G,D:!Color:!DrawProgressBar");
  std::string factoryOptions( "!V:!Silent:Transformations=I:Color:DrawProgressBar");
  auto factory = new TMVA::Factory( OutputMVAWeights.c_str(), outFile, factoryOptions );


  // global event weights per tree (see below for setting event-wise weights)
  Double_t signalWeight     = 1.0;
  Double_t backgroundWeight = 1.0;

  // ====== register trees ====================================================

  for(const auto& bgckFileName: vBckgFileNames) {
    auto inFile = TFile::Open(bgckFileName.c_str(), "READ");
    if (!inFile) {
        std::cerr << "Can't read input file: " << bgckFileName.c_str() << endl;
        std::exit(1);
    }
    auto TreeB = static_cast<TTree*>(inFile->Get(treeName.c_str()));
    if (!TreeB) {
        std::cerr << "There is no tree : " << bgckFileName.c_str() << endl;
        std::exit(1);
    }
    factory->AddBackgroundTree( TreeB, backgroundWeight );
  }

  for(const auto& sigFileName: vSigFileNames) {
    auto inFile = TFile::Open(sigFileName.c_str(), "READ");
    if (!inFile) {
        std::cerr << "Can't read input file: " << sigFileName.c_str() << endl;
        std::exit(1);
    }
    auto TreeS = static_cast<TTree*>(inFile->Get(treeName.c_str()));
    if (!TreeS) {
        std::cerr << "There is no tree : " << sigFileName.c_str() << endl;
        std::exit(1);
    }
    factory->AddSignalTree    ( TreeS,     signalWeight     );
  }

  // This would set individual event weights (the variables defined in the
  // expression need to exist in the original TTree)
  //    for signal    : factory->SetSignalWeightExpression("weight1*weight2");
  //    for background: factory->SetBackgroundWeightExpression("weight1*weight2");

factory->AddVariable( "multitopness", "Multitopness", "units", 'F' );
factory->AddVariable( "HTb", "HT of selected b jets", "units", 'F' );
factory->AddVariable( "HTH", "HT/H", "units", 'F' );
factory->AddVariable( "LeptonPt", "lepton p_T", "units", 'F' );
factory->AddVariable( "SumJetMassX", "Inv. mass of reduced hadronic system", "units", 'F' );
factory->AddVariable( "HTX", "HTX", "units", 'F' );
factory->AddVariable( "csvJetcsv3", "third highest csv", "units", 'F' );
factory->AddVariable( "csvJetcsv4", "fourth highest csv", "units", 'F' );
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

  cout << "done!" << endl;

    return 0;
}
