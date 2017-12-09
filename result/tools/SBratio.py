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

import pandas as pd
import numpy as np
import math

import ROOT

from cards_proc_list import proc_id
from cards_syst_list import systtypelist
from cards_syst_list import syst_norm_size_list, syst_shape_size_list
from cards_bin_list import binlist

#Global definitions


def getObservation(ch,file,observable):
    '''
    Fill per-bin datacounts list
    '''
    logging.debug("----getObservation:-----")
    obs = {ch:{}}
    for ibin in binlist[ch]:
        histname = ibin.replace(ch,'')  #Remove channel prefix e.g. mu6J2M->6J2M
        histname = histname + '/' + observable
        logging.debug("Observations filename: "+file.GetName())
        logging.debug("Observations histname: "+histname)
        integral = file.Get(histname).Integral()
        logging.debug("Integral: "+str(integral))
        obs[ch][ibin]=integral
    return obs

def mcRate(ch,files,observable):
    '''
    Get MC predictions for each process
    '''
    logging.debug("----mcRate:-----")
    rate = {}
    logging.debug(files)
    for proc in proc_id.keys():
        rate[proc]=getObservation(ch,files[proc],observable)
    return rate


def main(arguments):

        #pandas printing setting
        pd.set_option('expand_frame_repr', False)
        pd.set_option('max_columns', 999)
        
        #Read-in input ROOT files
        files = {}
        for proc in arguments.sources.keys():
            files[proc] = ROOT.TFile.Open(arguments.sources[proc],"READ")
        
        #Get observations
        datafile = ROOT.TFile.Open(arguments.data,"READ")
        obs = getObservation(arguments.channel, datafile,arguments.observable)
        logging.debug( obs )
        #Printout observation block to file
        obsline = pd.DataFrame(obs[arguments.channel], columns=binlist[arguments.channel], index=['observation'])
        
        #Get MC rate predictions            
        rate = mcRate(arguments.channel,files,arguments.observable)
        logging.debug( rate )
        
	frames = []
	for proc in proc_id.keys():
		if 'NP_overlay_ttttNLO' in proc: continue
		rateline = pd.DataFrame(rate[proc][arguments.channel], columns=binlist[arguments.channel], index=[proc])
		frames.append(rateline)
	res = pd.concat(frames)

	outputbg = {"bg":res.sum().to_dict()}
	rateline = pd.DataFrame(rate['NP_overlay_ttttNLO'][arguments.channel],columns=binlist[arguments.channel], index=['NP_overlay_ttttNLO'])
	output = {"sg":rateline.sum().to_dict()}
	output.update(outputbg)
	caption = {"caption":arguments.caption}
	output.update(caption)
	print output
    	json.dump(output, arguments.outfile)
        

        return 0

if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('--data', help="Data rootfile", required=True)
        parser.add_argument("--source", type=json.loads, dest='sources',
                            help='json dictionary with input definition', required=True)
        parser.add_argument('--channel', help="channel",default='mu')
        parser.add_argument('--caption', help="result caption",default='')
        parser.add_argument('--observable', help="observable",default='allSF/bdt')
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
