export TREENAME
#Muons
ifeq (${TREENAME},Craneen__Mu)
DATALUMI=36.811
ifeq (${ERA},B)
DATALUMI=5.887798814599 #BCDEF V4
endif
ifeq (${ERA},C)
DATALUMI=2.645968083093 #BCDEF V4
endif
ifeq (${ERA},D)
DATALUMI=4.353448810554 #BCDEF V4
endif
ifeq (${ERA},E)
DATALUMI=4.117098328143 #BCDEF V4
endif
ifeq (${ERA},F)
DATALUMI=3.185972003954 #BCDEF V4
endif
ifeq (${ERA},G)
DATALUMI=7.702190323334 #BCDEF V4
endif
ifeq (${ERA},H)
DATALUMI=8.857033337174 #BCDEF V4
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
DATALUMI=35.82604485738
ifeq (${ERA},BCDEF)
DATALUMI=20.194218843159 #BCDEF V4
endif
ifeq (${ERA},GH)
DATALUMI=16.577820960675 #GH V4
endif
endif

define calcEqLumi
	$(shell echo "from ROOT import TChain;a = TChain(\"bookkeeping\");a.Add(\"$(1)\");print ${DATALUMI}/(a.GetEntries()/$(2))"|python - -b)
endef

define calcEqLumiMCNLO
	$(shell echo "import ROOT;a=ROOT.TChain(\"bookkeeping\");a.Add(\"$(1)\");h=ROOT.TH1D(\"h\",\"\",1,-1.,1.);a.Draw(\"0.>>h\",\"Genweight\");nMC=h.Integral();print ${DATALUMI}/(nMC/$(2))"|python - -b)
endef

DATANORM=1.
TTTTNLOXS=9.2 #fb
TTNNLOXS=831760 #fb
TTCHNNLOXS=136020 #fb
TBARTCHNNLOXS=80950 #fb
TWNNLOXS=35600 #fb
TBARWNNLOXS=35600 #fb
WJETSNNLOXS=61526700 #fb
TTWNLOXS=1.
TTZNLOXS=1.
TTHNLOXS=1.
DY50XS=5765400. # 1921800 X 3 #fb 6025200
#SingleMuon reprov3
TTNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTJets_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTISRUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTISRDWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTFSRUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTFSRDWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTUEUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTUETuneup_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTUEDWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTUETunedown_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTTTNEGATIVEFRAC:=0.449449
TTTTSCALE:=100.0
#TTTTNORM:=$(shell echo "${TTTTNEGATIVEFRAC}*${DATALUMI}/266949.673913"|bc -l)
WJETSNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_WJets_Run2_TopTree_Study.root, ${WJETSNNLOXS})
DY50JETSNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_DYJets_50MG_Run2_TopTree_Study.root, ${DY50XS})
TTCHNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_T_tch_Run2_TopTree_Study.root, ${TTCHNNLOXS})
TBARTCHNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_Tbar_tch_Run2_TopTree_Study.root, ${TBARTCHNNLOXS})
TWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_T_tW_Run2_TopTree_Study.root, ${TWNNLOXS})
TBARWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_Tbar_tW_Run2_TopTree_Study.root, ${TBARWNNLOXS})
#TTWNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTW_Run2_TopTree_Study.root, ${TTWNLOXS})
#TTZNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTZ_Run2_TopTree_Study.root, ${TTZNLOXS})
TTTTNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_Run2_TopTree_Study.root, ${TTTTNLOXS})
#TTTTNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_ttttNLO_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTNORMSCALED=$(shell echo "${TTTTSCALE}*${TTTTNORM}"|bc -l)

