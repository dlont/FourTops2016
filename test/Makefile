.PHONY: test

STATTEST=~/t2016/StatTest-master/runtests.py --colors
CONFIGDATA=testconf_data.qa
CONFIGMC=testconf_mc.qa
configdataunbinned=testconf_data_unbinned.qa
configmcunbinned=testconf_mc_unbinned.qa

test: report_data.pdf report_TTJets.pdf report_TTTT.pdf
	@echo "Make test"

# Assumes that there is only one file matching the wildcard expression. Should be Craneen_Data_Run2_TopTree_Study.root or Craneen_Data_Run2_TopTree_Study_XYZ.root
# Order of prerequisites matters! Assumes ${CONFIG} ${TARGET}  ${REFERENCE}
report_data.pdf: ${CONFIGDATA} ${TARGET}/Hists_data.root ${REFERENCE}/Hists_data.root
	@echo "Test data"
	${STATTEST} -g $@ $^

report_TTJets.pdf: ${CONFIGMC} ${TARGET}/Hists_TT.root ${REFERENCE}/Hists_TT.root
	@echo "Test TT MC"
	${STATTEST} -g $@ $^

report_TTTT.pdf: ${CONFIGMC} ${TARGET}/Hists_TTTT_SCALED.root ${REFERENCE}/Hists_TTTT_SCALED.root
	@echo "Test TTTT MC"
	${STATTEST} -g $@ $^

testunbinned: report_data_unbinned.pdf report_TTJets_unbinned.pdf report_TTTT_unbinned.pdf
	@echo "Make test"

# Assumes that there is only one file matching the wildcard expression. Should be Craneen_Data_Run2_TopTree_Study.root or Craneen_Data_Run2_TopTree_Study_XYZ.root
# Order of prerequisites matters! Assumes ${CONFIG} ${TARGET}  ${REFERENCE}
report_data_unbinned.pdf: ${CONFIGDATA} $(wildcard ${TARGET}/Craneen_Data_Run2_TopTree_Study*.root) $(wildcard ${REFERENCE}/Craneen_Data_Run2_TopTree_Study*.root)
	@echo "Test data"
	${STATTEST} -g $@ $^

report_TTJets_unbinned.pdf: ${configmcunbinned} $(wildcard ${TARGET}/Craneen_TTJets_powheg_Run2_TopTree_Study*.root) $(wildcard ${REFERENCE}/Craneen_TTJets_powheg_Run2_TopTree_Study*.root)
	@echo "Test TT MC"
	${STATTEST} -g $@ $^

#report_TTTT_unbinned.pdf: ${configmcunbinned} $(wildcard ${TARGET}/Craneen_ttttNLO_fsrdown_Run2_TopTree_Study*.root) $(wildcard ${REFERENCE}/Craneen_ttttNLO_Run2_TopTree_Study*.root)
report_TTTT_unbinned.pdf: ${configmcunbinned} $(wildcard ${TARGET}/Craneen_ttttNLO_Run2_TopTree_Study*.root) $(wildcard ${REFERENCE}/Craneen_ttttNLO_Run2_TopTree_Study*.root)
	@echo "Test TTTT MC"
	${STATTEST} -g $@ $^
