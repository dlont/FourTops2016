#include "TH1.h"
#include "TH2.h"
#include "TString.h"
#include "TStyle.h"
#include "TFile.h"
#include "TTreeReader.h"
#include "TPad.h"
#include "TCanvas.h"
#include "TCutG.h"
#include "TTreeReaderArray.h"
#include "TLorentzVector.h"
#include "TMath.h"

TH1* style(TH1* h){
	if(h->GetName()) return h;
}

TH1* getCDF(const TH1* h) {
	auto str_result_name = TString::Format("%s_%s",h->GetName(),"_CDF");
	auto result = (TH1*)h->Clone(str_result_name);
	result->Reset();
	double sum = 0.;
	for (int ibin = 1; ibin <= result->GetNbinsX()-1; ++ibin) {
		sum+=h->GetBinContent(ibin);
		result->SetBinContent(ibin+1, sum);
	}
	return result;
}

int run_eff_htVSnj() {

	gStyle->SetOptStat(0);
	gStyle->SetPaintTextFormat("3.2f");

	auto hJetEt = make_shared<TH1D>("hJetEt","jet ET", 10, 0., 1000.);
	//make new histogram for sum jet ET HERE
	auto hGenJetMult = new TH1D("hGenJetMult",";N gen jets", 20, 0., 20.);
	auto hGenHTVSGenJetMult = new TH2D("hGenHTVSGenJetMult","gen HT(pT>30,|#eta|<2.4), gen mult(pT>30);gen jet mult;gen jet HT", 5, 5.5, 10.5,30,0.,3000.);
	auto hJetSumEt = new TH1D("hJetSumEt","Sum of jets ET", 35, 0., 3500.);
	auto hJetSumEtinEtaRange = new TH1D("hJetSumEtinEtaRange","gen HT(pT>30,|#eta|<2.4);gen HT (GeV);#frac{1}{N}dN/dHT", 35, 0., 3500.);
	//const auto fileNameTT = "Craneen_TTJets_powheg_central_Run2_TopTree_Study_XYZ.root";
	//const auto fileNameTT = "output/Craneens_Mu/Craneens5_3_2018/Craneen_TTJets_powheg_central_Run2_TopTree_Study_XYZ.root";
	//const auto fileNameTT = "output/Craneens_Mu/Craneens6_3_2018/Craneen_TTJets_powheg_central_Run2_TopTree_Study_XYZ.root";
	//const auto fileNameTT = "output/Craneens_Mu/Craneens14_3_2018/Craneen_TTJets_powheg_central_Run2_TopTree_Study_XYZ.root";
	const auto fileNameTT = "output/Craneens_Mu/Craneens14_3_2018/Craneen_TTJets_powheg_central_Run2_TopTree_Study_mother24.root";
	const auto fileTT = TFile::Open(fileNameTT,"READ");
	TTreeReader eventTT("bookkeeping",fileTT);
	TTreeReaderArray<TLorentzVector> jetsTT(eventTT, "genJets");
	TTreeReaderArray<TLorentzVector> leptonsTT(eventTT, "genLeptons");

	double npassed_HTMult[5] = {0,0,0,0,0};
	double npassed_HT[5] = {0,0,0,0,0};
	double npassed_Mult[5] = {0,0,0,0,0};
	double ntotal = 0;


	auto findMatchingLepton = [&leptonsTT](const TLorentzVector& jet)
	{
		for (auto lep: leptonsTT) {
			if ( jet.DeltaR(lep)<0.1 ) {
				cout << jet.Pt() << " " << jet.Eta() << " " << jet.Phi() << endl;
				cout << lep.Pt() << " " << lep.Eta() << " " << lep.Phi() << endl;
			}
		}
	};

	auto ev_id = 0;
	while (eventTT.Next()) {
		//event selection

		ntotal+=1.;
		if ( leptonsTT.GetSize()<1 ) continue;
		//cout << leptonsTT.GetSize() << endl;
		
                double JetSumEt = 0.; 
		double JetSumEtinEtaRange = 0;
		int nGenJets = 0;
    		for (auto jet: jetsTT) {

			//findMatchingLepton(jet);
			
			hJetEt->Fill(jet.Pt());
			//sum jet ET here
                        JetSumEt += jet.Pt();
			if (jet.Pt()>30) {
				nGenJets++;
				if ( abs(jet.Eta()) < 2.4 ) {
					JetSumEtinEtaRange += jet.Pt();
				}
			}
    		}
		hGenHTVSGenJetMult->Fill(nGenJets>10?10:nGenJets,JetSumEtinEtaRange);
		//fill new histogram with sum jet ET here
		hGenJetMult->Fill(nGenJets>10?10:nGenJets);
		hJetSumEt->Fill(JetSumEt);
		hJetSumEtinEtaRange->Fill(JetSumEtinEtaRange);
		int ngenj = nGenJets>10?10:nGenJets;
		int ibin = ngenj - 6;
		if (JetSumEtinEtaRange>500) npassed_HT[0]+=1.;
		if (ibin>=0 && JetSumEtinEtaRange>500) npassed_HTMult[ibin]+=1.;
		if (ibin>=0) npassed_Mult[ibin]+=1.;
  	}

	for (int ibin=0;ibin<5;ibin++){
		for (int jbin=ibin+1;jbin<5;jbin++){
			npassed_HTMult[ibin]+=npassed_HTMult[jbin];
			npassed_Mult[ibin]+=npassed_Mult[jbin];
		}
	}
	double eff_HTMult[5] = {0.,0.,0.,0.,0.};
	double eff_Mult[5] = {0.,0.,0.,0.,0.};
	double eff_HTMult_unc[5] = {0.,0.,0.,0.,0.};
	double eff_Mult_unc[5] = {0.,0.,0.,0.,0.};
	for (int ibin=0;ibin<5;ibin++){
		double eps = npassed_HTMult[ibin]/ntotal;
		double unc = TMath::Sqrt(ntotal*eps*(1.-eps))/ntotal;
		eff_HTMult[ibin] = eps;
		eff_HTMult_unc[ibin] = unc;
		eps = npassed_Mult[ibin]/ntotal;
		unc = TMath::Sqrt(ntotal*eps*(1.-eps))/ntotal;
		eff_Mult[ibin] = eps;
		eff_Mult_unc[ibin] = unc;
	}
	cout << "HT:" << endl;
	cout << npassed_HT[0]/ntotal << "+/-" << TMath::Sqrt( ntotal*npassed_HT[0]/ntotal*(1.-npassed_HT[0]/ntotal) )/ntotal << endl;
	cout << "HTMult:" << endl;
	for (int ibin=0;ibin<5;ibin++) cout << ibin+6 << ":\t" << eff_HTMult[ibin] << "+/-" << eff_HTMult_unc[ibin] << endl;
	cout << "Mult:" << endl;
	for (int ibin=0;ibin<5;ibin++) cout << ibin+6 << ":\t" << eff_Mult[ibin] << "+/-" << eff_Mult_unc[ibin] << endl;

	auto c2d = new TCanvas("CMS_gen_HT_Mult","CMS",5,45,500,500);
	c2d->SetGrid();
	hGenHTVSGenJetMult->Draw("BOX");
	for (auto ext: {".png", ".pdf"}) c2d->SaveAs(ext);
	
	auto cMult = new TCanvas("CMS_Mult_Eff","CMS",5,45,1200,800);
	cMult->Divide(2,1);
	cMult->cd(1);
	gPad->SetGrid();
	hGenJetMult->Scale(1./hGenJetMult->Integral());
	cMult->cd(2);
	auto hGenJetMult_CDF = getCDF(hGenJetMult);
	hGenJetMult_CDF->Draw("hist text");
	for (auto ext: {".png", ".pdf"}) cMult->SaveAs(ext);
	
 
	auto c = new TCanvas("CMS_HT_Mult_Eff","CMS",5,45,1200,800);
	c->Divide(3,2);
	c->cd(1);   gPad->SetGrid();
	auto proj = hGenHTVSGenJetMult->ProjectionY("HT_6jet",1,1);
	proj->Scale(1./proj->Integral());
	auto proj_CDF = getCDF(proj);
	proj_CDF->Draw("hist text");
	proj_CDF->SetTitle("gen HT(pT>30,|#eta|<2.4), n gen jets=6;gen HT (GeV);CDF");
	c->cd(2);  gPad->SetGrid();
	proj = hGenHTVSGenJetMult->ProjectionY("HT_7jet",2,2);
	proj->Scale(1./proj->Integral());
	proj_CDF = getCDF(proj);
	proj_CDF->Draw("hist text");
	proj_CDF->SetTitle("gen HT(pT>30,|#eta|<2.4), n gen jets=7;gen HT (GeV);CDF");
	c->cd(3);  gPad->SetGrid();
	proj = hGenHTVSGenJetMult->ProjectionY("HT_8jet",3,3);
	proj->Scale(1./proj->Integral());
	proj_CDF = getCDF(proj);
	proj_CDF->Draw("hist text");
	proj_CDF->SetTitle("gen HT(pT>30,|#eta|<2.4), n gen jets=8;gen HT (GeV);CDF");
	c->cd(4);  gPad->SetGrid();
	proj = hGenHTVSGenJetMult->ProjectionY("HT_9jet",4,4);
	proj->Scale(1./proj->Integral());
	proj_CDF = getCDF(proj);
	proj_CDF->Draw("hist text");
	proj_CDF->SetTitle("gen HT(pT>30,|#eta|<2.4), n gen jets=9;gen HT (GeV);CDF");
	c->cd(5);  gPad->SetGrid();
	proj = hGenHTVSGenJetMult->ProjectionY("HT_10jet",5,5);
	proj->Scale(1./proj->Integral());
	proj_CDF = getCDF(proj);
	proj_CDF->Draw("hist text");
	proj_CDF->SetTitle("gen HT(pT>30,|#eta|<2.4), n gen jets>=10;gen HT (GeV);CDF");
	c->cd(6); gPad->SetGrid();
	hGenHTVSGenJetMult->Draw("BOX");
	for (auto ext: {".png", ".pdf"}) c->SaveAs(ext);

	return 0;
}
