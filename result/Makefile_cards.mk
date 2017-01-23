include Makefile_norm.mk

CONFIG:=config_t2h_cards.py
SUPPRESSOUT=>/dev/null

#TTTT
$(BUILDDIR)/Hists_TTTT_MEScale.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} TTTT_MEScale ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_PU.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} PU ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_JERUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jerup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} JERUP ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_JERDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jerdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} JERDOWN ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_JESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jesup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} JESUP ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_JESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} JESDOWN ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_CARDS.root: $(BUILDDIR)/Hists_TTTT.root \
	$(BUILDDIR)/Hists_TTTT_JERUP.root $(BUILDDIR)/Hists_TTTT_JERDOWN.root \
	$(BUILDDIR)/Hists_TTTT_JESUP.root $(BUILDDIR)/Hists_TTTT_JESDOWN.root \
	$(BUILDDIR)/Hists_TTTT_MEScale.root $(BUILDDIR)/Hists_TTTT_PU.root
	@echo "MERGE TT SYSTEMATICS histograms $@ ($^)" 
	@hadd $@ $^ ${SUPPRESSOUT}

#TT
$(BUILDDIR)/Hists_TT_MEScale.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} TTJets_MEScale ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_PU.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} PU ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_JERUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_powheg_jerup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} JERUP ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_JERDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_powheg_jerdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} JERDOWN ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_JESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_powheg_jesup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} JESUP ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_JESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_powheg_jerdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} JESDOWN ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_CARDS.root: $(BUILDDIR)/Hists_TT.root \
	$(BUILDDIR)/Hists_TT_JERUP.root $(BUILDDIR)/Hists_TT_JERDOWN.root \
	$(BUILDDIR)/Hists_TT_JESUP.root $(BUILDDIR)/Hists_TT_JESDOWN.root \
	$(BUILDDIR)/Hists_TT_MEScale.root $(BUILDDIR)/Hists_TT_PU.root 
	@echo "MERGE TT SYSTEMATICS histograms $@ ($^)" 
	@hadd $@ $^ ${SUPPRESSOUT}


.PHONY: cards_mu
cards_mu: $(BUILDDIR)/Hists_data.root $(BUILDDIR)/Hists_WJets.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_TT_CARDS.root $(BUILDDIR)/Hists_TTTT_CARDS.root
	@echo "make HiggsCombine cards"
	@if [ -d "cards_mu" ]; then echo "cards_mu dir exists" ; else mkdir cards_mu ; fi
	@python tools/cards.py -o cards_mu/card.txt --channel=mu --data $(BUILDDIR)/Hists_data.root  --source '{"TTTT":"$(BUILDDIR)/Hists_TTTT_CARDS.root", "TT":"$(BUILDDIR)/Hists_TT_CARDS.root", "EW":"$(BUILDDIR)/Hists_WJets.root", "ST":"$(BUILDDIR)/Hists_T.root"}' --observable=bdt
	
