#Order of arguments matters (first config.py, second input_tree.root, third scale)
include Makefile_norm.mk

CONFIG:=config_t2h.py
SUPPRESSOUT=>/dev/null

$(BUILDDIR)/Hists_data.root: ${CONFIG} $(BUILDDIR)/Craneen_Data_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT_SCALED.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORMSCALED} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_WJets.root: ${CONFIG} $(BUILDDIR)/Craneen_WJets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${WJETSNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_T.root: $(BUILDDIR)/Hists_T_tW.root $(BUILDDIR)/Hists_Tbar_tW.root
	@echo "Merging single top histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_T_tW.root: ${CONFIG} $(BUILDDIR)/Craneen_T_tW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_Tbar_tW.root: ${CONFIG} $(BUILDDIR)/Craneen_Tbar_tW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TBARNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_SYST.root: $(BUILDDIR)/Hists_TT.root $(BUILDDIR)/Hists_tuneup.root $(BUILDDIR)/Hists_tunedown.root $(BUILDDIR)/Hists_isrscaleup.root $(BUILDDIR)/Hists_isrscaledown.root $(BUILDDIR)/Hists_fsrscaleup.root $(BUILDDIR)/Hists_fsrscaledown.root
	@echo "Preparing TT scale systematic histograms"
	@tools/scalehist.py -o $@ --nominal=$(BUILDDIR)/Hists_TT.root --isrscaleup=$(BUILDDIR)/Hists_isrscaleup.root --isrscaledown=$(BUILDDIR)/Hists_isrscaledown.root

$(BUILDDIR)/Hists_TT.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_tuneup.root: ${CONFIG} $(BUILDDIR)/Craneen_TTUETuneup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_tunedown.root: ${CONFIG} $(BUILDDIR)/Craneen_TTUETunedown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_isrscaleup.root: ${CONFIG} $(BUILDDIR)/Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TTNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_isrscaledown.root: ${CONFIG} $(BUILDDIR)/Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TTNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_fsrscaleup.root: ${CONFIG} $(BUILDDIR)/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TTNORM} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_fsrscaledown.root: ${CONFIG} $(BUILDDIR)/Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@tree2hists $^ $@ ${TREENAME}   ${TTNORM} ${SUPPRESSOUT}

#@if [ -d "$(dir $@)" ]; then echo "$(BUILDDIR) exists" ; else mkdir $@ ; fi
