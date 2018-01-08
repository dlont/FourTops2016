{
	auto outfilename = "MVA_comparison.root";

	//auto treename = "TreeS";
	auto treename = "TreeB";
	auto training_input = "train_samples.root";
	auto file = TFile::Open(training_input, "OPEN");

	map<string,string> MVAs = {
		{"BDT13TEV2016","/user/dlontkov/t2016/MVA/weights_13TeV_new/JetCombTrainer_BDT.weights.xml"},
		{"BDT13TEV2015","/user/dlontkov/t2016/MVA/weights_13TeV/JetCombTrainer_BDT.weights.xml"}
	};

	map<string,TH1*> MVA_hists;
	for (auto item: MVAs) {
		auto hist_name = TString::Format("hist_%s_%s",item.first.c_str(), treename);
		MVA_hists[item.first] = new TH1F(hist_name.Data(), "classifier output", 100, -1., 1.);
	}

	const int nVars = 6; 
	array<Double_t, nVars> dvar;
	array<Float_t, nVars> var;
	auto *tr = static_cast<TTree*>(file->Get(treename));
	tr->SetBranchAddress("btag", 				&dvar[0]);
	tr->SetBranchAddress("ThPtOverSumPt", 			&dvar[1]);
	tr->SetBranchAddress("AngleThWh", 			&dvar[2]);
	tr->SetBranchAddress("AngleThBh", 			&dvar[3]);
	tr->SetBranchAddress("HadrWmass", 			&dvar[4]);
	tr->SetBranchAddress("TopMass", 			&dvar[5]);

	auto reader = new TMVA::Reader( "!Color:!Silent" );
	reader->AddVariable( "btag",            &var[0] );
	reader->AddVariable( "ThPtOverSumPt",   &var[1] );
	reader->AddVariable( "AngleThWh", 	&var[2] );
	reader->AddVariable( "AngleThBh",       &var[3] );
	reader->AddVariable( "HadrWmass",       &var[4] );
	reader->AddVariable( "TopMass",         &var[5] );
	for (auto item: MVAs)	reader->BookMVA( item.first.c_str(), item.second.c_str() );

	for (Long64_t ievt=0; ievt< tr->GetEntries(); ++ievt) {
		if ( ievt > 1000000 ) break ;
		copy(dvar.cbegin(), dvar.cend(), var.begin());
		if (ievt%100000 == 0) std::cout << "--- ... Processing event: " << ievt << std::endl;
		tr->GetEntry(ievt);

		for (auto item: MVAs) {
			auto disc = reader->EvaluateMVA( item.first );
			MVA_hists[item.first]->Fill( disc ); 
		}
	}

	auto outFile = TFile::Open(outfilename, "UPDATE");
	for (auto item: MVAs) MVA_hists[item.first]->Write();
	outFile->Write();
	outFile->Close();
	delete outFile;
}
