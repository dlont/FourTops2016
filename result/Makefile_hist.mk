#Order of arguments matters (first config.py, second input_tree.root, third scale)
include Makefile_norm.mk
%/Hists_data.root: config_t2h.py Craneen_Data_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@" 
	@mkdir -p $(@D)
	@tree2hists $^ $@ ${TREENAME} ${DATANORM}

%/Hists_TTTT.root: config_t2h.py Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@" 
	@mkdir -p $(@D)
	@tree2hists $^ $@ ${TREENAME}  ${TTTTNORM}

%/Hists_TT.root: config_t2h.py Craneen_TTJets_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@mkdir -p $(@D)
	@tree2hists $^ $@ ${TREENAME}  ${TTNORM}

%/Hists_WJets.root: config_t2h.py Craneen_WJets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@mkdir -p $(@D)
	@tree2hists $^ $@ ${TREENAME}  ${WJETSNORM}

%/Hists_T.root: %/Hists_T_tW.root %/Hists_Tbar_tW.root
	@echo "Merging single top histograms"
	@mkdir -p $(@D)
	@hadd -f $@ $^

%/Hists_T_tW.root: config_t2h.py Craneen_T_tW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@mkdir -p $(@D)
	@tree2hists $^ $@ ${TREENAME}  ${TNORM}

%/Hists_Tbar_tW.root: config_t2h.py Craneen_Tbar_tW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@mkdir -p $(@D)
	@tree2hists $^ $@ ${TREENAME}   ${TBARNORM}

