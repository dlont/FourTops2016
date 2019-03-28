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
    void fill_electronVFID(bool);
    void fill(double [], double [][5], double [], double[], int , double [], double [], 
	      double [], double [], double [], double [], double [], 
              double [][6], double [][6], double [][6]);
    
    double BDT; // baseline tmva from top-16-016
    float  BDT1;// scikitlearn jet-split training
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
    double tritopness;
    double mt1;
    double mt2;
    double mt3;
    double mw1;
    double mw2;
    double mw3;
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
    bool electronVFIDflag;      //electron VF ID for isolation studies
    double electronparams[20]; // lepton parameter like nHits, Chi2, etc. (different for electrons and muons)
    double muonparams[20];  // lepton parameter like nHits, Chi2, etc. (different for electrons and muons)
    double jetvec[30][5];   // jet properties (pT,eta,phi,csv,E)
    double trijet1stpass[3][6]; // jet properties of the highest multitopness triplet (pT,eta,phi,csv,E,topness)
    double trijet2ndpass[3][6]; // jet properties of the 2nd highest multitopness triplet (pT,eta,phi,csv,E,topness)
    double trijet3rdpass[3][6]; // jet properties of the 3rd highest multitopness triplet (pT,eta,phi,csv,E,topness)
    double weight[9];       // ME scale variation weights
    double csvrsw[20];      // CSVRS systematic weights
    double hdampw[2];       // POWHEG hdamp weight variation 
    double pdfw[2];         // POWHEG CT10,MMH14 weight variation 
    double pdf_nnpdf[101];  // POWHEG NNPDF replicas weights
    double ttxw[2];         // POWHEG heavy-flavour fraction variation 
    double toprew;          // TOP pT reweighting factor
    double toprewunc[3];          // TOP pT reweighting factors
    int    ttxType;         // TTX event type (ttbb, ttcc, etc.)
    double ttxrew;          // Heavy flavour fraction reweighting
    double SFtrig;	    // Trigger scale factor
    double NjetsW; 	    // Transverse momentum weighted jet multiplicity
    long long runID;	    // run number
    long long eventID;	    // event number
    long long lumiID;	    // lumiblock number
   
}; //end Event

//______________________________________________________________________________
/**
 * Flush the content of the structure to be called before filling inside an event
 */
