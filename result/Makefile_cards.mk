include Makefile_norm.mk

export TTCENTRAL
export TARGETVAR

CONFIG:=config_t2h_cards.py
SUPPRESSOUT=>/dev/null

CARDGEN=/storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/result/tools/cards.py

TARGETVAR=BDT

#TTTT
$(BUILDDIR)/Hists_TTTT_MEScale.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} TTTTMEScale ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_PU.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} PU ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_JERUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jerup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} JERUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_JERDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jerdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} JERDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_JESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jesup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} JESUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_JESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} JESDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_BTAG.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} BTAG ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_BTAGJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jesup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} BJCORUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_BTAGJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} BJCORDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_ISRUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_isrup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTISRUPNORM} TTTTISRUp ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_ISRDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_isrdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTISRDWNORM} TTTTISRDown ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_FSRUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_fsrup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTFSRUPNORM} TTTTFSRUp ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_FSRDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_fsrdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTFSRDWNORM} TTTTFSRDown ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_CARDS.root: $(BUILDDIR)/Hists_TTTT.root \
	$(BUILDDIR)/Hists_TTTT_JERUP.root $(BUILDDIR)/Hists_TTTT_JERDOWN.root \
	$(BUILDDIR)/Hists_TTTT_JESUP.root $(BUILDDIR)/Hists_TTTT_JESDOWN.root \
	$(BUILDDIR)/Hists_TTTT_MEScale.root $(BUILDDIR)/Hists_TTTT_PU.root \
	$(BUILDDIR)/Hists_TTTT_BTAG.root $(BUILDDIR)/Hists_TTTT_BTAGJESUP.root $(BUILDDIR)/Hists_TTTT_BTAGJESDOWN.root \
	$(BUILDDIR)/Hists_TTTT_FSRDOWN.root $(BUILDDIR)/Hists_TTTT_FSRUP.root $(BUILDDIR)/Hists_TTTT_ISRDOWN.root $(BUILDDIR)/Hists_TTTT_ISRUP.root
	@echo "MERGE TTTT SYSTEMATICS histograms $@ ($^)" 
	@hadd -f $@ $^ ${SUPPRESSOUT}
	@python tools/renormsysshapes.py $@ -r $(BUILDDIR)/Hists_TTTT.root -t bdt -s MEScale
	#@python tools/renormsysshapes.py $@ -r $(BUILDDIR)/Hists_TTTT.root -t bdt -s MEScale,FSR,ISR

#TT
$(BUILDDIR)/Hists_TT_MEScale.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} ttMEScale ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_PDF.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} TTJets_PDF ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_HDAMP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} TTJets_HDAMP ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_HDAMPUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTHdampup_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} TTJets_HDAMPALTUP ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_HDAMPDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTHdampdown_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} TTJets_HDAMPALTDOWN ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_PU.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} PU ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_PT.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} TTPT ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_JERUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jerup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} JERUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_JERDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jerdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} JERDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_JESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jesup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} JESUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_JESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} JESDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_BTAG.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} BTAG ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_BTAGJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jesup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} BJCORUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_BTAGJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} BJCORDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_ISRUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTISRUPNORM} TTISRUp ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_ISRDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTISRDWNORM} TTISRDown ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_FSRUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTFSRUPNORM} TTFSRUp ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_FSRDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTFSRDWNORM} TTFSRDown ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_UEUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTUETuneup_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTUEUPNORM} TTUEUp ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_UEDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTUETunedown_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTUEDWNORM} TTUEDown ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_TTX.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} heavyFlav ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_CARDS.root: $(BUILDDIR)/Hists_TT.root \
	$(BUILDDIR)/Hists_TT_ISRUP.root $(BUILDDIR)/Hists_TT_ISRDOWN.root \
	$(BUILDDIR)/Hists_TT_FSRUP.root $(BUILDDIR)/Hists_TT_FSRDOWN.root \
	$(BUILDDIR)/Hists_TT_UEUP.root $(BUILDDIR)/Hists_TT_UEDOWN.root \
	$(BUILDDIR)/Hists_TT_JERUP.root $(BUILDDIR)/Hists_TT_JERDOWN.root \
	$(BUILDDIR)/Hists_TT_JESUP.root $(BUILDDIR)/Hists_TT_JESDOWN.root \
	$(BUILDDIR)/Hists_TT_TTX.root $(BUILDDIR)/Hists_TT_PU.root \
	$(BUILDDIR)/Hists_TT_MEScale.root $(BUILDDIR)/Hists_TT_PT.root \
	$(BUILDDIR)/Hists_TT_HDAMP.root $(BUILDDIR)/Hists_TT_PDF.root \
	$(BUILDDIR)/Hists_TT_BTAG.root  $(BUILDDIR)/Hists_TT_BTAGJESUP.root $(BUILDDIR)/Hists_TT_BTAGJESDOWN.root
	@echo "MERGE TT SYSTEMATICS histograms $@ ($^)" 
	@hadd -f $@ $^ ${SUPPRESSOUT}
	#@python tools/renormsysshapes.py $@ -r $(BUILDDIR)/Hists_TT.root -t bdt -s MEScale
	@python tools/renormsysshapes.py $@ -r $(BUILDDIR)/Hists_TT.root -t bdt -s MEScale,UE,FSR,ISR,PDF,HDAMP,TTPT


