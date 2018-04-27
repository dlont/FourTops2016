#!/usr/bin/python -u

"""
Script for job processing monitoring.
It analyses big-submission log file to extact IDs of submitted jobs and check their status.
Job status is queried usign a clock and torque job logs in cluster log folder.
If all jobs are successful the email is sent with notification message.
"""

from __future__ import print_function
import math  
import time
import sys, os
import argparse
import pprint as pp

from misc_parse_torque_accounting_log.launch_daughter_process import *
from misc_parse_torque_accounting_log.parse_cluster_logs import *

# Program options
parser = argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('infile', help="big-submission.log")
parser.add_argument('--builddir', help="make BUILDDIR variable")
parser.add_argument('--inputlocation', help="make INPUTLOCATION variable")
parser.add_argument('--print-jobs', help="Print out job statistics", action='store_true', default=False)
parser.add_argument('--ndays', help="Age of logs to check job status (days)", type=int, default=2)
parser.add_argument('--batch', help="Suppress output", action='store_true', default=False )
args = parser.parse_args(sys.argv[1:])
print(args)

if args.batch:
  f = open(os.devnull, 'w')
  sys.stdout = f

# Launch watchdog timer
start_time = time.time()

# Operate on this samples
init_list_of_samples_to_merge = [
'Data_Run2016B',
'Data_Run2016C',
'Data_Run2016D',
'Data_Run2016E',
'Data_Run2016F',
'Data_Run2016G',
'Data_Run2016H',
'ttttNLO',
'ttttNLO_fsrup',
'ttttNLO_fsrdown',
'ttttNLO_isrup',
'ttttNLO_isrdown',
'ttttNLO_totaljesup',
'ttttNLO_totaljesdown',
'ttttNLO_SubTotalPileUp_jesup',
'ttttNLO_SubTotalPileUp_jesdown',
'ttttNLO_SubTotalRelative_jesup',
'ttttNLO_SubTotalRelative_jesdown',
'ttttNLO_SubTotalPt_jesup',
'ttttNLO_SubTotalPt_jesdown',
'ttttNLO_SubTotalScale_jesup',
'ttttNLO_SubTotalScale_jesdown',
'ttttNLO_SubTotalFlavor_jesup',
'ttttNLO_SubTotalFlavor_jesdown',
'ttttNLO_jerup',
'ttttNLO_jerdown',
'TTJets_powheg_totaljesup',
'TTJets_powheg_totaljesdown',
'TTJets_powheg_SubTotalPileUp_jesup',
'TTJets_powheg_SubTotalPileUp_jesdown',
'TTJets_powheg_SubTotalRelative_jesup',
'TTJets_powheg_SubTotalRelative_jesdown',
'TTJets_powheg_SubTotalPt_jesup',
'TTJets_powheg_SubTotalPt_jesdown',
'TTJets_powheg_SubTotalScale_jesup',
'TTJets_powheg_SubTotalScale_jesdown',
'TTJets_powheg_SubTotalFlavor_jesup',
'TTJets_powheg_SubTotalFlavor_jesdown',
'TTJets_powheg_jerup',
'TTJets_powheg_jerdown',
'TTJets_powheg_herwig',
'TTJets_powheg_herwig_jesup',
'TTJets_powheg_herwig_jesdown',
'TTJets_powheg_herwig_jerup',
'TTJets_powheg_herwig_jerdown',
'TTJets_amcFXFX',
'TTJets_amcFXFX_jesdown',
'TTJets_amcFXFX_jesup',
'TTJets_amcFXFX_jerup',
'TTJets_amcFXFX_jerdown',
'TTJets_powheg_central',
'TTJets_amcnlo_central',
'TTFSRScaledown_powheg_p1',
'TTFSRScaledown_powheg_p2',
'TTFSRScaleup_powheg_p1',
'TTFSRScaleup_powheg_p2',
'TTISRScaledown_powheg_p1',
'TTISRScaledown_powheg_p2',
'TTISRScaleup_powheg_p1',
'TTISRScaleup_powheg_p2',
'TTUETunedown_powheg',
'TTUETuneup_powheg',
'TTHdampup_powheg',
'TTHdampdown_powheg',
'TTCRone_powheg',
'TTCRtwo_powheg',
'TTJets_powheg_mass1665',
'TTJets_powheg_mass1715',
'TTJets_powheg_mass1755',
'TTJets_powheg_mass1695',
'TTJets_powheg_mass1735',
'TTJets_powheg_mass1785',
'TTJets_powheg_width02',
'TTJets_powheg_width2',
'TTJets_powheg_width8',
'TTJets_powheg_width05',
'TTJets_powheg_width4',
'T_tW',
'Tbar_tW',
'T_tch',
'Tbar_tch',
'WZ',
'WZp1',
'WJets',
'W1Jets',
'W2Jets',
'W3Jets',
'W4Jets',
'DYJets_50MG',
'DY1Jets_50MG',
'DY2Jets_50MG',
'DY3Jets_50MG',
'DY4Jets_50MG',
'TTH',
'TTZ',
'TTW',
'TTTW',
'TTWZ',
'TTZZ',
'TTZH',
'TTHH',
'TTTJ'
]

