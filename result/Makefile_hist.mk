#Order of arguments matters (first config.py, second input_tree.root, third scale)
include Makefile_norm.mk
$(BUILDDIR)/Hists_data.root: config_t2h.py $(BUILDDIR)/Craneen_Data_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@" 
	@tree2hists $^ $@ ${TREENAME} ${DATANORM}

$(BUILDDIR)/Hists_TTTT.root: config_t2h.py $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@" 
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM}

$(BUILDDIR)/Hists_WJets.root: config_t2h.py $(BUILDDIR)/Craneen_WJets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@tree2hists $^ $@ ${TREENAME}  ${WJETSNORM}

$(BUILDDIR)/Hists_T.root: $(BUILDDIR)/Hists_T_tW.root $(BUILDDIR)/Hists_Tbar_tW.root
	@echo "Merging single top histograms"
	@hadd -f $@ $^

$(BUILDDIR)/Hists_T_tW.root: config_t2h.py $(BUILDDIR)/Craneen_T_tW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@tree2hists $^ $@ ${TREENAME}  ${TNORM}

$(BUILDDIR)/Hists_Tbar_tW.root: config_t2h.py $(BUILDDIR)/Craneen_Tbar_tW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@tree2hists $^ $@ ${TREENAME}   ${TBARNORM}

$(BUILDDIR)/Hists_SYST.root: $(BUILDDIR)/Hists_TT.root $(BUILDDIR)/Hists_tuneup.root $(BUILDDIR)/Hists_tunedown.root $(BUILDDIR)/Hists_isrscaleup.root $(BUILDDIR)/Hists_isrscaledown.root $(BUILDDIR)/Hists_fsrscaleup.root $(BUILDDIR)/Hists_fsrscaledown.root
	@echo "Preparing TT scale systematic histograms"
	@tools/scalehist.py -o $@ --nominal=$(dir $@)/Hists_TT.root --isrscaleup=$(dir $@)/Hists_isrscaleup.root --isrscaledown=$(dir $@)/Hists_isrscaledown.root

$(BUILDDIR)/Hists_TT.root: config_t2h.py $(BUILDDIR)/Craneen_TTJets_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM}

$(BUILDDIR)/Hists_tuneup.root: config_t2h.py $(BUILDDIR)/Craneen_TTUETuneup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM}

$(BUILDDIR)/Hists_tunedown.root: config_t2h.py $(BUILDDIR)/Craneen_TTUETunedown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM}

$(BUILDDIR)/Hists_isrscaleup.root: config_t2h.py $(BUILDDIR)/Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@tree2hists $^ $@ ${TREENAME}   ${TTNORM}

$(BUILDDIR)/Hists_isrscaledown.root: config_t2h.py $(BUILDDIR)/Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@tree2hists $^ $@ ${TREENAME}   ${TTNORM}

$(BUILDDIR)/Hists_fsrscaleup.root: config_t2h.py $(BUILDDIR)/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@tree2hists $^ $@ ${TREENAME}   ${TTNORM}

$(BUILDDIR)/Hists_fsrscaledown.root: config_t2h.py $(BUILDDIR)/Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@tree2hists $^ $@ ${TREENAME}   ${TTNORM}

#@if [ -d "$(dir $@)" ]; then echo "$(BUILDDIR) exists" ; else mkdir $@ ; fi
