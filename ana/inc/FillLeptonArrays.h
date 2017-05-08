#include "TopTreeAnalysisBase/Selection/interface/Run2Selection.h"

void FillElectronParams(const TRootElectron* lepton, double vec[]) {
	vec[0] = lepton->Pt();
	vec[1] = lepton->Eta();
	vec[2] = lepton->Phi();
	vec[3] = lepton->superClusterEta();
	vec[4] = lepton->deltaEtaIn();
	vec[5] = lepton->deltaPhiIn();
	vec[6] = lepton->sigmaIEtaIEta_full5x5();
	vec[7] = lepton->hadronicOverEm();
	vec[8] = lepton->ioEmIoP();
	vec[9] = lepton->missingHits();
	vec[10] = lepton->neutralHadronIso(3);
	vec[11] = lepton->photonIso(3);
}

void FillMuonParams(const TRootMuon* lepton, double vec[]) {
	vec[0] = lepton->Pt();
	vec[1] = lepton->Eta();
	vec[2] = lepton->Phi();
	vec[3] = lepton->chi2();
	vec[4] = lepton->nofTrackerLayersWithMeasurement();
	vec[5] = lepton->nofValidMuHits();
	vec[6] = lepton->d0();
	vec[7] = lepton->dz();
	vec[8] = lepton->nofValidPixelHits();
	vec[9] = lepton->nofMatchedStations();
	vec[10] = lepton->chargedHadronIso(4);
	vec[11] = lepton->neutralHadronIso(4);
	vec[12] = lepton->photonIso(4);
	vec[13] = lepton->puChargedHadronIso(4);
}
