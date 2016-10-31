/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   MultiTopEvent.cpp
 * Author: iihe
 * 
 * Created on June 30, 2016, 5:01 PM
 */

#include "TMatrixD.h"

#include "MultiTopEvent.h"

#include "TLorentzVector.h"
#include "TVector3.h"

#include "TopTreeAnalysisBase/KinFitter/interface/TKinFitter.h"
#include "TopTreeAnalysisBase/KinFitter/interface/TFitConstraintM.h"

MultiTopEvent::MultiTopEvent(const std::vector<TopTree::TRootPFJet*>& jets) : jets_(jets), fitter_(new TKinFitter("fitter", "fitter")) {
    
    const unsigned nMaxIter(30);
    const double MaxDeltaS(1e-2);
    const double MaxF(1e-1);
    //Set convergence criteria
    this->fitter_->setMaxNbIter(nMaxIter);
    this->fitter_->setMaxDeltaS(MaxDeltaS);
    this->fitter_->setMaxF(MaxF);
    this->fitter_->setVerbosity(0);
}

MultiTopEvent::~MultiTopEvent() {
    delete fitter_;
    for (auto &itr: this->topCandidates_) delete itr;
    this->topCandidates_.clear();
}

std::vector<TopTree::TRootParticle*> MultiTopEvent::FindHadronicTops() {

    const unsigned nTopDecayProducts = 3;
    const unsigned nJets = this->jets_.size();
    //
    // Sample all jet permutations of nTopDecayProducts out of nJets
    //
    std::vector<int> selector( nJets ); // contains yes/no decision for jet indexes of current permutation
    std::fill(selector.begin(), selector.begin() + nTopDecayProducts, 1);   // starting jet-index permutation mask 1 1 1 0 0 ...
    do {
        std::vector<TopTree::TRootPFJet*> vecJetsPermutation;
        for (int i = 0; i < nJets; i++) {
            if (selector[i]) vecJetsPermutation.push_back(this->jets_[i]);
        }

        TopTree::TRootParticle* topCand = AnalysePermutation(vecJetsPermutation);
        this->topCandidates_.push_back(topCand);
        
    } while (prev_permutation(selector.begin(), selector.end()));

    return this->topCandidates_;
}

TopTree::TRootParticle* MultiTopEvent::AnalysePermutation(std::vector<TopTree::TRootPFJet*>& permutation) {
    
    // sort according to csv disc value in descending order
    auto csvCompDesc = [](TopTree::TRootPFJet* jet1, TopTree::TRootPFJet* jet2) {
        return jet1->btag_combinedInclusiveSecondaryVertexV2BJetTags() < jet2->btag_combinedInclusiveSecondaryVertexV2BJetTags();
    };
    std::sort(permutation.begin(),permutation.end(),csvCompDesc);   
    
    // add measured jets
    std::vector<TFitParticleEtEtaPhi*> vecFitParticles;
    for ( auto& iJet: permutation ) {
        int jetNum = &iJet - &permutation[0];
        
        TMatrixD m(3,3);
        m.UnitMatrix();
        
        std::string name = "Jet"+std::to_string(jetNum);
        vecFitParticles.push_back(new TFitParticleEtEtaPhi( "Jet"+jetNum, "Jet"+jetNum, iJet, &m ));
        this->fitter_->addMeasParticle(vecFitParticles.back());
    }
    //add W mass constraint
    //light-flavour jets to be those with lowest CSV value
    TFitConstraintM* MWCon = new TFitConstraintM( "WMassConstraint", "WMass-Constraint", 0, 0 , 80.41);
    MWCon->addParticles1( vecFitParticles[0], vecFitParticles[1] );
    this->fitter_->addConstraint( MWCon );
    
    //Perform the fit
    this->fitter_->fit();
    this->Print();
    this->fitter_->reset();
    // @TODO: Return correct values of reconstructed trijet combinations
    
    const TLorentzVector momentum(0.,0.,0.,0.);
    const TVector3 vertex(0.,0.,0.);
    Int_t type = 6;
    Float_t charge = 0.6666;
    
    return new TopTree::TRootParticle(momentum, vertex, type, charge);
}

void MultiTopEvent::Print()
{
  std::cout << "=============================================" << std ::endl;
  std::cout << "-> Number of measured Particles  : " << this->fitter_->nbMeasParticles() << std::endl;
  std::cout << "-> Number of unmeasured particles: " << this->fitter_->nbUnmeasParticles() << std::endl;
  std::cout << "-> Number of constraints         : " << this->fitter_->nbConstraints() << std::endl;
  std::cout << "-> Number of degrees of freedom  : " << this->fitter_->getNDF() << std::endl;
  std::cout << "-> Number of parameters A        : " << this->fitter_->getNParA() << std::endl;
  std::cout << "-> Number of parameters B        : " << this->fitter_->getNParB() << std::endl;
  std::cout << "-> Maximum number of iterations  : " << this->fitter_->getMaxNumberIter() << std::endl;
  std::cout << "-> Maximum deltaS                : " << this->fitter_->getMaxDeltaS() << std::endl;
  std::cout << "-> Maximum F                     : " << this->fitter_->getMaxF() << std::endl;
  std::cout << "+++++++++++++++++++++++++++++++++++++++++++++" << std ::endl;
  std::cout << "-> Status                        : " << this->fitter_->getStatus() << std::endl;
  std::cout << "-> Number of iterations          : " << this->fitter_->getNbIter() << std::endl;
  std::cout << "-> S                             : " << this->fitter_->getS() << std::endl;
  std::cout << "-> F                             : " << this->fitter_->getF() << std::endl;
  std::cout << "=============================================" << std ::endl;
}