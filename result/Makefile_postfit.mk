# PLOTCONFIGDIR=tools/mountainrange/mountainrange_configs_raresplit
PLOTCONFIGDIR=tools/mountainrange/mountainrange_configs_tthz_ttwxy
PLOTMACRO=tools/mountainrange/mountainrange_pub_raresplit.py
CORRMATRMACRO=tools/plot_corr_matrix.py
PULLSMACRO=tools/plot_nuis_pulls.py
DIFFNUISDENYS=tools/nuispulls/diffNuisances_denys.py
POSTFITSHAPES=PostFitShapesFromWorkspaceDenys
SPECTATORMOUNTAINRANGEMAKECOMMAND=mountainrangefourbtagbinsrebin
# SPECTATORMOUNTAINRANGEMAKECOMMAND=mountainrangefourbtagbins
# SPECTATORMOUNTAINRANGEMAKECOMMAND=mountainrangeallbinsrebin

.PHONY: postfit_plots pulls correlations mountainrange spectatorcards spectatorcards_HT spectatorcards_multitopness spectatorcards_HTb spectatorcards_HTH spectatorcards_SumJetMassX spectatorcards_HTX spectatorcards_csvJetcsv3 spectatorcards_csvJetcsv4 spectatorcards_csvJetpt3 spectatorcards_csvJetpt4 spectatorcards_1stjetpt spectatorcards_2ndjetpt spectatorcards_5thjetpt spectatorcards_6thjetpt

postfit_plots: mountainrangeallbins mountainrangefourbtagbins pulls correlations

pulls: $(COMBINESHAPESFILE)
	python $(DIFFNUISDENYS) $(COMBINESHAPESFILE) -a -A -g $(BUILDDIR)/pulls_out.root
	python $(PULLSMACRO) $(BUILDDIR)/pulls_out.root -o $(BUILDDIR)/pulls -e $(FORMAT) -b

correlations: $(COMBINESHAPESFILE)
	python $(CORRMATRMACRO) $(COMBINESHAPESFILE) -o $(BUILDDIR)/corrmat -e $(FORMAT) -b

mountainrangefourbtagbins: $(COMBINESHAPESFILE)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_mu_tttt4btag_prefit.json -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_el_tttt4btag_prefit.json -b -e $(FORMAT) -r --dir $(BUILDDIR)

mountainrangefourbtagbinsrebin: $(COMBINESHAPESFILE)
		python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_mu_tttt4btag_prefit_rebin.json -b -e $(FORMAT) -r --dir $(BUILDDIR)
		python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_el_tttt4btag_prefit_rebin.json -b -e $(FORMAT) -r --dir $(BUILDDIR)

mountainrangeallbins: $(COMBINESHAPESFILE)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_mu_ttttall_prefit.json -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_el_ttttall_prefit.json -b -e $(FORMAT) -r --dir $(BUILDDIR)

mountainrangeallbinsrebin: $(COMBINESHAPESFILE)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_mu_ttttall_prefit_rebin.json -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_el_ttttall_prefit_rebin.json -b -e $(FORMAT) -r --dir $(BUILDDIR)

mountainrange: $(COMBINESHAPESFILE)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_mu_tttt10_prefit.json -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_mu_tttt9_prefit.json  -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_mu_tttt8_prefit.json  -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_mu_tttt7_prefit.json  -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_el_tttt10_prefit.json -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_el_tttt9_prefit.json  -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_el_tttt8_prefit.json  -b -e $(FORMAT) -r --dir $(BUILDDIR)

spectatormountainrange: mountainrange_HT mountainrange_multitopness mountainrange_HTb mountainrange_HTH mountainrange_SumJetMassX mountainrange_HTX \
                mountainrange_csvJetcsv3 mountainrange_csvJetcsv4 mountainrange_csvJetpt3 mountainrange_csvJetpt4 \
                mountainrange_1stjetpt mountainrange_2ndjetpt mountainrange_5thjetpt mountainrange_6thjetpt

spectatorcards: spectatorcards_HT spectatorcards_multitopness spectatorcards_HTb spectatorcards_HTH spectatorcards_SumJetMassX spectatorcards_HTX \
		spectatorcards_csvJetcsv3 spectatorcards_csvJetcsv4 spectatorcards_csvJetpt3 spectatorcards_csvJetpt4 \
		spectatorcards_1stjetpt spectatorcards_2ndjetpt spectatorcards_5thjetpt spectatorcards_6thjetpt

