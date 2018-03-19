include Makefile_norm.mk
include Makefile_sys.mk

export TTCENTRAL
export TARGETVAR

CONFIG:=config_t2h_cards.py
SUPPRESSOUT=>/dev/null

CARDGEN=/storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/result/tools/cards.py

TARGETVAR=BDT

MINIMIZER=Minuit
AUTOMCSTAT=--automcstat
STATONLY=

#TTTT
$(BUILDDIR)/Hists_TTTT_MEScale.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} TTTTMEScale ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_PU.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} PU ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_JERUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jerup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} JERUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_JERDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jerdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} JERDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_JESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jesup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} JESUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_JESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} JESDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
#$(BUILDDIR)/Hists_TTTT_JESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_totaljesup_Run2_TopTree_Study.root
#	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
#	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} JESUP ${TARGETVAR} ${SUPPRESSOUT}
#	
#$(BUILDDIR)/Hists_TTTT_JESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_totaljesdown_Run2_TopTree_Study.root
#	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
#	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} JESDOWN ${TARGETVAR} ${SUPPRESSOUT}
########################################################################################################################
$(BUILDDIR)/Hists_TTTT_SubTotalScaleJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_SubTotalScale_jesup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} SubTotalScaleJECUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_SubTotalScaleJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_SubTotalScale_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} SubTotalScaleJECDOWN ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_SubTotalRelativeJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_SubTotalRelative_jesup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} SubTotalRelativeJECUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_SubTotalRelativeJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_SubTotalRelative_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} SubTotalRelativeJECDOWN ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_SubTotalPtJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_SubTotalPt_jesup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} SubTotalPtJECUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_SubTotalPtJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_SubTotalPt_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} SubTotalPtJECDOWN ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_SubTotalPileUpJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_SubTotalPileUp_jesup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} SubTotalPileJECUP  ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_SubTotalPileUpJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_SubTotalPileUp_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} SubTotalPileJECDOWN  ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_SubTotalFlavorJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_SubTotalFlavor_jesup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} SubTotalFlavorJECUP   ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_SubTotalFlavorJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_SubTotalFlavor_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} SubTotalFlavorJECDOWN   ${TARGETVAR} ${SUPPRESSOUT}
########################################################################################################################

####
$(BUILDDIR)/Hists_TTTT_BTAG1.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} BTAG1 ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TTTT_BTAG2.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} BTAG2 ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TTTT_BTAG3.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} BTAG3 ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TTTT_BTAG4.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} BTAG4 ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TTTT_BTAG5.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} BTAG5 ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TTTT_BTAG6.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} BTAG6 ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TTTT_BTAG7.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} BTAG7 ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TTTT_BTAG8.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} BTAG8 ${TARGETVAR} ${SUPPRESSOUT}
####	
# $(BUILDDIR)/Hists_TTTT_BTAG.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
# 	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
# 	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} BTAG ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_BTAG.root: \
	$(BUILDDIR)/Hists_TTTT_BTAG1.root $(BUILDDIR)/Hists_TTTT_BTAG2.root\
	$(BUILDDIR)/Hists_TTTT_BTAG3.root $(BUILDDIR)/Hists_TTTT_BTAG4.root\
	$(BUILDDIR)/Hists_TTTT_BTAG5.root $(BUILDDIR)/Hists_TTTT_BTAG6.root\
	$(BUILDDIR)/Hists_TTTT_BTAG7.root $(BUILDDIR)/Hists_TTTT_BTAG8.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_BTAGJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jesup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} BJCORUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_BTAGJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} BJCORDOWN ${TARGETVAR} ${SUPPRESSOUT}

