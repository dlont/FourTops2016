export TREENAME
export TTCENTRAL
#Muons
ifeq (${TREENAME},Craneen__Mu)
DATALUMI=35.83		#V9
DATALABEL=Single \#mu
ifeq (${ERA},B)
DATALUMI=5.743725979478  #BCDEF V9
endif
ifeq (${ERA},C)
DATALUMI=2.573399420069 #BCDEF V9
endif
ifeq (${ERA},D)
DATALUMI=4.248383597366 #BCDEF V9
endif
ifeq (${ERA},E)
DATALUMI=4.008375931882 #BCDEF V9
endif
ifeq (${ERA},F)
DATALUMI=3.101618412335 #BCDEF V9
endif
ifeq (${ERA},G)
DATALUMI=7.540487735974  #BCDEF V9
endif
ifeq (${ERA},H)
DATALUMI=8.605689861909 #BCDEF V9
endif
ifeq (${ERA},BCDEF)
DATALUMI=20.190286040343 #BCDEF V4
endif
ifeq (${ERA},GH)
DATALUMI=16.57809061136 #GH
endif
endif

#Electrons
ifeq (${TREENAME},Craneen__El)
DATALUMI=35.84		# V5
DATALABEL=Single e
ifeq (${ERA},BCDEF)
DATALUMI=20.194218843159 #BCDEF V4
endif
ifeq (${ERA},GH)
DATALUMI=16.577820960675 #GH V4
endif
endif

define calcEqLumi
	$(shell echo "from ROOT import TChain;a = TChain(\"bookkeeping\");a.Add(\"$(1)\");print ${DATALUMI}/(a.GetEntries()/float($(2)))"|python - -b)
endef

define calcEqLumiMCNLO
	$(shell echo "import ROOT;a=ROOT.TChain(\"bookkeeping\");a.Add(\"$(1)\");h=ROOT.TH1D(\"h\",\"\",1,-1.,1.);a.Draw(\"0.>>h\",\"Genweight\",\"goff\");nMC=h.Integral();print ${DATALUMI}/(nMC/$(2))"|python - -b)
endef

DATANORM=1.
TTTTNLOXS=9.2 #fb				checked
TTNNLOXS=831760 #fb 				checked
TTFILTNNLOXS=2453.69 #fb			TTNNLOXS*FILTER EFF
TTCHNNLOXS=136020 #fb
TBARTCHNNLOXS=80950 #fb
TWNNLOXS=35600 #fb
TBARWNNLOXS=35600 #fb
WJETSNNLOXS  =61526700 #fb			checked
W1JJETSNNLOXS=9493000 #fb			checked
W2JJETSNNLOXS=3120000 #fb			checked
W3JJETSNNLOXS=942300 #fb			checked
W4JJETSNNLOXS=524200 #fb			checked
TTWNLOXS=611.	#fb				checked
TTZNLOXS=783.	#fb				checked
TTHNLOXS=293.	#fb				checked
TTTJNLOXS=0.4741#fb				checked
TTTWNLOXS=7.882	#fb				checked
TTWZNLOXS=2.974	#fb				checked
TTZZNLOXS=1.572	#fb				checked
TTZHNLOXS=1.253	#fb				checked
TTHHNLOXS=0.7408#fb				checked
DY50XS=5765400. # fb 				checked 
DY1J50XS=101600. # fb				checked
DY2J50XS=33140. # fb				checked
DY3J50XS=9640. # fb				checked
DY4J50XS=5140. # fb				checked
#SingleMuon reprov3
TTNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root, ${TTNNLOXS})
TT_MIXTURE_NORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_mixture_Run2_TopTree_Study.root, ${TTNNLOXS})
TT_M1665_NORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_mass1665_Run2_TopTree_Study.root, ${TTNNLOXS})
TT_M1695_NORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_mass1695_Run2_TopTree_Study.root, ${TTNNLOXS})
TT_M1715_NORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_mass1715_Run2_TopTree_Study.root, ${TTNNLOXS})
TT_M1735_NORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_mass1735_Run2_TopTree_Study.root, ${TTNNLOXS})
TT_M1755_NORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_mass1755_Run2_TopTree_Study.root, ${TTNNLOXS})
TT_M1785_NORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_mass1785_Run2_TopTree_Study.root, ${TTNNLOXS})
TT_W02_NORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_width02_Run2_TopTree_Study.root, ${TTNNLOXS})
TT_W05_NORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_width05_Run2_TopTree_Study.root, ${TTNNLOXS})
TT_W2_NORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_width2_Run2_TopTree_Study.root, ${TTNNLOXS})
TT_W4_NORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_width4_Run2_TopTree_Study.root, ${TTNNLOXS})
TT_W8_NORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_width8_Run2_TopTree_Study.root, ${TTNNLOXS})

TTJERUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_jerup_Run2_TopTree_Study.root, ${TTNNLOXS})
TTJERDOWNNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_jerdown_Run2_TopTree_Study.root, ${TTNNLOXS})
TTJESUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_jesup_Run2_TopTree_Study.root, ${TTNNLOXS})
TTJESDOWNNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_jesdown_Run2_TopTree_Study.root, ${TTNNLOXS})
TTSUBPUUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_SubTotalPileUp_jesup_Run2_TopTree_Study.root, ${TTNNLOXS})
TTSUBPUDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_SubTotalPileUp_jesdown_Run2_TopTree_Study.root, ${TTNNLOXS})
TTSUBPTUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_SubTotalPt_jesup_Run2_TopTree_Study.root, ${TTNNLOXS})
TTSUBPTDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_SubTotalPt_jesdown_Run2_TopTree_Study.root, ${TTNNLOXS})
TTSUBRELUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_SubTotalRelative_jesup_Run2_TopTree_Study.root, ${TTNNLOXS})
TTSUBRELDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_SubTotalRelative_jesdown_Run2_TopTree_Study.root, ${TTNNLOXS})
TTSUBSCALEUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_SubTotalScale_jesup_Run2_TopTree_Study.root, ${TTNNLOXS})
TTSUBSCALEDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_SubTotalScale_jesdown_Run2_TopTree_Study.root, ${TTNNLOXS})
TTSUBTIMEUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_SubTotalTimePtEta_jesup_Run2_TopTree_Study.root, ${TTNNLOXS})
TTSUBTIMEDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_SubTotalTimePtEta_jesdown_Run2_TopTree_Study.root, ${TTNNLOXS})
TTSUBFLAVUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_SubTotalFlavor_jesup_Run2_TopTree_Study.root, ${TTNNLOXS})
TTSUBFLAVDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_SubTotalFlavor_jesdown_Run2_TopTree_Study.root, ${TTNNLOXS})
TTBTAGJESUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root, ${TTNNLOXS})
TTBTAGJESDOWNNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root, ${TTNNLOXS})

TTISRUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTISRDWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTFSRUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTFSRDWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTUEUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTUETuneup_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTUEDWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTUETunedown_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTHDAMPUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTHdampup_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTHDAMPDWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTHdampdown_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})


TTFILTNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_central_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTJERUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_jerup_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTJERDOWNNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_jerdown_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTJESUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_jesup_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTJESDOWNNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_jesdown_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTSUBPUUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_SubTotalPileUp_jesup_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTSUBPUDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_SubTotalPileUp_jesdown_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTSUBPTUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_SubTotalPt_jesup_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTSUBPTDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_SubTotalPt_jesdown_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTSUBRELUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_SubTotalRelative_jesup_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTSUBRELDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_SubTotalRelative_jesdown_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTSUBSCALEUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_SubTotalScale_jesup_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTSUBSCALEDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_SubTotalScale_jesdown_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTSUBTIMEUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_SubTotalTimePtEta_jesup_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTSUBTIMEDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_SubTotalTimePtEta_jesdown_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTSUBFLAVUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_SubTotalFlavor_jesup_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTSUBFLAVDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_SubTotalFlavor_jesdown_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTBTAGJESUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_jesup_Run2_TopTree_Study.root, ${TTFILTNNLOXS})
TTFILTBTAGJESDOWNNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJetsFilt_$(TTCENTRAL)_jesdown_Run2_TopTree_Study.root, ${TTFILTNNLOXS})

