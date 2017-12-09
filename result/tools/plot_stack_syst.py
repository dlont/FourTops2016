import sys
sys.argv.append( '-b-' )
import ROOT as rt

root_file = sys.argv[2]
outputfolder = sys.argv[3]

f = rt.TFile.Open(root_file,'READ')

folders = ['7J2M','7J3M','7J4M','8J2M','8J3M','8J4M','9J2M','9J3M','9J4M','10J2M','10J3M','10J4M']
systematics = ['JER','PU','JES','TTTTMEScale','btagWeightCSVCFErr1','btagWeightCSVCFErr2','btagWeightCSVHF','btagWeightCSVHFStats1','btagWeightCSVHFStats2',
		'btagWeightCSVJES','btagWeightCSVLF','btagWeightCSVLFStats1','btagWeightCSVLFStats2']
suffix = ['Up','Down']

hist = 'bdt'

colors = [rt.kRed,rt.kGreen]

#check central histograms
for fold in folders:
	name = fold+'/'+hist
	h = f.Get(name)
	print name, ':'
	hs = rt.THStack('st','stack systematic histograms')
	hs.Add(h,"p")
	linestyle=1
	for sys in systematics:
		linestyle+=1
		for suff in suffix:
			name = fold+'_'+sys+suff+'/'+hist
			hsys = f.Get(name)
			hsys.SetMarkerStyle(0)
			hsys.SetLineStyle(linestyle);
			if 'Up' in name: hsys.SetLineColor(rt.kRed)
			if 'Down' in name: hsys.SetLineColor(rt.kBlue)
			hs.Add(hsys,"hist")
	c = rt.TCanvas('c')
	hs.Draw('nostack')
	c.Print(outputfolder+'/'+fold+'.png')
