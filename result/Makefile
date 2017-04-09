
FORMAT=png
#PLOTS='.*BDT.*'
PLOTS='.*'
CUSTOMIZE=
INPUTLOCATION=./
ERA=full
DATALABEL:=Single \#mu (BCDEFGH)
#DATALABEL:=Single \#mu (BCDEF)
#DATALABEL:=Single \#mu (GH)

TREENAME:=Craneen__Mu

VPATH:=$(shell readlink -f ${INPUTLOCATION})

ROOTPLOT=../rootplot/bin/rootplot

SIZE="1000x1000"
LEGEND:="${DATALABEL},EW,ST,t\#bar{t},t\#bar{t}t\#bar{t} (\#times 100)"
LEGENDLOC:="upper right"

#include Makefile_norm.mk
include Makefile_hist.mk
include Makefile_merge.mk
include Makefile_plots.mk
include Makefile_cards.mk

.PHONY: norm
norm:
	@echo 'DATALUMI' ${DATALUMI}
	@echo 'TT' ${TTNORM}
	@echo 'TTFSRUP' ${TTFSRUPNORM}
	@echo 'TTFSRDW' ${TTFSRDWNORM}
	@echo 'TTISRUP' ${TTISRUPNORM}
	@echo 'TTISRDW' ${TTISRDWNORM}
	@echo 'TTUEUPNORM' ${TTUEUPNORM}
	@echo 'TTUEDWNORM' ${TTUEDWNORM}
	@echo 'TTTT' ${TTTTNORM}
	@echo 'WJETS' ${WJETSNORM}
	@echo 'STTW' ${TWNORM}
	@echo 'STBARTW' ${TBARWNORM}
	@echo 'STTCH' ${TTCHNORM}
	@echo 'STBARTCH' ${TBARTCHNORM}

.PHONY: dirs
dirs:
	@echo "Creating folders"
	-mkdir plots_el plots_mu

.PHONY: clean
clean:
	@echo "Remove plots"
	-rm -rf plots_el plots_mu
