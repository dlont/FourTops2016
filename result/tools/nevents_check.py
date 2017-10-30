
from ROOT import TFile, TChain
import sys

inputfile=str(sys.argv[1])

f = TFile.Open(inputfile,"READ")
ch_b = f.Get("bookkeeping")
ch_c = f.Get("Craneen__Mu")

print "Total\t\t\tSelected\t",inputfile
print ch_b.GetEntries(), '\t\t', ch_c.GetEntries()
