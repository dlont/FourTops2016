
FORMAT=png
PLOTS='.*bdt.*'
#PLOTS='.*'
CUSTOMIZE=
INPUTLOCATION=./
DATALABEL:=Single \#mu (BCDEFGH)
TREENAME:=Craneen__Mu

VPATH:=$(shell readlink -f ${INPUTLOCATION})

ROOTPLOT=../rootplot/bin/rootplot

#include Makefile_norm.mk
include Makefile_hist.mk
include Makefile_merge.mk

SIZE="1000x1000"
LEGEND:="${DATALABEL},EW,Single top,t\#bar{t},t\#bar{t}t\#bar{t} (\#times 100)"
#SCALE=${WJETSNORM},${TTNORM},${TTTTNORM},1

#.PHONY: mergetrees
#mergetrees: tools/mergeCran4comparison.sh tools/listCran
#	@tools/mergeCran4comparison.sh ${INPUTLOCATION} tools/listCran
#	@echo "moving merged files to ${INPUTLOCATION}"
#	@mv Craneen*.root ${INPUTLOCATION}

.PHONY: plots_mu
#Order of arguments matters (1 - data, 4 - reference for the ratio when multiple ratios are requested, last - excluded from that ratio stack hist referece)
plots_mu: $(BUILDDIR)/Hists_data.root $(BUILDDIR)/Hists_WJets.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_SYST.root $(BUILDDIR)/Hists_TTTT_SCALED.root
	@echo "make muon plots"
	@if [ -d "$(dir $@)" ]; then echo "Muon dir exists" ; else mkdir $@ ; fi
	@mkdir -p $@
	@${ROOTPLOT} rootplot_config.py $^ --size=${SIZE} -f --data=1 --logy --ymin=0.1 --ratio-split=4 --overflow --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=log --stack ${CUSTOMIZE}
	@if [ -d "$(dir $@)/log" ]; then echo "$@/log dir exists" && rm -rf $@/log ; fi 
	@mv log $@
	@${ROOTPLOT} rootplot_config.py $^ --size=${SIZE} -f --data=1 --overflow --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=lin ${CUSTOMIZE}
	@if [ -d "$(dir $@)/lin" ]; then echo "$@/lin dir exists" && rm -rf $@/lin ; fi 
	@mv lin $@


.PHONY: plots_el 
#Order of arguments matters
plots_el: $(BUILDDIR)/Hists_data.root $(BUILDDIR)/Hists_WJets.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_SYST.root $(BUILDDIR)/Hists_TTTT_SCALED.root
	@echo "make electron plots"
	@if [ -d "$(dir $@)" ]; then echo "Electron dir exists" ; else mkdir $@ ; fi
	@mkdir -p $@
	@${ROOTPLOT} rootplot_config.py $^ --size=${SIZE} -f --data=1 --logy --ymin=0.1 --ratio-split=4 --overflow --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=log --stack ${CUSTOMIZE}
	@if [ -d "$(dir $@)/log" ]; then echo "$@/log dir exists" && rm -rf $@/log ; fi 
	@mv log $@
	@${ROOTPLOT} rootplot_config.py $^ --size=${SIZE} -f --data=1 --overflow --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=lin ${CUSTOMIZE}
	@if [ -d "$(dir $@)/lin" ]; then echo "$@/lin dir exists" && rm -rf $@/lin ; fi 
	@mv lin $@

.PHONY: cards_mu
cards_mu: $(BUILDDIR)/Hists_data.root $(BUILDDIR)/Hists_WJets.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_SYST.root $(BUILDDIR)/Hists_TTTT.root
	@echo "make HiggsCombine cards"
	@if [ -d "cards_mu" ]; then echo "cards_mu dir exists" ; else mkdir cards_mu ; fi
	@python tools/cards.py -o cards_mu/card.txt --channel=mu --data $(BUILDDIR)/Hists_data.root --signal $(BUILDDIR)/Hists_TTTT.root --tt $(BUILDDIR)/Hists_SYST.root --st $(BUILDDIR)/Hists_T.root --ew $(BUILDDIR)/Hists_WJets.root
	

.PHONY: clean
clean:
	@echo "Remove plots"
	-rm -rf plots_el plots_mu