#$(BUILDDIR)/Hists_TTTT_BTAGJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_totaljesup_Run2_TopTree_Study.root
#	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
#	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} BJCORUP ${TARGETVAR} ${SUPPRESSOUT}
#	
#$(BUILDDIR)/Hists_TTTT_BTAGJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_totaljesdown_Run2_TopTree_Study.root
#	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
#	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} BJCORDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_ISRUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_isrup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTISRUPNORM} TTTTISRUp ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_ISRDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_isrdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTISRDWNORM} TTTTISRDown ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_FSRUP.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_fsrup_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTFSRUPNORM} TTTTFSRUp ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TTTT_FSRDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_fsrdown_Run2_TopTree_Study.root
	@echo "Preparing TTTT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTFSRDWNORM} TTTTFSRDown ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_CARDS.root: $(BUILDDIR)/Hists_TTTT.root \
	$(BUILDDIR)/Hists_TTTT_JERUP.root $(BUILDDIR)/Hists_TTTT_JERDOWN.root \
	$(BUILDDIR)/Hists_TTTT_JESUP.root $(BUILDDIR)/Hists_TTTT_JESDOWN.root \
	$(BUILDDIR)/Hists_TTTT_SubTotalFlavorJESUP.root $(BUILDDIR)/Hists_TTTT_SubTotalFlavorJESDOWN.root \
	$(BUILDDIR)/Hists_TTTT_SubTotalScaleJESUP.root $(BUILDDIR)/Hists_TTTT_SubTotalScaleJESDOWN.root \
	$(BUILDDIR)/Hists_TTTT_SubTotalRelativeJESUP.root $(BUILDDIR)/Hists_TTTT_SubTotalRelativeJESDOWN.root \
	$(BUILDDIR)/Hists_TTTT_SubTotalPtJESUP.root $(BUILDDIR)/Hists_TTTT_SubTotalPtJESDOWN.root \
	$(BUILDDIR)/Hists_TTTT_SubTotalPileUpJESUP.root $(BUILDDIR)/Hists_TTTT_SubTotalPileUpJESDOWN.root \
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
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} ttMEScale ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_PDF.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} TTJets_PDF ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_HDAMP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} TTJets_HDAMP ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_HDAMPUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTHdampup_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTHDAMPUPNORM} TTJets_HDAMPALTUP ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_HDAMPDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTHdampdown_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTHDAMPDWNORM} TTJets_HDAMPALTDOWN ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_PU.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} PU ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_PT.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} TTPT ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_PAGPT.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} TTPAGPT ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_JERUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jerup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} JERUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_JERDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jerdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} JERDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_JESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jesup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} JESUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_JESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} JESDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
#$(BUILDDIR)/Hists_TT_JESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_totaljesup_Run2_TopTree_Study.root
#	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
#	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} JESUP ${TARGETVAR} ${SUPPRESSOUT}
#	
#$(BUILDDIR)/Hists_TT_JESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_totaljesdown_Run2_TopTree_Study.root
#	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
#	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} JESDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_SubTotalPileUpJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_SubTotalPileUp_jesup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTSUBPUUPNORM} SubTotalPileJECUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_SubTotalPileUpJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_SubTotalPileUp_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTSUBPUDOWNNORM} SubTotalPileJECDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_SubTotalPtJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_SubTotalPt_jesup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTSUBPTUPNORM} SubTotalPtJECUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_SubTotalPtJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_SubTotalPt_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTSUBPTDOWNNORM} SubTotalPtJECDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_SubTotalRelativeJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_SubTotalRelative_jesup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTSUBRELUPNORM} SubTotalRelativeJECUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_SubTotalRelativeJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_SubTotalRelative_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTSUBRELDOWNNORM} SubTotalRelativeJECDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_SubTotalScaleJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_SubTotalScale_jesup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTSUBSCALEUPNORM} SubTotalScaleJECUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_SubTotalScaleJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_SubTotalScale_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTSUBSCALEDOWNNORM} SubTotalScaleJECDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_SubTotalFlavorJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_SubTotalFlavor_jesup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTSUBSCALEUPNORM} SubTotalFlavorJECUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_SubTotalFlavorJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_SubTotalFlavor_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTSUBSCALEDOWNNORM} SubTotalFlavorJECDOWN ${TARGETVAR} ${SUPPRESSOUT}
############
$(BUILDDIR)/Hists_TT_BTAG1.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} BTAG1 ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TT_BTAG2.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} BTAG2 ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TT_BTAG3.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} BTAG3 ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TT_BTAG4.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} BTAG4 ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TT_BTAG5.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} BTAG5 ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TT_BTAG6.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} BTAG6 ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TT_BTAG7.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} BTAG7 ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TT_BTAG8.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} BTAG8 ${TARGETVAR} ${SUPPRESSOUT}
############
# $(BUILDDIR)/Hists_TT_BTAG.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
# 	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
# 	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} BTAG ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_BTAG.root: \
	$(BUILDDIR)/Hists_TT_BTAG1.root $(BUILDDIR)/Hists_TT_BTAG2.root\
	$(BUILDDIR)/Hists_TT_BTAG3.root $(BUILDDIR)/Hists_TT_BTAG4.root\
	$(BUILDDIR)/Hists_TT_BTAG5.root $(BUILDDIR)/Hists_TT_BTAG6.root\
	$(BUILDDIR)/Hists_TT_BTAG7.root $(BUILDDIR)/Hists_TT_BTAG8.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@hadd -f $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_BTAGJESUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jesup_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} BJCORUP ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_BTAGJESDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_jesdown_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} BJCORDOWN ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_ISRUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTISRUPNORM} TTISRUp ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_ISRDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTISRDWNORM} TTISRDown ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_FSRUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTFSRUPNORM} TTFSRUp ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_FSRDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTFSRDWNORM} TTFSRDown ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_UEUP.root: ${CONFIG} $(BUILDDIR)/Craneen_TTUETuneup_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTUEUPNORM} TTUEUp ${TARGETVAR} ${SUPPRESSOUT}
	
