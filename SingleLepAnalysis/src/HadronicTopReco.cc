//////////////////////////////////////////////
//          Make cutflow table              //
//////////////////////////////////////////////

#include "../interface/HadronicTopReco.h"
#include "TopTreeProducer/interface/TRootJet.h"
#include <regex>

HadronicTopReco::HadronicTopReco(TFile *fout, bool isMuon, bool isElectron, bool TrainMVA, vector < Dataset* > datasets, string MVAmethodIn, bool isdebug, float Lumi):
	MSPlot(),
	debug(false),
	leptonChoice(""),
	selectedLeptonTLV_JC(),
	mcParticlesTLV(), 
	selectedJetsTLV(),
	mcMuonsTLV(),
	mcParticlesMatching_(),
	leptonicBJet_(),
	hadronicBJet_(),
	hadronicWJet1_(),
	hadronicWJet2_(), //First index is the JET number(), second one is the parton
	mcParticles_flav(),
	JetPartonPair(),
	TriJetMass(0), DiJetMass(0),
	Topness(0), MultiTopness(0), DiTopness(0), TriTopness(0),
	MVAvals1(), //BDT discriminator value of highest ranked tri jet
	MVAvals2ndPass(), //BDT discriminator value of second highest ranked tri jet
	MVAvals3rdPass(), //BDT discriminator value of third highest ranked tri jet (if possible)
	selectedJets2ndPass(), //remaining jets after removing highest ranked tri jet
	selectedJets3rdPass(), //remaining jets after removing highest & second highest ranked tri jet
	MVASelJets1(), //the selected jets from the highest ranked tri jet
	MVASelJets2(), //the selected jets from the second highest ranked tri jet
	jetCombiner(0),
	bestTopMass1(0),
	bestTopMass2(0),
	bestTopMass2ndPass(0), 
	bestTopPt(0),
	nMVASuccesses(0),
	scaleFactor(0),
	Luminosity(Lumi),
	MVAmethod(MVAmethodIn),
	wj1(0), wj2(0), bj1(0), wj1_2ndpass(0), wj2_2ndpass(0), bj1_2ndpass(0),
	AngleT1T22ndpass(0),
	AngleT1Lep(0),
	SumJetMassX(0),
	HTX(0),
	sumpx_X(0),
	sumpy_X(0),
	sumpz_X(0),
	sume_X(0),
	sumjet_X(TLorentzVector(0,0,0,0)),
	angleT1AllJets(0)
	{
        std::string postfix;
	if (fout) postfix = fout->GetName();
//        std::string postfix = "FourTop_Run2_TopTree_Study";
        postfix = std::regex_replace(postfix, std::regex("Train"), "MVAOutput");
        
        jetCombiner = new JetCombiner(TrainMVA, Lumi, datasets, MVAmethodIn, false, "", postfix, "_13TeV_new"); //_13TeV in last arg for 13tev training
    
	if (isMuon){
		leptonChoice = "Muon";
	}
	else if (isElectron){
		leptonChoice = "Electron";
	}

	if(isdebug)	debug = true;
	
}

HadronicTopReco::~HadronicTopReco(){
    for(map<string,MultiSamplePlot*>::const_iterator it = MSPlot.begin(); it != MSPlot.end(); it++)
    {
        string name = it->first;
		MSPlot.erase(name);
    }
    delete jetCombiner;
}

void HadronicTopReco::SetCollections(vector<TRootPFJet*> selectJets,  vector<TRootMuon*> selectedMuons, vector<TRootElectron*> selectedElectrons, float scaleFac){
	if (leptonChoice == "Muon"){
	    selectedLeptonTLV_JC.push_back(selectedMuons[0]);               
	}
	else if (leptonChoice == "Electron"){
	    selectedLeptonTLV_JC.push_back(selectedElectrons[0]);               
	}
	scaleFactor = scaleFac;
}

// Fill training trees for hadronic top decay reconstruction
void HadronicTopReco::Train(unsigned int d, vector<TRootPFJet*> selectedJets, vector < Dataset* > datasets){
    selectedJets2ndPass.clear();
    selectedJets3rdPass.clear();
    MVASelJets1.clear();   

    jetCombiner->ProcessEvent_SingleHadTop(datasets[d], mcParticles_flav, selectedJets, selectedLeptonTLV_JC[0], scaleFactor);
}

void HadronicTopReco::SetMCParticles(const vector<TRootMCParticle*>& mcParticles){
    mcParticles_flav = mcParticles;
}

