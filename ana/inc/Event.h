/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File; double    Event.h
 * Author; double  iihe
 *
 * Created on December 11, 2016, 4; double 53 PM
 */

#ifndef EVENT_H
#define EVENT_H

#include "TTree.h"
#include <cstdlib>
#include <algorithm>

struct Event {
    void clear();
    void makeBranches(TTree* tree);
    void fill(double [], double [][5], int , double [], double []);
    
    double BDT;
    int nJets; 
    int NOrigJets; 
    int nLtags; 
    int nMtags; 
    int nTtags; 
    double HT; 
    double LeptonPt; 
    double LeptonEta; 
    double LeadingBJetPt; 
    double HT2M;
    double HTb; 
    double HTH; 
    double HTRat; 
    double HTX; 
    double SumJetMassX; 
    double multitopness; 
    double nbb; 
    double ncc; 
    double nll; 
    int ttbar_flav; 
    double ScaleFactor; 
    double SFlepton; 
    double SFbtag; 
    double SFbtagUp; 
    double SFbtagDown; 
    double SFPU; 
    double SFPU_up; 
    double SFPU_down; 
    int PU; 
    double NormFactor; 
    double GenWeight; 
    double weight1; 
    double weight2; 
    double weight3; 
    double weight4; 
    double weight5; 
    double weight6; 
    double weight7; 
    double weight8; 
    double met; 
    double angletop1top2; 
    double angletoplep; 
    double firstjetpt; 
    double secondjetpt; 
    double leptonIso; 
    double leptonphi; 
    double chargedHIso; 
    double neutralHIso; 
    double photonIso; 
    double PUIso;
    double jet5Pt; 
    double jet6Pt; 
    double jet5and6pt; 
    double csvJetcsv1;
    double csvJetcsv2; 
    double csvJetcsv3; 
    double csvJetcsv4; 
    double csvJetpt1; 
    double csvJetpt2; 
    double csvJetpt3; 
    double csvJetpt4;
    double jetvec[30][5];   //jet properties (pT,eta,phi,csv)
    double weight[9];       //ME scale variation weights
    double csvrsw[20];      //CSVRS systematic weights
}; //end Event


//______________________________________________________________________________
/*
 * Flush the content of the structure to be called before filling inside an event
 */
void Event::clear() {
      BDT = 0.;
      nJets = 0.; 
      NOrigJets = 0.; 
      nLtags = 0.; 
      nMtags = 0.; 
      nTtags = 0.; 
      HT = 0.; 
      LeptonPt = 0.; 
      LeptonEta = 0.; 
      LeadingBJetPt = 0.; 
      HT2M = 0.;
      HTb = 0.; 
      HTH = 0.; 
      HTRat = 0.; 
      HTX = 0.; 
      SumJetMassX = 0.; 
      multitopness = 0.; 
      nbb = 0.; 
      ncc = 0.; 
      nll = 0.; 
      ttbar_flav = 0.; 
      ScaleFactor = 0.; 
      SFlepton = 0.; 
      SFbtag = 0.; 
      SFbtagUp = 0.; 
      SFbtagDown = 0.; 
      SFPU = 0.; 
      SFPU_up = 0.; 
      SFPU_down = 0.; 
      PU = 0.; 
      NormFactor = 0.; 
      GenWeight = 0.; 
      weight1 = 0.; 
      weight2 = 0.; 
      weight3 = 0.; 
      weight4 = 0.; 
      weight5 = 0.; 
      weight6 = 0.; 
      weight7 = 0.; 
      weight8 = 0.; 
      met = 0.; 
      angletop1top2 = 0.; 
      angletoplep = 0.; 
      firstjetpt = 0.; 
      secondjetpt = 0.; 
      leptonIso = 0.; 
      leptonphi = 0.; 
      chargedHIso = 0.; 
      neutralHIso = 0.; 
      photonIso = 0.; 
      PUIso = 0.;
      jet5Pt = 0.; 
      jet6Pt = 0.; 
      jet5and6pt = 0.; 
      csvJetcsv1 = 0.;
      csvJetcsv2 = 0.; 
      csvJetcsv3 = 0.; 
      csvJetcsv4 = 0.; 
      csvJetpt1 = 0.; 
      csvJetpt2 = 0.; 
      csvJetpt3 = 0.; 
      csvJetpt4 = 0.;
      std::fill( &jetvec[0][0], &jetvec[0][0]+sizeof(jetvec), 0.);
      std::fill( weight, weight + sizeof(weight), 0.);
      std::fill( csvrsw, csvrsw + sizeof(csvrsw), 0.);
} //End Event::clear()

