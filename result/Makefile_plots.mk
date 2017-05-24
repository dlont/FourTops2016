.PHONY: plots_mu
#Order of arguments matters (1 - data, 4 - reference for the ratio when multiple ratios are requested, last - excluded from that ratio stack hist referece)
plots_mu: $(BUILDDIR)/Hists_data.root $(BUILDDIR)/Hists_EW.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_TT_RARE.root $(BUILDDIR)/Hists_SYST.root $(BUILDDIR)/Hists_TTTT_SCALED.root
	@echo "make muon plots"
	@if [ -d "$(dir $@)" ]; then echo "Muon dir exists" ; else mkdir $@ ; fi
	@mkdir -p $@
	@${ROOTPLOT} rootplot_config.py $^ --size=${SIZE} -f --data=1 --logy --ymin=0.1 --ratio-split=5 --overflow --legend-location='${LEGENDLOC}' --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=log --stack ${CUSTOMIZE}
	@if [ -d "$(dir $@)/log" ]; then echo "$@/log dir exists" && rm -rf $@/log ; fi 
	@mv log $@
	@${ROOTPLOT} rootplot_config.py $^ --size=${SIZE} -f --data=1 --overflow --legend-location='${LEGENDLOC}' --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=lin ${CUSTOMIZE}
	@if [ -d "$(dir $@)/lin" ]; then echo "$@/lin dir exists" && rm -rf $@/lin ; fi 
	@mv lin $@


.PHONY: plots_el 
#Order of arguments matters
plots_el: $(BUILDDIR)/Hists_data.root $(BUILDDIR)/Hists_EW.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_TT_RARE.root $(BUILDDIR)/Hists_SYST.root $(BUILDDIR)/Hists_TTTT_SCALED.root
	@echo "make electron plots"
	@if [ -d "$(dir $@)" ]; then echo "Electron dir exists" ; else mkdir $@ ; fi
	@mkdir -p $@
	@${ROOTPLOT} rootplot_config.py $^ --size=${SIZE} -f --data=1 --logy --ymin=0.1 --ratio-split=5 --overflow --legend-location='${LEGENDLOC}' --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=log --stack ${CUSTOMIZE}
	@if [ -d "$(dir $@)/log" ]; then echo "$@/log dir exists" && rm -rf $@/log ; fi 
	@mv log $@
	@${ROOTPLOT} rootplot_config.py $^ --size=${SIZE} -f --data=1 --overflow --legend-location='${LEGENDLOC}' --legend-entries=${LEGEND} -e ${FORMAT} --path=${PLOTS} --output=lin ${CUSTOMIZE}
	@if [ -d "$(dir $@)/lin" ]; then echo "$@/lin dir exists" && rm -rf $@/lin ; fi 
	@mv lin $@

