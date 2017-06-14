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

import sklearn_to_tmva as convert

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
	#infile_root = r.TFile.Open(arguments.infile, 'UPDATE')
	infile_root = r.TFile.Open(arguments.infile, 'READ')
	intree      = infile_root.Get(arguments.source_tree_name)
	#branchlist=['nJets','multitopness', 'HTb','HTH','LeptonPt','NjetsW','SumJetMassX','HTX','csvJetcsv3','csvJetcsv4'] #
	branchlist=['multitopness', 'HTb', 'HTH', 'LeptonPt', 'NjetsW', 'SumJetMassX', 'HTX', 'csvJetcsv3', 'csvJetcsv4', '1stjetpt', '2ndjetpt', '5thjetpt', '6thjetpt', 'angletop1top2', 'angletoplep', 'csvJetpt3', 'csvJetpt4'] #BDTAdaBoost_250_2.p

	#initialize mva reader
	#change this if you have a different package
	inputpicklefile=arguments.weight_file_name
	estimator = pl.load(open(inputpicklefile,"rb"))

	#recompute mva discriminant for every event
	X_in = tree2array(intree,branches=branchlist)
	print X_in[0], X_in[1], X_in[2], X_in[3], X_in[4]
	MVA_out = estimator.decision_function(pd.DataFrame(X_in)) # obviously needs to have the same members in branchlist variable as what was trained with
	MVA_out.dtype = [('MVAoutput', np.float64)]
	print MVA_out[0], MVA_out[1], MVA_out[2], MVA_out[3], MVA_out[4]
	friendtree = array2tree(MVA_out, name=arguments.friend_tree_name)
	#create friend tree with the new mva discriminant calculated from input tree variables
	intree.AddFriend(friendtree)

	#overwrite trees to avoid clones with different cycle numbers
	#friendtree.Write("",r.TObject.kOverwrite)
	#intree.Write("",r.TObject.kOverwrite)
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
