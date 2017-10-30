import sys
import subprocess
import os
import json
import pandas as pd
from pprint import  pprint
from prettytable import  PrettyTable
from prettytable import MSWORD_FRIENDLY
from itertools import *


def get_lim(lim_str, xsec, name, format='txt', json_filename=None, ch=''):
    """
	Convert combine tool output to different format.
	lim_str: raw combine output string with Observed or Expected strings only.
	xsec: constant SM cross section prediction.
	name: Process label (e.g. 'TTTT').
	format: target format [txt,tex,json and combinations thereof].
	out_filename: json output file name
    """
    d = {}
    for line in lim_str.splitlines():
        if "Observed" in line: d["obs"] = float(line.split("<")[-1])
        elif "Expected" in line: d["exp_"+line.split("%")[0].replace("Expected","").strip()] = float(line.split("<")[-1])
        elif "Significance" in line: d["signif"] = float(line.split(":")[-1])
        elif "Best" in line: 
		d["bestfit"] = float(line.split(":")[-1].split()[0])
		d["bestfit_16.0"] = float(line.split(":")[-1].split()[1].split("/")[0])
		d["bestfit_64.0"] = float(line.split(":")[-1].split()[1].split("/")[1])

    unit = "pb"
    if d["exp_50.0"]*xsec < 0.9:
        xsec *= 1000.0
        unit = "fb"
    obs = -1.
    if 'obs' in d: obs = d["obs"]*xsec
    exp = d["exp_50.0"]*xsec
    exp_sm1 = d["exp_16.0"]*xsec
    exp_sp1 = d["exp_84.0"]*xsec

    json_array = json.dumps(d)

    if 'txt' in format:
	print "Limits for %s" % name
    	if obs > 0.: print "  Obs: %.2f %s" % (obs, unit)
    	print "%s %.2f + %.2f - %.2f %s" % (ch, d["exp_50.0"], d["exp_84.0"]-d["exp_50.0"], d["exp_50.0"]-d["exp_16.0"], "xSM")
    	return "%s %.2f + %.2f - %.2f %s" % (ch, d["exp_50.0"], d["exp_84.0"]-d["exp_50.0"], d["exp_50.0"]-d["exp_16.0"], "")
    	#print "%s %.2f + %.2f - %.2f %s" % (ch, exp, exp_sp1-exp, exp-exp_sm1, unit)
    if 'tex' in format:
	if ch == 'Mu': ch = '\mu'
	if ch == 'El': ch = 'e'
        print "Limits for %s" % name
        if obs > 0.: print "  Obs: %.2f \%s" % (obs, unit)
        print "$%s$ & $%.1f^{+%.1f}_{-%.1f}$ & $%.0f^{+%.0f}_{-%.0f}$ \%s \T\B\\\\ \n\\hline" % (ch, d["exp_50.0"], d["exp_84.0"]-d["exp_50.0"], d["exp_50.0"]-d["exp_16.0"], exp, exp_sp1-exp, exp-exp_sm1, unit)
	return "$%s$ & $%.1f^{+%.1f}_{-%.1f}$ & $%.0f^{+%.0f}_{-%.0f}$ \%s \T\B\\\\ \n\\hline" % (ch, d["exp_50.0"], d["exp_84.0"]-d["exp_50.0"], d["exp_50.0"]-d["exp_16.0"], exp, exp_sp1-exp, exp-exp_sm1,unit)
        #print "$%s$ & $%.5f^{+%.5f}_{-%.5f}$ & $%.0f^{+%.0f}_{-%.0f}$ \%s \T\B\\\\ \n\\hline" % (ch, d["exp_50.0"], d["exp_84.0"]-d["exp_50.0"], d["exp_50.0"]-d["exp_16.0"], exp, exp_sp1-exp, exp-exp_sm1, unit)
	if 'signif' in d and 'bestfit' in d:
		print "$%s$ & $%.2f$ & $%.0f^{+%.1f}_{%.1f}$ & $%.1f^{+%.0f}_{%.0f}$ \%s \T\B\\\\ \n\\hline" % (ch, d["signif"], d['bestfit'], d['bestfit_64.0'], d['bestfit_16.0'], d['bestfit']*xsec, d['bestfit_64.0']*xsec, d['bestfit_16.0']*xsec, unit)
    if 'json' in format:
	if json_filename is not None:
		with open(json_filename, 'w') as outfile:
    			json.dump(d, outfile, sort_keys=True, indent=4)

