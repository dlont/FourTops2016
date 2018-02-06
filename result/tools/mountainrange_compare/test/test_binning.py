import unittest
import ROOT as rt
import json
import numpy as np
from autobinning import OprimizedBinning

class TestAutoBinning(unittest.TestCase):
    def setUp(self):
        filename = "/storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/result/JES_tests_before_unblinding/plots_mu/Craneen_Data*_Run2_TopTree_Study.root"    
        cuts = "(((HLT_IsoMu24==1||HLT_IsoTkMu24==1) && met > 50 && HT > 500 && fabs(LeptonEta)<2.1 ))"
        self.c = rt.TChain("Craneen__Mu")
        self.c.Add(filename)
        nev = self.c.Draw("leptonIso","nJets>=10&&nMtags>=4","goff")
        self.buf = self.c.GetVal(0)
        buf = np.array([self.buf[i] for i in range(0,nev)])
        self.ob = OprimizedBinning( buf )

    def test_nbins_scott(self):
        self.ob._lowstat_algo='scott'
        actual = self.ob.get_n_bins_scott()
        expected = 3
        self.assertEqual(actual,expected)

    def test_nbins_james(self):
        self.ob._lowstat_algo='james'
        actual = self.ob.get_n_bins_james(len(self.ob._vec))
        expected = 6
        self.assertEqual(actual,expected)

    def test_make_plot(self):
        rt.gStyle.SetOptStat(0)

        self.ob._lowstat_thresh=30
        self.ob._lowstat_algo='scott'
        h = self.ob.get_histogram()
        self.c.Draw("leptonIso>>sample_hist","nJets>=10&&nMtags>=4","goff")
        h.SetDrawOption('hist text pE0')
        h.SetName("h_scott")
        for ibin in range(1,h.GetNbinsX()+1):
            h.SetBinContent(ibin,h.GetBinContent(ibin)/h.GetBinWidth(ibin))
            h.SetBinError(ibin,h.GetBinError(ibin)/h.GetBinWidth(ibin))

        self.ob._lowstat_thresh=20
        h1 = self.ob.get_histogram()
        self.c.Draw("leptonIso>>sample_hist","nJets>=10&&nMtags>=4","goff")
        h1.SetDrawOption('hist text pE0')
        for ibin in range(1,h.GetNbinsX()+1):
            h1.SetBinContent(ibin,h1.GetBinContent(ibin)/h1.GetBinWidth(ibin))
            h1.SetBinError(ibin,h1.GetBinError(ibin)/h1.GetBinWidth(ibin))

        h.Draw()
        h1.Draw("same")
        rt.gPad.SetLogy()
        rt.gPad.SaveAs("out_comp.pdf")
        # rt.gPad.SaveAs("out_{}.pdf".format(ob._lowstat_algo))
        pass

if __name__ == '__main__':
    unittest.main()

