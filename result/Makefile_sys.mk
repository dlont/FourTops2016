SYSPLOTDIR=../sysplot
LATEXDUMPDIR=../latex
DIFFNUIS=~/CMSSW_7_4_7/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py

#MINOS=--minos=all
MINOS=
RUN=blind

sysplots: 	$(BUILDDIR)/Hists_TT_CARDS.root $(BUILDDIR)/Hists_TTTT_CARDS.root
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TT_CARDS.root -j $(SYSPLOTDIR)/JES_tt.json -r $(BUILDDIR)/Hists_TT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TTTT_CARDS.root -j $(SYSPLOTDIR)/JES_tttt.json -r $(BUILDDIR)/Hists_TTTT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TT_CARDS.root -j $(SYSPLOTDIR)/CSV_tt.json -r $(BUILDDIR)/Hists_TT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TTTT_CARDS.root -j $(SYSPLOTDIR)/CSV_tttt.json -r $(BUILDDIR)/Hists_TTTT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TT_CARDS.root -j $(SYSPLOTDIR)/Theory_tt.json -r $(BUILDDIR)/Hists_TT_CARDS.root -f $(FORMAT)
	@python -b $(SYSPLOTDIR)/sysplot.py -b $(BUILDDIR)/Hists_TTTT_CARDS.root -j $(SYSPLOTDIR)/Theory_tttt.json -r $(BUILDDIR)/Hists_TTTT_CARDS.root -f $(FORMAT)
	@if [ -d "$(BUILDDIR)/sys" ]; then echo "cards_mu dir exists" ; else mkdir $(BUILDDIR)/sys  ; fi 
	@mv JES_tt.$(FORMAT) JES_tttt.$(FORMAT) CSV_tt.$(FORMAT) CSV_tttt.$(FORMAT) Theory_tt.$(FORMAT) Theory_tttt.$(FORMAT) $(BUILDDIR)/sys
	@python -b $(LATEXDUMPDIR)/texplotspage.py -j $(LATEXDUMPDIR)/systematics.json app/syst

combinechecks: card_mu.txt card_el.txt datacard_elmu.txt
	@echo "Asimov checks"
	@echo "Asimov check: Single lepton combined"
	@combine -M MaxLikelihoodFit -t -1 --expectSignal 0 --robustFit=true $(MINOS) datacard_elmu.txt -n _AsymovComb0
	@python $(DIFFNUIS) --absolute -a mlfit_AsymovComb0.root -g plots_AsymovComb0.root
	@combine -M MaxLikelihoodFit -t -1 --expectSignal 1 --robustFit=true $(MINOS) datacard_elmu.txt -n _AsymovComb1
	@python $(DIFFNUIS) --absolute -a mlfit_AsymovComb1.root -g plots_AsymovComb1.root
	@echo "Asimov check: Single muon"
	@combine -M MaxLikelihoodFit -t -1 --expectSignal 0 --robustFit=true $(MINOS) --out cards_mu card_mu.txt -n _AsymovMu0
	@python $(DIFFNUIS) --absolute -a cards_mu/mlfit_AsymovMu0.root -g cards_mu/plots_AsymovMu0.root
	@combine -M MaxLikelihoodFit -t -1 --expectSignal 1 --robustFit=true $(MINOS) --out cards_mu card_mu.txt -n _AsymovMu1
	@python $(DIFFNUIS) --absolute -a cards_mu/mlfit_AsymovMu1.root -g cards_mu/plots_AsymovMu1.root
	@echo "Asimov check: Single electron"
	@combine -M MaxLikelihoodFit -t -1 --expectSignal 0 --robustFit=true $(MINOS) --out cards_el card_el.txt -n _AsymovEl0
	@python $(DIFFNUIS) --absolute -a cards_el/mlfit_AsymovEl0.root -g cards_el/plots_AsymovEl0.root
	@combine -M MaxLikelihoodFit -t -1 --expectSignal 1 --robustFit=true $(MINOS) --out cards_el card_el.txt -n _AsymovEl1
	@python $(DIFFNUIS) --absolute -a cards_el/mlfit_AsymovEl1.root -g cards_el/plots_AsymovEl1.root
	@echo "Pulls and correlations"
	@combine -M MaxLikelihoodFit --robustFit=true $(MINOS) --plots --saveShapes datacard_elmu.txt -n _CorrComb
	@combine -M MaxLikelihoodFit --robustFit=true $(MINOS) --plots --saveShapes --out cards_mu card_mu.txt -n _CorrMu
	@combine -M MaxLikelihoodFit --robustFit=true $(MINOS) --plots --saveShapes --out cards_el card_el.txt -n _CorrEl
