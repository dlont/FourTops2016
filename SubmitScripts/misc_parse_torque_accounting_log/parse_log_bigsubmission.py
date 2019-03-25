import re

#match color codes
ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
#match cn domain name
domain_name = re.compile(r'.cream02.iihe.ac.be')

def get_list_of_submitted_jobs_from_bigsubmission_log(filename):
	'''
	parse big-submission.log file and extract
	job id's and corresponding names
	'''

	# dictionary of the form
	# {pbsjobid: script.sh}
	jobs={}
	with open(filename,'r') as f_bigsub:
		name = ''
		id   = ''
		
		for l in f_bigsub:
			filtered_l = ansi_escape.sub('', l)				# strip linux color symbols
			
			# lines of type: Command: qsub ../submit_DY1Jets_50MG_101to104.sh
			if 'Command' in filtered_l: name = filtered_l.split()[-1]	# shell script name is the last word in the filtered_l

			# lines of type: 23510196.cream02.iihe.ac.be
			if '.iihe.ac.be' in filtered_l: 
				id = domain_name.sub('',filtered_l).strip()		# strip .cream02.iihe.ac.be
				jobs[id]=name
	return jobs