syst_dic = {
#'TTJets_norm':'lnN',
#'ttMEScale':'shape',
#'TTJets_HDAMP':'lnN',
#'TTJets_PDF':'shape',
#'heavyFlav':'shape',
#'tttt_norm':'lnN',
#'TTTTMEScale':'shape',
#'ST_tW_norm':'lnN',
#'EW_norm':'lnN',
#'TTRARE_norm':'lnN',
#'lumi':'lnN',
#'PU':'shape',
'SubTotalPileUpJES':'shape',
'SubTotalScaleJES':'shape',
'SubTotalPtJES':'shape',
'SubTotalRelativeJES':'shape',
#'JER':'shape',
#'leptonSFMu':'lnN',
#'TTISR':'lnN',
#'TTFSR':'lnN',
#'TTUE':'lnN',
#'TTPT':'shape',
#'TTTTISR':'lnN',
#'TTTTFSR':'lnN',
#'btagWeightCSVJES':'shape',
#'btagWeightCSVHF':'shape',
#'btagWeightCSVLF':'shape',
#'btagWeightCSVHFStats1':'shape',
#'btagWeightCSVHFStats2':'shape',
#'btagWeightCSVLFStats1':'shape',
#'btagWeightCSVLFStats2':'shape',
#'btagWeightCSVCFErr1':'shape',
#'btagWeightCSVCFErr2':'shape'
}

mask_channels10 = ',mask_EL_el10J2M=1,mask_EL_el10J3M=1,mask_EL_el10J4M=1,mask_MU_mu10J2M=1,mask_MU_mu10J3M=1,mask_MU_mu10J4M=1'
mask_channels9  = ',mask_EL_el9J2M=1,mask_EL_el9J3M=1,mask_EL_el9J4M=1,mask_MU_mu9J2M=1,mask_MU_mu9J3M=1,mask_MU_mu9J4M=1'
mask_channels8  = ',mask_EL_el8J2M=1,mask_EL_el8J3M=1,mask_EL_el8J4M=1,mask_MU_mu8J2M=1,mask_MU_mu8J3M=1,mask_MU_mu8J4M=1'
mask_channels7  = ',mask_MU_mu7J2M=0,mask_MU_mu7J3M=1,mask_MU_mu7J4M=1'
mask_channels   = mask_channels7+mask_channels8+mask_channels9+mask_channels10

card_file = "final_unblinding/datacard_elmu.root"

mask_flag = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
permutations = [list(mask_flag)]
#for i in range(0,1):
for i in range(0,len(mask_flag)-1):
	mask_flag.insert(i+1, mask_flag.pop(i))
	permutations.append(list(mask_flag))

pprint(permutations)

mask_template = ',mask_EL_el10J2M={},mask_EL_el10J3M={},mask_EL_el10J4M={},mask_MU_mu10J2M={},mask_MU_mu10J3M={},mask_MU_mu10J4M={}'+\
		',mask_EL_el9J2M={},mask_EL_el9J3M={},mask_EL_el9J4M={},mask_MU_mu9J2M={},mask_MU_mu9J3M={},mask_MU_mu9J4M={}'+\
		',mask_EL_el8J2M={},mask_EL_el8J3M={},mask_EL_el8J4M={},mask_MU_mu8J2M={},mask_MU_mu8J3M={},mask_MU_mu8J4M={}'+\
		',mask_MU_mu7J2M={},mask_MU_mu7J3M={},mask_MU_mu7J4M={}'

mask_flag = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
permutations = [list(mask_flag)]

xsec_tttt = 0.009201 # pb
x = PrettyTable(["Active bin","Syst","Central xSM", "Up xSM", "Down xSM"])
x.set_style(MSWORD_FRIENDLY)
for perm in permutations:
	mask_channels = mask_template.format(*perm)
	#identify sting name of the bin that is active
	active_bin = ''
	list_of_masked_channels=mask_channels.split(',')
	for elem in list_of_masked_channels:
		if '=0' in elem:
			active_bin = elem.split('=')[0].split('_')[2]	
	active_bin = 'all'
	for systematic in syst_dic.keys():
		print systematic, 'central'
		out = subprocess.check_output(["combine", "-M", "Asymptotic", card_file, "--run", "blind", \
					"--setParameters", systematic+"=0.0"+mask_channels, "--freezeParameters", systematic])
		cen = get_lim(out, xsec_tttt, "TTTT", "txt")

		print systematic, '-1.0 s.d.'
		print " ".join(["combine", "-M", "Asymptotic", card_file, "--run", "blind", \
                                        "--setParameters", systematic+"=-1.0"+mask_channels, "--freezeParameters", systematic])
		out = subprocess.check_output(["combine", "-M", "Asymptotic", card_file, "--run", "blind", \
					"--setParameters", systematic+"=-1.0"+mask_channels, "--freezeParameters", systematic])
		down = get_lim(out, xsec_tttt, "TTTT", "txt")

		print systematic, '+1.0 s.d.'
		out = subprocess.check_output(["combine", "-M", "Asymptotic", card_file, "--run", "blind", \
					"--setParameters", systematic+"=1.0"+mask_channels, "--freezeParameters", systematic])
		up = get_lim(out, xsec_tttt, "TTTT", "txt")
		x.add_row( [active_bin,systematic, cen, up, down] )
	
print x
