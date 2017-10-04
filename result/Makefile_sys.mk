SYSPLOTDIR=../sysplot
SYSNORMPLOTDIR=../sysplot/normalisation_rebin/
LATEXDUMPDIR=../latex
#DIFFNUIS=~/CMSSW_7_4_7/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py
DIFFNUIS=~/TTP_CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py

#MINOS=--minos=all
MINOS=
RUN=blind

sysplots: 	$(BUILDDIR)/Hists_TT_CARDS.root $(BUILDDIR)/Hists_TTTT_CARDS.root
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TT_CARDS.root -j $(SYSPLOTDIR)/JESCOMPONENTS_tt.json -r $(BUILDDIR)/Hists_TT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TTTT_CARDS.root -j $(SYSPLOTDIR)/JESCOMPONENTS_tttt.json -r $(BUILDDIR)/Hists_TTTT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TT_CARDS.root -j $(SYSPLOTDIR)/JES_tt.json -r $(BUILDDIR)/Hists_TT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TTTT_CARDS.root -j $(SYSPLOTDIR)/JES_tttt.json -r $(BUILDDIR)/Hists_TTTT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TT_CARDS.root -j $(SYSPLOTDIR)/CSV_tt.json -r $(BUILDDIR)/Hists_TT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TTTT_CARDS.root -j $(SYSPLOTDIR)/CSV_tttt.json -r $(BUILDDIR)/Hists_TTTT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TT_CARDS.root -j $(SYSPLOTDIR)/Theory_tt.json -r $(BUILDDIR)/Hists_TT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TTTT_CARDS.root -j $(SYSPLOTDIR)/Theory_tttt.json -r $(BUILDDIR)/Hists_TTTT_CARDS.root -f $(FORMAT)
	@if [ -d "$(BUILDDIR)/sys" ]; then echo "$(BUILDDIR)/sys dir exists" ; else mkdir $(BUILDDIR)/sys  ; fi 
	@mv JES_tt.$(FORMAT) JES_tttt.$(FORMAT) CSV_tt.$(FORMAT) CSV_tttt.$(FORMAT) Theory_tt.$(FORMAT) Theory_tttt.$(FORMAT) $(BUILDDIR)/sys

sysplotsnorm: 	$(BUILDDIR)/Hists_TT_CARDS.root $(BUILDDIR)/Hists_TTTT_CARDS.root
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TT_CARDS.root -j $(SYSNORMPLOTDIR)/JES_tt.json -r $(BUILDDIR)/Hists_TT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TTTT_CARDS.root -j $(SYSNORMPLOTDIR)/JES_tttt.json -r $(BUILDDIR)/Hists_TTTT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TT_CARDS.root -j $(SYSNORMPLOTDIR)/CSV_tt.json -r $(BUILDDIR)/Hists_TT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TTTT_CARDS.root -j $(SYSNORMPLOTDIR)/CSV_tttt.json -r $(BUILDDIR)/Hists_TTTT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TT_CARDS.root -j $(SYSNORMPLOTDIR)/Theory_tt.json -r $(BUILDDIR)/Hists_TT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TTTT_CARDS.root -j $(SYSNORMPLOTDIR)/Theory_tttt.json -r $(BUILDDIR)/Hists_TTTT_CARDS.root -f $(FORMAT)
	@if [ -d "$(BUILDDIR)/sysnorm" ]; then echo "$(BUILDDIR)/sysnorm dir exists" ; else mkdir $(BUILDDIR)/sysnorm  ; fi 
	@mv JES_tt.$(FORMAT) JES_tttt.$(FORMAT) CSV_tt.$(FORMAT) CSV_tttt.$(FORMAT) Theory_tt.$(FORMAT) Theory_tttt.$(FORMAT) $(BUILDDIR)/sysnorm
	#@python -b $(LATEXDUMPDIR)/texplotspage.py -j $(LATEXDUMPDIR)/systematics.json app/syst

$(BUILDDIR_MU)/card_mu.root: $(BUILDDIR_MU)/card_mu.txt
	@text2workspace.py --channel-masks $^ -o $@
$(BUILDDIR_EL)/card_el.root: $(BUILDDIR_EL)/card_el.txt
	@text2workspace.py --channel-masks $^ -o $@
$(BUILDDIR)/datacard_elmu.root: $(BUILDDIR)/datacard_elmu.txt
	@text2workspace.py --channel-masks $^ -o $@

maskchannels: $(BUILDDIR)/datacard_elmu.root
	@if [ -d "$(dir $(BUILDDIR)/masks)" ]; then echo "Muon dir exists" ; else mkdir $(BUILDDIR)/masks ; fi
	@combine -M MaxLikelihoodFit -d $(BUILDDIR)/datacard_elmu.root --plots --saveShapes --out $(BUILDDIR)/masks --robustFit=true $(MINOS) --setParameters mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=1,mask_EL_el8J3M=1,mask_EL_el8J2M=0,mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=1,mask_MU_mu8J3M=1,mask_MU_mu8J2M=0,mask_MU_mu7J4M=1,mask_MU_mu7J3M=1,mask_MU_mu7J2M=1

