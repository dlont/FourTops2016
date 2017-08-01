include Makefile_norm.mk

export TTCENTRAL

CONFIG:=config_t2h_cards.py
SUPPRESSOUT=>/dev/null

#TTTT
$(BUILDDIR)/Hists_TTTT_MEScale.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} TTTT_MEScale ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_PU.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} PU ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_JERUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jerup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} JERUP ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_JERDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jerdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} JERDOWN ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_JESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jesup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} JESUP ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_JESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} JESDOWN ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_BTAG.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} BTAG ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_BTAGJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jesup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} BJCORUP ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_BTAGJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} BJCORDOWN ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_ISRUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_isrup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTISRUPNORM} TTTTISRUp ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_ISRDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_isrdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTISRDWNORM} TTTTISRDown ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_FSRUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_fsrup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTFSRUPNORM} TTTTFSRUp ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_FSRDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_fsrdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTFSRDWNORM} TTTTFSRDown ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_CARDS.root: $(BUILDDIR)/Hists_TTTT.root \
	$(BUILDDIR)/Hists_TTTT_JERUP.root $(BUILDDIR)/Hists_TTTT_JERDOWN.root \
	$(BUILDDIR)/Hists_TTTT_JESUP.root $(BUILDDIR)/Hists_TTTT_JESDOWN.root \
	$(BUILDDIR)/Hists_TTTT_MEScale.root $(BUILDDIR)/Hists_TTTT_PU.root \
	$(BUILDDIR)/Hists_TTTT_BTAG.root $(BUILDDIR)/Hists_TTTT_BTAGJESUP.root $(BUILDDIR)/Hists_TTTT_BTAGJESDOWN.root \
	$(BUILDDIR)/Hists_TTTT_FSRDOWN.root $(BUILDDIR)/Hists_TTTT_FSRUP.root $(BUILDDIR)/Hists_TTTT_ISRDOWN.root $(BUILDDIR)/Hists_TTTT_ISRUP.root
	@echo "MERGE TTTT SYSTEMATICS histograms $@ ($^)" 
	@hadd -f $@ $^ ${SUPPRESSOUT}
	@python tools/renormsysshapes.py $@ -r $(BUILDDIR)/Hists_TTTT.root -t bdt -s MEScale

#TT
$(BUILDDIR)/Hists_TT_MEScale.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} ttMEScale ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_PDF.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} TTJets_PDF ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_HDAMP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} TTJets_HDAMP ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_HDAMPUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTHdampup_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} TTJets_HDAMPALTUP ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_HDAMPDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTHdampdown_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} TTJets_HDAMPALTDOWN ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_PU.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} PU ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_JERUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jerup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} JERUP ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_JERDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jerdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} JERDOWN ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_JESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jesup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} JESUP ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_JESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} JESDOWN ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_BTAG.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} BTAG ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_BTAGJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jesup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} BJCORUP ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_BTAGJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} BJCORDOWN ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_ISRUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTISRUPNORM} TTISRUp ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_ISRDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTISRDWNORM} TTISRDown ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_FSRUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTFSRUPNORM} TTFSRUp ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_FSRDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTFSRDWNORM} TTFSRDown ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_UEUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTUETuneup_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTUEUPNORM} TTUEUp ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_UEDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTUETunedown_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTUEDWNORM} TTUEDown ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_TTX.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} heavyFlav ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_CARDS.root: $(BUILDDIR)/Hists_TT.root \
	$(BUILDDIR)/Hists_TT_ISRUP.root $(BUILDDIR)/Hists_TT_ISRDOWN.root \
	$(BUILDDIR)/Hists_TT_FSRUP.root $(BUILDDIR)/Hists_TT_FSRDOWN.root \
	$(BUILDDIR)/Hists_TT_UEUP.root $(BUILDDIR)/Hists_TT_UEDOWN.root \
	$(BUILDDIR)/Hists_TT_JERUP.root $(BUILDDIR)/Hists_TT_JERDOWN.root \
	$(BUILDDIR)/Hists_TT_JESUP.root $(BUILDDIR)/Hists_TT_JESDOWN.root \
	$(BUILDDIR)/Hists_TT_TTX.root $(BUILDDIR)/Hists_TT_PU.root \
	$(BUILDDIR)/Hists_TT_MEScale.root \
	$(BUILDDIR)/Hists_TT_HDAMP.root $(BUILDDIR)/Hists_TT_PDF.root \
	$(BUILDDIR)/Hists_TT_BTAG.root  $(BUILDDIR)/Hists_TT_BTAGJESUP.root $(BUILDDIR)/Hists_TT_BTAGJESDOWN.root
	@echo "MERGE TT SYSTEMATICS histograms $@ ($^)" 
	@hadd -f $@ $^ ${SUPPRESSOUT}
	@python tools/renormsysshapes.py $@ -r $(BUILDDIR)/Hists_TT.root -t bdt -s MEScale,UE,FSR,ISR,PDF,HDAMP


