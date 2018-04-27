import ROOT as rt


# Disable garbage collection for this list of objects
rt.TCanvas.__init__._creates = False
rt.TFile.__init__._creates = False
rt.TH1.__init__._creates = False
rt.TH2.__init__._creates = False
rt.THStack.__init__._creates = False
rt.TGraph.__init__._creates = False
rt.TMultiGraph.__init__._creates = False
rt.TList.__init__._creates = False
rt.TCollection.__init__._creates = False
rt.TIter.__init__._creates = False

#
rt.gStyle.SetOptStat(0)

filtered_root_file = '/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt/Craneen_TTJetsFilt_powheg_central_Run2_TopTree_Study.root'
inclusive_root_file = '/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt/Craneen_TTJets_powheg_Run2_TopTree_Study.root'
craneen_name = 'Craneen__Mu'

histograms_filtered = { 'HT':rt.TH1F('h_filtered_HT','Filtered;gen HT (p_T>30,|#eta|<2.4)',30,0,3000),
                        'jetMult':rt.TH1F('h_filtered_jet_mult','Filtered;n gen jets (p_T>30)',14,6,20)}
histograms_inclusive = { 'HT':rt.TH1F('h_inclusive_HT','Inclusive;gen HT (p_T>30,|#eta|<2.4)',30,0,3000),
                        'jetMult':rt.TH1F('h_inclusive_jet_mult','Inclusive;n gen jets (p_T>30)',14,6,20)}
histograms_inclusive_full = { 'HT':rt.TH1F('h_inclusive_full_HT','Inclusive;gen HT (p_T>30,|#eta|<2.4)',30,0,3000),
                              'jetMult':rt.TH1F('h_inclusive_full_jet_mult','Inclusive;n gen jets (p_T>30)',14,6,20)}
histograms_sum = {'HT':rt.TH1F('h_sum_HT','Sum of filtered and inclusive;gen HT (p_T>30,|#eta|<2.4)',30,0,3000),
                   'jetMult':rt.TH1F('h_sum_mult','Sum of filtered and inclusive;n gen jets (p_T>30)',14,6,20)}

stacks = {'HT':rt.THStack('HT','HT'), 'jetMult':rt.THStack('jetMult','jetMult')}

f_filtered, f_inclusive = rt.TFile.Open(filtered_root_file), rt.TFile.Open(inclusive_root_file)
t_filtered, t_inclusive = f_filtered.Get(craneen_name), f_inclusive.Get(craneen_name)

LIMIT_N_EVENTS = 10000
LIMIT_N_EVENTS = 100000000000

t_filtered.SetBranchStatus ("*", 0)
t_filtered.SetBranchStatus ("genJets", 1)
t_filtered.SetBranchStatus ("genLeptons", 1)
t_filtered.SetBranchStatus ("nJets", 1)
t_filtered.SetBranchStatus ("nMtags", 1)
t_filtered.SetBranchStatus ("GenFilter", 1)

nev_filt = 0
for ev in t_filtered:

    nev_filt+=1
    gen_jets = ev.genJets
    gen_leptons = ev.genLeptons

    #if gen_leptons.size() != 1: continue

    gen_ht = 0
    jet_mult = 0
    for jet in gen_jets:
        if jet.Pt()>30 and abs(jet.Eta())<2.4: gen_ht+=jet.Pt()
        if jet.Pt()>30: jet_mult+=1

    #if True:
    if ev.nJets>9: 
    	histograms_filtered['HT'].Fill(gen_ht)
    	histograms_filtered['jetMult'].Fill(jet_mult)
    	#histograms_filtered['jetMult'].Fill(len(gen_leptons))

n_total_in_filtered_sample = 8327769.
n_total_in_inclusive_sample = 154652276.

efficiency = 0.00434*0.438				# actual efficiency value calculated as the product of branching ration and jet/HT efficiency
efficiency = 0.002950005
lumi_data = 35.9
xs_tt_tot = 831.0
xs_tt_veto = xs_tt_tot - xs_tt_tot*efficiency
eff_lumi_inclusive = n_total_in_inclusive_sample/831.0