TTTTNEGATIVEFRAC:=0.449449
TTTTSCALE:=10.0
#TTTTNORM:=$(shell echo "${TTTTNEGATIVEFRAC}*${DATALUMI}/266949.673913"|bc -l)
WJETSNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_WJets_Run2_TopTree_Study.root, ${WJETSNNLOXS})
W1JETSNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_W1Jets_Run2_TopTree_Study.root, ${W1JJETSNNLOXS})
W2JETSNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_W2Jets_Run2_TopTree_Study.root, ${W2JJETSNNLOXS})
W3JETSNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_W3Jets_Run2_TopTree_Study.root, ${W3JJETSNNLOXS})
W4JETSNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_W4Jets_Run2_TopTree_Study.root, ${W4JJETSNNLOXS})
DY50JETSNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_DYJets_50MG_Run2_TopTree_Study.root, ${DY50XS})
DY1J50JETSNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_DY1Jets_50MG_Run2_TopTree_Study.root, ${DY1J50XS})
DY2J50JETSNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_DY2Jets_50MG_Run2_TopTree_Study.root, ${DY1J50XS})
DY3J50JETSNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_DY3Jets_50MG_Run2_TopTree_Study.root, ${DY3J50XS})
DY4J50JETSNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_DY4Jets_50MG_Run2_TopTree_Study.root, ${DY4J50XS})
TTCHNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_T_tch_Run2_TopTree_Study.root, ${TTCHNNLOXS})
TBARTCHNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_Tbar_tch_Run2_TopTree_Study.root, ${TBARTCHNNLOXS})
TWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_T_tW_Run2_TopTree_Study.root, ${TWNNLOXS})
TBARWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_Tbar_tW_Run2_TopTree_Study.root, ${TBARWNNLOXS})
TTWNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTW_Run2_TopTree_Study.root, ${TTWNLOXS})
TTZNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTZ_Run2_TopTree_Study.root, ${TTZNLOXS})
TTHNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTH_Run2_TopTree_Study.root, ${TTHNLOXS})
TTTJNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTTJ_Run2_TopTree_Study.root, ${TTTJNLOXS})
TTTWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTTW_Run2_TopTree_Study.root, ${TTTWNLOXS})
TTWZNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTWZ_Run2_TopTree_Study.root, ${TTWZNLOXS})
TTZZNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTZZ_Run2_TopTree_Study.root, ${TTZZNLOXS})
TTZHNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTZH_Run2_TopTree_Study.root, ${TTZHNLOXS})
TTHHNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTHH_Run2_TopTree_Study.root, ${TTHHNLOXS})
#signal
TTTTNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTISRUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_isrup_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTISRDWNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_isrdown_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTFSRUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_fsrup_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTFSRDWNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_fsrdown_Run2_TopTree_Study.root, ${TTTTNLOXS})
#TTTTNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_ttttNLO_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTNORMSCALED=$(shell echo "${TTTTSCALE}*${TTTTNORM}"|bc -l)

TTTTJERUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_jerup_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTJERDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_jerdown_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTJESUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_jesup_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTJESDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_jesdown_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTSUBPUUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_SubTotalPileUp_jesup_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTSUBPUDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_SubTotalPileUp_jesdown_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTSUBPTUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_SubTotalPt_jesup_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTSUBPTDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_SubTotalPt_jesdown_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTSUBRELUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_SubTotalRelative_jesup_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTSUBRELDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_SubTotalRelative_jesdown_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTSUBSCALEUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_SubTotalScale_jesup_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTSUBSCALEDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_SubTotalScale_jesdown_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTSUBTIMEUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_SubTotalTimePtEta_jesup_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTSUBTIMEDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_SubTotalTimePtEta_jesdown_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTSUBFLAVUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_SubTotalFlavor_jesup_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTSUBFLAVDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_SubTotalFlavor_jesdown_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTBTAGJESUPNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTBTAGJESDOWNNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_Run2_TopTree_Study.root, ${TTTTNLOXS})