void Event::clear() {
      this->BDT = 0.;
      this->BDT1 = 0.;
      this->nJets = 0.; 
      this->NOrigJets = 0.; 
      this->nLtags = 0.; 
      this->nMtags = 0.; 
      this->nTtags = 0.; 
      this->HT = 0.; 
      this->LeptonPt = 0.; 
      this->LeptonEta = 0.; 
      this->LeadingBJetPt = 0.; 
      this->HT2M = 0.;
      this->HTb = 0.; 
      this->HTH = 0.; 
      this->HTRat = 0.; 
      this->HTX = 0.; 
      this->SumJetMassX = 0.; 
      this->multitopness = 0.; 
      this->mt1 = 0.;
      this->mt2 = 0.;
      this->mt3 = 0.;
      this->mw1 = 0.;
      this->mw2 = 0.;
      this->mw3 = 0.;
      this->nbb = 0.; 
      this->ncc = 0.; 
      this->nll = 0.; 
      this->ttbar_flav = 0.; 
      this->ScaleFactor = 0.; 
      this->SFlepton = 0.; 
      this->SFbtag = 0.; 
      this->SFbtagUp = 0.; 
      this->SFbtagDown = 0.; 
      this->SFPU = 0.; 
      this->SFPU_up = 0.; 
      this->SFPU_down = 0.; 
      this->PU = 0.; 
      this->NormFactor = 0.; 
      this->GenWeight = 0.; 
      this->weight1 = 0.; 
      this->weight2 = 0.; 
      this->weight3 = 0.; 
      this->weight4 = 0.; 
      this->weight5 = 0.; 
      this->weight6 = 0.; 
      this->weight7 = 0.; 
      this->weight8 = 0.; 
      this->met = 0.; 
      this->angletop1top2 = 0.; 
      this->angletoplep = 0.; 
      this->firstjetpt = 0.; 
      this->secondjetpt = 0.; 
      this->leptonIso = 0.; 
      this->leptonphi = 0.; 
      this->chargedHIso = 0.; 
      this->neutralHIso = 0.; 
      this->photonIso = 0.; 
      this->PUIso = 0.;
      this->jet5Pt = 0.; 
      this->jet6Pt = 0.; 
      this->jet5and6pt = 0.; 
      this->csvJetcsv1 = 0.;
      this->csvJetcsv2 = 0.; 
      this->csvJetcsv3 = 0.; 
      this->csvJetcsv4 = 0.; 
      this->csvJetpt1 = 0.; 
      this->csvJetpt2 = 0.; 
      this->csvJetpt3 = 0.; 
      this->csvJetpt4 = 0.;
      this->electronVFIDflag = false;
      std::fill_n( this->electronparams, 20, -10.);
      std::fill_n( this->muonparams, 20, -10.);
      std::fill( &this->jetvec[0][0], &this->jetvec[0][0]+sizeof(this->jetvec)/sizeof(this->jetvec[0][0]), -1.);
      std::fill( &this->trijet1stpass[0][0], &this->trijet1stpass[0][0]+sizeof(this->trijet1stpass)/sizeof(this->trijet1stpass[0][0]), -10.);
      std::fill( &this->trijet2ndpass[0][0], &this->trijet2ndpass[0][0]+sizeof(this->trijet2ndpass)/sizeof(this->trijet2ndpass[0][0]), -10.);
      std::fill( &this->trijet3rdpass[0][0], &this->trijet3rdpass[0][0]+sizeof(this->trijet3rdpass)/sizeof(this->trijet3rdpass[0][0]), -10.);
      std::fill_n( this->weight, 9, 0.);
      std::fill_n( this->csvrsw, 20, 0.);
      std::fill_n( this->hdampw, 2, 1.);
      std::fill_n( this->pdfw, 2, 1.);
      std::fill_n( this->pdf_nnpdf, 101, 1.);
      std::fill_n( this->ttxw, 2, 1.);
      std::fill_n( this->toprewunc, 3, 1.);
      this->toprew = 0.;
      this->ttxType = -1.;
      this->ttxrew = 1.;
      this->SFtrig = 1.;
      this->NjetsW = 0.;
} //End Event::clear()

/**
 * Create root TTree with proper branches
 * @param tree
 */
