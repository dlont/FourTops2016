import ROOT as rt
import sys

root_file = sys.argv[1]

f = rt.TFile.Open(root_file,'READ')

folders = ['7J2M','7J3M','7J4M','8J2M','8J3M','8J4M','9J2M','9J3M','9J4M','10J2M','10J3M','10J4M']
systematics = ['TTTTME']
suffix = ['Up','Down']

hist = 'bdt'

#check central histograms
for fold in folders:
	name = fold+'/'+hist
	h = f.Get(name)
	print name, ':'
	#loop over all bins
	for ibin in range(1,h.GetNbinsX()+1):
		if h.GetBinContent(ibin) < 0.: print ibin, h.GetBinContent(ibin)
