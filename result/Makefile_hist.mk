#Order of arguments matters (first config.py, second input_tree.root, third scale)
include Makefile_norm.mk

export TTCENTRAL
export TARGETVAR

#DATAENTRIES=0
TTTTENTRIES=0
EWENTRIES=0
STENTRIES=0
TTENTRIES=0

CONFIG:=config_t2h.py
SUPPRESSOUT=>/dev/null

define calcEntries
        $(shell echo "from ROOT import TH1, TFile;file = TFile.Open(\"$(1)\");hist = file.Get(\"allSF/bdt\");print hist.Integral()"|python)
endef

$(BUILDDIR)/Hists_dataB.root: ${CONFIG} $(BUILDDIR)/Craneen_DataB_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataC.root: ${CONFIG} $(BUILDDIR)/Craneen_DataC_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataD.root: ${CONFIG} $(BUILDDIR)/Craneen_DataD_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataE.root: ${CONFIG} $(BUILDDIR)/Craneen_DataE_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataF.root: ${CONFIG} $(BUILDDIR)/Craneen_DataF_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataG.root: ${CONFIG} $(BUILDDIR)/Craneen_DataG_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataH.root: ${CONFIG} $(BUILDDIR)/Craneen_DataH_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_data.root: $(BUILDDIR)/Hists_dataB.root $(BUILDDIR)/Hists_dataC.root $(BUILDDIR)/Hists_dataD.root $(BUILDDIR)/Hists_dataE.root $(BUILDDIR)/Hists_dataF.root $(BUILDDIR)/Hists_dataG.root $(BUILDDIR)/Hists_dataH.root
	@echo "Merge data histograms $@ ($^)" 
	@hadd -f $@ $^

$(BUILDDIR)/Hists_TTTT_SCALED.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORMSCALED} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} ${TARGETVAR} ${SUPPRESSOUT}

#$(BUILDDIR)/Hists_EW.root: $(BUILDDIR)/Hists_WJets.root $(BUILDDIR)/Hists_W1Jets.root $(BUILDDIR)/Hists_W2Jets.root $(BUILDDIR)/Hists_W3Jets.root $(BUILDDIR)/Hists_W4Jets.root $(BUILDDIR)/Hists_DY50.root $(BUILDDIR)/Hists_DY1J50.root $(BUILDDIR)/Hists_DY2J50.root  $(BUILDDIR)/Hists_DY3J50.root  $(BUILDDIR)/Hists_DY4J50.root 
$(BUILDDIR)/Hists_EW.root: $(BUILDDIR)/Hists_W1Jets.root $(BUILDDIR)/Hists_W2Jets.root $(BUILDDIR)/Hists_W3Jets.root $(BUILDDIR)/Hists_W4Jets.root $(BUILDDIR)/Hists_DY1J50.root $(BUILDDIR)/Hists_DY2J50.root  $(BUILDDIR)/Hists_DY3J50.root  $(BUILDDIR)/Hists_DY4J50.root 
	@echo "Merging EW histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTW.root: ${CONFIG} $(BUILDDIR)/Craneen_TTW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTWNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTZ.root: ${CONFIG} $(BUILDDIR)/Craneen_TTZ_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTZNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTH.root: ${CONFIG} $(BUILDDIR)/Craneen_TTH_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTHNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTJ.root: ${CONFIG} $(BUILDDIR)/Craneen_TTTJ_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTJNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTW.root: ${CONFIG} $(BUILDDIR)/Craneen_TTTW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTWNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTWZ.root: ${CONFIG} $(BUILDDIR)/Craneen_TTWZ_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTWZNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTZZ.root: ${CONFIG} $(BUILDDIR)/Craneen_TTZZ_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTZZNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTZH.root: ${CONFIG} $(BUILDDIR)/Craneen_TTZH_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTZHNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTHH.root: ${CONFIG} $(BUILDDIR)/Craneen_TTHH_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTHHNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTXY.root: $(BUILDDIR)/Hists_TTTJ.root $(BUILDDIR)/Hists_TTTW.root $(BUILDDIR)/Hists_TTWZ.root $(BUILDDIR)/Hists_TTZZ.root $(BUILDDIR)/Hists_TTZH.root $(BUILDDIR)/Hists_TTHH.root 
	@echo "Merging TTXY histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_RARE.root: $(BUILDDIR)/Hists_TTW.root $(BUILDDIR)/Hists_TTZ.root $(BUILDDIR)/Hists_TTH.root $(BUILDDIR)/Hists_TTXY.root
	@echo "Merging TT RARE histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TTV.root: $(BUILDDIR)/Hists_TTW.root $(BUILDDIR)/Hists_TTZ.root
	@echo "Merging TT RARE histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}


