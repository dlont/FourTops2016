
FORMAT=pdf
PLOTS='.*'
CUSTOMIZE=
INPUTLOCATION=./
DATALABEL:=Single \#mu (ABCDEFGH)
TREENAME:=Craneen__Mu

VPATH:=$(shell readlink -f ${INPUTLOCATION})

include Makefile_norm.mk
include Makefile_hist.mk
	
.PHONY: plots_mu plots_el

SIZE="500x500"
LEGEND:="t\#bar{t},t\#bar{t}t\#bar{t},EW,${DATALABEL}"
SCALE=${TTNORM},${TTTTNORM},${WJETSNORM},1

#Order of arguments matters
plots_mu: plots_mu/Hists_TT.root plots_mu/Hists_TTTT.root plots_mu/Hists_WJets.root plots_mu/Hists_data.root 
	@echo "make muon plots"
	@if [ -d "$@" ]; then echo "Muon dir exists" ; else mkdir $@ ; fi
	@mkdir -p $@
	@rootplot rootplot_config.py $^ --size=${SIZE} -f --data=4 --logy --overflow --scale=${SCALE} --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=log ${CUSTOMIZE}
	@if [ -d "$@/log" ]; then echo "$@/log dir exists" && rm -rf $@/log ; fi 
	@mv log $@
	@rootplot rootplot_config.py $^ --size=${SIZE} -f --data=4 --overflow --scale=${SCALE} --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=lin ${CUSTOMIZE}
	@if [ -d "$@/lin" ]; then echo "$@/lin dir exists" && rm -rf $@/lin ; fi 
	@mv lin $@

plots_el: plots_el/Hists_TT.root plots_el/Hists_TTTT.root plots_el/Hists_WJets.root plots_el/Hists_data.root 
	@echo "make electron plots"
	@if [ -d "$@" ]; then echo "Electron dir exists" ; else mkdir $@ ; fi
	@mkdir -p $@
	@rootplot rootplot_config.py $^ --size=${SIZE} -f --data=4 --logy --overflow --scale=${SCALE} --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=log ${CUSTOMIZE}
	@if [ -d "$@/log" ]; then echo "$@/log dir exists" && rm -rf $@/log ; fi 
	@mv log $@
	@rootplot rootplot_config.py $^ --size=${SIZE} -f --data=4 --overflow --scale=${SCALE} --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=lin ${CUSTOMIZE}
	@if [ -d "$@/lin" ]; then echo "$@/lin dir exists" && rm -rf $@/lin ; fi 
	@mv lin $@

.PHONY: clean
clean:
	@echo "Remove plots"
	-rm -rf plots_el plots_mu