spectatorpostfitshapes: postfitshapes_HT postfitshapes_multitopness postfitshapes_HTb postfitshapes_HTH postfitshapes_SumJetMassX postfitshapes_HTX \
		postfitshapes_csvJetcsv3 postfitshapes_csvJetcsv4 postfitshapes_csvJetpt3 postfitshapes_csvJetpt4 \
		postfitshapes_1stjetpt postfitshapes_2ndjetpt postfitshapes_5thjetpt postfitshapes_6thjetpt

spectatorcards_HT:
	if [ -d "$(BUILDDIR)/HT/plots_mu" ]; then echo "$(BUILDDIR)/HT/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/HT/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/HT/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/HT/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=HT
	if [ -d "$(BUILDDIR)/HT/plots_el" ]; then echo "$(BUILDDIR)/HT/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/HT/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/HT/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/HT/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=HT
	$(MAKE) $(BUILDDIR)/HT/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/HT/plots_el BUILDDIR_MU=$(BUILDDIR)/HT/plots_mu BUILDDIR=$(BUILDDIR)/HT
postfitshapes_HT: $(BUILDDIR)/HT/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/HT/datacard_elmu.root -o $(BUILDDIR)/HT/shapes_HT.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_HT: $(BUILDDIR)/HT/shapes_HT.root
	if [ -d "$(BUILDDIR)/HT/postfit_nominal" ]; then echo "$(BUILDDIR)/HT/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/HT/postfit_nominal ; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/HT/shapes_HT.root BUILDDIR=$(BUILDDIR)/HT/postfit_nominal



spectatorcards_multitopness:
	if [ -d "$(BUILDDIR)/multitopness/plots_mu" ]; then echo "$(BUILDDIR)/multitopness/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/multitopness/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/multitopness/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/multitopness/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=multitopness
	if [ -d "$(BUILDDIR)/multitopness/plots_el" ]; then echo "$(BUILDDIR)/multitopness/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/multitopness/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/multitopness/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/multitopness/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=multitopness
	$(MAKE) $(BUILDDIR)/multitopness/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/multitopness/plots_el BUILDDIR_MU=$(BUILDDIR)/multitopness/plots_mu BUILDDIR=$(BUILDDIR)/multitopness
postfitshapes_multitopness: $(BUILDDIR)/multitopness/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/multitopness/datacard_elmu.root -o $(BUILDDIR)/multitopness/shapes_multitopness.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_multitopness: $(BUILDDIR)/multitopness/shapes_multitopness.root
	if [ -d "$(BUILDDIR)/multitopness/postfit_nominal" ]; then echo "$(BUILDDIR)/multitopness/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/multitopness/postfit_nominal ; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/multitopness/shapes_multitopness.root BUILDDIR=$(BUILDDIR)/multitopness/postfit_nominal


spectatorcards_HTb:
	if [ -d "$(BUILDDIR)/HTb/plots_mu" ]; then echo "$(BUILDDIR)/HTb/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/HTb/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/HTb/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/HTb/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=HTb
	if [ -d "$(BUILDDIR)/HTb/plots_el" ]; then echo "$(BUILDDIR)/HTb/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/HTb/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/HTb/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/HTb/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=HTb
	$(MAKE) $(BUILDDIR)/HTb/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/HTb/plots_el BUILDDIR_MU=$(BUILDDIR)/HTb/plots_mu BUILDDIR=$(BUILDDIR)/HTb
postfitshapes_HTb: $(BUILDDIR)/HTb/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/HTb/datacard_elmu.root -o $(BUILDDIR)/HTb/shapes_HTb.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_HTb: $(BUILDDIR)/HTb/shapes_HTb.root
	if [ -d "$(BUILDDIR)/HTb/postfit_nominal" ]; then echo "$(BUILDDIR)/HTb/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/HTb/postfit_nominal ; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/HTb/shapes_HTb.root BUILDDIR=$(BUILDDIR)/HTb/postfit_nominal

spectatorcards_HTH:
	if [ -d "$(BUILDDIR)/HTH/plots_mu" ]; then echo "$(BUILDDIR)/HTH/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/HTH/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/HTH/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/HTH/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=HTH
	if [ -d "$(BUILDDIR)/HTH/plots_el" ]; then echo "$(BUILDDIR)/HTH/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/HTH/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/HTH/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/HTH/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=HTH
	$(MAKE) $(BUILDDIR)/HTH/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/HTH/plots_el BUILDDIR_MU=$(BUILDDIR)/HTH/plots_mu BUILDDIR=$(BUILDDIR)/HTH
