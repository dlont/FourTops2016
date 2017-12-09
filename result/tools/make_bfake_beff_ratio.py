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
from pprint import pprint
from prettytable import  PrettyTable
from prettytable import MSWORD_FRIENDLY
import pandas as pd
import ROOT as rt

def progress(current, total, status=''):
        fullBarLength = 80
        doneBarLength = int(round(fullBarLength * current / float(total)))

        percents = round(100.0 * current / float(total), 1)
        bar = '>' * doneBarLength + ' ' * (fullBarLength - doneBarLength)

        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()

def main(arguments):
        total = 1000
        i = 0
	rt.gStyle.SetOptStat(0)

	f = rt.TFile.Open(arguments.infile,"READ")

	h_fakeb_jetmult = f.Get("h_fakeb_jetmult"); h_fakeb_jetmult.Sumw2()
	h_effb_jetmult = f.Get("h_effb_jetmult"); h_effb_jetmult.Sumw2()
	h_totb_jetmult = f.Get("h_totb_jetmult"); h_totb_jetmult.Sumw2()

	h_fakeb_jetmult.Divide(h_fakeb_jetmult,h_totb_jetmult,1.,1.,"B")
	h_fakeb_jetmult.SetTitle("(N non-b jets that pass b tag)/(N jets that pass b tag)")
	h_effb_jetmult.Divide(h_effb_jetmult,h_totb_jetmult,1.,1.,"B")
	h_effb_jetmult.SetTitle("(N non-b jets that pass b tag)/(N jets that pass b tag)")

	c = rt.TCanvas("b_ratio_mult")
	c.Divide(2,1)
	c.cd(1)
	h_fakeb_jetmult.Draw("hist E")
	c.cd(2)
	h_effb_jetmult.Draw("hist E")

	c.Print(".png")


#h_fakeb_jetmult_pt = f.Get("h_fakeb_jetmult_pt"); h_fakeb_jetmult_pt.Sumw2()
#h_effb_jetmult_pt = f.Get("h_effb_jetmult_pt"); h_effb_jetmult_pt.Sumw2()
#h_totb_jetmult_pt = f.Get("h_totb_jetmult_pt"); h_totb_jetmult_pt.Sumw2()
#
#h_fakeb_jetmult_pt.Divide(h_fakeb_jetmult_pt,h_totb_jetmult_pt,1.,1.,"B")
#h_effb_jetmult_pt.Divide(h_effb_jetmult_pt,h_totb_jetmult_pt,1.,1.,"B")
#
#c1 = rt.TCanvas("b_ratio_mult_pt")
#c1.Divide(2,1)
#c1.cd(1)
#h_fakeb_jetmult_pt.Draw("colz text")
#c1.cd(2)
#h_effb_jetmult_pt.Draw("colz text")
#
#c1.Print(".png")
#
#
#h_fakeb_eta_pt = f.Get("h_fakeb_eta_pt"); h_fakeb_eta_pt.Sumw2()
#h_effb_eta_pt = f.Get("h_effb_eta_pt"); h_effb_eta_pt.Sumw2()
#h_totb_eta_pt = f.Get("h_totb_eta_pt"); h_totb_eta_pt.Sumw2()
#
#h_fakeb_eta_pt.Divide(h_fakeb_eta_pt,h_totb_eta_pt,1.,1.,"B")
#h_effb_eta_pt.Divide(h_effb_eta_pt,h_totb_eta_pt,1.,1.,"B")
#
#c2 = rt.TCanvas("b_ratio_eta_pt")
#c2.Divide(2,1)
#c2.cd(1)
#h_fakeb_eta_pt.Draw("colz text")
#c2.cd(2)
#h_effb_eta_pt.Draw("colz text")
#
#c2.Print(".png")

        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('infile', help="Input file")
        #parser.add_argument('-o', '--outfile', help="Output file")
        #parser.add_argument('-j', '--config-json', type=json.loads, help="JSON configuration file")
        parser.add_argument('-b', help="ROOT batch mode", dest='isBatch', action='store_true')
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

