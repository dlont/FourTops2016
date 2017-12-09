## This file contains all the necessary calls to the rootplot API to produce
## the same set of plots that were created from the command-line.

## You can use this file to intercept the objects and manipulate them before
## the figure is saved, making any custom changes that are not possible from
## the command-line.

## 'objects' is a python dictionary containing all the elements used in the
## plot, including 'hists', 'legend', etc.
##   ex: objects['hists'] returns a list of histograms

try:
  ## the normal way to import rootplot
  from rootplot import plot, plotmpl
except ImportError:
  ## special import for CMSSW installations of rootplot
  from PhysicsTools.PythonAnalysis.rootplot import plot, plotmpl

import os
os.chdir('..')  # return to the directory with the ROOT files

canvas, objects = plot('pileup_2016Data80X_Run271036-284044Cert__Full2016DataSet.root', 'pileup', 'pileupRun2016B-03Feb2017_ver2-v2crab33Nom', 'pileupRun2016C-03Feb2017-v1crab34Nom', 'pileupRun2016D-03Feb2017-v1crab35Nom', 'pileupRun2016E-03Feb2017-v1crab36Nom', 'pileupRun2016F-03Feb2017-v1crab37Nom', 'pileupRun2016G-03Feb2017-v1crab38Nom', 'pileupRun2016H-03Feb2017_ver2-v1crab39Nom', 'pileupRun2016H-03Feb2017_ver3-v1crab40Nom', 'rootplot_config.py', area_normalize=True)
canvas.SaveAs('plots/plot.png')
