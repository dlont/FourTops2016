#!/usr/bin/env python

"""
Add new branch to existing tree with new TMVA discriminant.
"""

import os
import sys
import time
import argparse
import logging
import json
from pprint import pprint

import ROOT as r
from array import array

def progress(current, total, status=''):
	"""
	Progress bar
	"""
        fullBarLength = 80
        doneBarLength = int(round(fullBarLength * current / float(total)))

        percents = round(100.0 * current / float(total), 1)
        bar = '>' * doneBarLength + ' ' * (fullBarLength - doneBarLength)

        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()
	if current >= total-1: print "\n"

def main(arguments):
	"""
	New MVA discriminant is recomputed and added to the file here
	"""

	# read input file and tree
	infile_root = r.TFile.Open(arguments.infile, 'UPDATE')
	intree      = infile_root.Get(arguments.source_tree_name)

	#create friend tree with the new mva discriminant calculated from input tree variables
	friendtree  = r.TTree(arguments.friend_tree_name,"Friend of "+arguments.source_tree_name)
	newmva = array( 'f', [ 0 ] )
	friendtree.Branch(arguments.friend_tree_name, newmva, arguments.friend_tree_name+"/F")
	intree.AddFriend(friendtree)

	#initialize tmva reader
	#change this if you have a different package
	reader = r.TMVA.Reader()
	BDT_trijet2    = array('f',[0]) ; reader.AddVariable("BDT_trijet2",BDT_trijet2)
	leptonpt       = array('f',[0]) ; reader.AddVariable("leptonpt",leptonpt)
	HTRat          = array('f',[0]) ; reader.AddVariable("HTRat",HTRat)
	HTb            = array('f',[0]) ; reader.AddVariable("HTb",HTb)
	HTX            = array('f',[0]) ; reader.AddVariable("HTX",HTX)
	nJets          = array('f',[0]) ; reader.AddVariable("nJets",nJets)
	csvJet3        = array('f',[0]) ; reader.AddVariable("csvJet3",csvJet3)
	csvJet4        = array('f',[0]) ; reader.AddVariable("csvJet4",csvJet4)
	njetW          = array('f',[0]) ; reader.AddVariable("njetW",njetW)
	SumJetMassX    = array('f',[0]) ; reader.AddVariable("SumJetMassX",SumJetMassX)
	reader.BookMVA("BDT",arguments.weight_file_name)


	#recompute mva discriminant for every event
	#change this to create a different discriminant
	i = 0
        total = intree.GetEntries()
        for ev in intree:
                if ( i % 100 == 1): progress(i, total, 'Progress')
                i += 1

		BDT_trijet2[0] = ev.multitopness
		leptonpt[0] = ev.LeptonPt
		HTRat[0] = ev.HTRat
		HTb[0] = ev.HTb
		HTX[0] = ev.HTX
		nJets[0] = ev.nJets
		csvJet3[0] = ev.csvJetcsv3
		csvJet4[0] = ev.csvJetcsv4
		njetW[0] = ev.NjetsW
		SumJetMassX[0] = ev.SumJetMassX
        	logging.info( "{} {} {} {} {} {} {} {} {} {}".format(ev.multitopness, ev.LeptonPt, ev.HTRat, ev.HTb, 
								     ev.HTX, ev.nJets, ev.csvJetcsv3, ev.csvJetcsv4, ev.NjetsW, ev.SumJetMassX) )
		newmva[0] = reader.EvaluateMVA("BDT")	# Actual discriminant calculation is perfomed here
		friendtree.Fill()

	#overwrite trees to avoid clones with different cycle numbers
	friendtree.Write("",r.TObject.kOverwrite)
	intree.Write("",r.TObject.kOverwrite)
	infile_root.Close()
        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('infile', help="Input file")
        parser.add_argument('-o', '--outfile', help="Output file")
        parser.add_argument('-s', '--source-tree-name', help="Source tree name")
        parser.add_argument('-f', '--friend-tree-name', help="Friend tree and branch name")
        parser.add_argument('-w', '--weight-file-name', help="TMVA weights file (.xml)")
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
