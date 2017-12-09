## This file is the same as allplots.py, except that it uses multiprocessing
## to make better use of machines with multiple cores

try:
  ## the normal way to import rootplot
  from rootplot import plot, plotmpl
  from rootplot.core import report_progress
except ImportError:
  ## special import for CMSSW installations of rootplot
  from PhysicsTools.PythonAnalysis.rootplot import plot, plotmpl
  from PhysicsTools.PythonAnalysis.rootplot.core import report_progress
import ROOT
import multiprocessing as multi

import os
os.chdir('..')  # return to the directory with the ROOT files

calls = []

calls.append("""
canvas, objects = plot('pileup_2016Data80X_Run271036-284044Cert__Full2016DataSet.root', 'pileup', 'pileupRun2016B-03Feb2017_ver2-v2crab33Nom', 'pileupRun2016C-03Feb2017-v1crab34Nom', 'pileupRun2016D-03Feb2017-v1crab35Nom', 'pileupRun2016E-03Feb2017-v1crab36Nom', 'pileupRun2016F-03Feb2017-v1crab37Nom', 'pileupRun2016G-03Feb2017-v1crab38Nom', 'pileupRun2016H-03Feb2017_ver2-v1crab39Nom', 'pileupRun2016H-03Feb2017_ver3-v1crab40Nom', 'rootplot_config.py', area_normalize=True)
canvas.SaveAs('plots/plot.png')
""")


queue = multi.JoinableQueue()
qglobals = multi.Manager().Namespace()
qglobals.nfinished = 0
qglobals.ntotal = len(calls)
for call in calls:
    queue.put(call)

def qfunc(queue, qglobals):
    from Queue import Empty
    while True:
        try: mycall = queue.get(timeout=5)
        except (Empty, IOError): break
        exec(mycall)
        ROOT.gROOT.GetListOfCanvases().Clear()
        qglobals.nfinished += 1
        report_progress(qglobals.nfinished, qglobals.ntotal, 
                        'plots', 'png')
        queue.task_done()

for i in range(8):
    p = multi.Process(target=qfunc, args=(queue, qglobals))
    p.daemon = True
    p.start()
queue.join()
report_progress(len(calls), len(calls), 'plots', 'png')
print ''
