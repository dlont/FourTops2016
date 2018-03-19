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
	@${TREE2HIST} $^ $@ ${TREENAME} ${DATANORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataC.root: ${CONFIG} $(BUILDDIR)/Craneen_DataC_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME} ${DATANORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataD.root: ${CONFIG} $(BUILDDIR)/Craneen_DataD_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME} ${DATANORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataE.root: ${CONFIG} $(BUILDDIR)/Craneen_DataE_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME} ${DATANORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataF.root: ${CONFIG} $(BUILDDIR)/Craneen_DataF_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME} ${DATANORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataG.root: ${CONFIG} $(BUILDDIR)/Craneen_DataG_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME} ${DATANORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_dataH.root: ${CONFIG} $(BUILDDIR)/Craneen_DataH_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME} ${DATANORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_data.root: $(BUILDDIR)/Hists_dataB.root $(BUILDDIR)/Hists_dataC.root $(BUILDDIR)/Hists_dataD.root $(BUILDDIR)/Hists_dataE.root $(BUILDDIR)/Hists_dataF.root $(BUILDDIR)/Hists_dataG.root $(BUILDDIR)/Hists_dataH.root
	@echo "Merge data histograms $@ ($^)"
	@hadd -f $@ $^

$(BUILDDIR)/Hists_TTTT_SCALED.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORMSCALED} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTT.root: ${CONFIG} $(BUILDDIR)/Craneen_ttttNLO_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTTNORM} ${TARGETVAR} ${SUPPRESSOUT}

#$(BUILDDIR)/Hists_EW.root: $(BUILDDIR)/Hists_WJets.root $(BUILDDIR)/Hists_W1Jets.root $(BUILDDIR)/Hists_W2Jets.root $(BUILDDIR)/Hists_W3Jets.root $(BUILDDIR)/Hists_W4Jets.root $(BUILDDIR)/Hists_DY50.root $(BUILDDIR)/Hists_DY1J50.root $(BUILDDIR)/Hists_DY2J50.root  $(BUILDDIR)/Hists_DY3J50.root  $(BUILDDIR)/Hists_DY4J50.root
$(BUILDDIR)/Hists_EW.root: $(BUILDDIR)/Hists_W1Jets.root $(BUILDDIR)/Hists_W2Jets.root $(BUILDDIR)/Hists_W3Jets.root $(BUILDDIR)/Hists_W4Jets.root $(BUILDDIR)/Hists_DY1J50.root $(BUILDDIR)/Hists_DY2J50.root  $(BUILDDIR)/Hists_DY3J50.root  $(BUILDDIR)/Hists_DY4J50.root
	@echo "Merging EW histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTW.root: ${CONFIG} $(BUILDDIR)/Craneen_TTW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTWNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTZ.root: ${CONFIG} $(BUILDDIR)/Craneen_TTZ_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTZNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTH.root: ${CONFIG} $(BUILDDIR)/Craneen_TTH_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTHNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTJ.root: ${CONFIG} $(BUILDDIR)/Craneen_TTTJ_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTJNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTTW.root: ${CONFIG} $(BUILDDIR)/Craneen_TTTW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTTWNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTWZ.root: ${CONFIG} $(BUILDDIR)/Craneen_TTWZ_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTWZNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTZZ.root: ${CONFIG} $(BUILDDIR)/Craneen_TTZZ_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTZZNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTZH.root: ${CONFIG} $(BUILDDIR)/Craneen_TTZH_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTZHNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTHH.root: ${CONFIG} $(BUILDDIR)/Craneen_TTHH_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTHHNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTXY.root: $(BUILDDIR)/Hists_TTTJ.root $(BUILDDIR)/Hists_TTTW.root $(BUILDDIR)/Hists_TTWZ.root $(BUILDDIR)/Hists_TTZZ.root $(BUILDDIR)/Hists_TTZH.root $(BUILDDIR)/Hists_TTHH.root
	@echo "Merging TTXY histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTWXY.root: $(BUILDDIR)/Hists_TTXY.root $(BUILDDIR)/Hists_TTW.root
	@echo "Merging TTWXY histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_HZmerged.root: $(BUILDDIR)/Hists_TTZ.root $(BUILDDIR)/Hists_TTH.root
	@echo "Merging TTH and TTZ histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_RARE.root: $(BUILDDIR)/Hists_TTW.root $(BUILDDIR)/Hists_TTZ.root $(BUILDDIR)/Hists_TTH.root $(BUILDDIR)/Hists_TTXY.root
	@echo "Merging TT RARE histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TTV.root: $(BUILDDIR)/Hists_TTW.root $(BUILDDIR)/Hists_TTZ.root
	@echo "Merging TT RARE histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_WJets.root: ${CONFIG} $(BUILDDIR)/Craneen_WJets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${WJETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_W1Jets.root: ${CONFIG} $(BUILDDIR)/Craneen_W1Jets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${W1JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_W2Jets.root: ${CONFIG} $(BUILDDIR)/Craneen_W2Jets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${W2JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_W3Jets.root: ${CONFIG} $(BUILDDIR)/Craneen_W3Jets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${W3JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_W4Jets.root: ${CONFIG} $(BUILDDIR)/Craneen_W4Jets_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${W4JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_DY50.root: ${CONFIG} $(BUILDDIR)/Craneen_DYJets_50MG_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${DY50JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_DY1J50.root: ${CONFIG} $(BUILDDIR)/Craneen_DY1Jets_50MG_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${DY1J50JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_DY2J50.root: ${CONFIG} $(BUILDDIR)/Craneen_DY2Jets_50MG_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${DY2J50JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_DY3J50.root: ${CONFIG} $(BUILDDIR)/Craneen_DY3Jets_50MG_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${DY3J50JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_DY4J50.root: ${CONFIG} $(BUILDDIR)/Craneen_DY4Jets_50MG_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${DY4J50JETSNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_T.root: $(BUILDDIR)/Hists_T_tW.root $(BUILDDIR)/Hists_Tbar_tW.root $(BUILDDIR)/Hists_T_tch.root $(BUILDDIR)/Hists_Tbar_tch.root
	@echo "Merging single top histograms"
	@hadd -f $@ $^ ${SUPPRESSOUT}

