#Order of arguments matters (first config.py, second input_tree.root, third scale)
include Makefile_norm.mk

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
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataC.root: ${CONFIG} $(BUILDDIR)/Craneen_DataC_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataD.root: ${CONFIG} $(BUILDDIR)/Craneen_DataD_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataE.root: ${CONFIG} $(BUILDDIR)/Craneen_DataE_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataF.root: ${CONFIG} $(BUILDDIR)/Craneen_DataF_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataG.root: ${CONFIG} $(BUILDDIR)/Craneen_DataG_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataH.root: ${CONFIG} $(BUILDDIR)/Craneen_DataH_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_data.root: $(BUILDDIR)/Hists_dataB.root $(BUILDDIR)/Hists_dataC.root $(BUILDDIR)/Hists_dataD.root $(BUILDDIR)/Hists_dataE.root $(BUILDDIR)/Hists_dataF.root $(BUILDDIR)/Hists_dataG.root $(BUILDDIR)/Hists_dataH.root
	@echo "Convert tree to hist $@ ($^)" 
	@hadd $@ $^

$(BUILDDIR)/Hists_TTTT_SCALED.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORMSCALED} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_EW.root: $(BUILDDIR)/Hists_WJets.root $(BUILDDIR)/Hists_DY50.root
	@echo "Merging EW histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTW.root: ${CONFIG} $(BUILDDIR)/Craneen_TTW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTWNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTZ.root: ${CONFIG} $(BUILDDIR)/Craneen_TTZ_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTZNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_RARE.root: $(BUILDDIR)/Hists_TTW.root $(BUILDDIR)/Hists_TTZ.root
	@echo "Merging TT RARE histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_WJets.root: ${CONFIG} $(BUILDDIR)/Craneen_WJets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${WJETSNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_DY50.root: ${CONFIG} $(BUILDDIR)/Craneen_DYJets_50MG_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${DY50JETSNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_T.root: $(BUILDDIR)/Hists_T_tW.root $(BUILDDIR)/Hists_Tbar_tW.root $(BUILDDIR)/Hists_T_tch.root $(BUILDDIR)/Hists_Tbar_tch.root
	@echo "Merging single top histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_T_tW.root: ${CONFIG} $(BUILDDIR)/Craneen_T_tW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TWNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_Tbar_tW.root: ${CONFIG} $(BUILDDIR)/Craneen_Tbar_tW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TBARWNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_T_tch.root: ${CONFIG} $(BUILDDIR)/Craneen_T_tch_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TTCHNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_Tbar_tch.root: ${CONFIG} $(BUILDDIR)/Craneen_Tbar_tch_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TBARTCHNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_SYST.root: $(BUILDDIR)/Hists_TT.root $(BUILDDIR)/Hists_tuneup.root $(BUILDDIR)/Hists_tunedown.root $(BUILDDIR)/Hists_isrscaleup.root $(BUILDDIR)/Hists_isrscaledown.root $(BUILDDIR)/Hists_fsrscaleup.root $(BUILDDIR)/Hists_fsrscaledown.root
	@echo "Preparing TT scale systematic histograms"
	@tools/scalehist.py -o $@ --nominal=$(BUILDDIR)/Hists_TT.root --isrscaleup=$(BUILDDIR)/Hists_isrscaleup.root --isrscaledown=$(BUILDDIR)/Hists_isrscaledown.root

$(BUILDDIR)/Hists_TT.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_tuneup.root: ${CONFIG} $(BUILDDIR)/Craneen_TTUETuneup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TTUEUPNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_tunedown.root: ${CONFIG} $(BUILDDIR)/Craneen_TTUETunedown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TTUEDWNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_isrscaleup.root: ${CONFIG} $(BUILDDIR)/Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TTISRUPNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_isrscaledown.root: ${CONFIG} $(BUILDDIR)/Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TTISRDWNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_fsrscaleup.root: ${CONFIG} $(BUILDDIR)/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TTFSRUPNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_fsrscaledown.root: ${CONFIG} $(BUILDDIR)/Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TTFSRDWNORM} ${SUPPRESSOUT}

#@if [ -d "$(dir $@)" ]; then echo "$(BUILDDIR) exists" ; else mkdir $@ ; fi
