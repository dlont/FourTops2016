SYSPLOTDIR=../sysplot
LATEXDUMPDIR=../latex

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
