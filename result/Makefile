
FORMAT=png
PLOTS='.*bdt.*'
#PLOTS='.*'
CUSTOMIZE=
INPUTLOCATION=./
DATALABEL:=Single \#mu (BCDEFGH)
TREENAME:=Craneen__Mu

VPATH:=$(shell readlink -f ${INPUTLOCATION})

ROOTPLOT=../rootplot/bin/rootplot

SIZE="1000x1000"
LEGEND:="${DATALABEL},EW,Single top,t\#bar{t},t\#bar{t}t\#bar{t} (\#times 100)"

#include Makefile_norm.mk
include Makefile_hist.mk
include Makefile_merge.mk
include Makefile_plots.mk
include Makefile_cards.mk

.PHONY: clean
clean:
	@echo "Remove plots"
	-rm -rf plots_el plots_mu
