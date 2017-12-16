PLOTCONFIGDIR=tools/mountainrange_configs_raresplit
PLOTMACRO=tools/mountainrange_pub_raresplit.py
CORRMATRMACRO=tools/plot_corr_matrix.py
PULLSMACRO=tools/plot_nuis_pulls.py
DIFFNUISDENYS=~/CMSSW_7_4_7/src/HiggsAnalysis/CombinedLimit/test/diffNuisances_denys.py

postfit_plots: mountainrange pulls correlations

pulls: $(COMBINESHAPESFILE)
	python $(DIFFNUISDENYS) $(COMBINESHAPESFILE) -a -A -g $(BUILDDIR)/pulls_out.root
	python $(PULLSMACRO) $(BUILDDIR)/pulls_out.root -o $(BUILDDIR)/pulls -e $(FORMAT) -b

correlations: $(COMBINESHAPESFILE)
	python $(CORRMATRMACRO) $(COMBINESHAPESFILE) -o $(BUILDDIR)/corrmat -e $(FORMAT) -b

mountainrange: $(COMBINESHAPESFILE)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_mu_tttt10_prefit.json -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_mu_tttt9_prefit.json  -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_mu_tttt8_prefit.json  -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_mu_tttt7_prefit.json  -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_el_tttt10_prefit.json -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_el_tttt9_prefit.json  -b -e $(FORMAT) -r --dir $(BUILDDIR)
	python $(PLOTMACRO) $(COMBINESHAPESFILE) -j $(PLOTCONFIGDIR)/mountain_el_tttt8_prefit.json  -b -e $(FORMAT) -r --dir $(BUILDDIR)
