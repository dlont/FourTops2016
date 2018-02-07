#!/usr/bin/env python
from sys import exit, argv, stderr

# import ROOT with a fix to get batch mode (http://root.cern.ch/phpBB3/viewtopic.php?t=3198)
argv.append( '-b-' )
import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.PyConfig.IgnoreCommandLineOptions = True
argv.remove( '-b-' )

from ROOT import TFile

if len(argv) != 2:
	print >> stderr, 'Wrong arguments: ', argv
	exit(0)

print "Testing ", argv[1]
f = TFile(argv[1],"READ")
if f.IsZombie(): 
	print argv[1] + ' is Zombie!'
	exit(1)

