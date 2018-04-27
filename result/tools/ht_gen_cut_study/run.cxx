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

TH1* style(TH1* h){
	if(h->GetName()) return h;
}

TH1* getCDF(const TH1* h) {
	auto str_result_name = TString::Format("%s_%s",h->GetName(),"_CDF");
	auto result = (TH1*)h->Clone(str_result_name);
	double sum = 0.;
	for (int ibin = 1; ibin <= result->GetNbinsX(); ++ibin) {
		sum+=result->GetBinContent(ibin);
		result->SetBinContent(ibin, sum);
	}
	return result;
}

int run() {

	gStyle->SetOptStat(0);
	gStyle->SetPaintTextFormat("3.2f");

	auto hJetEt = make_shared<TH1D>("hJetEt","jet ET", 10, 0., 1000.);
	//make new histogram for sum jet ET HERE
	auto hJetSumEtVSHT_TT = new TH2D("hJetSumEtVSHT_TT",";gen HT(|#eta|<2.4,pt>30);reco HT(|#eta|<2.4,pt>30)", 15, 0., 1500., 15, 0.,1500.);
	hJetSumEtVSHT_TT->GetYaxis()->SetTitleOffset(1.3);
	hJetSumEtVSHT_TT->SetMarkerColor(kBlue);
	hJetSumEtVSHT_TT->SetLineColor(kBlue);
	hJetSumEtVSHT_TT->SetMarkerSize(hJetSumEtVSHT_TT->GetMarkerSize()*1.2);
	auto hJetSumEtVSnJets_TT = new TH2D("hJetSumEtVSnJets_TT",";gen HT(|#eta|<2.4,pt>30);N reco jets", 15, 0., 1500., 5, 5.5, 10.5);
	hJetSumEtVSnJets_TT->GetYaxis()->SetTitleOffset(1.3);
	hJetSumEtVSnJets_TT->SetMarkerColor(kBlue);
	hJetSumEtVSnJets_TT->SetLineColor(kBlue);
	auto hJetSumEtVSBDT_TT = new TH2D("hJetSumEtVSBDT_TT",";gen HT(|#eta|<2.4,pt>30);BDT", 15, 0., 1500., 20, -1.,1.);
	hJetSumEtVSBDT_TT->GetYaxis()->SetTitleOffset(1.3);
	hJetSumEtVSBDT_TT->SetMarkerColor(kBlue);
	hJetSumEtVSBDT_TT->SetLineColor(kBlue);
	auto hJetSumEtVSHT_TTTT = new TH2D("hJetSumEtVSHT_TTTT",";gen HT(|#eta|<2.4,pt>30);reco HT(|#eta|<2.4,pt>30)", 15, 0., 1500., 15, 0.,1500.);
	hJetSumEtVSHT_TTTT->GetYaxis()->SetTitleOffset(1.3);
	hJetSumEtVSHT_TTTT->SetMarkerColor(kRed);
	hJetSumEtVSHT_TTTT->SetLineColor(kRed);
	auto hJetSumEtVSnJets_TTTT = new TH2D("hJetSumEtVSnJets_TTTT",";gen HT(|#eta|<2.4,pt>30);N reco jets", 15, 0., 1500., 5, 5.5, 10.5);
	hJetSumEtVSnJets_TTTT->GetYaxis()->SetTitleOffset(1.3);
	hJetSumEtVSnJets_TTTT->SetMarkerColor(kRed);
	hJetSumEtVSnJets_TTTT->SetLineColor(kRed);
	auto hJetSumEtVSBDT_TTTT = new TH2D("hJetSumEtVSBDT_TTTT",";gen HT(|#eta|<2.4,pt>30);N reco jets", 15, 0., 1500., 20, -1.,1.);
	hJetSumEtVSBDT_TTTT->GetYaxis()->SetTitleOffset(1.3);
	hJetSumEtVSBDT_TTTT->SetMarkerColor(kRed);
	hJetSumEtVSBDT_TTTT->SetLineColor(kRed);
	auto hJetSumEt = new TH1D("hJetSumEt","Sum of jets ET", 35, 0., 3500.);
	auto hJetSumEtinEtaRange = new TH1D("hJetSumEtinEtaRange","Sum of jets ET for |ETA| < 2.4", 35, 0., 3500.);
	auto hJetSumEtinEtaRange6TT = new TH1D("hJetSumEtinEtaRange6TT","Sum of jets(6) ET for |ETA| < 2.4 (tt);gen HT(|#eta|<2.4,pt>30);CDF", 35, 0., 3500.);
	hJetSumEtinEtaRange6TT->SetLineColor(kBlue);
	auto hJetSumEtinEtaRange7TT = new TH1D("hJetSumEtinEtaRange7TT","Sum of jets(7) ET for |ETA| < 2.4;gen HT(|#eta|<2.4,pt>30);CDF", 35, 0., 3500.);
	hJetSumEtinEtaRange7TT->SetLineColor(kBlue);
	auto hJetSumEtinEtaRange8TT = new TH1D("hJetSumEtinEtaRange8TT","Sum of jets(8) ET for |ETA| < 2.4;gen HT(|#eta|<2.4,pt>30);CDF", 35, 0., 3500.);
	hJetSumEtinEtaRange8TT->SetLineColor(kBlue);
	auto hJetSumEtinEtaRange9TT = new TH1D("hJetSumEtinEtaRange9TT","Sum of jets(9) ET for |ETA| < 2.4;gen HT(|#eta|<2.4,pt>30);CDF", 35, 0., 3500.);
	hJetSumEtinEtaRange9TT->SetLineColor(kBlue);
	auto hJetSumEtinEtaRange10TT = new TH1D("hJetSumEtinEtaRange10TT","Sum of jets(10) ET for |ETA| < 2.4;gen HT(|#eta|<2.4,pt>30);CDF", 35, 0., 3500.);
	hJetSumEtinEtaRange10TT->SetLineColor(kBlue);
	auto hJetSumEtinEtaRange6TTTT = new TH1D("hJetSumEtinEtaRange6TTTT","Sum of jets(6) ET for |ETA| < 2.4 (tttt);gen HT(|#eta|<2.4,pt>30);CDF", 35, 0., 3500.);
	hJetSumEtinEtaRange6TTTT->SetLineColor(kRed);
	auto hJetSumEtinEtaRange7TTTT = new TH1D("hJetSumEtinEtaRange7TTTT","Sum of jets(7) ET for |ETA| < 2.4;gen HT(|#eta|<2.4,pt>30);CDF", 35, 0., 3500.);
	hJetSumEtinEtaRange7TTTT->SetLineColor(kRed);
	auto hJetSumEtinEtaRange8TTTT = new TH1D("hJetSumEtinEtaRange8TTTT","Sum of jets(8) ET for |ETA| < 2.4;gen HT(|#eta|<2.4,pt>30);CDF", 35, 0., 3500.);
	hJetSumEtinEtaRange8TTTT->SetLineColor(kRed);
	auto hJetSumEtinEtaRange9TTTT = new TH1D("hJetSumEtinEtaRange9TTTT","Sum of jets(9) ET for |ETA| < 2.4;gen HT(|#eta|<2.4,pt>30);CDF", 35, 0., 3500.);
	hJetSumEtinEtaRange9TTTT->SetLineColor(kRed);
	auto hJetSumEtinEtaRange10TTTT = new TH1D("hJetSumEtinEtaRange10TTTT","Sum of jets(10) ET for |ETA| < 2.4;gen HT(|#eta|<2.4,pt>30);CDF", 35, 0., 3500.);
	hJetSumEtinEtaRange10TTTT->SetLineColor(kRed);

	auto hGenJetVSRecoJetMult_TT = new TH2D("hGenJetVSRecoJetMult_TT","Normalized nReco VS nGen jets;n gen jets;n reco jets", 5, 5.5, 10.5, 5, 5.5, 10.5);

	//const auto fileNameTT = "/user/dlontkov/t2016/result/final_unblinding/genjets_coll/plots_mu/Craneen_TTJets_powheg_mixture_Run2_TopTree_Study.root";
	const auto fileNameTT = "/storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/result/final_unblinding/genjets_genleptons_coll/Craneen_TTJets_powheg_mixture_Run2_TopTree_Study.root";
	const auto fileTT = TFile::Open(fileNameTT,"READ");
	TTreeReader eventTT("Craneen__Mu",fileTT);
	TTreeReaderArray<TLorentzVector> jetsTT(eventTT, "genJets");
	TTreeReaderArray<TLorentzVector> genLeptonsTT(eventTT, "genLeptons");
 	TTreeReaderValue<Int_t> nJetsTT(eventTT, "nJets");
 	TTreeReaderValue<Int_t> nMtagsTT(eventTT, "nMtags");
 	//TTreeReaderValue<Float_t> BDTTT(eventTT, "BDT9and10jetsplitNoNjw.BDT9and10jetsplitNoNjw");
 	TTreeReaderValue<Double_t> BDTTT(eventTT, "BDT");
 	TTreeReaderValue<Double_t> HTTT(eventTT, "HT");
 	TTreeReaderValue<Double_t> metTT(eventTT, "met");
 	TTreeReaderValue<Double_t> leptonIsoTT(eventTT, "leptonIso");
 	TTreeReaderValue<Double_t> LeptonPtTT(eventTT, "LeptonPt");
 	TTreeReaderValue<Double_t> LeptonEtaTT(eventTT, "LeptonEta");
        TTreeReaderValue<Int_t> HLT_IsoMu24TT(eventTT, "HLT_IsoMu24");
        TTreeReaderValue<Int_t> HLT_IsoTkMu24TT(eventTT, "HLT_IsoTkMu24");

	const auto fileNameTTTT = "/user/dlontkov/t2016/result/final_unblinding/genjets_coll/plots_mu/Craneen_ttttNLO_Run2_TopTree_Study.root";
	const auto fileTTTT = TFile::Open(fileNameTTTT,"READ");
	TTreeReader eventTTTT("Craneen__Mu",fileTTTT);
	TTreeReaderArray<TLorentzVector> jetsTTTT(eventTTTT, "genJets");
 	TTreeReaderValue<Int_t> nJetsTTTT(eventTTTT, "nJets");
 	TTreeReaderValue<Int_t> nMtagsTTTT(eventTTTT, "nMtags");
 	TTreeReaderValue<Float_t> BDTTTTT(eventTTTT, "BDT9and10jetsplitNoNjw.BDT9and10jetsplitNoNjw");
 	TTreeReaderValue<Double_t> HTTTTT(eventTTTT, "HT");
 	TTreeReaderValue<Double_t> metTTTT(eventTTTT, "met");
 	TTreeReaderValue<Double_t> leptonIsoTTTT(eventTTTT, "leptonIso");
 	TTreeReaderValue<Double_t> LeptonPtTTTT(eventTTTT, "LeptonPt");
 	TTreeReaderValue<Double_t> LeptonEtaTTTT(eventTTTT, "LeptonEta");
        TTreeReaderValue<Int_t> HLT_IsoMu24TTTT(eventTTTT, "HLT_IsoMu24");
        TTreeReaderValue<Int_t> HLT_IsoTkMu24TTTT(eventTTTT, "HLT_IsoTkMu24");

        TCutG *cutg = new TCutG("myhtcut",4);
	cutg->SetPoint(0,500.,-100000.);
	cutg->SetPoint(1,500.,100000.);
	cutg->SetPoint(2,50000.,-100000.);
	cutg->SetPoint(3,50000.,100000.);

	map<double,double> bias_total{{6,0},{7,0},{8,0},{9,0},{10,0}};
	map<double,double> bias_HT{{6,0},{7,0},{8,0},{9,0},{10,0}};
	map<double,double> bias_Mult8{{6,0},{7,0},{8,0},{9,0},{10,0}};
	map<double,double> bias_HTMult8{{6,0},{7,0},{8,0},{9,0},{10,0}};

	const char* denom_str = "N(N_{j}=8)";

	const int nGenJetsCut = 9;
	const int nGenLeptonsCut = 1;

	while (eventTT.Next()) {
		//event selection
		if (!(*HLT_IsoMu24TT==1 || *HLT_IsoTkMu24TT==1)) continue;
		if (!(fabs(*LeptonEtaTT)<2.1 && *leptonIsoTT<0.15)) continue;
		if (!(*metTT>50)) continue;
		if (!(*HTTT>500)) continue;
		if (!(*nMtagsTT>=2)) continue;
		//if (!((*nJetsTT)==8)) continue;

                double JetSumEt = 0.; 
		double JetSumEtinEtaRange = 0;
		double JetSumEtinEtaRange6 = 0;
		double JetSumEtinEtaRange7 = 0;
		double JetSumEtinEtaRange8 = 0;
		double JetSumEtinEtaRange9 = 0;
		double JetSumEtinEtaRange10 = 0;
		int nGenJets = 0;
		int nGenLeptons = genLeptonsTT.GetSize();
    		for (auto jet: jetsTT) {
			hJetEt->Fill(jet.Pt());
			//sum jet ET here
                        JetSumEt += jet.Pt();
			if ( jet.Pt()>30 ) {
				nGenJets++;
			}
			if (abs(jet.Eta()) < 2.4 && jet.Pt()>30) {
				JetSumEtinEtaRange += jet.Pt();
				if (*nJetsTT == 6) {JetSumEtinEtaRange6 += jet.Pt(); }
				if (*nJetsTT == 7) {JetSumEtinEtaRange7 += jet.Pt(); }
				if (*nJetsTT == 8) {JetSumEtinEtaRange8 += jet.Pt(); }
				if (*nJetsTT == 9) {JetSumEtinEtaRange9 += jet.Pt(); }
				if (*nJetsTT >= 10 ) {JetSumEtinEtaRange10 += jet.Pt(); }
			}

    		}
		if (*nJetsTT == 6)   { 
			bias_total[6]+=1.;
			if ( !(nGenJets>=nGenJetsCut && nGenLeptons==nGenLeptonsCut) ) bias_Mult8[6]+=1.;
			if ( !(JetSumEtinEtaRange>500 && nGenLeptons==nGenLeptonsCut) ) bias_HT[6]+=1.;
			if ( !(nGenJets>=nGenJetsCut && JetSumEtinEtaRange>500 && nGenLeptons==nGenLeptonsCut) ) bias_HTMult8[6]+=1.;
		}
		if (*nJetsTT == 7)   { 
			bias_total[7]+=1.;
			if ( !(nGenJets>=nGenJetsCut && nGenLeptons==nGenLeptonsCut) ) bias_Mult8[7]+=1.;
			if ( !(JetSumEtinEtaRange>500 && nGenLeptons==nGenLeptonsCut) ) bias_HT[7]+=1.;
			if ( !(nGenJets>=nGenJetsCut && JetSumEtinEtaRange>500 && nGenLeptons==nGenLeptonsCut) ) bias_HTMult8[7]+=1.;
		}
		if (*nJetsTT == 8)   { 
			bias_total[8]+=1.;
			if ( !(nGenJets>=nGenJetsCut && nGenLeptons==nGenLeptonsCut ) ) bias_Mult8[8]+=1.;
			if ( !(JetSumEtinEtaRange>500 && nGenLeptons==nGenLeptonsCut ) ) bias_HT[8]+=1.;
			if ( !(nGenJets>=nGenJetsCut && JetSumEtinEtaRange>500 && nGenLeptons==nGenLeptonsCut ) ) bias_HTMult8[8]+=1.;
		}
		if (*nJetsTT == 9)   { 
			bias_total[9]+=1.;
			if ( !(nGenJets>=nGenJetsCut && nGenLeptons>=nGenLeptonsCut ) ) bias_Mult8[9]+=1.;
			if ( !(JetSumEtinEtaRange>500 && nGenLeptons>=nGenLeptonsCut ) ) bias_HT[9]+=1.;
			if ( !(nGenJets>=nGenJetsCut && JetSumEtinEtaRange>500 && nGenLeptons==nGenLeptonsCut ) ) bias_HTMult8[9]+=1.;
		}
		if (*nJetsTT >= 10 ) { 
			bias_total[10]+=1.;
			if ( !(nGenJets>=nGenJetsCut && nGenLeptons>=nGenLeptonsCut ) ) bias_Mult8[10]+=1.;
			if ( !(JetSumEtinEtaRange>500 && nGenLeptons>=nGenLeptonsCut ) ) bias_HT[10]+=1.;
			if ( !(nGenJets>=nGenJetsCut && JetSumEtinEtaRange>500 && nGenLeptons==nGenLeptonsCut ) ) bias_HTMult8[10]+=1.;
		}
		hGenJetVSRecoJetMult_TT->Fill(nGenJets<10?nGenJets:10,*nJetsTT<10?*nJetsTT:10);
		hJetSumEtVSHT_TT->Fill(JetSumEtinEtaRange,*HTTT);
		//hJetSumEtVSHT_TT->Fill(JetSumEt,*HTTT);
		hJetSumEtVSnJets_TT->Fill(JetSumEtinEtaRange,*nJetsTT);
		//hJetSumEtVSnJets_TT->Fill(JetSumEt,*nJetsTT);
		if (nGenJets>=8) hJetSumEtVSBDT_TT->Fill(JetSumEtinEtaRange,*BDTTT);
		//fill new histogram with sum jet ET here
		hJetSumEt->Fill(JetSumEt);
		hJetSumEtinEtaRange->Fill(JetSumEtinEtaRange);
		if (*nJetsTT == 6) {hJetSumEtinEtaRange6TT->Fill(JetSumEtinEtaRange6);}
		if (*nJetsTT == 7) {hJetSumEtinEtaRange7TT->Fill(JetSumEtinEtaRange7);}
		if (*nJetsTT == 8) {hJetSumEtinEtaRange8TT->Fill(JetSumEtinEtaRange8);}
		if (*nJetsTT == 9) {hJetSumEtinEtaRange9TT->Fill(JetSumEtinEtaRange9);}
		if (*nJetsTT >= 10) {hJetSumEtinEtaRange10TT->Fill(JetSumEtinEtaRange10);}
  	}
	cout << "Acceptance bias" << endl;
	for (int ibin: {6,7,8,9,10}) {
		bias_Mult8[ibin] = bias_Mult8[ibin]/bias_total[ibin];
		bias_HT[ibin] = bias_HT[ibin]/bias_total[ibin];
		bias_HTMult8[ibin] = bias_HTMult8[ibin]/bias_total[ibin];
	}
	cout << "HT bias" << endl;
	auto printBias = [](map<double,double>& m) { 
		cout << "8:\t" << m[8] << endl;
		cout << "9:\t" << m[9] << endl;
		cout << "10:\t" << m[10] << endl;
	};
	printBias(bias_HT);
	cout << "Mult bias" << endl;
	printBias(bias_Mult8);
	cout << "Mult && HT bias" << endl;
	printBias(bias_HTMult8);
 
	auto c = new TCanvas("CMS1");
	c->Divide(3,1);
	c->cd(1);
	hJetEt->Draw();
	c->cd(2);
	hJetSumEt->Draw();
	c->cd(3);
	hJetSumEtinEtaRange->Draw();
	//Draw new histogram instead of old here
	for (auto ext: {".png", ".pdf"}) c->SaveAs(ext);

	//auto d = new TCanvas("CMS2");
	//d->Divide(3,2);
	//d->cd(1);
	//gPad->SetGrid();
	//hJetSumEtinEtaRange6TT->Scale(1./hJetSumEtinEtaRange6TT->Integral());
	//getCDF( hJetSumEtinEtaRange6TT )->Draw();
	//hJetSumEtinEtaRange6TTTT->Scale(1./hJetSumEtinEtaRange6TTTT->Integral());
	////getCDF( hJetSumEtinEtaRange6TTTT )->Draw("same");
	//auto leg = gPad->BuildLegend(0.3,0.2,0.8,0.4);
	//leg->Draw();
	//d->cd(2);
	//gPad->SetGrid();
	//hJetSumEtinEtaRange7TT->Scale(1./hJetSumEtinEtaRange7TT->Integral());
	//getCDF( hJetSumEtinEtaRange7TT )->Draw();
	//hJetSumEtinEtaRange7TTTT->Scale(1./hJetSumEtinEtaRange7TTTT->Integral());
	////getCDF( hJetSumEtinEtaRange7TTTT )->Draw("same");
	//d->cd(3);
	//gPad->SetGrid();
	//hJetSumEtinEtaRange8TT->Scale(1./hJetSumEtinEtaRange8TT->Integral());
	//getCDF( hJetSumEtinEtaRange8TT )->Draw();
	//hJetSumEtinEtaRange8TTTT->Scale(1./hJetSumEtinEtaRange8TTTT->Integral());
	////getCDF( hJetSumEtinEtaRange8TTTT )->Draw("same");
	//d->cd(4);
	//gPad->SetGrid();
	//hJetSumEtinEtaRange9TT->Scale(1./hJetSumEtinEtaRange9TT->Integral());
	//getCDF( hJetSumEtinEtaRange9TT )->Draw();
	//hJetSumEtinEtaRange9TTTT->Scale(1./hJetSumEtinEtaRange9TTTT->Integral());
	////getCDF( hJetSumEtinEtaRange9TTTT )->Draw("same");
	//d->cd(5);
	//gPad->SetGrid();
	//hJetSumEtinEtaRange10TT->Scale(1./hJetSumEtinEtaRange10TT->Integral());
	//getCDF( hJetSumEtinEtaRange10TT )->Draw();
	//hJetSumEtinEtaRange10TTTT->Scale(1./hJetSumEtinEtaRange10TTTT->Integral());
	////getCDF( hJetSumEtinEtaRange10TTTT )->Draw("same");
	//d->cd(6);
	//gPad->SetGrid();
	//hJetSumEtVSnJets_TT->Scale(1./hJetSumEtVSnJets_TT->Integral());
	//hJetSumEtVSnJets_TT->Draw("BOX");
	//hJetSumEtVSnJets_TTTT->Scale(1./hJetSumEtVSnJets_TTTT->Integral());
	////hJetSumEtVSnJets_TTTT->Draw("BOX same");
	////Draw new histogram instead of old here
	//for (auto ext: {".png", ".pdf"}) d->SaveAs(ext);

	auto e = new TCanvas("CMS3","CMS",5,45,1200,600);
	e->Divide(2,1);
	e->SetFillStyle(4000); gPad->SetPad(0.,0.,1.,1.); gPad->SetRightMargin(0.5); gPad->SetFrameFillColor(0);
	e->cd(1);gPad->SetFillStyle(4000); gPad->SetFrameFillColor(0);
	gPad->SetGrid();
	hJetSumEtVSHT_TT->Scale(1./hJetSumEtVSHT_TT->Integral());
	hJetSumEtVSHT_TT->SetFillStyle(4000);
	hJetSumEtVSHT_TT->Draw("BOX");
	hJetSumEtVSHT_TTTT->Scale(1./hJetSumEtVSHT_TTTT->Integral());
	//hJetSumEtVSHT_TTTT->Draw("BOX same");
	e->cd(2);gPad->SetFillStyle(4000); gPad->SetPad(0.,0.,1.,1.); gPad->SetLeftMargin(0.6); gPad->SetRightMargin(0.05); gPad->SetFrameFillColor(0);
	gPad->SetGrid();
	auto newName = TString::Format("%s_%s",hJetSumEtVSHT_TT->GetName(),"TEXT");
	auto hJetSumEtVSHT_TT_TEXT = (TH2*)hJetSumEtVSHT_TT->Clone(newName);
	//hJetSumEtVSHT_TT_TEXT->Scale(100);
	auto HTproj_aftercut = hJetSumEtVSHT_TT_TEXT->ProjectionY("HT_aftercut_py",0,-1,"[-myhtcut]");
	HTproj_aftercut->Draw();
	HTproj_aftercut->GetYaxis()->SetTitle(TString::Format("#frac{1}{%s}dN/dHT",denom_str));
	HTproj_aftercut->GetYaxis()->SetTitleOffset(1.1);
	
	for (auto ext: {".png", ".pdf"}) e->SaveAs(ext);

	auto e1 = new TCanvas("CMS4","CMS",5,45,1200,600);
	e1->Divide(2,1);
	e1->cd(1); gPad->SetFillStyle(4000);  
	gPad->SetGrid();
	hJetSumEtVSBDT_TT->Scale(1./hJetSumEtVSBDT_TT->Integral());
	hJetSumEtVSBDT_TT->Draw("BOX");
	hJetSumEtVSBDT_TTTT->Scale(1./hJetSumEtVSBDT_TTTT->Integral());
	//hJetSumEtVSBDT_TTTT->Draw("BOX same");
	e1->cd(2);gPad->SetFillStyle(4000); gPad->SetPad(0.,0.,1.,1.); gPad->SetLeftMargin(0.6); gPad->SetRightMargin(0.05); gPad->SetFrameFillColor(0);
	gPad->SetGrid();
	newName = TString::Format("%s_%s",hJetSumEtVSBDT_TT->GetName(),"TEXT");
	auto hJetSumEtVSBDT_TT_TEXT = (TH2*)hJetSumEtVSBDT_TT->Clone(newName);
	//hJetSumEtVSBDT_TT_TEXT->Scale(100);
	auto BDTproj_aftercut = hJetSumEtVSBDT_TT_TEXT->ProjectionY("BDT_aftercut_py",0,-1,"[-myhtcut]");
	BDTproj_aftercut->Draw();
	BDTproj_aftercut->GetYaxis()->SetTitle(TString::Format("#frac{1}{%s}dN/dBDT",denom_str));
	BDTproj_aftercut->GetYaxis()->SetTitleOffset(1.1);
	for (auto ext: {".png", ".pdf"}) e1->SaveAs(ext);

	auto e2 = new TCanvas("CMS5","CMS",5,45,600,600);
	gPad->SetGrid();
	//hGenJetVSRecoJetMult_TT->Scale(1./hGenJetVSRecoJetMult_TT->Integral()); 
	hGenJetVSRecoJetMult_TT->Draw("box text");
	for (auto ext: {".png", ".pdf"}) e2->SaveAs(ext);
	

	return 0;
}
