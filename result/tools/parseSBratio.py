#!/usr/bin/env python

"""
Script for Higgs Combine cards creation
"""

import os
import sys
import time
import argparse
import logging
import json
from datetime import datetime
from operator import itemgetter, attrgetter, methodcaller

import pandas as pd
import numpy as np
import math

import ROOT

def strbin2tup(strbin):
	origname = strbin
	strbin.strip()
	ch = strbin[0:2]
	strbin = strbin[2:]
	jetbin = strbin.split("J")[0]
	bjetbin= strbin.split("J")[1].split("M")[0]
	return (origname, ch, int(jetbin), int(bjetbin))

class makeTable_tex:
	def __init__(self):
		self.JSONs = []
	def execute(self):
		searchcategories = self.JSONs[0]["bg"].keys()
		searchcategories = [strbin2tup(x) for x in searchcategories]
		searchcategories = sorted(searchcategories,key=itemgetter(2,3))
		header = '{:20}'
		header += '&{:>15}&{:>15}&{:>15}'*len(self.JSONs)
		header += '\\\\'
		columnnames = ["BG rate", "Signal rate", "S/B ratio"]*len(self.JSONs)
		columnnames.insert(0,"Search category")
		print columnnames
		print header.format(*columnnames)
		for cat in searchcategories:
			str = ''
			for item, json in enumerate(self.JSONs):
				tempstr = ''
				if item == 0:
					tempstr = '{:20}&{:>15.2f}&{:>15.2f}&{:>15.5f}'.format(cat[0], json["bg"][cat[0]], json["sg"][cat[0]], json["sg"][cat[0]]/json["bg"][cat[0]])
				else:
					tempstr = '&{:>15.2f}&{:>15.2f}&{:>15.5f}'.format(json["bg"][cat[0]], json["sg"][cat[0]], json["sg"][cat[0]]/json["bg"][cat[0]])
				str += tempstr
			str += '\\\\'
			print str

class makeTable_txt:
	def __init__(self):
		self.JSONs = []
	def execute(self):
		searchcategories = self.JSONs[0]["bg"].keys()
		searchcategories = [strbin2tup(x) for x in searchcategories]
		searchcategories = sorted(searchcategories,key=itemgetter(2,3))
		header = '{:20}'
		header += '{:>15}{:>15}{:>15}'*len(self.JSONs)
		columnnames = ["BG rate", "Signal rate", "S/B ratio"]*len(self.JSONs)
		columnnames.insert(0,"Search category")
		print columnnames
		print header.format(*columnnames)
		for cat in searchcategories:
			str = ''
			for item, json in enumerate(self.JSONs):
				tempstr = ''
				if item == 0:
					tempstr = '{:20}{:>15.2f}{:>15.2f}{:>15.5f}'.format(cat[0], json["bg"][cat[0]], json["sg"][cat[0]], json["sg"][cat[0]]/json["bg"][cat[0]])
				else:
					tempstr = '{:>15.2f}{:>15.2f}{:>15.5f}'.format(json["bg"][cat[0]], json["sg"][cat[0]], json["sg"][cat[0]]/json["bg"][cat[0]])
				str += tempstr
			print str
class MakeTable:
	def __init__(self, input_list=None, operator=None):
		self.JSONs = []
		if input_list: 
			for item in input_list:
				with open(item) as json_data:
					jsondic = json.load(json_data)
					self.JSONs.append(jsondic)
		if operator:
			self.execute = operator.execute
			operator.JSONs = self.JSONs

	def execute(self):
		print 'output type is not specified'

def main(args):
	outputProcessor = MakeTable
	if 'tex' in args.format:
		mt = makeTable_tex()
		outputProcessor = MakeTable(args.files,mt)
	elif 'txt' in args.format:
		mt = makeTable_txt()
		outputProcessor = MakeTable(args.files,mt)

	else:
		print "Output format is not recognized!"
		print  args.format
		sys.exit(1)

	
	outputProcessor.execute()

if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('files', nargs='+', help='Input JSON files')
	parser.add_argument('-f', '--format', help="Output format (.txt, .tex)", default='.tex')
        parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))
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
