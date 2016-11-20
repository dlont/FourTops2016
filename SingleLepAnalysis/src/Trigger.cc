#include "../interface/Trigger.h"

Trigger::Trigger(bool isMuon, bool isElectron):
muon(false), electron(false), trigged(false), redotrigmap(false), triggerListData(), triggerListMC(), triggerList(), currentRun(0), previousRun(-1), currentFilename(""),
 previousFilename(""), iFile(-1), triggermapData(), triggermapMC(), triggermap(), runInfos2(new TRootRun()), previousDatasetName("")
{
	if(isMuon){
		muon = true;
	}
	else if(isElectron){
		electron = true;
	}
	else{
		cout<<"neither lepton selection"<<endl;
	}
}

Trigger::~Trigger(){

}

void Trigger::bookTriggers(){
    if(muon){
        
//        triggerListData.push_back("HLT_IsoMu24_v*");
//        triggerListMC.push_back("HLT_IsoMu24_v2");
        triggerListData.push_back("HLT_IsoTkMu24_v*");
        triggerListMC.push_back("HLT_IsoTkMu24_v2");
//        triggerListData.push_back("HLT_Iso(Tk)Mu22_v*");
//        triggerListMC.push_back("HLT_Iso(Tk)Mu22_v3");
    }

    if (electron){
	    triggerListData.push_back("HLT_Ele32_eta2p1_WPTight_Gsf_v*");    	
	    triggerListMC.push_back("HLT_Ele32_eta2p1_WPTight_Gsf_v3");
    }

    for(UInt_t itrig=0; itrig<triggerListMC.size(); itrig++){
        triggermapMC[triggerListMC[itrig]]=std::pair<int,bool>(-999,false);
    }

    for(UInt_t itrig=0; itrig<triggerListData.size(); itrig++){
        triggermapData[triggerListData[itrig]]=std::pair<int,bool>(-999,false);
    }
 
}

void Trigger::checkAvail(int currentRun, vector < Dataset* > datasets, unsigned int d, TTreeLoader *treeLoader, TRootEvent* event, int treeNumber){
	redotrigmap=false;
	currentFilename = datasets[d]->eventTree()->GetFile()->GetName();
	if(previousFilename != currentFilename){
	    previousFilename = currentFilename;
	    iFile++;
	    redotrigmap=true;
	    cout<<"File changed!!! => iFile = "<<iFile << " new file is " << datasets[d]->eventTree()->GetFile()->GetName() << " in sample " << datasets[d]->Name() << endl;
	}
	if(previousRun != currentRun){
	    previousRun = currentRun;
	    cout<<"*****!!!!new run!!!! => new run = "<<previousRun<<" *****"<<endl;
	    redotrigmap=true;
	}

	iFile = treeNumber;

	// get trigger info:
	string datasetName = datasets[d]->Name();
	if(datasetName.find("Data")==string::npos){ // if MC
	
		for(std::map<std::string,std::pair<int,bool> >::iterator iter = triggermapMC.begin(); iter != triggermapMC.end(); iter++){
		    if(redotrigmap){
		        Int_t loc = treeLoader->iTrigger(iter->first, currentRun, iFile);
		        string trigname = iter->first;
		        cout<<"trigname: "<<trigname<<"  location: "<<loc<<endl;
		        iter->second.first=loc;
		    }
		    // and check if it exists and if it fired:
		    if(iter->second.first>=0 && iter->second.first!=9999) // trigger exists
		        iter->second.second=event->trigHLT(iter->second.first);
		    else
		        iter->second.second=false;
#ifdef NOTRIGMC
#warning "WARNING: Code for MC without triggers switched on!!!"
                    if (iter->second.first >= 0 && iter->second.first == 9999) // For MC samples without triggers
                         iter->second.second = true;                            // Force trigger to be fired 
#endif
		}  
	}
	else { // if DATA
		for(std::map<std::string,std::pair<int,bool> >::iterator iter = triggermapData.begin(); iter != triggermapData.end(); iter++){
		    if(redotrigmap){
		        Int_t loc = treeLoader->iTrigger(iter->first, currentRun, iFile);
		        string trigname = iter->first;
		        cout<<"trigname: "<<trigname<<"  location: "<<loc<<endl;
		        iter->second.first=loc;
		    }
		    // and check if it exists and if it fired:
		    if(iter->second.first>=0 && iter->second.first!=9999) // trigger exists
		        iter->second.second=event->trigHLT(iter->second.first);
		    else
		        iter->second.second=false;
#ifdef NOTRIGMC
#warning "WARNING: Code for MC without triggers switched on!!!"
                    if (iter->second.first >= 0 && iter->second.first == 9999) // For MC samples without triggers
                         iter->second.second = true;                            // Force trigger to be fired 
#endif
		}  		
	}

}


int Trigger::checkIfFired(int currentRun, vector < Dataset* > datasets, unsigned int d){
	// now check if the appropriate triggers fired for each analysis:
	trigged =0;
	string datasetName = datasets[d]->Name();

	if(datasetName.find("Data")==string::npos){ // if MC
		for(UInt_t itrig=0; itrig<triggerListMC.size() && trigged==0; itrig++){
			// cout<<"fired: "<<triggermapMC[triggerListMC[itrig]].second<<endl;
		    if(triggermapMC[triggerListMC[itrig]].second)   trigged=1;
		}
	}
	else { // if DATA
		for(UInt_t itrig=0; itrig<triggerListData.size() && trigged==0; itrig++){
			// cout<<"fired: "<<triggermapDataC[triggerListDataC[itrig]].second<<endl;
		    if(triggermapData[triggerListData[itrig]].second)   trigged=1;
		}		
	}

	return trigged;
}