$(BUILDDIR)/Hists_TT_UEDOWN.root: ${CONFIG} $(BUILDDIR)/Craneen_TTUETunedown_powheg_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTUEDWNORM} TTUEDown ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_TTX.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Preparing TT SYSTEMATICS histograms $@ ($^)" 
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} heavyFlav ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_CARDS_OLDHDAMP.root: $(BUILDDIR)/Hists_TT.root \
	$(BUILDDIR)/Hists_TT_ISRUP.root $(BUILDDIR)/Hists_TT_ISRDOWN.root \
	$(BUILDDIR)/Hists_TT_FSRUP.root $(BUILDDIR)/Hists_TT_FSRDOWN.root \
	$(BUILDDIR)/Hists_TT_UEUP.root $(BUILDDIR)/Hists_TT_UEDOWN.root \
	$(BUILDDIR)/Hists_TT_JERUP.root $(BUILDDIR)/Hists_TT_JERDOWN.root \
	$(BUILDDIR)/Hists_TT_JESUP.root $(BUILDDIR)/Hists_TT_JESDOWN.root \
	$(BUILDDIR)/Hists_TT_SubTotalFlavorJESUP.root $(BUILDDIR)/Hists_TT_SubTotalFlavorJESDOWN.root \
	$(BUILDDIR)/Hists_TT_SubTotalScaleJESUP.root $(BUILDDIR)/Hists_TT_SubTotalScaleJESDOWN.root \
	$(BUILDDIR)/Hists_TT_SubTotalRelativeJESUP.root $(BUILDDIR)/Hists_TT_SubTotalRelativeJESDOWN.root \
	$(BUILDDIR)/Hists_TT_SubTotalPileUpJESUP.root $(BUILDDIR)/Hists_TT_SubTotalPileUpJESDOWN.root \
	$(BUILDDIR)/Hists_TT_SubTotalPtJESUP.root $(BUILDDIR)/Hists_TT_SubTotalPtJESDOWN.root \
	$(BUILDDIR)/Hists_TT_TTX.root $(BUILDDIR)/Hists_TT_PU.root \
	$(BUILDDIR)/Hists_TT_MEScale.root $(BUILDDIR)/Hists_TT_PT.root $(BUILDDIR)/Hists_TT_PAGPT.root\
	$(BUILDDIR)/Hists_TT_HDAMP.root $(BUILDDIR)/Hists_TT_PDF.root \
	$(BUILDDIR)/Hists_TT_BTAG.root  $(BUILDDIR)/Hists_TT_BTAGJESUP.root $(BUILDDIR)/Hists_TT_BTAGJESDOWN.root
	@echo "MERGE TT SYSTEMATICS histograms $@ ($^)" 
	@hadd -f $@ $^ ${SUPPRESSOUT}
	@python tools/renormsysshapes.py $@ -r $(BUILDDIR)/Hists_TT.root -t bdt -s MEScale,TTPT,TTPAGPT,PDF
	#@python tools/renormsysshapes.py $@ -r $(BUILDDIR)/Hists_TT.root -t bdt -s MEScale,UE,FSR,ISR,PDF,HDAMP,TTPT

