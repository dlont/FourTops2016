#!/usr/bin/python

from __future__ import print_function
import math  
import time
from parse_log_functions import *

HIGH_MEM=2048000
PRINT_USERS=False
PRINT_HOSTS=False

# COLORS
BLUE='\033[1;34m'
CYAN='\033[1;36m'
RED='\033[1;31m'
GREEN='\033[1;32m'
YEL='\033[1;33m'
PURP='\033[1;35m'
DEF='\033[0;m'

class mean_class:
  tot=0
  tot_of_square=0
  n=0

  def mean( self ):
    if self.n != 0:
      return float(self.tot / self.n)
    else:
      return 0

  def rms( self ):
    if self.n != 0:
      r=self.tot_of_square / self.n - self.mean() * self.mean()
      return math.sqrt( r ) 
      #return  r  
    else:
      return 0

  def add( self , val , w = 1 ):
    self.tot+=float(val*w)
    self.tot_of_square+=float(val*val*w)
    self.n+=w

#########################
#      JOB CLASS
#########################

def get_job_id_from_accounting( fields ):
  jobID=fields[1].split('.cream')[0].split(';')[2]
  return str(jobID)
def get_job_id_from_apel( line ):
  jobID=line.split('lrmsID=')[1].split('.cream')[0]
  return str(jobID)

class job_class:
  job_id=''
  user=""
  group=""
  jobname=''
  exit=""
  vmem=0
  mem=0
  start=0
  end=0
  cput=0
  walltime=0
  host=""
  vmem_pledged=0
  walltime_pledged=0

  #types : queue, end, start
  def fill( self , fields , type='end'):
    
    # Getting the job ID through the defined function
    self.job_id=get_job_id_from_accounting( fields )

    for f in fields:
      if "user=" in f:
        self.user=f.split("user=")[1]
      if "group=" in f:
        self.group=f.split("=")[1]

      if "jobname=" in f:
        self.jobname=f.split("=")[1]

      if "exec_host=" in f:
        self.host=f.split("=")[1].split(".wn")[0] 

      if "start=" in f:
        self.start=int(f.split("=")[1])

      if "Resource_List.vmem=" in f:
        self.vmem_pledged=f.split("=")[1]
        self.vmem_pledged=mem_to_kb(self.vmem_pledged)

      if "Resource_List.walltime=" in f:
        self.walltime_pledged=f.split("=")[1]

      # Fields are there only if job has ended
      if type == 'start':
        return

      if "Exit_status" in f:
        self.exit=str(f.split("=")[1])
      if "end=" in f:
        self.end=int(f.split("=")[1])

      if "resources_used.cput" in f:
        self.cput=hms_to_s(f.split("=")[1])

      if "resources_used.walltime=" in f:
        self.walltime=hms_to_s(f.split("=")[1])

      if "resources_used.vmem=" in f:
        self.vmem=float(f.split("=")[1][:-2])

      if "resources_used.mem=" in f:
        self.mem=float(f.split("=")[1][:-2])

  def f_Print(self):
    # Calculating eff
    if self.walltime != 0:
      eff = 100.*self.cput/self.walltime
    else:
      eff = 0

    # Printing
    print(BLUE+"ID:"+DEF+" %-8s " % self.job_id,end='')
    print(BLUE+"ExCode:"+DEF+"%4s " % self.exit,end='')
    print(BLUE+"Mem:"+DEF+"%5.0fM " % (self.mem/1024),end='')
    print(BLUE+"cpuT:"+DEF+" %6is " % self.cput,end='')
    print(BLUE+"wallT:"+DEF+" %6is " % self.walltime,end='')
    print(BLUE+"eff:"+DEF+"%5.1f%% " % (eff),end='')
    print((RED+"%7s"+DEF) % self.jobname)

