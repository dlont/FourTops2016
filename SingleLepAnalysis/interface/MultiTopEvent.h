/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   MultiTopEvent.h
 * Author: iihe
 *
 * Created on June 30, 2016, 5:01 PM
 */

#ifndef MULTITOPEVENT_H
#define MULTITOPEVENT_H

#include <vector>

#include "TopTreeProducer/interface/TRootPFJet.h"
#include "TopTreeProducer/interface/TRootParticle.h"

#include "TopTreeAnalysisBase/KinFitter/interface/TKinFitter.h"
#include "TopTreeAnalysisBase/KinFitter/interface/TFitParticleEtEtaPhi.h"

class MultiTopEvent {
public:
    MultiTopEvent(const std::vector<TopTree::TRootPFJet*>&);
    
    virtual ~MultiTopEvent();
    
    std::vector<TopTree::TRootParticle*> FindHadronicTops();
    
    TopTree::TRootParticle* AnalysePermutation(std::vector<TopTree::TRootPFJet*>&);
    
    void Print();
private:

    const std::vector<TopTree::TRootPFJet*>& jets_;
    std::vector<TopTree::TRootParticle*> topCandidates_;
    
    TKinFitter* fitter_;
};

#endif /* MULTITOPEVENT_H */