$(BUILDDIR)/Hists_TT_CARDS.root: $(BUILDDIR)/Hists_TT.root \
	$(BUILDDIR)/Hists_TT_ISRUP.root $(BUILDDIR)/Hists_TT_ISRDOWN.root \
	$(BUILDDIR)/Hists_TT_FSRUP.root $(BUILDDIR)/Hists_TT_FSRDOWN.root \
	$(BUILDDIR)/Hists_TT_UEUP.root $(BUILDDIR)/Hists_TT_UEDOWN.root \
	$(BUILDDIR)/Hists_TT_JERUP.root $(BUILDDIR)/Hists_TT_JERDOWN.root \
	$(BUILDDIR)/Hists_TT_JESUP.root $(BUILDDIR)/Hists_TT_JESDOWN.root \
	$(BUILDDIR)/Hists_TT_SubTotalFlavorJESUP.root $(BUILDDIR)/Hists_TT_SubTotalFlavorJESDOWN.root \
	$(BUILDDIR)/Hists_TT_SubTotalScaleJESUP.root $(BUILDDIR)/Hists_TT_SubTotalScaleJESDOWN.root \
	$(BUILDDIR)/Hists_TT_SubTotalRelativeJESUP.root $(BUILDDIR)/Hists_TT_SubTotalRelativeJESDOWN.root \
	$(BUILDDIR)/Hists_TT_SubTotalPileUpJESUP.root $(BUILDDIR)/Hists_TT_SubTotalPileUpJESDOWN.root \
	$(BUILDDIR)/Hists_TT_SubTotalPtJESUP.root $(BUILDDIR)/Hists_TT_SubTotalPtJESDOWN.root \
	$(BUILDDIR)/Hists_TT_TTX.root $(BUILDDIR)/Hists_TT_PU.root \
	$(BUILDDIR)/Hists_TT_MEScale.root $(BUILDDIR)/Hists_TT_PT.root $(BUILDDIR)/Hists_TT_PAGPT.root\
	$(BUILDDIR)/Hists_TT_HDAMPUP.root $(BUILDDIR)/Hists_TT_HDAMPDOWN.root $(BUILDDIR)/Hists_TT_PDF.root \
	$(BUILDDIR)/Hists_TT_BTAG.root  $(BUILDDIR)/Hists_TT_BTAGJESUP.root $(BUILDDIR)/Hists_TT_BTAGJESDOWN.root
	@echo "MERGE TT SYSTEMATICS histograms $@ ($^)" 
	@hadd -f $@ $^ ${SUPPRESSOUT}
	@python tools/renormsysshapes.py $@ -r $(BUILDDIR)/Hists_TT.root -t bdt -s MEScale,TTPT,TTPAGPT,PDF
	#@python tools/renormsysshapes.py $@ -r $(BUILDDIR)/Hists_TT.root -t bdt -s MEScale,UE,FSR,ISR,PDF,HDAMP,TTPT


card_mu.txt: $(BUILDDIR)/Hists_data.root $(BUILDDIR)/Hists_EW.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_TT_CARDS.root $(BUILDDIR)/Hists_TTTT_CARDS.root $(BUILDDIR)/Hists_TTWXY.root $(BUILDDIR)/Hists_TT_HZmerged.root
	@echo "make HiggsCombine cards"
	@cd $(BUILDDIR); python $(CARDGEN) -o $@ --channel=mu --data Hists_data.root  --source '{"NP_overlay_ttttNLO":"Hists_TTTT_CARDS.root", "ttbarTTX":"Hists_TT_CARDS.root", "EW":"Hists_EW.root", "ST_tW":"Hists_T.root", "TTRARE_plus":"Hists_TTWXY.root", "Rare1TTHZ":"Hists_TT_HZmerged.root"}' --observable=bdt $(AUTOMCSTAT); cd -
	
card_el.txt: $(BUILDDIR)/Hists_data.root $(BUILDDIR)/Hists_EW.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_TT_CARDS.root $(BUILDDIR)/Hists_TTTT_CARDS.root $(BUILDDIR)/Hists_TTWXY.root $(BUILDDIR)/Hists_TT_HZmerged.root
	@echo "make HiggsCombine cards"
	@cd $(BUILDDIR); python $(CARDGEN) -o $@ --channel=el --data Hists_data.root  --source '{"NP_overlay_ttttNLO":"Hists_TTTT_CARDS.root", "ttbarTTX":"Hists_TT_CARDS.root", "EW":"Hists_EW.root", "ST_tW":"Hists_T.root", "TTRARE_plus":"Hists_TTWXY.root", "Rare1TTHZ":"Hists_TT_HZmerged.root"}' --observable=bdt $(AUTOMCSTAT); cd -