void Event::makeBranches(TTree* tree) {
    if (tree == nullptr) {
        std::cerr << "tree pointer is NULL. Aborting!.." << std::endl;
        std::exit(EXIT_FAILURE);
    }
    
      tree -> Branch("BDT", &BDT    ,"BDT/D");
      tree -> Branch("nJets", &nJets    ,"nJets/I"); 
      tree -> Branch("NOrigJets", &NOrigJets    ,"NOrigJets/I"); 
      tree -> Branch("nLtags", &nLtags    ,"nLtags/I"); 
      tree -> Branch("nMtags", &nMtags    ,"nMtags/I"); 
      tree -> Branch("nTtags", &nTtags    ,"nTtags/I"); 
      tree -> Branch("HT", &HT    ,"HT/D"); 
      tree -> Branch("LeptonPt", &LeptonPt    ,"LeptonPt/D"); 
      tree -> Branch("LeptonEta", &LeptonEta    ,"LeptonEta/D"); 
      tree -> Branch("LeadingBJetPt", &LeadingBJetPt    ,"LeadingBJetPt/D"); 
      tree -> Branch("HT2M", &HT2M    ,"HT2M/D");
      tree -> Branch("HTb", &HTb    ,"HTb/D"); 
      tree -> Branch("HTH", &HTH   ,"HTH/D"); 
      tree -> Branch("HTRat", &HTRat    ,"HTRat/D"); 
      tree -> Branch("HTX", &HTX    ,"HTX/D"); 
      tree -> Branch("SumJetMassX", &SumJetMassX    ,"SumJetMassX/D"); 
      tree -> Branch("multitopness", &multitopness    ,"multitopness/D"); 
      tree -> Branch("nbb", &nbb    ,"nbb/I"); 
      tree -> Branch("ncc", &ncc    ,"ncc/I"); 
      tree -> Branch("nll", &nll    ,"nll/I"); 
      tree -> Branch("ttbar_flav", &ttbar_flav    ,"ttbar_flav/D"); 
      tree -> Branch("ScaleFactor", &ScaleFactor   ,"ScaleFactor/D"); 
      tree -> Branch("SFlepton", &SFlepton    ,"SFlepton/D"); 
      tree -> Branch("SFbtag", &SFbtag    ,"SFbtag/D"); 
      tree -> Branch("SFbtagUp", &SFbtagUp    ,"SFbtagUp/D"); 
      tree -> Branch("SFbtagDown", &SFbtagDown    ,"SFbtagDown/D"); 
      tree -> Branch("SFPU", &SFPU    ,"SFPU/D"); 
      tree -> Branch("SFPU_up", &SFPU_up    ,"SFPU_up/D"); 
      tree -> Branch("SFPU_down", &SFPU_down    ,"SFPU_down/D"); 
      tree -> Branch("PU", &PU    ,"PU/I"); 
      tree -> Branch("NormFactor", &NormFactor    ,"NormFactor/D"); 
      tree -> Branch("GenWeight", &GenWeight    ,"GenWeight/D"); 
      tree -> Branch("weight1", &weight1   ,"weight1/D"); 
      tree -> Branch("weight2", &weight2    ,"weight2/D"); 
      tree -> Branch("weight3", &weight3    ,"weight3/D"); 
      tree -> Branch("weight4", &weight4    ,"weight4/D"); 
      tree -> Branch("weight5", &weight5    ,"weight5/D"); 
      tree -> Branch("weight6", &weight6    ,"weight6/D"); 
      tree -> Branch("weight7", &weight7    ,"weight7/D"); 
      tree -> Branch("weight8", &weight8    ,"weight8/D"); 
      tree -> Branch("met", &met    ,"met/D"); 
      tree -> Branch("angletop1top2", &angletop1top2    ,"angletop1top2/D"); 
      tree -> Branch("angletoplep", &angletoplep    ,"angletoplep/D"); 
      tree -> Branch("1stjetpt", &firstjetpt    ,"1stjetpt/D"); 
      tree -> Branch("2ndjetpt", &secondjetpt    ,"2ndjetpt/D"); 
      tree -> Branch("leptonIso", &leptonIso    ,"leptonIso/D"); 
      tree -> Branch("leptonphi", &leptonphi    ,"leptonphi/D"); 
      tree -> Branch("chargedHIso", &chargedHIso    ,"chargedHIso/D"); 
      tree -> Branch("neutralHIso", &neutralHIso    ,"neutralHIso/D"); 
      tree -> Branch("photonIso", &photonIso    ,"photonIso/D"); 
      tree -> Branch("PUIso", &PUIso    ,"PUIso/D");
      tree -> Branch("5thjetpt", &jet5Pt    ,"5thjetpt/D"); 
      tree -> Branch("6thjetpt", &jet6Pt   ,"6thjetpt/D"); 
      tree -> Branch("jet5and6pt", &jet5and6pt    ,"jet5and6pt/D"); 
      tree -> Branch("csvJetcsv1", &csvJetcsv1    ,"csvJetcsv1/D");
      tree -> Branch("csvJetcsv2", &csvJetcsv2    ,"csvJetcsv2/D"); 
      tree -> Branch("csvJetcsv3", &csvJetcsv3    ,"csvJetcsv3/D"); 
      tree -> Branch("csvJetcsv4", &csvJetcsv4    ,"csvJetcsv4/D"); 
      tree -> Branch("csvJetpt1", &csvJetpt1    ,"csvJetpt1/D"); 
      tree -> Branch("csvJetpt2", &csvJetpt2    ,"csvJetpt2/D"); 
      tree -> Branch("csvJetpt3", &csvJetpt3    ,"csvJetpt3/D"); 
      tree -> Branch("csvJetpt4", &csvJetpt4    ,"csvJetpt4/D");
      tree -> Branch("jetvec", jetvec    ,"jetvec[nJets][5]/D");
      tree -> Branch("weight", weight    ,"weight[8]/D");
      tree -> Branch("csvrsw", csvrsw    ,"csvrsw[19]/D");
} // end Event::makeBranches()

