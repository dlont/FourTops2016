from misc_parse_torque_accounting_log.parse_log_classes import *
from misc_parse_torque_accounting_log.parse_log_functions import *
from misc_parse_torque_accounting_log.parse_log_bigsubmission import *

def parse_cluster_logs(LOG_DIR, N_DAYS, USER, PRINT_JOBS=False):

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

				# Init the user array
				if not u.has_key(j.user):
					u[j.user]=user_class()

				# Filling the user/host with the job
				u[j.user].fill(j)

				# If printing is enabled, print the job info
				if PRINT_JOBS:  
					j.f_Print()
		fi.close()
	return u
