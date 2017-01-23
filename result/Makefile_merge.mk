SUPPRESSOUT=&>/dev/null

$(BUILDDIR)/Craneen_Data_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_Data_Run2016*.root)
	@echo merging $@
	@hadd $@ $^ 

$(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_ttttNLO*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_ttttNLO_jerup_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_ttttNLO_jerup_Run2_TopTree_Study*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_ttttNLO_jerdown_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_ttttNLO_jerdown_Run2_TopTree_Study*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_ttttNLO_jesup_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_ttttNLO_jesup_Run2_TopTree_Study*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_ttttNLO_jesdown_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_ttttNLO_jesdown_Run2_TopTree_Study*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_TTJets_powheg_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTJets_powheg*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTISRScaledown_powheg*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTISRScaleup_powheg*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTFSRScaledown_powheg*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTFSRScaleup_powheg*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_TTUETunedown_powheg_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTUETunedown_powheg*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_TTUETuneup_powheg_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTUETuneup_powheg*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_TTJets_powheg_jerup_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTJets_powheg_jerup_Run2_TopTree_Study*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_TTJets_powheg_jerdown_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTJets_powheg_jerdown_Run2_TopTree_Study*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_TTJets_powheg_jesup_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTJets_powheg_jesup_Run2_TopTree_Study*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_TTJets_powheg_jesdown_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTJets_powheg_jesdown_Run2_TopTree_Study*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_T_tW_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_T_tW*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_Tbar_tW_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_Tbar_tW*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_WJets_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_WJets*.root)
	@echo merging $@
	@hadd $@ $^ ${SUPPRESSOUT}

