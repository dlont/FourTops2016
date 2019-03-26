#!/usr/bin/python

import ROOT as rt
import os
import pprint

CRANEEN_FILES_PATH = '/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v3/Craneen_Data*.root' # wildcards are supported
TREE_NAME          = 'Craneen__Mu' # must be Craneen__Mu or Craneen__El

ch = rt.TChain(TREE_NAME)
ch.Add(CRANEEN_FILES_PATH)

# HEADER OF THE TABLE
print '************************************************'
print '****           INTERESTING EVENTS          *****'
print '************************************************'

print '{0: <15}:{1: <15}:{2: <20}{3: <10}{4: <10}{5: <10}{6: <10}{7: <10}'.format("Runnr", "LumiSec", "EventNr", "nJets", "HTX", "HTb", "BDT1", "topness")

N_READ_EVENTS      = 0
N_SELECTED_EVENTS = 0
for ev in ch:

	N_READ_EVENTS += 1
	# Code your selection options here
	if ev.nJets < 10: continue
	if ev.nMtags < 4: continue
	if ev.BDT1 < 0.8: continue

	N_SELECTED_EVENTS += 1
	# Print out Run, Lumi section, Event numbers for interesting events
	print '{0: <15}:{1: <15}:{2: <20}{3: <10}{4: <10}{5: <10}{6: <10}{7: <10}{8}'.format(ev.Runnr,ev.Lumisec,ev.Evnr,
									ev.nJets,round(ev.HTX,2),round(ev.HTb,2),round(ev.BDT1,3),round(ev.multitopness,3),
									os.path.basename(ch.GetFile().GetName()))
	#if ev.Evnr == 225770321:
	if ev.Evnr == 548714092:
		alljets = [round(el,1) for el in ev.jetvec]
		alljets = [alljets[i:i+5] for i in range(0,len(alljets),5)]
		pprint.pprint(alljets)		

# FOOTER OF THE TABLE
print '************************************************'
print 'N EVENTS READ:    ', N_READ_EVENTS
print 'N EVENTS SELECTED:', N_SELECTED_EVENTS
print '************************************************'
