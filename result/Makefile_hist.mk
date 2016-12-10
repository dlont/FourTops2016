#Order of arguments matters (first config.py second input_tree.root)
%/Hists_data.root: config_t2h.py Craneen_Data_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@" 
	@mkdir -p $(@D)
	@tree2hists $^ $@ ${TREENAME}

%/Hists_TTTT.root: config_t2h.py Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@" 
	@mkdir -p $(@D)
	@tree2hists $^ $@ ${TREENAME}  

%/Hists_TT.root: config_t2h.py Craneen_TTJets_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@mkdir -p $(@D)
	@tree2hists $^ $@ ${TREENAME}  

%/Hists_WJets.root: config_t2h.py Craneen_WJets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@mkdir -p $(@D)
	@tree2hists $^ $@ ${TREENAME}  

%/Hists_T_tW.root: config_t2h.py Craneen_T_tW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@mkdir -p $(@D)
	@tree2hists $^ $@ ${TREENAME}  

%/Hists_Tbar_tW.root: config_t2h.py Craneen_Tbar_tW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@"
	@mkdir -p $(@D)
	@tree2hists $^ $@ ${TREENAME}  