card_mu.txt: $(BUILDDIR)/Hists_data.root $(BUILDDIR)/Hists_EW.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_TT_CARDS.root $(BUILDDIR)/Hists_TTTT_CARDS.root $(BUILDDIR)/Hists_TT_RARE.root
	@echo "make HiggsCombine cards"
	@if [ -d "cards_mu" ]; then echo "cards_mu dir exists" ; else mkdir cards_mu ; fi
	@python tools/cards.py -o $@ --channel=mu --data $(BUILDDIR)/Hists_data.root  --source '{"NP_overlay_ttttNLO":"$(BUILDDIR)/Hists_TTTT_CARDS.root", "ttbarTTX":"$(BUILDDIR)/Hists_TT_CARDS.root", "EW":"$(BUILDDIR)/Hists_EW.root", "ST_tW":"$(BUILDDIR)/Hists_T.root", "TTRARE":"$(BUILDDIR)/Hists_TT_RARE.root"}' --observable=bdt
	
card_el.txt: $(BUILDDIR)/Hists_data.root $(BUILDDIR)/Hists_EW.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_TT_CARDS.root $(BUILDDIR)/Hists_TTTT_CARDS.root $(BUILDDIR)/Hists_TT_RARE.root
	@echo "make HiggsCombine cards"
	@if [ -d "cards_el" ]; then echo "cards_el dir exists" ; else mkdir cards_el ; fi
	@python tools/cards.py -o $@ --channel=el --data $(BUILDDIR)/Hists_data.root  --source '{"NP_overlay_ttttNLO":"$(BUILDDIR)/Hists_TTTT_CARDS.root", "ttbarTTX":"$(BUILDDIR)/Hists_TT_CARDS.root", "EW":"$(BUILDDIR)/Hists_EW.root", "ST_tW":"$(BUILDDIR)/Hists_T.root", "TTRARE":"$(BUILDDIR)/Hists_TT_RARE.root"}' --observable=bdt

datacard_elmu.txt:	card_el.txt card_mu.txt
	@echo "Combining datacards $^"
	@combineCards.py EL=card_el.txt MU=card_mu.txt > $@

datacard_elmu.res: datacard_elmu.txt
	@combine -M Asymptotic --run $(RUN) $^ >> temp.comb.1
	@combine -M MaxLikelihoodFit $^ -t -1 --expectSignal=1 --robustFit=1 >>temp.comb.2
	@combine -M ProfileLikelihood $^ -t -1 --expectSignal=1 --significance >>temp.comb.3
	@cat temp.comb.* > $@
	@rm temp.comb.*
card_el.res: card_el.txt
	@combine -M Asymptotic --run $(RUN) $^ >> temp.el.1
	@combine -M MaxLikelihoodFit $^ -t -1 --expectSignal=1 --robustFit=1 >>temp.el.2
	@combine -M ProfileLikelihood $^ -t -1 --expectSignal=1 --significance >>temp.el.3
	@cat temp.el.* > $@
	@rm temp.el.*
card_mu.res: card_mu.txt
	@combine -M Asymptotic --run $(RUN) $^ >> temp.mu.1
	@combine -M MaxLikelihoodFit $^ -t -1 --expectSignal=1 --robustFit=1 >>temp.mu.2
	@combine -M ProfileLikelihood $^ -t -1 --expectSignal=1 --significance >>temp.mu.3
	@cat temp.mu.* > $@
	@rm temp.mu.*
limits: datacard_elmu.res card_el.res card_mu.res
	@python ./tools/parseLimits.py -i card_el.res -f $(FORMAT) | tail -n2
	@python ./tools/parseLimits.py -i card_mu.res -f $(FORMAT) | tail -n2
	@python ./tools/parseLimits.py -i datacard_elmu.res -f $(FORMAT) | tail -n2

