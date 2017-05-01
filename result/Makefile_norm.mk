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
	$(shell echo "from ROOT import TChain;a = TChain(\"bookkeeping\");a.Add(\"$(1)\");print ${DATALUMI}/(a.GetEntries()/$(2))"|python)
endef

DATANORM=1.
TTNNLOXS=831760 #fb
TTCHNNLOXS=136020 #fb
TBARTCHNNLOXS=80950 #fb
TWNNLOXS=35600 #fb
TBARWNNLOXS=35600 #fb
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
TTTTNORM:=$(shell echo "${TTTTNEGATIVEFRAC}*${DATALUMI}/266949.673913"|bc -l)
TTTTNORMSCALED:=$(shell echo "${TTTTSCALE}*${TTTTNORM}"|bc -l)
WJETSNORM:=$(shell echo "${DATALUMI}/0.472120891981"|bc -l)
TTCHNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_T_tch_Run2_TopTree_Study.root, ${TTCHNNLOXS})
TBARTCHNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_Tbar_tch_Run2_TopTree_Study.root, ${TBARTCHNNLOXS})
TWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_T_tW_Run2_TopTree_Study.root, ${TWNNLOXS})
TBARWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_Tbar_tW_Run2_TopTree_Study.root, ${TBARWNNLOXS})

