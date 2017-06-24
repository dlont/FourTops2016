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

	#global style settings
	rt.gStyle.SetOptStat(0)
	rt.gStyle.SetTitleOffset(1.2,'Y')
	rt.gStyle.SetTitleSize(0.04,'Y')
	rt.gStyle.SetTitleSize(0.04,'X')


	file_TT = rt.TFile.Open(arguments.infile,"READ")
	tree_TT = file_TT.Get(arguments.tree)

	# Fake rate
	c1 = rt.TCanvas('ttbb_fake','ttbb_fake',5,45,800,800); c1.Divide(2,2)
	
	#7j category
	c1.cd(1);	rt.gPad.SetLogy()
	tree_TT.Draw('nMtags>>h_njet7',"ttxType%100 == 0 && nJets == 7")
	h_njet7 = rt.gPad.GetPrimitive('h_njet7')
	h_njet7.SetTitle('n Reco Jets = 7, t#bar{t}jj at the particle level;Number of medium csvv2 tags;rel. contribution')
	h_njet7.Scale(1./h_njet7.Integral())
	h_njet7.SetMarkerSize(2.5)
	h_njet7.Draw('hist text0')
	c1.cd(2);	rt.gPad.SetLogy()
	tree_TT.Draw('nMtags>>h_njet8',"ttxType%100 == 0 && nJets == 8")
	h_njet8 = rt.gPad.GetPrimitive('h_njet8')
	h_njet8.SetTitle('n Reco Jets = 8, t#bar{t}jj at the particle level;Number of medium csvv2 tags;rel. contribution')
	h_njet8.Scale(1./h_njet8.Integral())
	h_njet8.SetMarkerSize(2.5)
	h_njet8.Draw('hist text0')
	c1.cd(3);	rt.gPad.SetLogy()
	tree_TT.Draw('nMtags>>h_njet9',"ttxType%100 == 0 && nJets == 9")
	h_njet9 = rt.gPad.GetPrimitive('h_njet9')
	h_njet9.SetTitle('n Reco Jets = 9, t#bar{t}jj at the particle level;Number of medium csvv2 tags;rel. contribution')
	h_njet9.Scale(1./h_njet9.Integral())
	h_njet9.SetMarkerSize(2.5)
	h_njet9.Draw('hist text0')
	c1.cd(4);	rt.gPad.SetLogy()
	tree_TT.Draw('nMtags>>h_njet10',"ttxType%100 == 0 && nJets >= 10")
	h_njet10 = rt.gPad.GetPrimitive('h_njet10')
	h_njet10.SetTitle('n Reco Jets #geq 10, t#bar{t}jj at the particle level;Number of medium csvv2 tags;rel. contribution')
	h_njet10.Scale(1./h_njet10.Integral())
	h_njet10.SetMarkerSize(2.5)
	h_njet10.Draw('hist text0')
	c1.Print(arguments.fmt)

	# Fake rate
	c2 = rt.TCanvas('ttbb_eff','ttbb_eff',5,45,800,800); c2.Divide(2,2)
	
	#7j category
	c2.cd(1);	rt.gPad.SetLogy()
	tree_TT.Draw('nMtags>>h_njet7',"(ttxType%100)%10 >= 2 && nJets == 7")
	h_njet7 = rt.gPad.GetPrimitive('h_njet7')
	h_njet7.SetTitle('n Reco Jets = 7, t#bar{t}c#bar{c}+b#bar{b} at the particle level;Number of medium csvv2 tags;rel. contribution')
	h_njet7.Scale(1./h_njet7.Integral())
	h_njet7.SetMarkerSize(2.5)
	h_njet7.Draw('hist text0')
	c2.cd(2);	rt.gPad.SetLogy()
	tree_TT.Draw('nMtags>>h_njet8',"(ttxType%100)%10 >= 2 && nJets == 8")
	h_njet8 = rt.gPad.GetPrimitive('h_njet8')
	h_njet8.SetTitle('n Reco Jets = 8, t#bar{t}c#bar{c}+b#bar{b} at the particle level;Number of medium csvv2 tags;rel. contribution')
	h_njet8.Scale(1./h_njet8.Integral())
	h_njet8.SetMarkerSize(2.5)
	h_njet8.Draw('hist text0')
	c2.cd(3);	rt.gPad.SetLogy()
	tree_TT.Draw('nMtags>>h_njet9',"(ttxType%100)%10 >= 2 && nJets == 9")
	h_njet9 = rt.gPad.GetPrimitive('h_njet9')
	h_njet9.SetTitle('n Reco Jets = 9, t#bar{t}c#bar{c}+b#bar{b} at the particle level;Number of medium csvv2 tags;rel. contribution')
	h_njet9.Scale(1./h_njet9.Integral())
	h_njet9.SetMarkerSize(2.5)
	h_njet9.Draw('hist text0')
	c2.cd(4);	rt.gPad.SetLogy()
	tree_TT.Draw('nMtags>>h_njet10',"(ttxType%100)%10 >= 2 && nJets >= 10")
	h_njet10 = rt.gPad.GetPrimitive('h_njet10')
	h_njet10.SetTitle('n Reco Jets #geq 10, t#bar{t}c#bar{c}+b#bar{b} at the particle level;Number of medium csvv2 tags;rel. contribution')
	h_njet10.Scale(1./h_njet10.Integral())
	h_njet10.SetMarkerSize(2.5)
	h_njet10.Draw('hist text0')
	c2.Print(arguments.fmt)

        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('infile', help='Input file')
	parser.add_argument('-b', dest='batch', action='store_true', help="ROOT batch mode")
	parser.add_argument('-t', '--tree', help="tree name")
        parser.add_argument('-f', '--format', dest='fmt', help="Output file")
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
