import sys
import ROOT as rt

filedata = rt.TFile.Open(sys.argv[1])
histdata = filedata.Get("allSF/bdt")
filemctt = rt.TFile.Open(sys.argv[2])
histmctt = filemctt.Get("allSF/bdt")
filemcst = rt.TFile.Open(sys.argv[3])
histmcst = filemcst.Get("allSF/bdt")
filemcwj = rt.TFile.Open(sys.argv[4])
histmcwj = filemcwj.Get("allSF/bdt")

histmc = histmctt.Clone("result")
histmc.Add(histmcst)
histmc.Add(histmcwj)

print "{} {} {} +/- {}" . format(histdata.Integral(), histmc.Integral(), histdata.Integral()/histmc.Integral(), rt.TMath.Sqrt(histdata.Integral())/histmc.Integral())
