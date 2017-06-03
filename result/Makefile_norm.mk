export TREENAME
export TTCENTRAL
#Muons
ifeq (${TREENAME},Craneen__Mu)
DATALUMI=35.83		#V9
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
	$(shell echo "import ROOT;a=ROOT.TChain(\"bookkeeping\");a.Add(\"$(1)\");h=ROOT.TH1D(\"h\",\"\",1,-1.,1.);a.Draw(\"0.>>h\",\"Genweight\");nMC=h.Integral();print ${DATALUMI}/(nMC/$(2))"|python - -b)
endef

DATANORM=1.
TTTTNLOXS=9.2 #fb
TTNNLOXS=831760 #fb 				checked
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
DY50XS=5765400. # fb 				checked 
DY1J50XS=101600. # fb				checked
DY2J50XS=33140. # fb				checked
DY3J50XS=9640. # fb				checked
DY4J50XS=5140. # fb				checked
#SingleMuon reprov3
TTNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_TTJets_$(TTCENTRAL)_Run2_TopTree_Study.root, ${TTNNLOXS})
TTISRUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTISRDWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTFSRUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTFSRDWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTUEUPNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTUETuneup_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
TTUEDWNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTUETunedown_powheg_Run2_TopTree_Study.root, ${TTNNLOXS})
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
TTHNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_TTH_Run2_TopTree_Study.root, ${TTHNLOXS})
TTTTNORM=$(call calcEqLumiMCNLO, ${BUILDDIR}/Craneen_ttttNLO_Run2_TopTree_Study.root, ${TTTTNLOXS})
#TTTTNORM=$(call calcEqLumi, ${BUILDDIR}/Craneen_ttttNLO_Run2_TopTree_Study.root, ${TTTTNLOXS})
TTTTNORMSCALED=$(shell echo "${TTTTSCALE}*${TTTTNORM}"|bc -l)

