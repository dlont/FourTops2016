#!/usr/bin/python

from __future__ import print_function
from parse_log_classes import *
import os

# Get list of torque accounting log files
# Ordered by date , taking the last N_DAYS
def get_list_of_log_files(LOG_DIR='' , N_DAYS = 3):
  log_files_all=[]
  for file in os.listdir(LOG_DIR):
    if file.startswith("201"):
      log_files_all.append(file)

  log_files_all.sort()
  if len(log_files_all) >= N_DAYS:
    return log_files_all[-N_DAYS:]
  else:
    return log_files_all



#Converts seconds to DAYS:HOURS:MINUTES:SECONDS
def s_to_dhms( s=0 ):
  (rest,seconds)=divmod(s,60.)
  (rest,minutes)=divmod(rest,60.)
  (days,hours)=divmod(rest,24.)
  return str("%02.f:%02.f:%02.f:%02.f" % (days,hours,minutes,seconds))

#Converts HOURS:MINUTES:SECONDS into seconds
def hms_to_s( t="00:00:00" ):
  f=t.split(':')
  return int(f[0])*3600+int(f[1])*60+int(f[2])

def print_header_for_users():
  print("-"*160)
  print("%10s\t%5s\t%18s %8s %8s" % ("user[G]","# Jobs", "<MEM> +- RMS     ","#HiMem","MAX Mem") , end='')
  print("%17s %13s %7s %15s %20s" % ("<CPU time> ","<walltime> ","<Eff>","% WT/WT_TOT  "," # Jobs with Error code (% of user job)") )
  print("-"*160)

def print_header_for_hosts():
  print("-"*160)
  print("%9s  %5s %6s\t%18s %8s %8s" % ("host  ","#Jobs",'#Users', "<MEM> +- RMS     ","#HiMem","MAX Mem") , end='')
  print("%17s %13s %7s %15s %20s" % ("<CPU time> ","<walltime> ","<Eff>","% WT/WT_TOT  "," # Jobs with Error code (% of user job)") )
  print("-"*160)


# Possibilities: n_jobs , n_jobs_high_ram , n_jobs_high_ram_pc
def print_per_day( d , u , val_to_print="n_jobs"):
  #Print the first line of days
  print("\t\t",end='')
  #for day in d.keys():
  for day in log_files:
    print(day+"  ",end='')
  print('')
  
  #Print line for each users
  for user in u.keys():
    print(user+"    \t", end='')
    #for day in d.keys():
    for day in log_files:
      if d[day].u.has_key(user):
        if val_to_print == "n_jobs":
          print("%6.0f    " % ( d[day].u[user].n_jobs) ,end='') 
        if val_to_print == "n_jobs_high_ram":
          print("%6.0f    " % ( d[day].u[user].n_jobs_high_ram) ,end='')
        if val_to_print == "n_jobs_high_ram_pc":
          print("%6.1f    " % ( float(d[day].u[user].n_jobs_high_ram) / float(d[day].u[user].n_jobs) * 100.) ,end='') 
      else:
        print("%6s    " % ( '--' ) ,end='')
    print('')
  print('\n\n')


def mem_to_kb( m ):
  if "gb" in m:
    return float(m[:-2])*1024.*1024.
  elif "mb" in m:
    return float(m[:-2])*1024.
  elif "kb" in m:
    return float(m[:-2])
  else:
    return 0