void HadronicTopReco::Compute1st(unsigned int d, vector<TRootPFJet*> selectedJets, vector < Dataset* > datasets){
	selectedJets2ndPass.clear();
	selectedJets3rdPass.clear();
	MVASelJets1.clear();   

    jetCombiner->ProcessEvent_SingleHadTop(datasets[d], mcParticles_flav, selectedJets, selectedLeptonTLV_JC[0], scaleFactor);


	if (debug) cout <<"Processing event with jetcombiner :  "<< endl;

    MVAvals1 = jetCombiner->getMVAValue(MVAmethod, 1); // 1 means the highest MVA value
    Topness = MVAvals1.first;

    if (debug) cout <<"Processing event with jetcombiner : 1 "<< endl;
}

void HadronicTopReco::Compute2nd(unsigned int d, vector<TRootPFJet*> selectedJets, vector < Dataset* > datasets){
	selectedJets2ndPass.clear();
	MVASelJets1.clear();   
	HTX = 0;
	sumpx_X = 0, sumpy_X = 0, sumpz_X = 0, sume_X =0;

    //make vector of jets excluding these selected by 1st pass of mass reco
    for (unsigned int seljet1 =0; seljet1 < selectedJets.size(); seljet1++ ){
        if (seljet1 == MVAvals1.second[0] || seljet1 == MVAvals1.second[1] || seljet1 == MVAvals1.second[2]){ 
            MVASelJets1.push_back(selectedJets[seljet1]);
            continue;
        }
        selectedJets2ndPass.push_back(selectedJets[seljet1]);
        HTX += selectedJets[seljet1]->Pt();
        sumpx_X = sumpx_X + selectedJets[seljet1]->Px();
        sumpy_X = sumpy_X + selectedJets[seljet1]->Py();
        sumpz_X = sumpz_X + selectedJets[seljet1]->Pz();
        sume_X = sume_X + selectedJets[seljet1]->E();          
    }
    sumjet_X = TLorentzVector (sumpx_X, sumpy_X, sumpz_X,sume_X ); //Object representing all the jets summed minus the hadronic system
    SumJetMassX = sumjet_X.M();	

    //Perform jet combiner a second time with top tri-jet removed
    jetCombiner->ProcessEvent_SingleHadTop(datasets[d], mcParticles_flav, selectedJets2ndPass, selectedLeptonTLV_JC[0], scaleFactor);
 

    MVAvals2ndPass = jetCombiner->getMVAValue(MVAmethod, 1);
    DiTopness = MVAvals2ndPass.first;
    if (debug) cout <<"Processing event with jetcombiner : 2 "<< endl;
}

void HadronicTopReco::Compute3rd(unsigned int d, vector<TRootPFJet*> selectedJets, vector < Dataset* > datasets){
	selectedJets3rdPass.clear();

    //make vector of jets excluding these selected by 1st pass of mass reco
    for (unsigned int seljet1 =0; seljet1 < selectedJets2ndPass.size(); seljet1++ ){
        if (seljet1 == MVAvals2ndPass.second[0] || seljet1 == MVAvals2ndPass.second[1] || seljet1 == MVAvals2ndPass.second[2]){ 
            MVASelJets2.push_back(selectedJets2ndPass[seljet1]);
            continue;
        }
        selectedJets3rdPass.push_back(selectedJets2ndPass[seljet1]);
    }

    if (selectedJets3rdPass.size()>=3) {
	     //Perform jet combiner a third time with top tri-jet removed if there are 3 jets remaining, otherwise it's not possible
	    jetCombiner->ProcessEvent_SingleHadTop(datasets[d], mcParticles_flav, selectedJets3rdPass, selectedLeptonTLV_JC[0], scaleFactor);

	    MVAvals3rdPass = jetCombiner->getMVAValue(MVAmethod, 1);
	    TriTopness = MVAvals3rdPass.first;
    }

}

float HadronicTopReco::ReturnAnglet1Jet(){
	return angleT1AllJets;
}

float HadronicTopReco::ReturnSumJetMassX(){
    return SumJetMassX;
}

float HadronicTopReco::ReturnHTX(){
	return HTX;
}

float HadronicTopReco::ReturnAnglet1t2(){
	return AngleT1T22ndpass;
}

float HadronicTopReco::ReturnAngletoplep(){
	return AngleT1Lep;
}

