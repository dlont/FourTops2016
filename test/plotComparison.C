//________________________________________________________________________________
TObjArray* commonSubset(  TObjArray* arr1,  TObjArray* arr2 ) {
//
// Compare two TObjArrays and find their common elements
// Return sorted TObjArray filled with elements present in both arrays
//

	TObjArray* result = new TObjArray;	// output array
	
	// sort both input arrays
        arr1->SetOwner(kFALSE);
        arr1->Sort();

        arr2->SetOwner(kFALSE);
        arr2->Sort();

	// Find arrays intersection

	unsigned int iArr1 = 0;
	unsigned int iArr2 = 0;
	while ( iArr1 < arr1->GetEntries()  &&  iArr2 < arr2->GetEntries() ) {
		if ( strcmp( arr1->At(iArr1)->GetName(), arr2->At(iArr2)->GetName() ) == 0 )	{	// lexicographic comparison
			result->AddLast( arr1->At(iArr1) );
			++iArr1;
			++iArr2;
		} else if ( strcmp( arr1->At(iArr1)->GetName(), arr2->At(iArr2)->GetName() ) > 0 ) ++iArr2;	// lexicographic comparison
		else ++iArr1;
	}

	return result;
}





//________________________________________________________________________________
void plotComparison( TString fileName, TString fileNameRef, TString treeName )
{
	gROOT->Reset();
	gROOT->SetStyle("Plain");
	gStyle->SetOptStat(0);
	gStyle->SetOptTitle(0);
	TH1::SetDefaultSumw2();

	// Number of subpads on canvas
	const int nPlotsX = 3;
	const int nPlotsY = 2;
	const int nPlotsPerCanvas = nPlotsX*nPlotsY;

	// Normalised plots comparison
	bool isNorm = true;

	// Distributions ratio switch
	bool hasRatioPanel = true;

	// Logarithmic scale switch
	bool isLogY = false;
	bool isLogX = false;

	// Output format
	const char* fmt = ".pdf";

	// Prefix of the output filename
	TString prefix = fileName;
	prefix.ReplaceAll(".root", "_");

	// Legend captions
	const char* histLegend = "new";
	const char* histRefLegend = "old";

	// Read files
	TFile *_file0 = TFile::Open( fileName.Data() );
	if ( !_file0 ) {
		cout << "Can't read file: " << fileName.Data() << endl;
		cout << "ABORTING" << endl;
		return;
	}
	TFile *_file1 = TFile::Open( fileNameRef.Data() );
	if ( !_file1 ) {
		cout << "Can't read file: " << fileNameRef.Data() << endl;
		cout << "ABORTING" << endl;
		return;
	}

	// Read trees
	TTree *t = (TTree*)_file0->Get( treeName );
	if (!t) 
	{
		cerr << "Tree " << treeName.Data() << " does not exist in " << fileName.Data() << endl;
		cerr << "ABORTING!" << endl;
	}

	TTree *tRef = (TTree*)_file1->Get( treeName );
	if (!tRef) 
	{
		cerr << "Tree " << treeName.Data() << " does not exist in " << fileName.Data() << endl;
		cerr << "ABORTING!" << endl;
	}

	// Read branch names in to arrays
	TObjArray *arrBranches = (TObjArray*)t->GetListOfBranches()->Clone();
	TObjArray *arrBranchesRef = (TObjArray*)tRef->GetListOfBranches()->Clone();

	// Find common branches present in both trees
	TObjArray *mycopy = commonSubset( arrBranches, arrBranchesRef );

	TCanvas *c;
 	TPad *aPad;

	// Superimpose histograms from different files
	// Loop over branches names
	for(int i = 0; i < 6; ++i) { 	// testing
	//for(int i = 0; i < mycopy->GetEntries(); ++i) { //full set of histograms

		// Create new canvas
		if ( i%nPlotsPerCanvas == 0 ) {
			c = new TCanvas(TString::Format("c_%d",i/nPlotsPerCanvas+1), "CMS", 5, 45, 300*nPlotsX, 300*nPlotsY);
			c->Divide(nPlotsX, nPlotsY, 0.001, 0.001);
		}
		cout << i << " " << (i%nPlotsPerCanvas)+1 << endl;
		c->cd( (i%nPlotsPerCanvas)+1 );
		TString padNameRoot = gPad->GetName(); 

		//Ratio plot
		gPad->Divide(1,2);

		// Upper part of the plot
		TString padNameTop = padNameRoot; padNameTop += "_1";
		cout << padNameTop << endl;
		aPad = (TPad*)gROOT->FindObject(padNameTop.Data());
		aPad->SetPad(0.1,0.36,0.95,0.95);
		aPad->SetFillStyle(0);
		aPad->SetBottomMargin(0.01);
		if ( isLogY ) aPad->SetLogy(kTRUE);
		aPad->cd();
		
		// Get temporary TH1 objects from tree entries
		cout << mycopy->At(i)->GetName() << endl;
		TString variableName = mycopy->At(i)->GetName();
		TString drawVariable = TString::Format("%s>>h_%s", variableName.Data(), variableName.Data());
		t->Draw( drawVariable );
		drawVariable  = TString::Format("%s>>hRef_%s", variableName.Data(), variableName.Data());
		tRef->Draw( drawVariable );

		// Put comparison and reference histograms into stack and draw them
		THStack *hstack = new THStack(TString::Format("hStack_%d", i/nPlotsPerCanvas), TString::Format(";%s;Entries", variableName.Data()) );
		TH1 *h = (TH1F*)gDirectory->Get( TString::Format( "h_%s", variableName.Data() ).Data() );
		if (isNorm) h->Scale( 1./h->Integral() );
		h->SetLineColor(kBlue);
		hstack->Add( h, "hist" );
		TH1 *hRef = (TH1F*)gDirectory->Get( TString::Format( "hRef_%s", variableName.Data() ).Data() );
		if (isNorm) hRef->Scale( 1./hRef->Integral() );
		hRef->SetLineColor(kRed);
		hRef->SetMarkerStyle(20);
		hstack->Add( hRef, "pe" );
		hstack->Draw("nostack");
		hstack->GetYaxis()->SetLabelSize(0.07);

		// Lower part of the plot
		TString padNameBottom = padNameRoot; padNameBottom += "_2";
		aPad = (TPad*)gROOT->FindObject(padNameBottom.Data());
		aPad->SetPad(0.1,0.01,0.95,0.35);
		aPad->SetFillStyle(0);
		aPad->SetGridy();
		aPad->SetTopMargin(0.01);	aPad->SetBottomMargin(0.17);
		//aPad->SetLeftMargin(0.01);	aPad->SetRightMargin(0.01);
		aPad->cd();
		TH1 *hRatSelfRef = (TH1*)hRef->Clone(TString(hRef->GetName())+"_SelfRefRat"); hRatSelfRef->Divide(hRef,hRef,1.,1.);
		TH1 *hRatRef = (TH1*)hRef->Clone(TString(hRef->GetName())+"_RefRat"); hRatRef->Divide(h,hRef,1.,1.);
		//hRatSelfRef->Draw("e");
		hRatRef->Draw("p");
		hRatRef->GetYaxis()->SetNdivisions(506);
		hRatRef->GetYaxis()->SetLabelSize(0.1);
		hRatRef->GetXaxis()->SetTitle( hstack->GetXaxis()->GetTitle() );
		hRatRef->GetXaxis()->SetLabelSize( 0.1 );
		hRatRef->GetXaxis()->SetTitleSize( 0.08 );

		// if this is the last pad of the canvas 
		// draw a legend and print canvas to the file
		if ( i%nPlotsPerCanvas == nPlotsX*nPlotsY-1 || i==mycopy->GetEntries()-1 ) {
			TLegend *leg = new TLegend( 0.75,0.8,0.99,0.99 );
			TString label = histLegend + TString::Format("(%5.1f entries)",h->GetEntries());
			leg->AddEntry(h, label);
			label = histRefLegend + TString::Format("(%5.1f entries)",hRef->GetEntries());
			leg->AddEntry(hRef, label );
			leg->Draw();
			TString outputCanvasName(prefix);
			if ( isLogY ) outputCanvasName += "log_";
			outputCanvasName += i/nPlotsPerCanvas;
			outputCanvasName += fmt;
			c->Print( outputCanvasName );
			//delete c;
		}
	} // for(int i = 0; i < mycopy->GetEntries(); ++i)
	return ;
} //plotComparison