n_total = 0
n_passing_filter = 0

t_inclusive.SetBranchStatus ("*", 0)
t_inclusive.SetBranchStatus ("genJets", 1)
t_inclusive.SetBranchStatus ("genLeptons", 1)
t_inclusive.SetBranchStatus ("nJets", 1)
t_inclusive.SetBranchStatus ("nMtags", 1)
t_inclusive.SetBranchStatus ("GenFilter", 1)
nev = 0
for ev in t_inclusive:

    nev+=1
    gen_jets = ev.genJets
    gen_leptons = ev.genLeptons

    n_total+=1

    gen_ht = 0
    jet_mult = 0
    for jet in gen_jets:
        if jet.Pt()>30 and abs(jet.Eta())<2.4: gen_ht+=jet.Pt()
        if jet.Pt()>30: jet_mult+=1

    #if True:
    if ev.nJets>9: 
    	histograms_inclusive_full['HT'].Fill(gen_ht)
    	histograms_inclusive_full['jetMult'].Fill(jet_mult)
    	#histograms_inclusive_full['jetMult'].Fill(len(gen_leptons))

    if ev.GenFilter==1: continue
    n_passing_filter+=1
    #if True: 
    if ev.nJets>9: 
    	histograms_inclusive['HT'].Fill(gen_ht)
    	#histograms_inclusive['jetMult'].Fill(jet_mult)
    	histograms_inclusive['jetMult'].Fill(len(gen_leptons))

c = rt.TCanvas('c','CMS',1200,600)
c.Divide(2,3)

c.cd(1)
print "Inclusive full HT:"
histograms_inclusive_full['HT'].Print("all")
print "Filtered HT:"
histograms_filtered['HT'].Print("all")


#efficiency = float(n_passing_filter)/float(n_total)	# calculation from visible phase space
#print 'efficiency after offline selection', efficiency
#print "passing events", n_passing_filter
#print 'Actual efficiency used for stitching', efficiency

histograms_filtered['HT'].Sumw2(True)
#histograms_filtered['HT'].Scale(1./histograms_filtered['HT'].Integral()*float(n_passing_filter)) # stupid method
histograms_filtered['HT'].Scale(lumi_data/eff_lumi_inclusive*efficiency*n_total_in_inclusive_sample/n_total_in_filtered_sample) # correct method for filtered sample normalization
histograms_filtered['HT'].SetLineColor(rt.kBlue)
histograms_inclusive['HT'].Sumw2(True)
histograms_inclusive['HT'].Scale(lumi_data/eff_lumi_inclusive) # XXX correct method
histograms_inclusive['HT'].SetLineColor(rt.kGreen)
histograms_inclusive_full['HT'].Sumw2(True)
histograms_inclusive_full['HT'].Scale(lumi_data/eff_lumi_inclusive) # XXX correct method
histograms_inclusive_full['HT'].SetLineColor(rt.kRed)
stacks['HT'].Add(histograms_filtered['HT'],'hist')
stacks['HT'].Add(histograms_inclusive['HT'],'hist')
stacks['HT'].Add(histograms_inclusive_full['HT'],'hist')
histograms_sum['HT'].Sumw2(True)
histograms_sum['HT'].Add(histograms_filtered['HT'],histograms_inclusive['HT'])
histograms_sum['HT'].SetLineColor(rt.kRed); histograms_sum['HT'].SetLineStyle(2);
stacks['HT'].Add(histograms_sum['HT'],'hist')

stacks['HT'].Draw('nostack')
rt.gPad.SetLogy()

leg1 = rt.TLegend(0.7,0.7,0.98,0.98)
leg1.SetHeader('Events passing offline selection: nJ>=9,nM>=2,recHT>500,trig,1l')
leg1.AddEntry(histograms_filtered['HT'],'Filtered sample (1l,genHT>500,genNJ>=9)')
leg1.AddEntry(histograms_inclusive['HT'],'Veto events from inclusive sample !(1l,genHT>500,genNJ>=9)')
leg1.AddEntry(histograms_sum['HT'],'Filtered+Veto')
leg1.AddEntry(histograms_inclusive_full['HT'],'Inclusive sample (no gen cuts)')
leg1.Draw()

