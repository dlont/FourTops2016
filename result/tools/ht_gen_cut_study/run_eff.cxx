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
	auto hGenJetMult = new TH1D("hGenJetMult",";N gen jets", 10, 0., 10.);
	auto hLeptonPt = new TH1D("hLeptonPt","Lepton pT;gen lepton pT;", 300, 0., 300.);
	auto hLeptonPtHT500 = new TH1D("hLeptonPtHT500","Lepton pT, HT>500;gen lepton pT;", 300, 0., 300.); hLeptonPtHT500->SetLineColor(kRed);
	auto hLeptonPtVSReco = new TH2D("hLeptonPtVSReco","Lepton pT;gen lepton pT;reco lepton pT", 30, 0., 30.,100,0.,100.);
	auto hJetSumEt = new TH1D("hJetSumEt","Sum of jets ET", 35, 0., 3500.);
	auto hJetSumEtinEtaRange = new TH1D("hJetSumEtinEtaRange","gen HT(pT>30,|#eta|<2.4);gen HT (GeV);#frac{1}{N}dN/dHT", 35, 0., 3500.);
	//const auto fileNameTT = "Craneen_TTJets_powheg_central_Run2_TopTree_Study_XYZ.root";
	//const auto fileNameTT = "output/Craneens_Mu/Craneens5_3_2018/Craneen_TTJets_powheg_central_Run2_TopTree_Study_XYZ.root";
	//const auto fileNameTT = "output/Craneens_Mu/Craneens6_3_2018/Craneen_TTJets_powheg_central_Run2_TopTree_Study_XYZ.root";
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

    		for (auto jet: jetsTT) {
			hJetEt->Fill(jet.Pt());
			//sum jet ET here
                        JetSumEt += jet.Pt();
			if (abs(jet.Eta()) < 2.4 && jet.Pt()>30) {
				nGenJets++;
				JetSumEtinEtaRange += jet.Pt();
			}

    		}
		//fill new histogram with sum jet ET here
		hGenJetMult->Fill(nGenJets);
		if (nGenJets>7) {
			hJetSumEt->Fill(JetSumEt);
			hJetSumEtinEtaRange->Fill(JetSumEtinEtaRange);
		}
		if (leptonsTT.GetSize()==1 && JetSumEtinEtaRange>500) hLeptonPtHT500->Fill(leptonsTT[0].Pt());
		//cout << JetSumEtinEtaRange << endl;
  	}

	TTreeReader eventTT_cran("Craneen__Mu",fileTT);
	TTreeReaderArray<TLorentzVector> leptonsTT_cran(eventTT_cran, "genLeptons");
	TTreeReaderValue<Double_t> LeptonPtTT_cran(eventTT_cran, "LeptonPt");
	while( eventTT_cran.Next() ) {
		if ( leptonsTT_cran.GetSize()==1 ) hLeptonPtVSReco->Fill(leptonsTT_cran[0].Pt(), *LeptonPtTT_cran);
	}
 
	auto c = new TCanvas("CMS_Eff1","CMS",5,45,1000,500);
	c->Divide(2,1);
	c->cd(1); gPad->SetLogy();
	hJetSumEtinEtaRange->Scale(1./hJetSumEtinEtaRange->Integral());
	hJetSumEtinEtaRange->Draw();
	c->cd(2); gPad->SetGrid();
	auto hJetSumEtinEtaRange_CDF = getCDF(hJetSumEtinEtaRange);
	hJetSumEtinEtaRange_CDF->SetTitle("gen HT(pT>30,|#eta|<2.4);gen HT (GeV);CDF");
	hJetSumEtinEtaRange_CDF->Draw("hist text");
	for (auto ext: {".png", ".pdf"}) c->SaveAs(ext);
	auto c1 = new TCanvas("CMS_Eff2","CMS",5,45,1000,500);
	c1->Divide(2,1);
	c1->cd(1); gPad->SetLogy();
	hGenJetMult->Scale(1./hGenJetMult->Integral());
	hGenJetMult->Draw();
	c1->cd(2); gPad->SetGrid();
	auto hGenJetMult_CDF = getCDF(hGenJetMult);
	hGenJetMult_CDF->SetTitle("jet pT>30,|#eta|<2.4;n gen jets;CDF");
	hGenJetMult_CDF->Draw("hist text");
	for (auto ext: {".png", ".pdf"}) c1->SaveAs(ext);
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