card_mu.txt: $(BUILDDIR)/Hists_data.root $(BUILDDIR)/Hists_EW.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_TT_CARDS.root $(BUILDDIR)/Hists_TTTT_CARDS.root $(BUILDDIR)/Hists_TT_RARE.root
	@echo "make HiggsCombine cards"
	@cd $(BUILDDIR); python $(CARDGEN) -o $@ --channel=mu --data Hists_data.root  --source '{"NP_overlay_ttttNLO":"Hists_TTTT_CARDS.root", "ttbarTTX":"Hists_TT_CARDS.root", "EW":"Hists_EW.root", "ST_tW":"Hists_T.root", "TTRARE":"Hists_TT_RARE.root"}' --observable=bdt; cd -
	
card_el.txt: $(BUILDDIR)/Hists_data.root $(BUILDDIR)/Hists_EW.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_TT_CARDS.root $(BUILDDIR)/Hists_TTTT_CARDS.root $(BUILDDIR)/Hists_TT_RARE.root
	@echo "make HiggsCombine cards"
	@cd $(BUILDDIR); python $(CARDGEN) -o $@ --channel=el --data Hists_data.root  --source '{"NP_overlay_ttttNLO":"Hists_TTTT_CARDS.root", "ttbarTTX":"Hists_TT_CARDS.root", "EW":"Hists_EW.root", "ST_tW":"Hists_T.root", "TTRARE":"Hists_TT_RARE.root"}' --observable=bdt; cd -

datacard_elmu.txt:	$(BUILDDIR_EL)/card_el.txt $(BUILDDIR_MU)/card_mu.txt
	@echo "Combining datacards $^"
	@combineCards.py EL=$(BUILDDIR_EL)/card_el.txt MU=$(BUILDDIR_MU)/card_mu.txt > $(BUILDDIR)/$@

datacard_elmu.res: $(BUILDDIR)/datacard_elmu.txt
	@combine -M Asymptotic --run $(RUN) --X-rtd MINIMIZER_analytic --picky --cminDefaultMinimizerType=Minuit $^ >> temp.comb.1
	@combine -M MaxLikelihoodFit $^ -t -1 --expectSignal=1 --robustFit=1 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=Minuit >>temp.comb.2
	@combine -M ProfileLikelihood $^ -t -1 --expectSignal=1 --significance --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=Minuit >>temp.comb.3
	@cat temp.comb.* > $(BUILDDIR)/$@
	@rm temp.comb.*
card_el.res: $(BUILDDIR_EL)/card_el.txt
	@combine -M Asymptotic --run $(RUN) $^ --X-rtd MINIMIZER_analytic --picky --cminDefaultMinimizerType=Minuit >> temp.el.1
	@combine -M MaxLikelihoodFit $^ -t -1 --expectSignal=1 --robustFit=1 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=Minuit >>temp.el.2
	@combine -M ProfileLikelihood $^ -t -1 --expectSignal=1 --significance --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=Minuit >>temp.el.3
	@cat temp.el.* > $(BUILDDIR_EL)/$@
	@rm temp.el.*
card_mu.res: $(BUILDDIR_MU)/card_mu.txt
	@combine -M Asymptotic --run $(RUN) $^ --X-rtd MINIMIZER_analytic --picky --cminDefaultMinimizerType=Minuit >> temp.mu.1
	@combine -M MaxLikelihoodFit $^ -t -1 --expectSignal=1 --robustFit=1 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=Minuit2 >>temp.mu.2
	@combine -M ProfileLikelihood $^ -t -1 --expectSignal=1 --significance --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=Minuit >>temp.mu.3
	@cat temp.mu.* > $(BUILDDIR_MU)/$@
	@rm temp.mu.*
limits: $(BUILDDIR)/datacard_elmu.res $(BUILDDIR_EL)/card_el.res $(BUILDDIR_MU)/card_mu.res
	@python ./tools/parseLimits.py -i $(BUILDDIR_EL)/card_el.res -f $(FORMAT) | tail -n2
	@python ./tools/parseLimits.py -i $(BUILDDIR_MU)/card_mu.res -f $(FORMAT) | tail -n2
	@python ./tools/parseLimits.py -i $(BUILDDIR)/datacard_elmu.res -f $(FORMAT) | tail -n2