SUCCESS_FRACTION_THRESHOLD = 0.95
SLEEP = 15.*60. #0.5      # delay between cluster job status queries (should be more than 15 mins to update user dir)
#SLEEP = 10 #0.5      # delay between cluster job status queries (should be more than 15 mins to update user dir)
MAX_RUNNING_TIME = 10 #Maximum ten hrs

USER=os.environ.get('USER','none')
PRINT_JOBS=args.print_jobs
N_DAYS=args.ndays

LOG_DIR="/group/log/torque/"

u = {}

#Parse big-submission log
bigsub_jobs = get_list_of_submitted_jobs_from_bigsubmission_log(args.infile)

#Remove samples that are not in the big-submission log
list_of_samples_to_merge = []
for sample in init_list_of_samples_to_merge:
	if any([sample in bigsub_jobs[job] for job in bigsub_jobs.keys()]): list_of_samples_to_merge.append(sample)
	else:
		print(RED+'No logs for sample '+BLUE+'{0}'.format(sample)+RED+' in'+BLUE+' {0}'.format(args.infile)+DEF)
		print('Removing it from the list')

#Iterate over list of samples until it is empty or maximum running time is exceeded
running_time = 0
while len(list_of_samples_to_merge)>0 and running_time<MAX_RUNNING_TIME:

  running_time = (time.time()-start_time)/(60.0*60.0) # running_time [hrs]

  u = parse_cluster_logs(LOG_DIR, N_DAYS, USER, PRINT_JOBS)
  # wait until cluster logs are updated
  if USER not in u:
    time.sleep(60)
    continue

  list_of_samples_to_remove = []
  for sample in list_of_samples_to_merge:
    is_sample_ok = False
    job_success = 0	# number of successeded jobs for this sample
    job_fail = 0	# number of failed jobs for this sample

    # list of all submitted jobs for 'sample'
    job_id_with_selection = [job for job in bigsub_jobs.keys() if sample in bigsub_jobs[job]]

    # loop over completed jobs
    for job in job_id_with_selection:
      if job in u[USER].jobs and u[USER].jobs[job]['exit_code'] == 0:
	job_success+=1
      elif job in u[USER].jobs and u[USER].jobs[job]['exit_code'] != 0: 
        print(RED+'Job '+BLUE+'{0} {1}'.format(job,bigsub_jobs[job])+DEF+\
              RED+' failed with exit code:{0}'.format(u[USER].jobs[job]['exit_code'])+DEF)
	job_fail+=1

    success_fraction = float(job_success)/float(len(job_id_with_selection)) # check fraction of failed non-data jobs
    if job_success == len(job_id_with_selection): is_sample_ok = True
    if (job_success+job_fail) == len(job_id_with_selection) and success_fraction>=SUCCESS_FRACTION_THRESHOLD and 'data' not in sample.lower(): is_sample_ok = True

    if not is_sample_ok:
	if job_success+job_fail == len(job_id_with_selection) and job_fail>0: 

		list_of_samples_to_remove.append(sample)

		print('Some jobs from sample: '+BLUE+'{0}'.format(sample)+RED+' failed'+DEF)
		if 'data' in sample.lower(): notify_fail(sample,success=job_success,fail=job_fail) # fail data immediately

		if 'data' not in sample.lower() and success_fraction<SUCCESS_FRACTION_THRESHOLD: 
			print('SEVERE FAILURES!!! Fraction of failed jobs is {0}\%.'.format((1.-float(success_fraction))*100.))
			notify_fail(sample,success=job_success,fail=job_fail)	# fail mc with high fraction of fails

	elif job_success+job_fail != len(job_id_with_selection):
		print(u)
		print('{0}/{0}. Total: {0}'.format(job_success,job_fail,len(job_id_with_selection)))
		print('Skipping sample {0} for now'.format(sample))

    if is_sample_ok:#sample successed

        list_of_samples_to_remove.append(sample)

        print(GREEN+'Init merging'+DEF+' {0}'.format(sample))
	notify_success(sample,success=job_success,fail=job_fail)
        merge_craneens_process(sample,builddir=args.builddir,inputlocation=args.inputlocation)
  if len(list_of_samples_to_merge)>0:
	temp_list = [sample for sample in list_of_samples_to_merge if sample not in list_of_samples_to_remove]
	list_of_samples_to_merge = temp_list
  	time.sleep(SLEEP)