void Event::makeBranches(TTree* tree) {
    if (tree == nullptr) {
        std::cerr << "tree pointer is NULL. Aborting!.." << std::endl;
        std::exit(EXIT_FAILURE);
    }
    
      tree -> Branch("BDT",                  &this->BDT,                 "BDT/D");
      tree -> Branch("BDT1",                 &this->BDT1,                "BDT1/F");
      //
      tree -> Branch("NOrigJets",            &this->NOrigJets,           "NOrigJets/I"); 
      tree -> Branch("nJets",                &this->nJets,               "nJets/I"); 
      tree -> Branch("jetvec",                this->jetvec,              "jetvec[nJets][5]/D");
      tree -> Branch("trijet1stpass",         this->trijet1stpass,       "trijet1stpass[3][6]/D");
      tree -> Branch("trijet2ndpass",         this->trijet2ndpass,       "trijet2ndpass[3][6]/D");
      tree -> Branch("trijet3rdpass",         this->trijet3rdpass,       "trijet3rdpass[3][6]/D");
      tree -> Branch("1stjetpt",             &this->firstjetpt,          "1stjetpt/D"); 
      tree -> Branch("2ndjetpt",             &this->secondjetpt,         "2ndjetpt/D"); 
      tree -> Branch("5thjetpt",             &this->jet5Pt,              "5thjetpt/D"); 
      tree -> Branch("6thjetpt",             &this->jet6Pt,              "6thjetpt/D"); 
      //
      tree -> Branch("ElectronVFid",         &this->electronVFIDflag,    "ElectronVFid/O");
      tree -> Branch("Electronparam",         this->electronparams,      "Electronparam[20]/D");
      tree -> Branch("Muonparam",             this->muonparams,          "Muonparam[20]/D");
      tree -> Branch("LeptonPt",             &this->LeptonPt,            "LeptonPt/D"); 
      tree -> Branch("LeptonEta",            &this->LeptonEta,           "LeptonEta/D"); 
      tree -> Branch("leptonIso",            &this->leptonIso,           "leptonIso/D"); 
      tree -> Branch("leptonphi",            &this->leptonphi,           "leptonphi/D"); 
      tree -> Branch("NjetsW",               &this->NjetsW,              "NjetsW/D"); 
      tree -> Branch("chargedHIso",          &this->chargedHIso,         "chargedHIso/D"); 
      tree -> Branch("neutralHIso",          &this->neutralHIso,         "neutralHIso/D"); 
      tree -> Branch("photonIso",            &this->photonIso,           "photonIso/D"); 
      tree -> Branch("PUIso",                &this->PUIso,               "PUIso/D");
      //
      tree -> Branch("PU",                   &this->PU,                  "PU/I"); 
      tree -> Branch("HT",                   &this->HT,                  "HT/D"); 
      tree -> Branch("HT2M",                 &this->HT2M,                "HT2M/D");
      tree -> Branch("HTb",                  &this->HTb,                 "HTb/D"); 
      tree -> Branch("HTH",                  &this->HTH,                 "HTH/D"); 
      tree -> Branch("HTRat",                &this->HTRat,               "HTRat/D"); 
      tree -> Branch("HTX",                  &this->HTX,                 "HTX/D"); 
      tree -> Branch("SumJetMassX",          &this->SumJetMassX,         "SumJetMassX/D"); 
      tree -> Branch("multitopness",         &this->multitopness,        "multitopness/D"); 
      tree -> Branch("mt1",                  &this->mt1,                 "mt1/D"); 
      tree -> Branch("mt2",                  &this->mt2,                 "mt2/D"); 
      tree -> Branch("mt3",                  &this->mt3,                 "mt3/D"); 
      tree -> Branch("mw1",                  &this->mw1,                 "mw1/D"); 
      tree -> Branch("mw2",                  &this->mw2,                 "mw2/D"); 
      tree -> Branch("mw3",                  &this->mw3,                 "mw3/D"); 
      tree -> Branch("met",                  &this->met,                 "met/D"); 
      tree -> Branch("angletop1top2",        &this->angletop1top2,       "angletop1top2/D"); 
      tree -> Branch("angletoplep",          &this->angletoplep,         "angletoplep/D"); 
      //
      tree -> Branch("ttxType",              &this->ttxType,             "ttxType/I");
      tree -> Branch("nbb",                  &this->nbb,                 "nbb/I"); 
      tree -> Branch("ncc",                  &this->ncc,                 "ncc/I"); 
      tree -> Branch("nll",                  &this->nll,                 "nll/I"); 
      tree -> Branch("ttbar_flav",           &this->ttbar_flav,          "ttbar_flav/D"); 
      tree -> Branch("ScaleFactor",          &this->ScaleFactor,         "ScaleFactor/D"); 
      tree -> Branch("SFlepton",             &this->SFlepton,            "SFlepton/D"); 
      tree -> Branch("SFbtag",               &this->SFbtag,              "SFbtag/D"); 
      tree -> Branch("SFbtagUp",             &this->SFbtagUp,            "SFbtagUp/D"); 
      tree -> Branch("SFbtagDown",           &this->SFbtagDown,          "SFbtagDown/D"); 
      tree -> Branch("SFPU",                 &this->SFPU,                "SFPU/D"); 
      tree -> Branch("SFPU_up",              &this->SFPU_up,             "SFPU_up/D"); 
      tree -> Branch("SFPU_down",            &this->SFPU_down,           "SFPU_down/D"); 
      tree -> Branch("SFtrig",               &this->SFtrig,              "SFtrig/D"); 
      tree -> Branch("csvrsw",                this->csvrsw,              "csvrsw[19]/D");
      tree -> Branch("toprew",               &this->toprew,              "toprew/D");
      tree -> Branch("ttxrew",               &this->ttxrew,              "ttxrew/D");
      tree -> Branch("NormFactor",           &this->NormFactor,          "NormFactor/D"); 
      tree -> Branch("GenWeight",            &this->GenWeight,           "GenWeight/D"); 
      //
      tree -> Branch("weight",                this->weight,              "weight[9]/D");
      tree -> Branch("weight1",              &this->weight1,             "weight1/D"); 
      tree -> Branch("weight2",              &this->weight2,             "weight2/D"); 
      tree -> Branch("weight3",              &this->weight3,             "weight3/D"); 
      tree -> Branch("weight4",              &this->weight4,             "weight4/D"); 
      tree -> Branch("weight5",              &this->weight5,             "weight5/D"); 
      tree -> Branch("weight6",              &this->weight6,             "weight6/D"); 
      tree -> Branch("weight7",              &this->weight7,             "weight7/D"); 
      tree -> Branch("weight8",              &this->weight8,             "weight8/D"); 
      tree -> Branch("hdampw",                this->hdampw,              "hdamp[2]/D");
      tree -> Branch("pdfw",                  this->pdfw,                "pdfw[2]/D");
      tree -> Branch("pdf_nnpdf",             this->pdf_nnpdf,           "pdf_nnpdf[101]/D");
      tree -> Branch("ttxw",                  this->ttxw,                "ttxw[2]/D");
      tree -> Branch("toprewunc",             this->toprewunc,           "toprewunc[3]/D");
      //
      tree -> Branch("LeadingBJetPt",        &this->LeadingBJetPt,       "LeadingBJetPt/D"); 
      tree -> Branch("nLtags",               &this->nLtags,              "nLtags/I"); 
      tree -> Branch("nMtags",               &this->nMtags,              "nMtags/I"); 
      tree -> Branch("nTtags",               &this->nTtags,              "nTtags/I");       
      tree -> Branch("jet5and6pt",           &this->jet5and6pt,          "jet5and6pt/D"); 
      tree -> Branch("csvJetcsv1",           &this->csvJetcsv1,          "csvJetcsv1/D");
      tree -> Branch("csvJetcsv2",           &this->csvJetcsv2,          "csvJetcsv2/D"); 
      tree -> Branch("csvJetcsv3",           &this->csvJetcsv3,          "csvJetcsv3/D"); 
      tree -> Branch("csvJetcsv4",           &this->csvJetcsv4,          "csvJetcsv4/D"); 
      tree -> Branch("csvJetpt1",            &this->csvJetpt1,           "csvJetpt1/D"); 
      tree -> Branch("csvJetpt2",            &this->csvJetpt2,           "csvJetpt2/D"); 
      tree -> Branch("csvJetpt3",            &this->csvJetpt3,           "csvJetpt3/D"); 
      tree -> Branch("csvJetpt4",            &this->csvJetpt4,           "csvJetpt4/D");
} // end Event::makeBranches()

