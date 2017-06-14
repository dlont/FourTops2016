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
from root_numpy import root2array, tree2array, array2tree, rec2array
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
	infile_root = r.TFile.Open(arguments.infile, 'UPDATE')
	intree      = infile_root.Get(arguments.source_tree_name)
	#branchlist=['nJets','multitopness', 'HTb','HTH','LeptonPt','NjetsW','SumJetMassX','HTX','csvJetcsv3','csvJetcsv4'] #
	branchlist=['multitopness', 'HTb', 'HTH', 'LeptonPt', 'NjetsW', 'SumJetMassX', 'HTX', 'csvJetcsv3', 'csvJetcsv4', '1stjetpt', '2ndjetpt', '5thjetpt', '6thjetpt', 'angletop1top2', 'angletoplep', 'csvJetpt3', 'csvJetpt4'] #BDTAdaBoost_250_2.p

	#initialize mva reader
	#change this if you have a different package
	inputpicklefile=arguments.weight_file_name
	estimator = pl.load(open(inputpicklefile,"rb"))
	print dir(estimator)

	#Load tree
	X_in = tree2array(intree,branches=branchlist)
	X_in = rec2array(X_in)

	#convert pickle to tmva xml
	convert.gbr_to_tmva(estimator, X_in, "tmva_out.xml", mva_name = "BDTG", coef = 10, var_names = branchlist)

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
