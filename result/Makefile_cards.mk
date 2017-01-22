.PHONY: cards_mu
cards_mu: $(BUILDDIR)/Hists_data.root $(BUILDDIR)/Hists_WJets.root $(BUILDDIR)/Hists_T.root $(BUILDDIR)/Hists_TT.root $(BUILDDIR)/Hists_TTTT.root
	@echo "make HiggsCombine cards"
	@if [ -d "cards_mu" ]; then echo "cards_mu dir exists" ; else mkdir cards_mu ; fi
	@python tools/cards.py -o cards_mu/card.txt --channel=mu --data $(BUILDDIR)/Hists_data.root  --source '{"TTTT":"$(BUILDDIR)/Hists_TTTT.root", "TT":"$(BUILDDIR)/Hists_TT.root", "EW":"$(BUILDDIR)/Hists_WJets.root", "ST":"$(BUILDDIR)/Hists_T.root"}' --observable=bdt
	
