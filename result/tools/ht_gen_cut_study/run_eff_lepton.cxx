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

int run_eff() {

	gStyle->SetOptStat(0);
	gStyle->SetPaintTextFormat("3.2f");

	auto hJetEt = make_shared<TH1D>("hJetEt","jet ET", 10, 0., 1000.);
	//make new histogram for sum jet ET HERE
	auto hLeptonPt = new TH1D("hLeptonPt","Lepton pT;gen lepton pT;", 300, 0., 300.);
	const auto fileNameTT = "output/Craneens_Mu/Craneens8_3_2018/Craneen_TTJets_powheg_central_Run2_TopTree_Study_XYZ.root";
	const auto fileTT = TFile::Open(fileNameTT,"READ");
	TTreeReader eventTT("bookkeeping",fileTT);
	TTreeReaderArray<TLorentzVector> jetsTT(eventTT, "genJets");
	TTreeReaderArray<TLorentzVector> leptonsTT(eventTT, "genLeptons");

        TCutG *cutg = new TCutG("myhtcut",4);
	cutg->SetPoint(0,400.,-100000.);
	cutg->SetPoint(1,400.,100000.);
	cutg->SetPoint(2,50000.,-100000.);
	cutg->SetPoint(3,50000.,100000.);

	auto ev_id = 0;
	while (eventTT.Next()) {
		//event selection

		double JetSumEt = 0.;
		double JetSumEtinEtaRange = 0;
		int nGenJets = 0;

		if (leptonsTT.GetSize()==1) hLeptonPt->Fill(leptonsTT[0].Pt());

  	}

	auto c2 = new TCanvas("CMS_Eff3","CMS",5,45,1000,500);
	c2->Divide(2,1);
	c2->cd(1); gPad->SetLogy(); 
	hLeptonPt->Scale(1./hLeptonPt->Integral());
	hLeptonPt->Draw();
	hLeptonPtHT500->Scale(1./hLeptonPtHT500->Integral());
	hLeptonPtHT500->Draw("same");
	//auto leg = gPad->BuildLegend(0.5,0.12,0.89,0.5); leg->Draw();
	auto leg = gPad->BuildLegend(0.5,0.7,0.89,0.89); leg->Draw();
	c2->cd(2); gPad->SetGrid();
	auto hLeptonPt_CDF = getCDF(hLeptonPt);
	hLeptonPt_CDF->SetTitle(";gen lepton pT;CDF");
	hLeptonPt_CDF->Draw("hist");
	auto hLeptonPtHT500_CDF = getCDF(hLeptonPtHT500);
	hLeptonPtHT500_CDF->SetTitle(";gen lepton pT;CDF");
	hLeptonPtHT500_CDF->Draw("hist same");
	//c2->cd(3); gPad->SetGrid();
	//hLeptonPtVSReco->Draw("box text");
	for (auto ext: {".png", ".pdf"}) c2->SaveAs(ext);


	return 0;
}
