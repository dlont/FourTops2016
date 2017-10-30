#!/usr/bin/env python

"""
A simple python script template.
"""

import os
import sys
import time
import argparse
import logging
import json
import itertools
import ntpath
from prettytable import  PrettyTable
from prettytable import MSWORD_FRIENDLY
from pprint import pprint, pformat
import ROOT as rt

def progress(current, total, status=''):
        fullBarLength = 80
        doneBarLength = int(round(fullBarLength * current / float(total)))

        percents = round(100.0 * current / float(total), 1)
        bar = '>' * doneBarLength + ' ' * (fullBarLength - doneBarLength)

        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()

class table:
	def __init__(self,x):
		self.decorated_tab = [[x]]
		return
	def printout(self):
		return


def main(arguments):

	bins = ["10J4M","10J3M","10J2M","9J4M","9J3M","9J2M","8J4M","8J3M","8J2M","7J4M","7J3M","7J2M",]
	#syst = ['SubTotalPileUpJES', 'SubTotalScaleJES', 'SubTotalPtJES', 'SubTotalRelativeJES']
	#syst = ['heavyFlav', 'PU', 'JER']
	#syst = ['TTFSR', 'TTISR', 'TTUE','TTJets_HDAMP']
	syst = ['btagWeightCSVCFErr1','btagWeightCSVCFErr2','btagWeightCSVHF','btagWeightCSVHFStats1',
		'btagWeightCSVHFStats2','btagWeightCSVJES','btagWeightCSVLF','btagWeightCSVLFStats1','btagWeightCSVLFStats2']
	var  = ['Up','Down']
	
	histname = 'bdt'


	files = [rt.TFile.Open(f) for f in arguments.infile]

	generic_column_names = ["Central (events) ", "Up (rel.%) ", "Down (rel.%) "]
	column_names = []
	for f in arguments.infile:
		proc = ''
		if 'Hists_TT_CARDS.root' in f: proc = 'TT'
		if 'Hists_TTTT_CARDS.root' in f: proc = 'TTTT'
		column_names = column_names + [col+proc for col in generic_column_names]

	x = PrettyTable(["SR", "Syst"]+column_names)
	x.set_style(MSWORD_FRIENDLY)

	for b in bins:
		for s in syst:
			numbers_for_files = []
			for f in files:
				events = []
				#central histo
				name = b+'/'+histname
				hist = f.Get(name)
				logging.info(name)
				events.append(hist.Integral())
				#up/down variations histo
				for v in var:
					name = b+'_'+s+v+'/'+histname
					logging.info(name)
					hist = f.Get(name)
					events.append(hist.Integral())
				numbers_for_files = numbers_for_files + [round(events[0],2)]+[round(ev/events[0],2)-1. for ev in events[1:]]
			x.add_row([b, s]+numbers_for_files)

	print x
        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('infile', nargs='+', help="Input file")
        parser.add_argument('-o', '--outfile', help="Output file")
        parser.add_argument('-j', '--config-json', type=json.loads, help="JSON configuration file")
        #parser.add_argument('-b', help="ROOT batch mode", dest='isBatch', action='store_true')
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