$(BUILDDIR)/Hists_T_tW.root: ${CONFIG} $(BUILDDIR)/Craneen_T_tW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TWNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_Tbar_tW.root: ${CONFIG} $(BUILDDIR)/Craneen_Tbar_tW_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}   ${TBARWNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_T_tch.root: ${CONFIG} $(BUILDDIR)/Craneen_T_tch_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTCHNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_Tbar_tch.root: ${CONFIG} $(BUILDDIR)/Craneen_Tbar_tch_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}   ${TBARTCHNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_SYST.root: $(BUILDDIR)/Hists_TT.root $(BUILDDIR)/Hists_tuneup.root $(BUILDDIR)/Hists_tunedown.root $(BUILDDIR)/Hists_isrscaleup.root $(BUILDDIR)/Hists_isrscaledown.root $(BUILDDIR)/Hists_fsrscaleup.root $(BUILDDIR)/Hists_fsrscaledown.root $(BUILDDIR)/Hists_EW.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_TT_RARE.root
	@echo "Preparing TT scale systematic histograms"
	@tools/scalehist.py -o $(BUILDDIR)/Hists_SYST_temp.root --nominal=$(BUILDDIR)/Hists_TT.root --isrscaleup=$(BUILDDIR)/Hists_isrscaleup.root --isrscaledown=$(BUILDDIR)/Hists_isrscaledown.root
	@hadd $@ $(BUILDDIR)/Hists_SYST_temp.root $(BUILDDIR)/Hists_EW.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_TT_RARE.root

$(BUILDDIR)/Hists_TT_central.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} ${TARGETVAR} ${SUPPRESSOUT}
#$(BUILDDIR)/Hists_TTll.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
#	@echo "Convert tree to hist $@ ($^)"
#	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} ${TARGETVAR} ${SUPPRESSOUT}
#$(BUILDDIR)/Hists_TTbb.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
#	@echo "Convert tree to hist $@ ($^)"
#	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} ${TARGETVAR} ${SUPPRESSOUT}
#$(BUILDDIR)/Hists_TTcc.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root
#	@echo "Convert tree to hist $@ ($^)"
#	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTNORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TTll.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_powheg_mixture_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_MIXTURE_NORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TTbb.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_powheg_mixture_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_MIXTURE_NORM} ${TARGETVAR} ${SUPPRESSOUT}
$(BUILDDIR)/Hists_TTcc.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_powheg_mixture_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_MIXTURE_NORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_tuneup.root: ${CONFIG} $(BUILDDIR)/Craneen_TTUETuneup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTUEUPNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_tunedown.root: ${CONFIG} $(BUILDDIR)/Craneen_TTUETunedown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TTUEDWNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_isrscaleup.root: ${CONFIG} $(BUILDDIR)/Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}   ${TTISRUPNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_isrscaledown.root: ${CONFIG} $(BUILDDIR)/Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}   ${TTISRDWNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_fsrscaleup.root: ${CONFIG} $(BUILDDIR)/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}   ${TTFSRUPNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_fsrscaledown.root: ${CONFIG} $(BUILDDIR)/Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}   ${TTFSRDWNORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_mass1665.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_mass1665_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_M1665_NORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_mass1695.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_mass1695_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_M1695_NORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_mass1715.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_mass1715_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_M1715_NORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_mass1735.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_mass1735_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_M1735_NORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_mass1755.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_mass1755_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_M1755_NORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_mass1785.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_mass1785_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_M1785_NORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_width02.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_width02_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_W02_NORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_width05.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_width05_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_W05_NORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_width2.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_width2_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_W2_NORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_width4.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_width4_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_W4_NORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT_width8.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_$(TTCENTRAL)_width8_Run2_TopTree_Study.root
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_W8_NORM} ${TARGETVAR} ${SUPPRESSOUT}

$(BUILDDIR)/Hists_TT.root: ${CONFIG} $(BUILDDIR)/Craneen_TTJets_powheg_mixture_Run2_TopTree_Study.root
	@echo "Merge nominal, mass variation and width variation samples"
	@echo "Convert tree to hist $@ ($^)"
	@${TREE2HIST} $^ $@ ${TREENAME}  ${TT_MIXTURE_NORM} ${TARGETVAR} ${SUPPRESSOUT}

mergechannelsplots:
	@echo "Combining Electron and Muon histograms"
	@for i in $(BUILDDIR_EL)/Hist*.root; do hadd $(BUILDDIR)/`basename $$i` $(BUILDDIR_MU)/`basename $$i`;done

#@if [ -d "$(dir $@)" ]; then echo "$(BUILDDIR) exists" ; else mkdir $@ ; fi