class user_class:
  user=""
  group=""
  n_jobs=0
  n_jobs_high_ram=0
  max_ram=0 
 
  def __init__( self):
    self.ram=mean_class()
    self.cput=mean_class()
    self.walltime=mean_class()
    self.efficiency=mean_class()
    self.exit={} 
    self.jobs={}  #dictionary of user jobs

  def f_Print( self , total_walltime=0. , print_ec=True ):  
    print("%10s[%s]\t%6.0f\t" % (self.user,self.group[:1],self.n_jobs) , end='')
    print("%6.0f +- %-5.0f MB" % (self.ram.mean()/1024,self.ram.rms()/1024) , end='')
    print(" %6.0f  %6.0f MB" % (self.n_jobs_high_ram,self.max_ram/1024) , end='')
    print("  |  %s  %s" % ( s_to_dhms(int(round(self.cput.mean()))) , s_to_dhms(int(round(self.walltime.mean()))) ) , end='')
    print("  (%4.1f%%)" % ( self.efficiency.mean() ) , end='')
    frac_walltime = -1
    if total_walltime != 0:
      frac_walltime = self.walltime.tot / total_walltime * 100.
    print(" (%5.2f%% of tot)" % ( frac_walltime ) , end='')
    if print_ec:
      print(" | # EC: ", end='')
      for key in sorted(self.exit.keys()):
        print("%3s=>%-5s(%4.1f%%) ; " % (key , self.exit[key] , float(self.exit[key]) / float(self.n_jobs) * 100. ), end='') 
    print("")

  def fill( self , j ):
    self.user=j.user
    self.group=j.group
    self.n_jobs+=1
    self.ram.add(j.mem)
    self.cput.add(j.cput)
    self.walltime.add(j.walltime)
    if j.walltime != 0:
      self.efficiency.add(float(j.cput)/float(j.walltime)*100.)
    if j.mem > HIGH_MEM:
      self.n_jobs_high_ram+=1
    if self.max_ram < j.mem:
      self.max_ram=j.mem
    if j.exit != "0":
      if self.exit.has_key(j.exit):
        self.exit[j.exit]+=1
      else:
        self.exit[j.exit]=1

    #dictionary of user jobs by name
    self.jobs[j.job_id]={'name':j.jobname,'exit_code':int(j.exit)}


class error_class:
  n_jobs=0
  n_over_ram=0
  n_over_walltime=0

class host_class:
  host=""
  n_jobs=0
  n_jobs_high_ram=0
  max_ram=0

  def __init__( self ):
    self.users=[]
    self.ram=mean_class()
    self.cput=mean_class()
    self.walltime=mean_class()
    self.efficiency=mean_class()
    self.exit={}

  def f_Print( self , total_walltime=0. , print_ec=True ):
    print("%-9s  %6.0f  %2.0f\t" % (self.host,self.n_jobs,len(self.users)) , end='')
    print("%6.0f +- %-5.0f MB" % (self.ram.mean()/1024,self.ram.rms()/1024) , end='')
    print(" %6.0f  %6.0f MB" % (self.n_jobs_high_ram,self.max_ram/1024) , end='')
    print("  |  %s  %s" % ( s_to_dhms(int(round(self.cput.mean()))) , s_to_dhms(int(round(self.walltime.mean()))) ) , end='')
    print("  (%4.1f%%)" % ( self.efficiency.mean() ) , end='')
    if total_walltime != 0:
      print(" (%5.2f%% of tot)" % ( self.walltime.tot / total_walltime * 100. ) , end='')
    #print("  %6.0f  %6.0f  (%4.1f%%)" % ( self.cput.mean() , self.walltime.mean() , self.efficiency.mean() ) , end='')
    if print_ec:
      print(" | # EC: ", end='')
      for key in sorted(self.exit.keys()):
        print("%3s=>%-5s(%4.1f%%) ; " % (key , self.exit[key] , float(self.exit[key]) / float(self.n_jobs) * 100. ), end='')
    print("")



  def fill( self , j ):
    if j.user not in self.users:
      self.users.append(j.user)
    self.host=j.host
    self.n_jobs+=1
    self.ram.add(j.mem)
    self.cput.add(j.cput)
    self.walltime.add(j.walltime)
    if j.walltime != 0:
      self.efficiency.add(float(j.cput)/float(j.walltime)*100.)
    if j.mem > HIGH_MEM:
      self.n_jobs_high_ram+=1
    if self.max_ram < j.mem:
      self.max_ram=j.mem
    if j.exit != "0":
      if self.exit.has_key(j.exit):
        self.exit[j.exit]+=1
      else:
        self.exit[j.exit]=1




class day_class:
  day=""
  n_jobs=0
  walltime=0
 
  def __init__( self , print_users = False , print_hosts = False):
    self.u={}
    self.h={}
    self.print_bool={}
    self.print_bool["users"]=print_users
    self.print_bool["hosts"]=print_hosts
   
   
  def f_Print( self ):
    if self.print_bool["users"]:
      print_header_for_users()
      for key in sorted(self.u.keys()):
        self.u[key].f_Print(self.walltime)

    if self.print_bool["hosts"]:
      print_header_for_hosts()
      for key in sorted(self.h.keys()):
        self.h[key].f_Print(self.walltime)