void Event::fill(double vals[], double jets[][5], int njet, double w[], double csvrs[]) {

    BDT = vals[0];
    nJets = vals[1]; 
    NOrigJets = vals[2]; 
    nLtags = vals[3]; 
    nMtags = vals[4]; 
    nTtags = vals[5]; 
    HT = vals[6]; 
    LeptonPt = vals[7]; 
    LeptonEta = vals[8]; 
    LeadingBJetPt = vals[9]; 
    HT2M = vals[10];
    HTb = vals[11]; 
    HTH = vals[12]; 
    HTRat = vals[13]; 
    HTX = vals[14]; 
    SumJetMassX = vals[15]; 
    multitopness = vals[16]; 
    nbb = vals[17]; 
    ncc = vals[18]; 
    nll = vals[19]; 
    ttbar_flav = vals[20]; 
    ScaleFactor = vals[21]; 
    SFlepton = vals[22]; 
    SFbtag = vals[23]; 
    SFbtagUp = vals[24]; 
    SFbtagDown = vals[25]; 
    SFPU = vals[26]; 
    SFPU_up = vals[27]; 
    SFPU_down = vals[28]; 
    PU = vals[29]; 
    NormFactor = vals[30]; 
    GenWeight = vals[31]; 
    weight1 = vals[32]; 
    weight2 = vals[33]; 
    weight3 = vals[34]; 
    weight4 = vals[35]; 
    weight5 = vals[36]; 
    weight6 = vals[37]; 
    weight7 = vals[38]; 
    weight8 = vals[39]; 
    met = vals[40]; 
    angletop1top2 = vals[41]; 
    angletoplep = vals[42]; 
    firstjetpt = vals[43]; 
    secondjetpt = vals[44]; 
    leptonIso = vals[45]; 
    leptonphi = vals[46]; 
    chargedHIso = vals[47]; 
    neutralHIso = vals[48]; 
    photonIso = vals[49]; 
    PUIso = vals[50];
    jet5Pt = vals[51]; 
    jet6Pt = vals[52]; 
    jet5and6pt = vals[53]; 
    csvJetcsv1 = vals[54];
    csvJetcsv2 = vals[55]; 
    csvJetcsv3 = vals[56]; 
    csvJetcsv4 = vals[57]; 
    csvJetpt1 = vals[58]; 
    csvJetpt2 = vals[59]; 
    csvJetpt3 = vals[60]; 
    csvJetpt4 = vals[61];
    
    for (auto i = 0; i < njet; ++i) {
        for (auto par = 0; par < 5; ++par) jetvec[i][par]=jets[i][par];
    }
    for (auto par = 0; par < 8; ++par) weight[par]=w[par];
    for (auto par = 0; par < 19; ++par) csvrsw[par]=csvrs[par];
} // end Event::fill()

#endif /* EVENT_H */

