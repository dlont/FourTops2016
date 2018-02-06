MINIMIZER=Minuit
STATONLY=

$(BUILDDIR_OS)/datacard_os.txt: $(BUILDDIR_OS)/datacardElEl_BDT_ElEl18thSep2017_13TeVHadTop_JTS.txt $(BUILDDIR_OS)/datacardMuEl_BDT_MuEl18thSep2017_13TeVHadTop_JTS.txt $(BUILDDIR_OS)/datacardMuMu_BDT_MuMu18thSep2017_13TeVHadTop_JTS.txt
	@combineCards.py ELEL=$(BUILDDIR_OS)/datacardElEl_BDT_ElEl18thSep2017_13TeVHadTop_JTS.txt MUEL=$(BUILDDIR_OS)/datacardMuEl_BDT_MuEl18thSep2017_13TeVHadTop_JTS.txt MUMU=$(BUILDDIR_OS)/datacardMuMu_BDT_MuMu18thSep2017_13TeVHadTop_JTS.txt > $@

$(BUILDDIR)/fullcombo_cor.root: $(BUILDDIR_SL)/datacard_elmu_total_jes_correctedpath.txt $(BUILDDIR_OS)/datacard_os.txt $(BUILDDIR_SS)/card_tttt_srcr_rename_nuis.txt
	@combineCards.py SL=$(BUILDDIR_SL)/datacard_elmu_total_jes_correctedpath.txt DL=$(BUILDDIR_OS)/datacard_os.txt SS=$(BUILDDIR_SS)/card_tttt_srcr_rename_nuis.txt > $(BUILDDIR)/fullcombo_cor.txt
	@text2workspace.py --channel-masks $(BUILDDIR)/fullcombo_cor.txt

$(BUILDDIR)/fullcombo_uncor.root: $(BUILDDIR_EL)/card_el.txt $(BUILDDIR_MU)/card_mu.txt $(BUILDDIR_OS)/datacard_os.txt $(BUILDDIR_SS)/card_tttt_srcr.txt
	@combineCards.py EL=$(BUILDDIR_EL)/card_el.txt MU=$(BUILDDIR_MU)/card_mu.txt DL=$(BUILDDIR_OS)/datacard_os.txt SS=$(BUILDDIR_SS)/card_tttt_srcr.txt > $(BUILDDIR)/fullcombo.txt
	@text2workspace.py --channel-masks $(BUILDDIR)/fullcombo.txt

$(BUILDDIR)/fullcombo_uncor.res: $(BUILDDIR)/fullcombo.root
	-combine -M Asymptotic --run $(RUN) $^ --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=$(MINIMIZER) $(STATONLY) >> temp.comb.1
