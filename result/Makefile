
FORMAT=png
PLOTS='.*'
CUSTOMIZE=
INPUTLOCATION=./
DATALABEL:=Single \#mu (BCDEFGH)
TREENAME:=Craneen__Mu

VPATH:=$(shell readlink -f ${INPUTLOCATION})

#include Makefile_norm.mk
include Makefile_hist.mk
include Makefile_merge.mk

SIZE="1000x1000"
LEGEND:="${DATALABEL},EW,Single top,t\#bar{t},t\#bar{t}t\#bar{t}"
#SCALE=${WJETSNORM},${TTNORM},${TTTTNORM},1

#.PHONY: mergetrees
#mergetrees: tools/mergeCran4comparison.sh tools/listCran
#	@tools/mergeCran4comparison.sh ${INPUTLOCATION} tools/listCran
#	@echo "moving merged files to ${INPUTLOCATION}"
#	@mv Craneen*.root ${INPUTLOCATION}

.PHONY: plots_mu 
#Order of arguments matters
plots_mu: plots_mu/Hists_data.root plots_mu/Hists_WJets.root plots_mu/Hists_T.root plots_mu/Hists_TT.root plots_mu/Hists_TTTT.root
	@echo "make muon plots"
	@if [ -d "$(dir $@)" ]; then echo "Muon dir exists" ; else mkdir $@ ; fi
	@mkdir -p $@
	@rootplot rootplot_config.py $^ --size=${SIZE} -f --data=1 --logy --overflow --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=log ${CUSTOMIZE}
	@if [ -d "$(dir $@)/log" ]; then echo "$@/log dir exists" && rm -rf $@/log ; fi 
	@mv log $@
	@rootplot rootplot_config.py $^ --size=${SIZE} -f --data=1 --overflow --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=lin ${CUSTOMIZE}
	@if [ -d "$(dir $@)/lin" ]; then echo "$@/lin dir exists" && rm -rf $@/lin ; fi 
	@mv lin $@


.PHONY: plots_el 
#Order of arguments matters
plots_el: plots_el/Hists_data.root plots_el/Hists_WJets.root plots_el/Hists_T.root plots_el/Hists_TT.root plots_el/Hists_TTTT.root
	@echo "make elon plots"
	@if [ -d "$(dir $@)" ]; then echo "Muon dir exists" ; else mkdir $@ ; fi
	@mkdir -p $@
	@rootplot rootplot_config.py $^ --size=${SIZE} -f --data=1 --logy --overflow --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=log ${CUSTOMIZE}
	@if [ -d "$(dir $@)/log" ]; then echo "$@/log dir exists" && rm -rf $@/log ; fi 
	@mv log $@
	@rootplot rootplot_config.py $^ --size=${SIZE} -f --data=1 --overflow --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=lin ${CUSTOMIZE}
	@if [ -d "$(dir $@)/lin" ]; then echo "$@/lin dir exists" && rm -rf $@/lin ; fi 
	@mv lin $@

.PHONY: clean
clean:
	@echo "Remove plots"
	-rm -rf plots_el plots_mu
