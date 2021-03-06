import ROOT as rt

rt.gStyle.SetOptStat(0)
rt.gStyle.SetPaintTextFormat("4.2f")

f_cran = rt.TFile.Open("../histos/Craneen_TTJets_powheg_Run2_TopTree_Study.root","READ")
f_histo = rt.TFile.Open("../histos/Hist_powheg_80X.root","READ")

BtaggedJets = f_histo.Get("BtaggedJets"); BtaggedJets.Sumw2()
BtaggedBJets = f_histo.Get("BtaggedBJets"); BtaggedBJets.Sumw2()
TotalNofBJets = f_histo.Get("TotalNofBJets"); TotalNofBJets.Sumw2()
BtaggedCJets = f_histo.Get("BtaggedCJets"); BtaggedCJets.Sumw2()
TotalNofCJets = f_histo.Get("TotalNofCJets"); TotalNofCJets.Sumw2()
BtaggedLightJets = f_histo.Get("BtaggedLightJets"); BtaggedLightJets.Sumw2()
TotalNofLightJets = f_histo.Get("TotalNofLightJets"); TotalNofLightJets.Sumw2()

eff_histo = BtaggedJets.Clone("eff_histo"); eff_histo.Reset(); eff_histo.SetTitle("Inclusive powheg efficiency;pt;#eta")
eff_histo.Divide(BtaggedBJets,TotalNofBJets,1.,1.,'B')

fake_histo = BtaggedJets.Clone("fake_histo"); fake_histo.Reset(); fake_histo.SetTitle("Inclusive fake rate;pt;#eta")
fake_histo_num = BtaggedJets.Clone("fake_histo_num"); fake_histo_num.Reset()
fake_histo_num.Add(BtaggedCJets)
fake_histo_num.Add(BtaggedLightJets)
fake_histo_den = BtaggedJets.Clone("fake_histo_den"); fake_histo_den.Reset();
fake_histo_den.Add(TotalNofCJets)
fake_histo_den.Add(TotalNofLightJets)
fake_histo.Divide(fake_histo_num,fake_histo_den,1.,1.,'B')


BtaggedJets = f_cran.Get("BtaggedJets"); BtaggedJets.Sumw2()
BtaggedBJets = f_cran.Get("BtaggedBJets"); BtaggedBJets.Sumw2()
TotalNofBJets = f_cran.Get("TotalNofBJets"); TotalNofBJets.Sumw2()
BtaggedCJets = f_cran.Get("BtaggedCJets"); BtaggedCJets.Sumw2()
TotalNofCJets = f_cran.Get("TotalNofCJets"); TotalNofCJets.Sumw2()
BtaggedLightJets = f_cran.Get("BtaggedLightJets"); BtaggedLightJets.Sumw2()
TotalNofLightJets = f_cran.Get("TotalNofLightJets"); TotalNofLightJets.Sumw2()

eff_cran = BtaggedJets.Clone("eff_cran"); eff_cran.Reset(); eff_cran.SetTitle("Selected powheg efficiency;pt;#eta")
eff_cran.Divide(BtaggedBJets,TotalNofBJets,1.,1.,'B')

fake_cran = BtaggedJets.Clone("fake_cran"); fake_cran.Reset(); fake_cran.SetTitle("Selected fake rate;pt;#eta")
fake_cran_num = BtaggedJets.Clone("fake_cran_num"); fake_cran_num.Reset()
fake_cran_num.Add(BtaggedCJets)
fake_cran_num.Add(BtaggedLightJets)
fake_cran_den = BtaggedJets.Clone("fake_cran_den"); fake_cran_den.Reset()
fake_cran_den.Add(TotalNofCJets)
fake_cran_den.Add(TotalNofLightJets)
fake_cran.Divide(fake_cran_num,fake_cran_den,1.,1.,'B')

eff_histo_cran_rat = eff_histo.Clone("eff_histo_cran_rat"); eff_histo_cran_rat.Reset(); eff_histo_cran_rat.SetTitle("efficiency ratio;pt;#eta")
eff_histo_cran_rat.Divide(eff_histo,eff_cran)
fake_histo_cran_rat = fake_histo.Clone("fake_histo_cran_rat"); fake_histo_cran_rat.Reset(); fake_histo_cran_rat.SetTitle("fake rate ratio;pt;#eta")
fake_histo_cran_rat.Divide(fake_histo,fake_cran)

c_eff = rt.TCanvas("b_eff_histo_cran")
c_eff.Divide(3,1)
c_eff.cd(1)
eff_histo.SetAxisRange(0.,1.,'Z')
eff_histo.Draw("colz")
c_eff.cd(2)
eff_cran.SetAxisRange(0.,1.,'Z')
eff_cran.Draw("colz")
c_eff.cd(3)
eff_histo_cran_rat.SetMarkerSize(2.3)
eff_histo_cran_rat.Draw("colz text89")
c_eff.Print(".png")

c_fake = rt.TCanvas("b_fake_histo_cran")
c_fake.Divide(3,1)
c_fake.cd(1)
fake_histo.SetAxisRange(0.,1.,'Z')
fake_histo.Draw("colz text89")
c_fake.cd(2)
fake_cran.SetAxisRange(0.,1.,'Z')
fake_cran.Draw("colz text89")
c_fake.cd(3)
fake_histo_cran_rat.SetMarkerSize(2.3)
fake_histo_cran_rat.Draw("colz text89")
c_fake.Print(".png")
c_fake.Print(".pdf")

