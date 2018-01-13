#include "BookMethods.hpp"

//Changing to these include paths for compatibility with ROOT v5.34
#include "TMVA/Factory.h"

#include <map>
#include <string>

// default MVA methods to be trained + tested
std::map<std::string,bool> Use;

void SwitchTrainMethods()
{
    Use["BDTA10"]            = true;
    Use["BDTA20"]            = true;
    Use["BDTA30"]            = false;
    Use["BDTA40"]            = false;
    Use["BDTA50"]            = false;
    Use["BDTA100"]           = true;
    Use["BDTA200"]           = false;
    Use["BDTA500"]           = false;
    // ------------------------------
    Use["BDTASIG10"]            = true;
    Use["BDTASIG20"]            = true;
    Use["BDTASIG30"]            = false;
    Use["BDTASIG40"]            = false;
    Use["BDTASIG50"]            = false;
    Use["BDTASIG100"]           = true;
    Use["BDTASIG200"]           = false;
    Use["BDTASIG500"]           = false;
    // ------------------------------
    Use["BDTG10"]            = true;
    Use["BDTG20"]            = true;
    Use["BDTG30"]            = false;
    Use["BDTG40"]            = false;
    Use["BDTG50"]            = false;
    Use["BDTG100"]           = true;
    Use["BDTG200"]           = false;
    Use["BDTG500"]           = false;
    // ------------------------------
    Use["BDTGMD3PRAY10"]            = true;
    Use["BDTGMD3PRAY20"]            = true;
    Use["BDTGMD3PRAY30"]            = false;
    Use["BDTGMD3PRAY40"]            = false;
    Use["BDTGMD3PRAY50"]            = false;
    Use["BDTGMD3PRAY100"]           = true;
    Use["BDTGMD3PRAY200"]           = false;
    Use["BDTGMD3PRAY500"]           = false;
    // ------------------------------
    Use["BDTGPRAY10"]            = true;
    Use["BDTGPRAY20"]            = true;
    Use["BDTGPRAY30"]            = false;
    Use["BDTGPRAY40"]            = false;
    Use["BDTGPRAY50"]            = false;
    Use["BDTGPRAY100"]           = true;
    Use["BDTGPRAY200"]           = false;
    Use["BDTGPRAY500"]           = false;
    // ------------------------------
    return;
}

void bookMethods(TMVA::Factory *factory, const std::map<std::string,bool>& Use) {
   // Boosted Decision Trees
   if (Use.find("BDTGMD3PRAY10")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGMD3PRAY10",
                           "!H:!V:DoBoostMonitor:NTrees=10:BoostType=Grad:MaxDepth=3:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGMD3PRAY20")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGMD3PRAY20",
                           "!H:!V:DoBoostMonitor:NTrees=20:BoostType=Grad:MaxDepth=3:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGMD3PRAY30")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGMD3PRAY30",
                           "!H:!V:DoBoostMonitor:NTrees=30:BoostType=Grad:MaxDepth=3:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGMD3PRAY40")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGMD3PRAY40",
                           "!H:!V:DoBoostMonitor:NTrees=40:BoostType=Grad:MaxDepth=3:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGMD3PRAY50")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGMD3PRAY50",
                           "!H:!V:DoBoostMonitor:NTrees=50:BoostType=Grad:MaxDepth=3:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGMD3PRAY100")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGMD3PRAY100",
                           "!H:!V:DoBoostMonitor:NTrees=100:BoostType=Grad:MaxDepth=3:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGMD3PRAY200")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGMD3PRAY200",
                           "!H:!V:DoBoostMonitor:NTrees=200:BoostType=Grad:MaxDepth=3:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGMD3PRAY500")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGMD3PRAY500",
                           "!H:!V:DoBoostMonitor:NTrees=500:BoostType=Grad:MaxDepth=3:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
// --------------------------------------------------------------
   if (Use.find("BDTGPRAY10")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGPRAY10",
                           "!H:!V:DoBoostMonitor:NTrees=10:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGPRAY20")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGPRAY20",
                           "!H:!V:DoBoostMonitor:NTrees=20:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGPRAY30")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGPRAY30",
                           "!H:!V:DoBoostMonitor:NTrees=30:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGPRAY40")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGPRAY40",
                           "!H:!V:DoBoostMonitor:NTrees=40:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGPRAY50")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGPRAY50",
                           "!H:!V:DoBoostMonitor:NTrees=50:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGPRAY100")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGPRAY100",
                           "!H:!V:DoBoostMonitor:NTrees=100:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGPRAY200")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGPRAY200",
                           "!H:!V:DoBoostMonitor:NTrees=200:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGPRAY500")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGPRAY500",
                           "!H:!V:DoBoostMonitor:NTrees=500:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