$(BUILDDIR)/Hists_WJets.root: ${CONFIG} $(BUILDDIR)/Craneen_WJets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${WJETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_W1Jets.root: ${CONFIG} $(BUILDDIR)/Craneen_W1Jets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${W1JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_W2Jets.root: ${CONFIG} $(BUILDDIR)/Craneen_W2Jets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${W2JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_W3Jets.root: ${CONFIG} $(BUILDDIR)/Craneen_W3Jets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${W3JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_W4Jets.root: ${CONFIG} $(BUILDDIR)/Craneen_W4Jets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${W4JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_DY50.root: ${CONFIG} $(BUILDDIR)/Craneen_DYJets_50MG_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${DY50JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_DY1J50.root: ${CONFIG} $(BUILDDIR)/Craneen_DY1Jets_50MG_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${DY1J50JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_DY2J50.root: ${CONFIG} $(BUILDDIR)/Craneen_DY2Jets_50MG_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${DY2J50JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_DY3J50.root: ${CONFIG} $(BUILDDIR)/Craneen_DY3Jets_50MG_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${DY3J50JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_DY4J50.root: ${CONFIG} $(BUILDDIR)/Craneen_DY4Jets_50MG_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${DY4J50JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_T.root: $(BUILDDIR)/Hists_T_tW.root $(BUILDDIR)/Hists_Tbar_tW.root $(BUILDDIR)/Hists_T_tch.root $(BUILDDIR)/Hists_Tbar_tch.root
	@echo "Merging single top histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_T_tW.root: ${CONFIG} $(BUILDDIR)/Craneen_T_tW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TWNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_Tbar_tW.root: ${CONFIG} $(BUILDDIR)/Craneen_Tbar_tW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TBARWNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_T_tch.root: ${CONFIG} $(BUILDDIR)/Craneen_T_tch_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TTCHNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_Tbar_tch.root: ${CONFIG} $(BUILDDIR)/Craneen_Tbar_tch_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TBARTCHNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_SYST.root: $(BUILDDIR)/Hists_TT.root $(BUILDDIR)/Hists_tuneup.root $(BUILDDIR)/Hists_tunedown.root $(BUILDDIR)/Hists_isrscaleup.root $(BUILDDIR)/Hists_isrscaledown.root $(BUILDDIR)/Hists_fsrscaleup.root $(BUILDDIR)/Hists_fsrscaledown.root $(BUILDDIR)/Hists_EW.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_TT_RARE.root
	@echo "Preparing TT scale systematic histograms"
	@tools/scalehist.py -o $(BUILDDIR)/Hists_SYST_temp.root --nominal=$(BUILDDIR)/Hists_TT.root --isrscaleup=$(BUILDDIR)/Hists_isrscaleup.root --isrscaledown=$(BUILDDIR)/Hists_isrscaledown.root
	@hadd $@ $(BUILDDIR)/Hists_SYST_temp.root $(BUILDDIR)/Hists_EW.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_TT_RARE.root

$(BUILDDIR)/Hists_TT.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TTll.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TTbb.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TTcc.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_tuneup.root: ${CONFIG} $(BUILDDIR)/Craneen_TTUETuneup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TTUEUPNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_tunedown.root: ${CONFIG} $(BUILDDIR)/Craneen_TTUETunedown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TTUEDWNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_isrscaleup.root: ${CONFIG} $(BUILDDIR)/Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TTISRUPNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_isrscaledown.root: ${CONFIG} $(BUILDDIR)/Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TTISRDWNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_fsrscaleup.root: ${CONFIG} $(BUILDDIR)/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TTFSRUPNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_fsrscaledown.root: ${CONFIG} $(BUILDDIR)/Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TTFSRDWNORM} ${TARGETVAR} ${SUPPRESSOUT}

#@if [ -d "$(dir $@)" ]; then echo "$(BUILDDIR) exists" ; else mkdir $@ ; fi
