#!/usr/bin/python

from __future__ import print_function
import math  
import time
import sys, os
from misc_parse_torque_accounting_log.parse_log_classes import *
from misc_parse_torque_accounting_log.parse_log_functions import *

USER=os.environ.get('USER','none')
PRINT_JOBS=True
N_DAYS=2

LOG_DIR="/group/log/torque/"

# Making auto list file
log_files=get_list_of_log_files( LOG_DIR , N_DAYS ) 

n_jobs_total=0
u={}  # array of users with key=username

n_days=0
for day in log_files:
  n_days+=1
  if n_days > N_DAYS:
    break

  fi=open(LOG_DIR+day, 'r')

  # Looping over lines for one day log
  for line in fi:

    # Selecting only info from jobs that ended
    if "Exit" in line:

      # Init of the job container for each log line
      j = job_class()

      # Incrementing the number of jobs
      n_jobs_total+=1
 
      fields = line.split()
  
      # Getting the fields 
      j.fill( fields )

      # Looking only at user USER
      if j.user != USER:
        continue
      
      # If printing is enabled, print the job info
      if PRINT_JOBS:  
        j.f_Print()
        #print(day,j.user,j.exit,str(int(j.vmem/1024))+"M",str(j.cput)+"s",str(j.walltime)+"s",j.host)

      # Init the user array
      if not u.has_key(j.user):
        u[j.user]=user_class()

      # Filling the user/host with the job
      u[j.user].fill(j)
     

#Print users total for all days
print_header_for_users()
for key in sorted(u.keys()):
  u[key].f_Print(print_ec=True)

