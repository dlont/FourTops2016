export TREENAME
ifeq (${TREENAME},Craneen__Mu)
DATALUMI=36.7684
endif
ifeq (${TREENAME},Craneen__El)
DATALUMI=36.7720
endif
DATANORM=1.
#SingleMuon reprov3
TTNORM:=$(shell echo "${DATALUMI}/92.9806638934"|bc -l)
TTSCUPNORM:=$(shell echo "${DATALUMI}/1."|bc -l)
TTSCDWNORM:=$(shell echo "${DATALUMI}/1."|bc -l)
TTTTNEGATIVEFRAC:=0.449449
TTTTSCALE:=100.0
TTTTNORM:=$(shell echo "${TTTTNEGATIVEFRAC}*${DATALUMI}/266949.673913"|bc -l)
TTTTNORMSCALED:=$(shell echo "${TTTTSCALE}*${TTTTNORM}"|bc -l)
WJETSNORM:=$(shell echo "${DATALUMI}/0.472120891981"|bc -l)
TNORM:=$(shell echo "${DATALUMI}/195.122162921"|bc -l)
TBARNORM:=$(shell echo "${DATALUMI}/191.754634831"|bc -l)

