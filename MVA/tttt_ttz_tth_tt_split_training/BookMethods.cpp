#include "BookMethods.hpp"

//Changing to these include paths for compatibility with ROOT v5.34
#include "TMVA/Factory.h"

#include <map>
#include <string>

void bookMethods(TMVA::Factory *factory, const std::map<std::string,bool>& Use) {
   // Boosted Decision Trees
   if (Use.find("BDTGSIG10")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGSIG10",
                           "!H:!V:DoBoostMonitor:NTrees=10:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGSIG20")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGSIG20",
                           "!H:!V:DoBoostMonitor:NTrees=20:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGSIG30")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGSIG30",
                           "!H:!V:DoBoostMonitor:NTrees=30:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGSIG40")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGSIG40",
                           "!H:!V:DoBoostMonitor:NTrees=40:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGSIG50")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGSIG50",
                           "!H:!V:DoBoostMonitor:NTrees=50:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGSIG100")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGSIG100",
                           "!H:!V:DoBoostMonitor:NTrees=100:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGSIG200")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGSIG200",
                           "!H:!V:DoBoostMonitor:NTrees=200:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTGSIG500")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTGSIG500",
                           "!H:!V:DoBoostMonitor:NTrees=500:BoostType=Grad:MaxDepth=5:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
// --------------------------------------------------------------
   if (Use.find("BDTG10")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG10",
                           "!H:!V:DoBoostMonitor:NTrees=10:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTG20")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG20",
                           "!H:!V:DoBoostMonitor:NTrees=20:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTG30")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG30",
                           "!H:!V:DoBoostMonitor:NTrees=30:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTG40")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG40",
                           "!H:!V:DoBoostMonitor:NTrees=40:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTG50")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG50",
                           "!H:!V:DoBoostMonitor:NTrees=50:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTG100")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG100",
                           "!H:!V:DoBoostMonitor:NTrees=100:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTG200")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG200",
                           "!H:!V:DoBoostMonitor:NTrees=200:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
    if (Use.find("BDTG500")->second) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG500",
                           "!H:!V:DoBoostMonitor:NTrees=500:BoostType=Grad:MaxDepth=3:UseBaggedBoost:nCuts=20:MinNodeSize=10:GradBaggingFraction=0.6:Shrinkage=0.30:NegWeightTreatment=Pray" );
// --------------------------------------------------------------
   if (Use.find("BDTASIG10")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG10",
                           "!H:!V:DoBoostMonitor:NTrees=10:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
   if (Use.find("BDTASIG20")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG20",
                           "!H:!V:DoBoostMonitor:NTrees=20:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
   if (Use.find("BDTASIG30")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG30",
                           "!H:!V:DoBoostMonitor:NTrees=30:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
   if (Use.find("BDTASIG40")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG40",
                           "!H:!V:DoBoostMonitor:NTrees=40:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
   if (Use.find("BDTASIG50")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG50",
                           "!H:!V:DoBoostMonitor:NTrees=50:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
    if (Use.find("BDTASIG100")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG100",
                           "!H:!V:DoBoostMonitor:NTrees=100:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
    if (Use.find("BDTASIG200")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG200",
                           "!H:!V:DoBoostMonitor:NTrees=200:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
    if (Use.find("BDTASIG500")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTASIG500",
                           "!H:!V:DoBoostMonitor:NTrees=500:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=SDivSqrtSPlusB:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
// --------------------------------------------------------------
   if (Use.find("BDTA10")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA10",
                           "!H:!V:DoBoostMonitor:NTrees=10:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
   if (Use.find("BDTA20")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA20",
                           "!H:!V:DoBoostMonitor:NTrees=20:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
   if (Use.find("BDTA30")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA30",
                           "!H:!V:DoBoostMonitor:NTrees=30:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
   if (Use.find("BDTA40")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA40",
                           "!H:!V:DoBoostMonitor:NTrees=40:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
   if (Use.find("BDTA50")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA50",
                           "!H:!V:DoBoostMonitor:NTrees=50:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
    if (Use.find("BDTA100")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA100",
                           "!H:!V:DoBoostMonitor:NTrees=100:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
    if (Use.find("BDTA200")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA200",
                           "!H:!V:DoBoostMonitor:NTrees=200:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
    if (Use.find("BDTA500")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTA500",
                           "!H:!V:DoBoostMonitor:NTrees=500:BoostType=AdaBoost:MaxDepth=3:UseBaggedBoost:SeparationType=GiniIndex:nCuts=20:MinNodeSize=10:PruneMethod=NoPruning" );
// --------------------------------------------------------------
  if (Use.find("BDT8TEV")->second)  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDT8TEV",
                           "!H:!V:DoBoostMonitor:NTrees=400:BoostType=AdaBoost:MaxDepth=3:SeparationType=GiniIndex:nCuts=20:MinNodeSize=5:PruneMethod=NoPruning" );

   if (Use.find("BDTB")->second) // Bagging
      factory->BookMethod( TMVA::Types::kBDT, "BDTB",
                           "!H:!V:NTrees=100:BoostType=Bagging:SeparationType=GiniIndex:nCuts=20:PruneMethod=NoPruning" );

   if (Use.find("BDTD")->second) // Decorrelation + Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTD",
                           "!H:!V:NTrees=100:MinNodeSize=5:MaxDepth=3:BoostType=AdaBoost:SeparationType=GiniIndex:nCuts=20:PruneMethod=NoPruning:VarTransform=Decorrelate" );
}