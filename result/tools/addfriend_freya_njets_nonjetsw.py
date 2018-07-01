#!/usr/bin/env python

"""
Add new branch to existing tree with new sci-kit discriminant.
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
import pickle as pl


import numpy as np
import pandas as pd
import sklearn
from root_numpy import root2array, tree2array, array2tree
from root_numpy.testdata import get_filepath
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_gaussian_quantiles
from sklearn.ensemble import RandomForestClassifier

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
	#branchlist=['multitopness', 'HTb', 'HTH', 'LeptonPt', 'NjetsW', 'SumJetMassX', 'HTX', 'csvJetcsv4', 'csvJetcsv4', '1stjetpt', '2ndjetpt', '5thjetpt', '6thjetpt', 'angletop1top2', 'angletoplep', 'csvJetpt3', 'csvJetpt4'] # njet split training

	#initialize mva reader
	#change this if you have a different package
	inputpicklejson=json.loads(arguments.config_json)
	estimator10 = pl.load(open(inputpicklejson['10j'],"rb"))
	estimator9  = pl.load(open(inputpicklejson['9j'] ,"rb"))
	estimator8  = pl.load(open(inputpicklejson['8j'] ,"rb"))
	estimator7  = pl.load(open(inputpicklejson['7j'] ,"rb"))

	#recompute mva discriminant for every event
	intree.SetBranchStatus("*",0);
	intree.SetBranchStatus("nJets",1);
	BDT_trijet2    = array('f',[0]) ; intree.SetBranchAddress("multitopness",BDT_trijet2);		intree.SetBranchStatus("multitopness",1);
	HTb            = array('f',[0]) ; intree.SetBranchAddress("HTb",HTb);				intree.SetBranchStatus("HTb",1);
	HTH	       = array('f',[0]) ; intree.SetBranchAddress("HTH",HTH);				intree.SetBranchStatus("HTH",1);
	leptonpt       = array('f',[0]) ; intree.SetBranchAddress("LeptonPt",leptonpt);			intree.SetBranchStatus("LeptonPt",1);
	njetW          = array('f',[0]) ; intree.SetBranchAddress("NjetsW",njetW);			intree.SetBranchStatus("NjetsW",1);
	SumJetMassX    = array('f',[0]) ; intree.SetBranchAddress("SumJetMassX",SumJetMassX);		intree.SetBranchStatus("SumJetMassX",1);
	HTX            = array('f',[0]) ; intree.SetBranchAddress("HTX",HTX);				intree.SetBranchStatus("HTX",1);
	csvJetcsv3     = array('f',[0]) ; intree.SetBranchAddress("csvJetcsv3",csvJetcsv3);		intree.SetBranchStatus("csvJetcsv3",1);
	csvJetcsv4     = array('f',[0]) ; intree.SetBranchAddress("csvJetcsv4",csvJetcsv4);		intree.SetBranchStatus("csvJetcsv4",1);
	firstjetpt     = array('f',[0]) ; intree.SetBranchAddress("1stjetpt",firstjetpt);		intree.SetBranchStatus("1stjetpt",1);
	secondjetpt    = array('f',[0]) ; intree.SetBranchAddress("2ndjetpt",secondjetpt);		intree.SetBranchStatus("2ndjetpt",1);
	fifthjetpt     = array('f',[0]) ; intree.SetBranchAddress("5thjetpt",fifthjetpt);		intree.SetBranchStatus("5thjetpt",1);
	sixjetpt       = array('f',[0]) ; intree.SetBranchAddress("6thjetpt",sixjetpt);			intree.SetBranchStatus("6thjetpt",1);
	angletop1top2  = array('f',[0]) ; intree.SetBranchAddress("angletop1top2",angletop1top2);	intree.SetBranchStatus("angletop1top2",1);
	angletoplep    = array('f',[0]) ; intree.SetBranchAddress("angletoplep",angletoplep);		intree.SetBranchStatus("angletoplep",1);
	csvJetpt3      = array('f',[0]) ; intree.SetBranchAddress("csvJetpt3",csvJetpt3);		intree.SetBranchStatus("csvJetpt3",1);
	csvJetpt4      = array('f',[0]) ; intree.SetBranchAddress("csvJetpt4",csvJetpt4);		intree.SetBranchStatus("csvJetpt4",1);
	i = 0
        total = intree.GetEntries()
        for ev in intree:
                #if ( i % 100 == 1): progress(i, total, 'Progress')
                i += 1

		branchlist=[[ ev.multitopness, ev.HTb, ev.HTH, ev.LeptonPt, ev.SumJetMassX, \
			      ev.HTX, ev.csvJetcsv3, ev.csvJetcsv4, getattr(ev, '1stjetpt'), \
			      getattr(ev, '2ndjetpt'), getattr(ev,'5thjetpt'), getattr(ev,'6thjetpt'), \
			      ev.angletop1top2, ev.angletoplep, ev.csvJetpt3, ev.csvJetpt4]] # njet split training
		X_in = np.array(branchlist)
		MVA_out = None
		try:
			if ev.nJets < 8 : MVA_out = estimator7.decision_function(X_in) 
			elif ev.nJets == 8: MVA_out = estimator8.decision_function(X_in)
			elif ev.nJets == 9: MVA_out = estimator9.decision_function(X_in)
			elif ev.nJets > 9: MVA_out = estimator10.decision_function(X_in)
		except ValueError:
			newmva[0] = -999.
			friendtree.Fill()
			continue
		newmva[0] = MVA_out[0]
		#print newmva[0]
		friendtree.Fill()

	#enable all branches in the input tree
	intree.SetBranchStatus("*",1)

	#create friend tree with the new mva discriminant calculated from input tree variables
	intree.AddFriend(friendtree)

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
        parser.add_argument('-w', '--weight-file-name', help="TMVA weights file (.xml). Not implemented.")
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