c.cd(3)
rt.gPad.SetGridy()
#histograms_inclusive_full['HT'].Sumw2(False)
h_ratio_ht = histograms_inclusive_full['HT'].Clone("HT_ratio")
h_ratio_ht.Divide(histograms_sum['HT'])
h_ratio_ht.Draw('hist E')
h_ratio_ht.SetTitle('inclusive full/(inclusive veto+fitered)')
h_ratio_ht.GetYaxis().SetTitle('ratio')

c.cd(5)
rt.gPad.SetGridy()
histograms_inclusive_full['HT'].Sumw2(True)
h_ratio_unc1_ht = histograms_inclusive_full['HT'].Clone("HT_ratio_unc1")
#h_ratio_unc1_ht.Sumw2(True)
for ibin in range(1,h_ratio_unc1_ht.GetNbinsX()+1):
	if h_ratio_unc1_ht.GetBinContent(ibin)>0: h_ratio_unc1_ht.SetBinError(ibin,h_ratio_unc1_ht.GetBinError(ibin)/h_ratio_unc1_ht.GetBinContent(ibin))
	h_ratio_unc1_ht.SetBinContent(ibin,0.)
#h_ratio_unc1_ht.Divide(histograms_inclusive_full['HT'])
h_ratio_unc1_ht.Draw('hist E')
h_ratio_unc1_ht.SetTitle('relative uncertainty')
h_ratio_unc1_ht.GetYaxis().SetTitle('ratio')

histograms_sum['HT'].Sumw2(True)
h_ratio_unc2_ht = histograms_sum['HT'].Clone("HT_ratio_unc2"); h_ratio_unc2_ht.SetLineColor(rt.kBlue)
for ibin in range(1,h_ratio_unc2_ht.GetNbinsX()+1):
	if h_ratio_unc2_ht.GetBinContent(ibin)>0: h_ratio_unc2_ht.SetBinError(ibin,h_ratio_unc2_ht.GetBinError(ibin)/h_ratio_unc2_ht.GetBinContent(ibin))
	h_ratio_unc2_ht.SetBinContent(ibin,0.)
#h_ratio_unc2_ht.Divide(histograms_sum['HT'])
h_ratio_unc2_ht.Draw('same hist E')

c.cd(2)
histograms_filtered['jetMult'].Sumw2()
#histograms_filtered['jetMult'].Scale(1./histograms_filtered['jetMult'].Integral()*float(n_passing_filter))
histograms_filtered['jetMult'].Scale(lumi_data/eff_lumi_inclusive*efficiency*n_total_in_inclusive_sample/n_total_in_filtered_sample)
histograms_filtered['jetMult'].SetLineColor(rt.kBlue)
histograms_inclusive['jetMult'].SetLineColor(rt.kGreen)
histograms_inclusive['jetMult'].Sumw2()
histograms_inclusive['jetMult'].Scale(lumi_data/eff_lumi_inclusive)
histograms_inclusive_full['jetMult'].SetLineColor(rt.kRed)
histograms_inclusive_full['jetMult'].Sumw2()
histograms_inclusive_full['jetMult'].Scale(lumi_data/eff_lumi_inclusive)
stacks['jetMult'].Add(histograms_filtered['jetMult'],'hist e')
stacks['jetMult'].Add(histograms_inclusive['jetMult'],'hist e')
stacks['jetMult'].Add(histograms_inclusive_full['jetMult'],'hist e')
histograms_sum['jetMult'].Sumw2()
histograms_sum['jetMult'].Add(histograms_filtered['jetMult'],histograms_inclusive['jetMult'])
histograms_sum['jetMult'].SetLineColor(rt.kRed); histograms_sum['jetMult'].SetLineStyle(2);
stacks['jetMult'].Add(histograms_sum['jetMult'],'hist')

