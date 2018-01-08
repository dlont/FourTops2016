{
	gStyle->SetOptStat(0);
	gStyle->SetOptTitle(0);
	
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

	map<string,pair<TH1*,TH1*>> map_bdthist;
	map<string,TGraph*> MVA_rej;
	map<string,TGraph*> MVA_eff;
	map<string,TGraph*> MVA_roc;
	for (auto&& item: MVAs) {
		auto gr_roc  = new TGraph();
		auto gr_eff = new TGraph();
		auto gr_rej = new TGraph();
		const int nBins = MVA_hists.find(item+"TreeS")->second->GetNbinsX();
		auto hs = MVA_hists.find(item+"TreeS")->second;
		auto hb = MVA_hists.find(item+"TreeB")->second;
		const double xmax = hs -> GetXaxis() -> GetXmax();
		const double xmin = hs -> GetXaxis() -> GetXmin();

		auto hb_name = TString::Format("%s_norm",hb->GetName());
		auto hb_norm = new TH1F(hb_name, TString::Format("%s;Normalized output;Number of events",item.c_str()),nBins,-1.,1.);
		auto hs_name = TString::Format("%s_norm",hs->GetName());
		auto hs_norm = new TH1F(hs_name, TString::Format("%s;Normalized output;Number of events",item.c_str()),nBins,-1.,1.);
		for (int iBin = 1; iBin < nBins; iBin++) {
			hb_norm->SetBinContent(iBin, hb->GetBinContent(iBin));
			hs_norm->SetBinContent(iBin, hs->GetBinContent(iBin));
			double bdt_normalized =  ( hs -> GetXaxis() -> GetBinCenter(iBin) - xmin ) / (xmax - xmin);
			double esp_sig = (hs->Integral(iBin,nBins)/hs->Integral(1,nBins));
			double esp_bg = (hb->Integral(iBin,nBins)/hb->Integral(1,nBins));
			gr_eff -> SetPoint( iBin-1, bdt_normalized, esp_sig );
			gr_rej -> SetPoint( iBin-1, bdt_normalized, 1.-esp_bg );
			gr_roc->SetPoint(iBin-1,esp_sig,1.-esp_bg);
		}
		gr_roc->SetLineColor(colors[item]);
		gr_eff->SetLineColor(colors[item]);
		gr_rej->SetLineColor(colors[item]);
		gr_rej->SetLineStyle(2);
		MVA_roc[item]=gr_roc;
		MVA_eff[item]=gr_eff;
		MVA_rej[item]=gr_rej;

		hs_norm->SetFillColor(colors[item]);
		hs_norm->SetFillStyle(3005);
		hb_norm->SetFillColor(colors[item]);
		hb_norm->SetFillStyle(3004);
		hs_norm->Scale(1./hs_norm->Integral());
		hb_norm->Scale(1./hb_norm->Integral());
		map_bdthist[item]=make_pair(hb_norm,hs_norm);
	}

	auto a = new TCanvas("mva_norm_plots","Normalised MVA distributions",5,45,500,500);
	a->SetLogy();
	for(auto&& item: map_bdthist) {
		item.second.first->Draw("hist same");
		item.second.second->Draw("hist same");
	}
	auto leg_a = a->BuildLegend(0.75,0.65,0.95,0.89);

	auto c = new TCanvas("c_perf","MVA performance",5,45,1000,500);
	c->Divide(2,1);

	c->cd(1);
	TMultiGraph *mg = new TMultiGraph();
	for (auto&& item: MVA_rej) mg->Add(item.second);
	for (auto&& item: MVA_eff) mg->Add(item.second);
	mg->Draw("AC");	
	mg->GetXaxis()->SetTitle("Normalised MVA response"); 
	mg->GetYaxis()->SetTitle("Singnal efficiency");
	TText* t = new TText( 0.95, 0.54, "Background rejection" );
	t->SetNDC();
	t->SetTextFont(42);
	t->SetTextSize( 0.040 );
	t->SetTextAngle( 90 );
	t->AppendPad();

	gPad->SetGridx(); gPad->SetGridy();
	TLegend *leg = new TLegend(0.65,0.65,0.85,0.85);
	leg->SetBorderSize(0);
	for (auto&& item: MVA_eff) leg->AddEntry(item.second,TString(item.first.c_str())+" efficiency","l");
	for (auto&& item: MVA_rej) leg->AddEntry(item.second,TString(item.first.c_str())+" rejection","l");
	leg->Draw();

	c->cd(2);
	TMultiGraph *mg_roc = new TMultiGraph();
	for (auto&& item: MVA_roc) mg_roc->Add(item.second);
	mg_roc->Draw("AC");	
	mg_roc->GetXaxis()->SetTitle("Signal efficiency"); 
	mg_roc->GetYaxis()->SetTitle("Background rejection");

	gPad->SetGridx(); gPad->SetGridy();
	TLegend *leg_roc = new TLegend(0.25,0.25,0.59,0.59);
	leg_roc->SetBorderSize(0);
	for (auto&& item: MVA_roc) leg_roc->AddEntry(item.second,item.first.c_str(),"l");
	leg_roc->Draw();
}

