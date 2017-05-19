#!/usr/bin/env python

"""
Draw systematic comparison in multiple bins.
"""

import os
import sys
import time
import argparse
import logging
import json
from pprint import pprint, pformat

from ROOT import TFile
from ROOT import gStyle

from plotter import *


def main(arguments):
	total = 1000
	i = 0

	json_dic = {}
	if arguments.config_json is not None:
		with open (arguments.config_json) as configuration_file:
			json_dic = json.load(configuration_file)
		logging.debug(pformat(json_dic))


	p = plotter(inputfolder=arguments.infolder) 
	p.make_pages(json_dic)

        return 0

if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('infolder', help="Input folder")
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
        parser.add_argument('-b', dest='batch', action='store_true', help="ROOT batch mode")

        args = parser.parse_args(sys.argv[1:])
	if args.batch:
		sys.argv.append( '-b-' )

        print(args)
        
        logging.basicConfig(level=args.loglevel)

        logging.info( time.asctime() )
        exitcode = main(args)
        logging.info( time.asctime() )
        logging.info( 'TOTAL TIME IN MINUTES:' + str((time.time() - start_time) / 60.0))
        sys.exit(exitcode)