// --------------------------------------------------------------
   if (Use.find("BDTG10")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG10",
                           "!H:!V:DoBoostMonitor:NTrees=10:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=IgnoreNegWeightsInTraining" );
    if (Use.find("BDTG20")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG20",
                           "!H:!V:DoBoostMonitor:NTrees=20:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=IgnoreNegWeightsInTraining" );
    if (Use.find("BDTG30")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG30",
                           "!H:!V:DoBoostMonitor:NTrees=30:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=IgnoreNegWeightsInTraining" );
    if (Use.find("BDTG40")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG40",
                           "!H:!V:DoBoostMonitor:NTrees=40:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=IgnoreNegWeightsInTraining" );
    if (Use.find("BDTG50")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG50",
                           "!H:!V:DoBoostMonitor:NTrees=50:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=IgnoreNegWeightsInTraining" );
    if (Use.find("BDTG100")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG100",
                           "!H:!V:DoBoostMonitor:NTrees=100:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=IgnoreNegWeightsInTraining" );
    if (Use.find("BDTG200")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG200",
                           "!H:!V:DoBoostMonitor:NTrees=200:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=IgnoreNegWeightsInTraining" );
    if (Use.find("BDTG500")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG500",
                           "!H:!V:DoBoostMonitor:NTrees=500:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=5:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=IgnoreNegWeightsInTraining" );
// --------------------------------------------------------------
   if (Use.find("BDTASIG10")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG10",
                           "!H:!V:DoBoostMonitor:NTrees=10:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
   if (Use.find("BDTASIG20")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG20",
                           "!H:!V:DoBoostMonitor:NTrees=20:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
   if (Use.find("BDTASIG30")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG30",
                           "!H:!V:DoBoostMonitor:NTrees=30:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
   if (Use.find("BDTASIG40")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG40",
                           "!H:!V:DoBoostMonitor:NTrees=40:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
   if (Use.find("BDTASIG50")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG50",
                           "!H:!V:DoBoostMonitor:NTrees=50:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
    if (Use.find("BDTASIG100")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG100",
                           "!H:!V:DoBoostMonitor:NTrees=100:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
    if (Use.find("BDTASIG200")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG200",
                           "!H:!V:DoBoostMonitor:NTrees=200:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
    if (Use.find("BDTASIG500")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG500",
                           "!H:!V:DoBoostMonitor:NTrees=500:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
// --------------------------------------------------------------
   if (Use.find("BDTA10")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA10",
                           "!H:!V:DoBoostMonitor:NTrees=10:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
   if (Use.find("BDTA20")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA20",
                           "!H:!V:DoBoostMonitor:NTrees=20:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
   if (Use.find("BDTA30")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA30",
                           "!H:!V:DoBoostMonitor:NTrees=30:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
   if (Use.find("BDTA40")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA40",
                           "!H:!V:DoBoostMonitor:NTrees=40:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
   if (Use.find("BDTA50")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA50",
                           "!H:!V:DoBoostMonitor:NTrees=50:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
    if (Use.find("BDTA100")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA100",
                           "!H:!V:DoBoostMonitor:NTrees=100:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
    if (Use.find("BDTA200")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA200",
                           "!H:!V:DoBoostMonitor:NTrees=200:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
    if (Use.find("BDTA500")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA500",
                           "!H:!V:DoBoostMonitor:NTrees=500:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );
// --------------------------------------------------------------
  if (Use.find("BDT8TEV")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDT8TEV",
                           "!H:!V:DoBoostMonitor:NTrees=400:BoostType=AdaBoost:MaxDepth=3:SeparationType=GiniIndex:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );

   if (Use.find("BDTB")->second) // Bagging
      factory->BookMethod( TMVA::Types::kBDT, "BDTB",
                           "!H:!V:NTrees=100:BoostType=Bagging:SeparationType=GiniIndex:nCuts=20:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining" );

   if (Use.find("BDTD")->second) // Decorrelation + Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTD",
                           "!H:!V:NTrees=100:MinNodeSize=5:MaxDepth=3:BoostType=AdaBoost:SeparationType=GiniIndex:nCuts=20:PruneMethod=NoPruning:NegWeightTreatment=IgnoreNegWeightsInTraining:VarTransform=Decorrelate" );
}