float HadronicTopReco::ReturnBestTopPt(){
	return bestTopPt;
}
void HadronicTopReco::ComputeMVASuccesses(){
    if(   ( hadronicBJet_.first == MVAvals1.second[0] || hadronicBJet_.first == MVAvals1.second[1] || hadronicBJet_.first == MVAvals1.second[2]   )  && ( hadronicWJet1_.first == MVAvals1.second[0] || hadronicWJet1_.first == MVAvals1.second[1] || hadronicWJet1_.first == MVAvals1.second[2]   )    && ( hadronicWJet2_.first == MVAvals1.second[0] || hadronicWJet2_.first == MVAvals1.second[1] || hadronicWJet2_.first == MVAvals1.second[2]   )      ){
	    nMVASuccesses++;
	}
}

int HadronicTopReco::ReturnMVASuccesses(){
	return nMVASuccesses;
}

float HadronicTopReco::ReturnTopness(){
	return Topness;
}

float HadronicTopReco::ReturnDiTopness(){
	return DiTopness;
}

float HadronicTopReco::ReturnTriTopness(){
	return TriTopness;
}


void HadronicTopReco::RecoCheck(bool debug, vector<TRootMuon*> selectedMuons, vector<TRootElectron*> selectedElectrons, vector<TRootPFJet*> selectedJets){
	/////////////////////////////////
	/// Find indices of jets from Tops
	////////////////////////////////

	bool muPlusFromTop = false, muMinusFromTop = false;
	// bool elPlusFromTop = false, elMinusFromTop = false;

	leptonicBJet_ = hadronicBJet_ = hadronicWJet1_ = hadronicWJet2_ = pair<unsigned int,unsigned int>(9999,9999);

	//match jets to partons
	for(unsigned int i=0; i<selectedJets.size(); i++) selectedJetsTLV.push_back(*selectedJets[i]);
	    JetPartonMatching matching = JetPartonMatching(mcParticlesTLV, selectedJetsTLV, 2, true, true, 0.3);

	//loop through mc particles and find matched jets
	for(unsigned int i=0; i<mcParticlesTLV.size(); i++) 
	{
		int matchedJetNumber = matching.getMatchForParton(i, 0);
	    if(matchedJetNumber != -1)
	        JetPartonPair.push_back( pair<unsigned int, unsigned int> (matchedJetNumber, i) );// Jet index, MC Particle index
	}

	if (debug) cout <<"n sel jets  "<<selectedJets.size()  << "   n mc particles tlv : "<< mcParticlesTLV.size() << " jet parton pari size :   "<< JetPartonPair.size()<<"  "<< muPlusFromTop<<muMinusFromTop<<endl;

	for(unsigned int i=0; i<JetPartonPair.size(); i++)//looping through matched jet-parton pairs
	{
	    unsigned int j = JetPartonPair[i].second;     //get index of matched mc particle

	    if( fabs(mcParticlesMatching_[j]->type()) < 5 )
	    {
	        if( ( muPlusFromTop && mcParticlesMatching_[j]->motherType() == -24 && mcParticlesMatching_[j]->grannyType() == -6 )
	            || ( muMinusFromTop && mcParticlesMatching_[j]->motherType() == 24 && mcParticlesMatching_[j]->grannyType() == 6 ) )
	        {
	            if(hadronicWJet1_.first == 9999)
	            {
	                hadronicWJet1_ = JetPartonPair[i];
	                // MCPermutation[0] = JetPartonPair[i].first;
	            }
	            else if(hadronicWJet2_.first == 9999)
	            {
	                hadronicWJet2_ = JetPartonPair[i];
	                //MCPermutation[1] = JetPartonPair[i].first;
	            }
	            //else cerr<<"Found a third jet coming from a W boson Wh1ich comes from a top quark..."<<endl;
	        }
	    }
	    else if( fabs(mcParticlesMatching_[j]->type()) == 5 )
	    {

	        if(  ( muPlusFromTop && mcParticlesMatching_[j]->motherType() == -6) || ( muMinusFromTop && mcParticlesMatching_[j]->motherType() == 6 ) )
	        {
	            hadronicBJet_ = JetPartonPair[i];
	            //MCPermutation[2] = JetPartonPair[i].first;
	        }
	        else if((muPlusFromTop && mcParticlesMatching_[j]->motherType() == 6) ||  ( muMinusFromTop &&mcParticlesMatching_[j]->motherType() == -6) )
	        {
	            leptonicBJet_ = JetPartonPair[i];
	            //MCPermutation[3] = JetPartonPair[i].first;
	        }
	    }
	}

	if (debug) cout <<"Indices of matched jets are :  "<< hadronicBJet_.first<<"  "<< hadronicWJet1_.first  <<" " << hadronicWJet2_.first <<endl;

}

 JetCombiner* HadronicTopReco::GetJetCombiner() {
    return jetCombiner;
}
