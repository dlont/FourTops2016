{
	auto inputfile = "MVA_comparison.root";
	auto f = TFile::Open(inputfile, "OPEN");

	vector<string> MVAs = {
		"BDT13TEV2016", "BDT13TEV2015"
	};

	map<string,EColor> colors = {
		{"BDT13TEV2016",kGreen},{"BDT13TEV2015",kBlue}
	};

	map<string,TH1*> MVA_hists;
	for (auto&& item: MVAs) {
		for (auto&& treename: {"TreeS", "TreeB"}) {
			auto hist_name = TString::Format("hist_%s_%s",item.c_str(), treename);
			auto hist = static_cast<TH1F*>(f->Get(hist_name)); 
			if (!hist) {cerr<<"No "<<hist_name<<endl; exit(1);}
			MVA_hists[item+treename] = hist;
		}
	}

	map<string,TGraph*> MVA_roc;
	for (auto&& item: MVAs) {
		auto grROC  = new TGraph();
		double esp_sig, esp_bg;
		const int nBins = MVA_hists.find(item+"TreeS")->second->GetNbinsX();
		auto hs = MVA_hists.find(item+"TreeS")->second;
		auto hb = MVA_hists.find(item+"TreeB")->second;
		for (int iBin = 1; iBin < nBins; iBin++) {
			esp_sig = (hs->Integral(iBin,nBins)/hs->Integral(1,nBins));
			esp_bg = (hb->Integral(iBin,nBins)/hb->Integral(1,nBins));
			grROC->SetPoint(iBin-1,esp_sig,1.-esp_bg);
		}
		MVA_roc[item]=grROC;
		grROC->SetLineColor(colors[item]);
	}


	TMultiGraph *mg = new TMultiGraph();
	for (auto&& item: MVA_roc) mg->Add(item.second);
	mg->Draw("AC");	
	mg->GetXaxis()->SetTitle("Signal efficiency"); 
	mg->GetYaxis()->SetTitle("Background rejection");

	gPad->SetGridx(); gPad->SetGridy();
	TLegend *leg = new TLegend(0.75,0.75,0.89,0.899);
	for (auto&& item: MVA_roc) leg->AddEntry(item.second,item.first.c_str(),"l");
	leg->Draw();
}

