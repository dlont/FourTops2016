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

def progress(current, total, status=''):
        fullBarLength = 80
        doneBarLength = int(round(fullBarLength * current / float(total)))

        percents = round(100.0 * current / float(total), 1)
        bar = '>' * doneBarLength + ' ' * (fullBarLength - doneBarLength)

        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()

def main(arguments):
	#Manipulate python garbage collection
        rt.TGraph.__init__._creates = False


	file_sig = rt.TFile.Open(arguments.signal,"READ")
	tree_sig = file_sig.Get(arguments.tree)

	file_bg = rt.TFile.Open(arguments.background,"READ")
	tree_bg = file_bg.Get(arguments.tree)

	c = rt.TCanvas('c'); c.Divide(2,2)
	
	#MT1 vs MT2
	c.cd(1)
	tree_bg.Draw("mt2:mt1")
	gr_bg1 = rt.gPad.GetPrimitive("Graph").Clone("gr_bg_mt1_mt2")
	gr_bg1.SetMarkerColor(rt.kBlue)

	tree_sig.Draw("mt2:mt1")
	gr_sig1 = rt.gPad.GetPrimitive("Graph").Clone("gr_sig_mt1_mt2")
	gr_sig1.SetMarkerColor(rt.kRed)

	gr_bg1.Draw("P")
	gr_sig1.Draw("P same")

	#MW1 vs MW2
	c.cd(2)
	tree_bg.Draw("mw2:mw1")
	gr_bg2 = rt.gPad.GetPrimitive("Graph").Clone("gr_bg_mw1_mw2")
	gr_bg2.SetMarkerColor(rt.kBlue)

	tree_sig.Draw("mw2:mw1")
	gr_sig2 = rt.gPad.GetPrimitive("Graph").Clone("gr_sig_mw1_mw2")
	gr_sig2.SetMarkerColor(rt.kRed)

	gr_bg2.Draw("P")
	gr_sig2.Draw("P same")

	#MT1 vs MW1
	c.cd(3)
	tree_bg.Draw("mt1:mw1")
	gr_bg3 = rt.gPad.GetPrimitive("Graph").Clone("gr_bg_mt1_mw1")
	gr_bg3.SetMarkerColor(rt.kBlue)

	tree_sig.Draw("mt1:mw1")
	gr_sig3 = rt.gPad.GetPrimitive("Graph").Clone("gr_sig_mt1_mw1")
	gr_sig3.SetMarkerColor(rt.kRed)

	gr_bg3.Draw("P")
	gr_sig3.Draw("P same")

	#MT2 vs MW2
	c.cd(4)
	tree_bg.Draw("mt2:mw2")
	gr_bg4 = rt.gPad.GetPrimitive("Graph").Clone("gr_bg_mt2_mw2")
	gr_bg4.SetMarkerColor(rt.kBlue)

	tree_sig.Draw("mt2:mw2")
	gr_sig4 = rt.gPad.GetPrimitive("Graph").Clone("gr_sig_mt2_mw2")
	gr_sig4.SetMarkerColor(rt.kRed)

	gr_bg4.Draw("P")
	gr_sig4.Draw("P same")

	c.Print(arguments.outfile)

        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('-b', dest='batch', action='store_true', help="ROOT batch mode")
	parser.add_argument('-s', '--signal', help="signal root file")
	parser.add_argument('-g', '--background', help="background root file")
	parser.add_argument('-t', '--tree', help="tree name")
        parser.add_argument('-o', '--outfile', help="Output file")
        parser.add_argument('-j', '--config-json', type=json.loads, help="JSON configuration file")
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