postfitshapes_HTH: $(BUILDDIR)/HTH/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/HTH/datacard_elmu.root -o $(BUILDDIR)/HTH/shapes_HTH.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_HTH: $(BUILDDIR)/HTH/shapes_HTH.root
	if [ -d "$(BUILDDIR)/HTH/postfit_nominal" ]; then echo "$(BUILDDIR)/HTH/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/HTH/postfit_nominal ; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/HTH/shapes_HTH.root BUILDDIR=$(BUILDDIR)/HTH/postfit_nominal

spectatorcards_LeptonPt:
	if [ -d "$(BUILDDIR)/LeptonPt/plots_mu" ]; then echo "$(BUILDDIR)/LeptonPt/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/LeptonPt/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/LeptonPt/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/LeptonPt/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=LeptonPt
	if [ -d "$(BUILDDIR)/LeptonPt/plots_el" ]; then echo "$(BUILDDIR)/LeptonPt/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/LeptonPt/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/LeptonPt/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/LeptonPt/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=LeptonPt
	$(MAKE) $(BUILDDIR)/LeptonPt/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/LeptonPt/plots_el BUILDDIR_MU=$(BUILDDIR)/LeptonPt/plots_mu BUILDDIR=$(BUILDDIR)/LeptonPt
postfitshapes_LeptonPt: $(BUILDDIR)/LeptonPt/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/LeptonPt/datacard_elmu.root -o $(BUILDDIR)/LeptonPt/shapes_LeptonPt.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_LeptonPt: $(BUILDDIR)/LeptonPt/shapes_LeptonPt.root
	if [ -d "$(BUILDDIR)/LeptonPt/postfit_nominal" ]; then echo "$(BUILDDIR)/LeptonPt/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/LeptonPt/postfit_nominal ; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/LeptonPt/shapes_LeptonPt.root BUILDDIR=$(BUILDDIR)/LeptonPt/postfit_nominal


spectatorcards_SumJetMassX:
	if [ -d "$(BUILDDIR)/SumJetMassX/plots_mu" ]; then echo "$(BUILDDIR)/SumJetMassX/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/SumJetMassX/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/SumJetMassX/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/SumJetMassX/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=SumJetMassX
	if [ -d "$(BUILDDIR)/SumJetMassX/plots_el" ]; then echo "$(BUILDDIR)/SumJetMassX/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/SumJetMassX/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/SumJetMassX/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/SumJetMassX/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=SumJetMassX
	$(MAKE) $(BUILDDIR)/SumJetMassX/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/SumJetMassX/plots_el BUILDDIR_MU=$(BUILDDIR)/SumJetMassX/plots_mu BUILDDIR=$(BUILDDIR)/SumJetMassX
postfitshapes_SumJetMassX: $(BUILDDIR)/SumJetMassX/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/SumJetMassX/datacard_elmu.root -o $(BUILDDIR)/SumJetMassX/shapes_SumJetMassX.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_SumJetMassX: $(BUILDDIR)/SumJetMassX/shapes_SumJetMassX.root
	if [ -d "$(BUILDDIR)/SumJetMassX/postfit_nominal" ]; then echo "$(BUILDDIR)/SumJetMassX/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/SumJetMassX/postfit_nominal ; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/SumJetMassX/shapes_SumJetMassX.root BUILDDIR=$(BUILDDIR)/SumJetMassX/postfit_nominal


spectatorcards_HTX:
	if [ -d "$(BUILDDIR)/HTX/plots_mu" ]; then echo "$(BUILDDIR)/HTX/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/HTX/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/HTX/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/HTX/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=HTX
	if [ -d "$(BUILDDIR)/HTX/plots_el" ]; then echo "$(BUILDDIR)/HTX/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/HTX/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/HTX/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/HTX/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=HTX
	$(MAKE) $(BUILDDIR)/HTX/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/HTX/plots_el BUILDDIR_MU=$(BUILDDIR)/HTX/plots_mu BUILDDIR=$(BUILDDIR)/HTX
