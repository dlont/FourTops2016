#!/usr/bin/env python

"""A simple python script template.
"""

import os
import sys
import time
import argparse
import logging
import json
from pprint import pprint

import ROOT as rt
import re
from array import array
from sets import Set

def progress(current, total, status=''):
        fullBarLength = 80
        doneBarLength = int(round(fullBarLength * current / float(total)))

        percents = round(100.0 * current / float(total), 1)
        bar = '>' * doneBarLength + ' ' * (fullBarLength - doneBarLength)

        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()

def efficiency(root_file,args):
	
	exec("tree = root_file.%s" % (args.tree_name))

	list_of_triggers = args.triggers.split(':') # reference trigger is always at [0]
	ref_trigger_name = list_of_triggers[0]
	study_trigger = list(filter(None,re.split('(\|\||&&)',list_of_triggers[1]))) # use spaces to make the formula for the trigger decision

	cpp2python_logic = {"||":" or ", "&&":" and "}
	trigger_requirement = ''

	#study trigger combination
	for token in study_trigger:
		if len(Set(['||', '&&']) & Set([token])) > 0: trigger_requirement += cpp2python_logic[token]
		else: trigger_requirement += 'event.{}==1'.format(token)
	#study trigger && reference trigger
	trigger_requirement += 'and event.{}==1'.format(ref_trigger_name)
	event_filter = 'pass_study = ('+trigger_requirement+')'

	logging.info(event_filter)
	
	histbinning = (0, 0, 0) #(nbins, xmin, xmax)
	xbins_list = []
	xbins = None
	if 'Pt' in args.variable_name:
		#uniform
		histbinning = (25,0.,500.)
		#non uniform
		xbins_list = [0., 10., 15., 18., 22., 24., 26., 30., 40., 50., 60., 80., 120., 200., 500.]
		xbins = array('d',xbins_list)
	if 'Eta' in args.variable_name:
		#uniform
		histbinning = (50,-2.5,2.5)
		#non uniform
		xbins_list = [-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0., 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4]
		xbins = array('d',xbins_list)

	#Uniform binning
	#pEff = rt.TEfficiency("eff","{};{};#epsilon".format(trigger_requirement,args.variable_name),histbinning[0],histbinning[1],histbinning[2])
	#Non uniform binning
	pEff = rt.TEfficiency("eff","{};{};#epsilon".format(trigger_requirement,args.variable_name),len(xbins)-1,xbins)

	nentries = tree.GetEntries()
        ientry = 0
	for event in tree:
		exec("var = event.%s" % (args.variable_name))
		exec("pass_ref = event.%s == 1" % (ref_trigger_name))
		exec(event_filter)
		logging.info(pass_study)
		if pass_ref:
			pEff.Fill(pass_study,var)
                
		if (ientry % 100 == 0): progress(ientry, nentries, 'Progress. N entries={}'.format(nentries))
		ientry += 1
	print '\n'

	c = rt.TCanvas("c","CMS",5,45,500,500)
	pEff.Draw("AP")
	rt.gPad.Update()

	if args.outfile: 
		outfile = rt.TFile.Open(args.outfile,"RECREATE")
		graph = pEff.GetPaintedGraph()
		graph.Write()
		pEff.GetPassedHistogram().Write()
		pEff.GetTotalHistogram().Write()
	

def main(arguments):

	input_root_file = rt.TFile.Open(arguments.infile, "READ")
	efficiency(input_root_file,arguments)

        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('infile', help="Input file")
        parser.add_argument( '--tree-name', help="Tree Name where variables are stored")
        parser.add_argument( '--variable-name', help="Variable the function of which efficiency will be calculated")
        parser.add_argument( '--triggers', help="Triggers to be used for calculation. [TRG_REF:TRG_UNDER_TEST]")
        parser.add_argument('-o', '--outfile', help="Output file")
        parser.add_argument('-j', '--config-json', help="JSON configuration file")
        parser.add_argument(
                        '-d', '--debug',
                        help="Print lots of debugging statements",
                        action="store_const", dest="loglevel", const=logging.DEBUG,
                        default=logging.WARNING,
                        )
        parser.add_argument(
                        '-v', '--verbose',
                        help="Be verbose",
                        action="store_const", dest="loglevel", const=logging.INFO,
                        )

        args = parser.parse_args(sys.argv[1:])

        print(args)
        
        logging.basicConfig(level=args.loglevel)

        logging.info( time.asctime() )
        exitcode = main(args)
        logging.info( time.asctime() )
        logging.info( 'TOTAL TIME IN MINUTES:' + str((time.time() - start_time) / 60.0))
        sys.exit(exitcode)
