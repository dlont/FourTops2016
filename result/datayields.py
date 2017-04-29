import ROOT
import json
import sys
import math

# json format
# { 'label':['file1','treename1',lumi1,], 'label':['file2','treename',lumi2], ...}
data=json.loads(sys.argv[1])
print data

h = ROOT.TH1D("h",";;Event yields",len(data),1,len(data)+1)

ibin=1
for label, entry in sorted(data.iteritems()):
	print label, entry
	temp_f = ROOT.TFile.Open(entry[0],'READ')
	temp_t = temp_f.Get(entry[1].encode('ascii'))
	#temp_t.Draw("BDT>>h_temp","(HLT_PFHT400_SixJet30_DoubleBTagCSV_p056==1)")
	temp_t.Draw("BDT>>h_temp")
	temp_h = ROOT.gDirectory.Get("h_temp")
	temp_nevents = temp_h.GetEntries()
	print "Nevents: ", temp_nevents
	h.SetBinContent(ibin, temp_nevents/entry[2])
	h.SetBinError(ibin, math.sqrt(temp_nevents)/entry[2])
	h.GetXaxis().SetBinLabel(ibin,label)
	ibin+=1

h.Draw("pe")
