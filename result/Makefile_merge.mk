export ERA
DATASUFFIX=*
ifeq (${ERA},B)
DATASUFFIX=[B]*
endif
ifeq (${ERA},C)
DATASUFFIX=[C]*
endif
ifeq (${ERA},D)
DATASUFFIX=[D]*
endif
ifeq (${ERA},E)
DATASUFFIX=[E]*
endif
ifeq (${ERA},F)
DATASUFFIX=[F]*
endif
ifeq (${ERA},G)
DATASUFFIX=[G]*
endif
ifeq (${ERA},H)
DATASUFFIX=[H]*
endif
ifeq (${ERA},BCDEF)
DATASUFFIX=[B-F]*
endif
ifeq (${ERA},GH)
DATASUFFIX=[G-H]*
endif

SUPPRESSOUT=&>/dev/null

HADD=hadd -k

##################################### SINGLE LEPTON ##############################################
$(BUILDDIR)/Craneen_DataB_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_Data_Run2016B*.root)
	@echo ERA=$(ERA), DATASUFFIX=$(DATASUFFIX)
	@echo merging $@
	@$(HADD) $@ $^
$(BUILDDIR)/Craneen_DataC_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_Data_Run2016C*.root)
	@echo ERA=$(ERA), DATASUFFIX=$(DATASUFFIX)
	@echo merging $@
	@$(HADD) $@ $^
$(BUILDDIR)/Craneen_DataD_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_Data_Run2016D*.root)
	@echo ERA=$(ERA), DATASUFFIX=$(DATASUFFIX)
	@echo merging $@
	@$(HADD) $@ $^
$(BUILDDIR)/Craneen_DataE_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_Data_Run2016E*.root)
	@echo ERA=$(ERA), DATASUFFIX=$(DATASUFFIX)
	@echo merging $@
	@$(HADD) $@ $^
$(BUILDDIR)/Craneen_DataF_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_Data_Run2016F*.root)
	@echo ERA=$(ERA), DATASUFFIX=$(DATASUFFIX)
	@echo merging $@
	@$(HADD) $@ $^
$(BUILDDIR)/Craneen_DataG_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_Data_Run2016G*.root)
	@echo ERA=$(ERA), DATASUFFIX=$(DATASUFFIX)
	@echo merging $@
	@$(HADD) $@ $^
$(BUILDDIR)/Craneen_DataH_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_Data_Run2016H*.root)
	@echo ERA=$(ERA), DATASUFFIX=$(DATASUFFIX)
	@echo merging $@
	@$(HADD) $@ $^

$(BUILDDIR)/Craneen_Data_Run2_TopTree_Study.root: $(BUILDDIR)/Craneen_DataH_Run2_TopTree_Study.root $(BUILDDIR)/Craneen_DataG_Run2_TopTree_Study.root $(BUILDDIR)/Craneen_DataF_Run2_TopTree_Study.root $(BUILDDIR)/Craneen_DataE_Run2_TopTree_Study.root $(BUILDDIR)/Craneen_DataD_Run2_TopTree_Study.root $(BUILDDIR)/Craneen_DataC_Run2_TopTree_Study.root $(BUILDDIR)/Craneen_DataB_Run2_TopTree_Study.root
	@echo merging $@
	@$(HADD) $@ $^

$(BUILDDIR)/Craneen_Data_Run2_TopTree_Study$(DATASUFFIX).root: $(wildcard $(INPUTLOCATION)/Craneen_Data_Run2016$(DATASUFFIX).root)
	@echo ERA=$(ERA), DATASUFFIX=$(DATASUFFIX)
	@echo merging $@
	@$(HADD) $@ $^ 
##################################### JETHT ##############################################
$(BUILDDIR)/Craneen_dataJETHT_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_data_JetHt_Run_2016$(DATASUFFIX).root)
	@echo ERA=$(ERA), DATASUFFIX=$(DATASUFFIX)
	@echo merging $@
	@$(HADD) $@ $^ 
##################################### MET ##############################################
$(BUILDDIR)/Craneen_dataMET_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_data_MET_Run_2016$(DATASUFFIX).root)
	@echo ERA=$(ERA), DATASUFFIX=$(DATASUFFIX)
	@echo merging $@
	@$(HADD) $@ $^ 

$(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_ttttNLO_Run2*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_ttttNLO_jerup_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_ttttNLO_jerup_Run2_TopTree_Study*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_ttttNLO_jerdown_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_ttttNLO_jerdown_Run2_TopTree_Study*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_ttttNLO_jesup_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_ttttNLO_jesup_Run2_TopTree_Study*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_ttttNLO_jesdown_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_ttttNLO_jesdown_Run2_TopTree_Study*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_TTJets_powheg_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTJets_powheg_central*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTISRScaledown_powheg*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTISRScaleup_powheg*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTFSRScaledown_powheg*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTFSRScaleup_powheg*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_TTUETunedown_powheg_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTUETunedown_powheg*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_TTUETuneup_powheg_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTUETuneup_powheg*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_TTJets_powheg_jerup_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTJets_powheg_jerup_Run2_TopTree_Study*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_TTJets_powheg_jerdown_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTJets_powheg_jerdown_Run2_TopTree_Study*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_TTJets_powheg_jesup_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTJets_powheg_jesup_Run2_TopTree_Study*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}
	
$(BUILDDIR)/Craneen_TTJets_powheg_jesdown_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_TTJets_powheg_jesdown_Run2_TopTree_Study*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_T_tW_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_T_tW*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_Tbar_tW_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_Tbar_tW*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_T_tch_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_T_tch*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_Tbar_tch_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_Tbar_tch*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_WJets_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_WJets*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Craneen_QCD_MuEnriched_Run2_TopTree_Study.root: $(wildcard $(INPUTLOCATION)/Craneen_QCD_MuEnriched*.root)
	@echo merging $@
	@$(HADD) $@ $^ ${SUPPRESSOUT}