void Event::fill_electronVFID(bool flag) {
    electronVFIDflag = flag;
}

/**
 * Fill ROOT ntuple with event variables
 * @param vals Original Craneen values
 * @param jets jet properties [njet][5] pT,eta,phi,csv,empty
 * @param njet number of elements in jets[njet][] vector
 * @param w ME scale variation weights
 * @param csvrs CSVRS systematics weights breakdown 
 * @param hdamp POWHEG hdamp weights
 * @param pdf   POWHEG CT10,MMHT14 weights
 * @param topr top reweighting event weight
 * @param trj1st trijet combination with highest topness score
 * @param trj2nd trijet combination with 2nd highest topness score
 * @param trj3rd trijet combination with 3rd highest topness score
 */
void Event::fill(double vals[], double jets[][5], double electron[], double muon[], int njet, 
                 double w[], double csvrs[], double hdamp[], double pdf[], double nnpdf[], double ttx[], 
                 double topptreww[], double trj1st[][6], double trj2nd[][6], double trj3rd[][6]) {

    this->BDT = vals[0];
    this->nJets = vals[1]; 
    this->NOrigJets = vals[2]; 
    this->nLtags = vals[3]; 
    this->nMtags = vals[4]; 
    this->nTtags = vals[5]; 
    this->HT = vals[6]; 
    this->LeptonPt = vals[7]; 
    this->LeptonEta = vals[8]; 
    this->LeadingBJetPt = vals[9]; 
    this->HT2M = vals[10];
    this->HTb = vals[11]; 
    this->HTH = vals[12]; 
    this->HTRat = vals[13]; 
    this->HTX = vals[14]; 
    this->SumJetMassX = vals[15]; 
    this->multitopness = vals[16]; 
    this->nbb = vals[17]; 
    this->ncc = vals[18]; 
    this->nll = vals[19]; 
    this->ttbar_flav = vals[20]; 
    this->ScaleFactor = vals[21]; 
    this->SFlepton = vals[22]; 
    this->SFbtag = vals[23]; 
    this->SFbtagUp = vals[24]; 
    this->SFbtagDown = vals[25]; 
    this->SFPU = vals[26]; 
    this->SFPU_up = vals[27]; 
    this->SFPU_down = vals[28]; 
    this->PU = vals[29]; 
    this->NormFactor = vals[30]; 
    this->GenWeight = vals[31]; 
    this->weight1 = vals[32]; 
    this->weight2 = vals[33]; 
    this->weight3 = vals[34]; 
    this->weight4 = vals[35]; 
    this->weight5 = vals[36]; 
    this->weight6 = vals[37]; 
    this->weight7 = vals[38]; 
    this->weight8 = vals[39]; 
    this->met = vals[40]; 
    this->angletop1top2 = vals[41]; 
    this->angletoplep = vals[42]; 
    this->firstjetpt = vals[43]; 
    this->secondjetpt = vals[44]; 
    this->leptonIso = vals[45]; 
    this->leptonphi = vals[46]; 
    this->chargedHIso = vals[47]; 
    this->neutralHIso = vals[48]; 
    this->photonIso = vals[49]; 
    this->PUIso = vals[50];
    this->jet5Pt = vals[51]; 
    this->jet6Pt = vals[52]; 
    this->jet5and6pt = vals[53]; 
    this->csvJetcsv1 = vals[54];
    this->csvJetcsv2 = vals[55]; 
    this->csvJetcsv3 = vals[56]; 
    this->csvJetcsv4 = vals[57]; 
    this->csvJetpt1 = vals[58]; 
    this->csvJetpt2 = vals[59]; 
    this->csvJetpt3 = vals[60]; 
    this->csvJetpt4 = vals[61];
    this->toprew = vals[62];
    this->ttxType = vals[63];
    this->ttxrew = vals[64];
    this->SFtrig = vals[65];
    this->NjetsW = vals[66];
    this->mt1 = vals[67];
    this->mt2 = vals[68];
    this->mt3 = vals[69];
    this->mw1 = vals[70];
    this->mw2 = vals[71];
    this->mw3 = vals[72];
    this->BDT1 = vals[73];
    for (auto i = 0; i < njet; ++i) {
        for (auto par = 0; par < 5; ++par) this->jetvec[i][par]=jets[i][par];
    }
    for (auto i = 0; i < 3; ++i) {
        for (auto par = 0; par < 6; ++par) this->trijet1stpass[i][par]=trj1st[i][par];
    }
    for (auto i = 0; i < 3; ++i) {
        for (auto par = 0; par < 6; ++par) this->trijet2ndpass[i][par]=trj2nd[i][par];
    }
    for (auto i = 0; i < 3; ++i) {
        for (auto par = 0; par < 6; ++par) this->trijet3rdpass[i][par]=trj3rd[i][par];
    }
    std::copy ( electron, electron+20, this->electronparams);
    std::copy ( muon, muon+20, this->muonparams);
    std::copy ( w, w+9, this->weight);
    std::copy ( csvrs, csvrs+19, this->csvrsw);
    std::copy ( hdamp, hdamp+2, this->hdampw );
    std::copy ( pdf, pdf+2, this->pdfw );
    std::copy ( nnpdf, nnpdf+101, this->pdf_nnpdf );
    std::copy ( ttx, ttx+2, this->ttxw );
    std::copy ( topptreww, topptreww+3, this->toprewunc );
    //for (auto par = 0; par < 8; ++par) weight[par]=w[par];
    //for (auto par = 0; par < 19; ++par) csvrsw[par]=csvrs[par];
    
} // end Event::fill()

#endif /* EVENT_H */