$(BUILDDIR)/datacard_elmu.txt:	$(BUILDDIR_EL)/card_el.txt $(BUILDDIR_MU)/card_mu.txt
	@echo "Combining datacards $^"
	@combineCards.py EL=$(BUILDDIR_EL)/card_el.txt MU=$(BUILDDIR_MU)/card_mu.txt > $@

$(BUILDDIR)/datacard_elmu.res: $(BUILDDIR)/datacard_elmu.txt
	-combine -M Asymptotic --run $(RUN) $^ --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=$(MINIMIZER) $(STATONLY) >> temp.comb.1
	-combine -M MaxLikelihoodFit $^ -t -1 --expectSignal=1 --robustFit=1 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=$(MINIMIZER)  $(STATONLY) --plots --out=$(BUILDDIR) >>temp.comb.2
	-combine -M ProfileLikelihood $^ -t -1 --expectSignal=1 --significance --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=$(MINIMIZER)  $(STATONLY) >>temp.comb.3
	@cat temp.comb.* > $@
	@rm temp.comb.*
$(BUILDDIR_EL)/card_el.res: $(BUILDDIR_EL)/card_el.txt
	-combine -M Asymptotic --run $(RUN) $^ --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=$(MINIMIZER)  $(STATONLY) >> temp.el.1
	-combine -M MaxLikelihoodFit $^ -t -1 --expectSignal=1 --robustFit=1 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=$(MINIMIZER)  $(STATONLY) --plots --out=$(BUILDDIR_EL) >>temp.el.2 
	-combine -M ProfileLikelihood $^ -t -1 --expectSignal=1 --significance --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=$(MINIMIZER)  $(STATONLY) >>temp.el.3
	@cat temp.el.* > $@
	@rm temp.el.*
$(BUILDDIR_MU)/card_mu.res: $(BUILDDIR_MU)/card_mu.txt
	-combine -M Asymptotic --run $(RUN) $^ --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=$(MINIMIZER)  $(STATONLY) >> temp.mu.1
	-combine -M MaxLikelihoodFit $^ -t -1 --expectSignal=1 --robustFit=1 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerType=$(MINIMIZER)  $(STATONLY) --plots --out=$(BUILDDIR_MU) >>temp.mu.2
	-combine -M ProfileLikelihood $^ -t -1 --expectSignal=1 --significance --X-rtd MINIMIZER_analytic  --cminDefaultMinimizerType=$(MINIMIZER) $(STATONLY) >>temp.mu.3
	@cat temp.mu.* > $@
	@rm temp.mu.*
limits: $(BUILDDIR)/datacard_elmu.res $(BUILDDIR_EL)/card_el.res $(BUILDDIR_MU)/card_mu.res
	@python ./tools/parseLimits.py -i $(BUILDDIR_EL)/card_el.res -f $(FORMAT) | tail -n4
	@python ./tools/parseLimits.py -i $(BUILDDIR_MU)/card_mu.res -f $(FORMAT) | tail -n4
	@python ./tools/parseLimits.py -i $(BUILDDIR)/datacard_elmu.res -f $(FORMAT) | tail -n4

#Likelihood scans
#combine -M MultiDimFit --robustFit=1 --rMax=3 -t -1 --expectSignal=1 --saveNLL combo.root --algo grid -n _combo
#combine -M MultiDimFit --robustFit=1 --rMax=3 -t -1 --expectSignal=1 --saveNLL sl.root --algo grid -n _sl
#combine -M MultiDimFit --robustFit=1 --rMax=3 -t -1 --expectSignal=1 --saveNLL dl.root --algo grid -n _dl

#
#python NLL_scans.py -f .pdf -j '{"sl":"higgsCombine_sl.MultiDimFit.mH120.root","dl":"higgsCombine_dl.MultiDimFit.mH120.root","combo":"higgsCombine_combo.MultiDimFit.mH120.root", "sl_fit":[1.0,2.47,-1.0],"dl_fit":[1.0,1.74,-1.0],"combo_fit":[1.0,1.34,-1.0]}' -b
#
#