impacts_combined_elmu_blind.pdf: $(BUILDDIR)/datacard_elmu.root
	@combineTool.py -M Impacts -d $(BUILDDIR)/datacard_elmu.root --doInitialFit -m 125 -t -1 --expectSignal=1 --robustFit=1
	@combineTool.py -M Impacts -d $(BUILDDIR)/datacard_elmu.root --doFits -m 125 --parallel 4 -t -1 --expectSignal=1 --robustFit=1
	@combineTool.py -M Impacts -d $(BUILDDIR)/datacard_elmu.root -o impacts_combined_elmu.json -m 125 -t -1 --expectSignal=1 --robustFit=1
	@plotImpacts.py -i impacts_combined_elmu.json -o impacts_combined_elmu_blind --per-page 35
	@mv $@ $(BUILDDIR)

impacts_combined_elmu_bgregion.pdf: $(BUILDDIR)/datacard_elmu.root
	@combineTool.py -M Impacts -d $(BUILDDIR)/datacard_elmu.root --doInitialFit -m 125 --robustFit=1 --setParameters mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=1,mask_EL_el8J3M=1,mask_EL_el8J2M=0,mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=1,mask_MU_mu8J3M=1,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0
	@combineTool.py -M Impacts -d $(BUILDDIR)/datacard_elmu.root --doFits -m 125 --parallel 4 --robustFit=1 --setParameters mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=1,mask_EL_el8J3M=1,mask_EL_el8J2M=0,mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=1,mask_MU_mu8J3M=1,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0
	@combineTool.py -M Impacts -d $(BUILDDIR)/datacard_elmu.root -o impacts_combined_elmu.json -m 125 --robustFit=1 --setParameters mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=1,mask_EL_el8J3M=1,mask_EL_el8J2M=0,mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=1,mask_MU_mu8J3M=1,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0
	@plotImpacts.py -i impacts_combined_elmu.json -o impacts_combined_elmu_bgregion --per-page 35
	@mv $@ $(BUILDDIR)

combinechecks: $(BUILDDIR_MU)/card_mu.root $(BUILDDIR_EL)/card_el.root $(BUILDDIR)/datacard_elmu.root
	@echo "Asimov checks"
	@echo "Asimov check: Single lepton combined"
	@combine -M MaxLikelihoodFit -t -1 --expectSignal 0 --robustFit=true $(MINOS) $(BUILDDIR)/datacard_elmu.root -n _AsimovComb0 --out $(BUILDDIR)
	@python $(DIFFNUIS) --absolute -a $(BUILDDIR)/fitDiagnostics_AsimovComb0.root -g $(BUILDDIR)/plots_AsimovComb0.root
	@combine -M MaxLikelihoodFit -t -1 --expectSignal 1 --robustFit=true $(MINOS) $(BUILDDIR)/datacard_elmu.root -n _AsimovComb1 --out $(BUILDDIR)
	@python $(DIFFNUIS) --absolute -a $(BUILDDIR)/mlfit_AsimovComb1.root -g $(BUILDDIR)/plots_AsimovComb1.root
	@echo "Asimov check: Single muon"
	@combine -M MaxLikelihoodFit -t -1 --expectSignal 0 --robustFit=true $(MINOS) $(BUILDDIR_MU)/card_mu.root -n _AsimovMu0 --out $(BUILDDIR_MU); \
	python $(DIFFNUIS) --absolute -a $(BUILDDIR_MU)/fitDiagnostics_AsimovMu0.root -g $(BUILDDIR_MU)/plots_AsimovMu0.root
	@combine -M MaxLikelihoodFit -t -1 --expectSignal 1 --robustFit=true $(MINOS) $(BUILDDIR_MU)/card_mu.root -n _AsimovMu1 --out $(BUILDDIR_MU); \
	python $(DIFFNUIS) --absolute -a $(BUILDDIR_MU)/fitDiagnostics_AsimovMu1.root -g $(BUILDDIR_MU)/plots_AsimovMu1.root
	@echo "Asimov check: Single electron"
	@combine -M MaxLikelihoodFit -t -1 --expectSignal 0 --robustFit=true $(MINOS) $(BUILDDIR_EL)/card_el.root -n _AsimovEl0 --out $(BUILDDIR_EL); \
	python $(DIFFNUIS) --absolute -a $(BUILDDIR_EL)/fitDiagnostics_AsimovEl0.root -g $(BUILDDIR_EL)/plots_AsimovEl0.root
	@combine -M MaxLikelihoodFit -t -1 --expectSignal 1 --robustFit=true $(MINOS) $(BUILDDIR_EL)/card_el.root -n _AsimovEl1 --out $(BUILDDIR_EL); \
	python $(DIFFNUIS) --absolute -a $(BUILDDIR_EL)/fitDiagnostics_AsimovEl1.root -g $(BUILDDIR_EL)/plots_AsimovEl1.root
	#@echo "Pulls and correlations"
	#@combine -M MaxLikelihoodFit --robustFit=true $(MINOS) --plots --saveShapes --out $(BUILDDIR)     $(BUILDDIR)/datacard_elmu.txt -n _CorrComb
	#@combine -M MaxLikelihoodFit --robustFit=true $(MINOS) --plots --saveShapes --out $(BUILDDIR_MU)  $(BUILDDIR_MU)/card_mu.txt -n _CorrMu
	#@combine -M MaxLikelihoodFit --robustFit=true $(MINOS) --plots --saveShapes --out $(BUILDDIR_EL)  $(BUILDDIR_EL)/card_el.txt -n _CorrEl