postfitshapes_HTX: $(BUILDDIR)/HTX/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/HTX/datacard_elmu.root -o $(BUILDDIR)/HTX/shapes_HTX.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_HTX: $(BUILDDIR)/HTX/shapes_HTX.root
	if [ -d "$(BUILDDIR)/HTX/postfit_nominal" ]; then echo "$(BUILDDIR)/HTX/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/HTX/postfit_nominal ; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/HTX/shapes_HTX.root BUILDDIR=$(BUILDDIR)/HTX/postfit_nominal


spectatorcards_csvJetcsv3:
	if [ -d "$(BUILDDIR)/csvJetcsv3/plots_mu" ]; then echo "$(BUILDDIR)/csvJetcsv3/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/csvJetcsv3/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/csvJetcsv3/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/csvJetcsv3/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=csvJetcsv3
	if [ -d "$(BUILDDIR)/csvJetcsv3/plots_el" ]; then echo "$(BUILDDIR)/csvJetcsv3/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/csvJetcsv3/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/csvJetcsv3/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/csvJetcsv3/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=csvJetcsv3
	$(MAKE) $(BUILDDIR)/csvJetcsv3/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/csvJetcsv3/plots_el BUILDDIR_MU=$(BUILDDIR)/csvJetcsv3/plots_mu BUILDDIR=$(BUILDDIR)/csvJetcsv3
postfitshapes_csvJetcsv3: $(BUILDDIR)/csvJetcsv3/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/csvJetcsv3/datacard_elmu.root -o $(BUILDDIR)/csvJetcsv3/shapes_csvJetcsv3.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_csvJetcsv3: $(BUILDDIR)/csvJetcsv3/shapes_csvJetcsv3.root
	if [ -d "$(BUILDDIR)/csvJetcsv3/postfit_nominal" ]; then echo "$(BUILDDIR)/csvJetcsv3/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/csvJetcsv3/postfit_nominal ; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/csvJetcsv3/shapes_csvJetcsv3.root BUILDDIR=$(BUILDDIR)/csvJetcsv3/postfit_nominal


spectatorcards_csvJetcsv4:
	if [ -d "$(BUILDDIR)/csvJetcsv4/plots_mu" ]; then echo "$(BUILDDIR)/csvJetcsv4/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/csvJetcsv4/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/csvJetcsv4/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/csvJetcsv4/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=csvJetcsv4
	if [ -d "$(BUILDDIR)/csvJetcsv4/plots_el" ]; then echo "$(BUILDDIR)/csvJetcsv4/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/csvJetcsv4/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/csvJetcsv4/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/csvJetcsv4/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=csvJetcsv4
	$(MAKE) $(BUILDDIR)/csvJetcsv4/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/csvJetcsv4/plots_el BUILDDIR_MU=$(BUILDDIR)/csvJetcsv4/plots_mu BUILDDIR=$(BUILDDIR)/csvJetcsv4
postfitshapes_csvJetcsv4: $(BUILDDIR)/csvJetcsv4/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/csvJetcsv4/datacard_elmu.root -o $(BUILDDIR)/csvJetcsv4/shapes_csvJetcsv4.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_csvJetcsv4: $(BUILDDIR)/csvJetcsv4/shapes_csvJetcsv4.root
	if [ -d "$(BUILDDIR)/csvJetcsv4/postfit_nominal" ]; then echo "$(BUILDDIR)/csvJetcsv4/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/csvJetcsv4/postfit_nominal ; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/csvJetcsv4/shapes_csvJetcsv4.root BUILDDIR=$(BUILDDIR)/csvJetcsv4/postfit_nominal


spectatorcards_csvJetpt3:
	if [ -d "$(BUILDDIR)/csvJetpt3/plots_mu" ]; then echo "$(BUILDDIR)/csvJetpt3/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/csvJetpt3/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/csvJetpt3/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/csvJetpt3/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=csvJetpt3
	if [ -d "$(BUILDDIR)/csvJetpt3/plots_el" ]; then echo "$(BUILDDIR)/csvJetpt3/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/csvJetpt3/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/csvJetpt3/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/csvJetpt3/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=csvJetpt3
	$(MAKE) $(BUILDDIR)/csvJetpt3/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/csvJetpt3/plots_el BUILDDIR_MU=$(BUILDDIR)/csvJetpt3/plots_mu BUILDDIR=$(BUILDDIR)/csvJetpt3
