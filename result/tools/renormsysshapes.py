#!/usr/bin/env python

"""
Scale histograms to the integral of the reference one.
"""

import os
import sys
import time
import argparse
import logging
import json
from pprint import pprint, pformat

import ROOT as rt

def progress(current, total, status=''):
        fullBarLength = 80
        doneBarLength = int(round(fullBarLength * current / float(total)))

        percents = round(100.0 * current / float(total), 1)
        bar = '>' * doneBarLength + ' ' * (fullBarLength - doneBarLength)

        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()

def main(arguments):

	referencefile = rt.TFile.Open(arguments.reffile,"READ")
	infile        = rt.TFile.Open(arguments.infile,"UPDATE")
	
	syslist       = arguments.syslist.split(',')
	logging.info("List of systematics to be rescaled: " + pformat(syslist))

	for key in infile.GetListOfKeys():
		folder = key.ReadObj()
		hist = None
		hist = folder.Get(arguments.hist)
		if hist is None:
			print 'Input folder {}'.format(folder.GetName())
			raise Exception('Can find histogram {} in the input file!'.format(arguments.hist))

		#find corresponding histogram in the reference files
		splitlist = folder.GetName().split('_')
		if len(splitlist) < 2: continue
		reffoldename = splitlist[0]
		systname     = ''.join(splitlist[1:])
		refhist = None
		refhist = referencefile.Get(reffoldename+'/'+arguments.hist)
		if refhist is None:
			print 'Reference folder {}' % folder.GetName()
			raise Exception('Can find histogram {} in the input file!' % arguments.hist)

		# Skip systematic folders that are not in the syslist
		if not any(item in systname for item in syslist): 
			logging.debug("Folder skipped: {}".format(folder.GetName()))
			continue
		logging.debug("Rescaling {} to {}".format(arguments.infile+'/'+folder.GetName()+'/'+arguments.hist,
							  arguments.reffile+'/'+reffoldename+'/'+arguments.hist))
		i1 = hist.Integral()
		i2 = refhist.Integral()
                if i2 == 0:
                        logging.warning("Ref hist integral is 0! Something is potentially wrong. Hist name: {}".format(arguments.reffile+'/'+reffoldename+'/'+arguments.hist))
                        if i1 == 0:
                                logging.warning("Target histogram has no events. Check what is going on!")
		        folder.cd()
		        infile.cd()
                else:
		        logging.debug("Scale factor source/target: {} / {}".format(i1,i2))
		        hist.Scale(i2/i1)
		        folder.cd()
		        hist.Write(hist.GetName(),rt.TObject.kOverwrite)
		        infile.cd()
	
        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('infile', help="Input file")
        parser.add_argument('-r', '--reffile', help="Reference normalisation file")
        parser.add_argument('-t', '--hist', help="Histogram name")
        parser.add_argument('-s', '--syslist', help="Coma separated list of systematic unceratinties to be rescaled")
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