stacks['jetMult'].Draw('nostack')
rt.gPad.SetLogy()

c.cd(4)
rt.gPad.SetGridy()
histograms_inclusive_full['jetMult'].Sumw2()
h_ratio_jetmult = histograms_inclusive_full['jetMult'].Clone("jetMult_ratio")
h_ratio_jetmult.Divide(histograms_sum['jetMult'])
h_ratio_jetmult.Draw('hist E')
h_ratio_jetmult.SetAxisRange(0., 2.,"Y");
h_ratio_jetmult.SetTitle('inclusive full/(inclusive veto+fitered)')
h_ratio_jetmult.GetYaxis().SetTitle('ratio')

#leg2 = rt.TLegend(0.7,0.7,0.98,0.98)
#leg2.AddEntry(histograms_filtered['HT'],'Filtered sample')
#leg2.AddEntry(histograms_inclusive['HT'],'Veto event from inclusive sample')
##leg2.AddEntry(histograms_sum['HT'],'Filtered+Veto')
#leg2.AddEntry(histograms_inclusive_full['HT'],'Inclusive sample (no gen cuts)')
#leg2.Draw()

print 'Efficiency estimate:', float(n_passing_filter)/float(n_total)
print histograms_inclusive_full['HT'].Integral(), histograms_sum['HT'].Integral()
print histograms_inclusive_full['jetMult'].Integral(), histograms_sum['jetMult'].Integral()
#print 'Extra normalization correction factor to get perfect agreement in normalization'
#print 'HT:', float(histograms_inclusive_full['HT'].Integral())/float(histograms_sum['HT'].Integral())
#print 'jetMult:', float(histograms_inclusive_full['jetMult'].Integral())/float(histograms_sum['jetMult'].Integral())

c.cd(6)
rt.gPad.SetGridy()
histograms_inclusive_full['jetMult'].Sumw2(True)
h_ratio_unc1_jetmult = histograms_inclusive_full['jetMult'].Clone("jetMult_ratio_unc1")
#h_ratio_unc1_ht.Sumw2(True)
for ibin in range(1,h_ratio_unc1_jetmult.GetNbinsX()+1):
	if h_ratio_unc1_jetmult.GetBinContent(ibin)>0: h_ratio_unc1_jetmult.SetBinError(ibin,h_ratio_unc1_jetmult.GetBinError(ibin)/h_ratio_unc1_jetmult.GetBinContent(ibin))
	h_ratio_unc1_jetmult.SetBinContent(ibin,0.)
#h_ratio_unc1_ht.Divide(histograms_inclusive_full['HT'])
h_ratio_unc1_jetmult.Draw('hist E')
h_ratio_unc1_jetmult.SetTitle('relative uncertainty')
h_ratio_unc1_jetmult.GetYaxis().SetTitle('ratio')

histograms_sum['jetMult'].Sumw2(True)
h_ratio_unc2_jetMult = histograms_sum['jetMult'].Clone("jetMult_ratio_unc2"); h_ratio_unc2_jetMult.SetLineColor(rt.kBlue)
for ibin in range(1,h_ratio_unc2_ht.GetNbinsX()+1):
	if h_ratio_unc2_jetMult.GetBinContent(ibin)>0: h_ratio_unc2_jetMult.SetBinError(ibin,h_ratio_unc2_jetMult.GetBinError(ibin)/h_ratio_unc2_jetMult.GetBinContent(ibin))
	h_ratio_unc2_jetMult.SetBinContent(ibin,0.)
#h_ratio_unc2_ht.Divide(histograms_sum['HT'])
h_ratio_unc2_jetMult.Draw('same hist E')

c.SaveAs('stitching_actualformula1.pdf')
c.SaveAs('stitching_actualformula1.png')

outputfile = rt.TFile.Open('output.root','RECREATE')
histograms_filtered['HT'].Write()
histograms_inclusive['HT'].Write()
histograms_inclusive_full['HT'].Write()
histograms_sum['HT'].Write()