postfitshapes_csvJetpt3: $(BUILDDIR)/csvJetpt3/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/csvJetpt3/datacard_elmu.root -o $(BUILDDIR)/csvJetpt3/shapes_csvJetpt3.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_csvJetpt3: $(BUILDDIR)/csvJetpt3/shapes_csvJetpt3.root
	if [ -d "$(BUILDDIR)/csvJetpt3/postfit_nominal" ]; then echo "$(BUILDDIR)/csvJetpt3/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/csvJetpt3/postfit_nominal; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/csvJetpt3/shapes_csvJetpt3.root BUILDDIR=$(BUILDDIR)/csvJetpt3/postfit_nominal


spectatorcards_csvJetpt4:
	if [ -d "$(BUILDDIR)/csvJetpt4/plots_mu" ]; then echo "$(BUILDDIR)/csvJetpt4/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/csvJetpt4/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/csvJetpt4/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/csvJetpt4/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=csvJetpt4
	if [ -d "$(BUILDDIR)/csvJetpt4/plots_el" ]; then echo "$(BUILDDIR)/csvJetpt4/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/csvJetpt4/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/csvJetpt4/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/csvJetpt4/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=csvJetpt4
	$(MAKE) $(BUILDDIR)/csvJetpt4/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/csvJetpt4/plots_el BUILDDIR_MU=$(BUILDDIR)/csvJetpt4/plots_mu BUILDDIR=$(BUILDDIR)/csvJetpt4
postfitshapes_csvJetpt4: $(BUILDDIR)/csvJetpt4/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/csvJetpt4/datacard_elmu.root -o $(BUILDDIR)/csvJetpt4/shapes_csvJetpt4.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_csvJetpt4: $(BUILDDIR)/csvJetpt4/shapes_csvJetpt4.root
	if [ -d "$(BUILDDIR)/csvJetpt4/postfit_nominal" ]; then echo "$(BUILDDIR)/csvJetpt4/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/csvJetpt4/postfit_nominal ; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/csvJetpt4/shapes_csvJetpt4.root BUILDDIR=$(BUILDDIR)/csvJetpt4/postfit_nominal


spectatorcards_1stjetpt:
	if [ -d "$(BUILDDIR)/1stjetpt/plots_mu" ]; then echo "$(BUILDDIR)/1stjetpt/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/1stjetpt/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/1stjetpt/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/1stjetpt/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=1stjetpt
	if [ -d "$(BUILDDIR)/1stjetpt/plots_el" ]; then echo "$(BUILDDIR)/1stjetpt/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/1stjetpt/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/1stjetpt/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/1stjetpt/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=1stjetpt
	$(MAKE) $(BUILDDIR)/1stjetpt/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/1stjetpt/plots_el BUILDDIR_MU=$(BUILDDIR)/1stjetpt/plots_mu BUILDDIR=$(BUILDDIR)/1stjetpt
postfitshapes_1stjetpt: $(BUILDDIR)/1stjetpt/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/1stjetpt/datacard_elmu.root -o $(BUILDDIR)/1stjetpt/shapes_1stjetpt.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_1stjetpt: $(BUILDDIR)/1stjetpt/shapes_1stjetpt.root
	if [ -d "$(BUILDDIR)/1stjetpt/postfit_nominal" ]; then echo "$(BUILDDIR)/1stjetpt/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/1stjetpt/postfit_nominal ; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/1stjetpt/shapes_1stjetpt.root BUILDDIR=$(BUILDDIR)/1stjetpt/postfit_nominal


spectatorcards_2ndjetpt:
	if [ -d "$(BUILDDIR)/2ndjetpt/plots_mu" ]; then echo "$(BUILDDIR)/2ndjetpt/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/2ndjetpt/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/2ndjetpt/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/2ndjetpt/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=2ndjetpt
	if [ -d "$(BUILDDIR)/2ndjetpt/plots_el" ]; then echo "$(BUILDDIR)/2ndjetpt/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/2ndjetpt/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/2ndjetpt/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/2ndjetpt/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=2ndjetpt
	$(MAKE) $(BUILDDIR)/2ndjetpt/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/2ndjetpt/plots_el BUILDDIR_MU=$(BUILDDIR)/2ndjetpt/plots_mu BUILDDIR=$(BUILDDIR)/2ndjetpt
postfitshapes_2ndjetpt: $(BUILDDIR)/2ndjetpt/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/2ndjetpt/datacard_elmu.root -o $(BUILDDIR)/2ndjetpt/shapes_2ndjetpt.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_2ndjetpt: $(BUILDDIR)/2ndjetpt/shapes_2ndjetpt.root
	if [ -d "$(BUILDDIR)/2ndjetpt/postfit_nominal" ]; then echo "$(BUILDDIR)/2ndjetpt/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/2ndjetpt/postfit_nominal ; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/2ndjetpt/shapes_2ndjetpt.root BUILDDIR=$(BUILDDIR)/2ndjetpt/postfit_nominal


