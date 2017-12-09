import ROOT as rt
import os
import sys

# input file is specified via the first argument
inputfile=str(sys.argv[1])
f = rt.TFile.Open(inputfile)

# list of folders storing histograms for all search regions used in the analysis
mufolders = ['10J2M',  '10J3M',  '10J4M',  '7J2M',  '7J3M',  '7J4M',  '8J2M',  '8J3M',  '8J4M',  '9J2M',  '9J3M',  '9J4M']
elfolders = ['10J2M',  '10J3M',  '10J4M',  '8J2M',  '8J3M',  '8J4M',  '9J2M',  '9J3M',  '9J4M']

# loop over all folders in the list and sum up the number of non-empty bins
n_totbins = 0
for folder in mufolders:
	h = f.Get(folder+'/bdt')
	# count only non-empty bins
	for ibin in range(1,h.GetNbinsX()+1):
		if h.GetBinContent(ibin)>0: n_totbins += 1

print "Number of filled bins: ", n_totbins