spectatorcards_5thjetpt:
	if [ -d "$(BUILDDIR)/5thjetpt/plots_mu" ]; then echo "$(BUILDDIR)/5thjetpt/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/5thjetpt/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/5thjetpt/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/5thjetpt/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=5thjetpt
	if [ -d "$(BUILDDIR)/5thjetpt/plots_el" ]; then echo "$(BUILDDIR)/5thjetpt/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/5thjetpt/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/5thjetpt/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/5thjetpt/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=5thjetpt
	$(MAKE) $(BUILDDIR)/5thjetpt/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/5thjetpt/plots_el BUILDDIR_MU=$(BUILDDIR)/5thjetpt/plots_mu BUILDDIR=$(BUILDDIR)/5thjetpt
postfitshapes_5thjetpt: $(BUILDDIR)/5thjetpt/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/5thjetpt/datacard_elmu.root -o $(BUILDDIR)/5thjetpt/shapes_5thjetpt.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_5thjetpt: $(BUILDDIR)/5thjetpt/shapes_5thjetpt.root
	if [ -d "$(BUILDDIR)/5thjetpt/postfit_nominal" ]; then echo "$(BUILDDIR)/5thjetpt/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/5thjetpt/postfit_nominal ; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/5thjetpt/shapes_5thjetpt.root BUILDDIR=$(BUILDDIR)/5thjetpt/postfit_nominal


spectatorcards_6thjetpt:
	if [ -d "$(BUILDDIR)/6thjetpt/plots_mu" ]; then echo "$(BUILDDIR)/6thjetpt/plots_mu dir exists" ; else mkdir -p $(BUILDDIR)/6thjetpt/plots_mu ; fi \
	&& cp -P $(BUILDDIR)/plots_mu/Cran*.root $(BUILDDIR)/6thjetpt/plots_mu \
	&& $(MAKE) card_mu.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/6thjetpt/plots_mu INPUTLOCATION=$(INPUTLOCATION)/plots_mu DATALABEL="Single\ \#mu" TREENAME=Craneen__Mu TARGETVAR=6thjetpt
	if [ -d "$(BUILDDIR)/6thjetpt/plots_el" ]; then echo "$(BUILDDIR)/6thjetpt/plots_el dir exists" ; else mkdir -p $(BUILDDIR)/6thjetpt/plots_el ; fi \
	&& cp -P $(BUILDDIR)/plots_el/Cran*.root $(BUILDDIR)/6thjetpt/plots_el \
	&& $(MAKE) card_el.txt AUTOMCSTAT= BUILDDIR=$(BUILDDIR)/6thjetpt/plots_el INPUTLOCATION=$(INPUTLOCATION)/plots_el DATALABEL="Single\ e" TREENAME=Craneen__El TARGETVAR=6thjetpt
	$(MAKE) $(BUILDDIR)/6thjetpt/datacard_elmu.root BUILDDIR_EL=$(BUILDDIR)/6thjetpt/plots_el BUILDDIR_MU=$(BUILDDIR)/6thjetpt/plots_mu BUILDDIR=$(BUILDDIR)/6thjetpt
postfitshapes_6thjetpt: $(BUILDDIR)/6thjetpt/datacard_elmu.root
	$(POSTFITSHAPES) -w $(BUILDDIR)/6thjetpt/datacard_elmu.root -o $(BUILDDIR)/6thjetpt/shapes_6thjetpt.root -f $(COMBINESHAPESFILE):fit_s --postfit --sampling
mountainrange_6thjetpt: $(BUILDDIR)/6thjetpt/shapes_6thjetpt.root
	if [ -d "$(BUILDDIR)/6thjetpt/postfit_nominal" ]; then echo "$(BUILDDIR)/6thjetpt/postfit_nominal dir exists" ; else mkdir -p $(BUILDDIR)/6thjetpt/postfit_nominal ; fi && $(MAKE) $(SPECTATORMOUNTAINRANGEMAKECOMMAND) COMBINESHAPESFILE=$(BUILDDIR)/6thjetpt/shapes_6thjetpt.root BUILDDIR=$(BUILDDIR)/6thjetpt/postfit_nominal
