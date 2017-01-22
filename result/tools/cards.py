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

import ROOT

from cards_proc_list import proc_id
from cards_syst_list import systtypelist
from cards_syst_list import syst_norm_size_list, syst_shape_size_list
from cards_bin_list import binlist

#Global definitions


def getObservation(ch,datafile,observable):
    '''
    Fill per-bin datacounts list
    '''
    obs = {ch:{}}
    for ibin in binlist[ch]:
        histname = ibin.replace(ch,'')
        histname = histname + '/' + observable
        integral = datafile.Get(histname).Integral()
        obs[ch][ibin]=integral
    return obs

def mcRate(ch,files,observable):
    '''
    Get MC predictions for each process
    '''
    
    rate = {}
    for proc in proc_id.keys():
        rate[proc]=getObservation(ch,files[proc],observable)
    return rate

def printCardHeader(arguments):
    print >> arguments.outfile, '#',str(datetime.now()), arguments
    print >> arguments.outfile, '-'*100
    print >> arguments.outfile, 'imax', 1
    print >> arguments.outfile, 'jmax', len(proc_id)-1
    print >> arguments.outfile, 'kmax', '*'
    print >> arguments.outfile, '-'*100
    
def printShapeFilesBlock(arguments):
    print >> arguments.outfile, '-'*100
    for ibin in binlist[arguments.channel]:
        for proc in proc_id.keys():
            filename = arguments.sources[proc]
            logging.debug(filename)
            print >> arguments.outfile, 'shapes', proc, ibin, \
                     filename, arguments.observable,  '$SYSTEMATIC/'+arguments.observable
        print >> arguments.outfile, 'shapes', 'data_obs', ibin, arguments.data, arguments.observable
    print >> arguments.outfile, '-'*100
    return

def main(arguments):

        #pandas printing setting
        pd.set_option('expand_frame_repr', False)
        pd.set_option('max_columns', 999)
        
        #Read-in input ROOT files
        files = {}
        for proc in arguments.sources.keys():
            files[proc] = ROOT.TFile.Open(arguments.sources[proc],"READ")
        
        printCardHeader(arguments)
        printShapeFilesBlock(arguments)
        #Get observations
        datafile = ROOT.TFile.Open(arguments.data,"READ")
        obs = getObservation(arguments.channel, datafile,arguments.observable)
        logging.debug( obs )
        #Printout observation block to file
        obsline = pd.DataFrame(obs[arguments.channel], columns=binlist[arguments.channel], index=['bin'])
        print >> arguments.outfile, '-'*100
        print >> arguments.outfile, obsline
        print >> arguments.outfile, '-'*100
        
        
        #Get MC rate predictions            
        rate = mcRate(arguments.channel,files,arguments.observable)
        logging.debug( rate )
        
        ch_dfs = []
        for proc in proc_id.keys():
            #Create new table for given process
            s = pd.DataFrame('NA', 
                             columns=binlist[arguments.channel], 
                             index=systtypelist[arguments.channel].keys()
                            )
            #Fill systematics desctiption for this process
            #Normalization
            df_update = pd.DataFrame.from_dict(syst_norm_size_list[arguments.channel][proc], orient='index')
            df_update.columns = binlist[arguments.channel]
            s.update(df_update)
            #Shape
            df_update = pd.DataFrame.from_dict(syst_shape_size_list[arguments.channel][proc], orient='index')
            df_update.columns = binlist[arguments.channel]
            s.update(df_update)
            #Add process labels and id (first and second line, respectively)
            processline = pd.DataFrame(proc, columns=binlist[arguments.channel], index=['process'])
            s = pd.concat([s.ix[:0], processline, s.ix[1:]])
            processline = pd.DataFrame(proc_id[proc], columns=binlist[arguments.channel], index=['process '])
            s = pd.concat([s.ix[:1], processline, s.ix[2:]])
            rateline = pd.DataFrame(rate[proc][arguments.channel], columns=binlist[arguments.channel], index=['rate'])
            s = pd.concat([s.ix[:2], rateline, s.ix[3:]])
            
            print arguments.channel, proc
            logging.debug(s)
            ch_dfs.append(s)
        result = pd.concat(ch_dfs,axis=1)
        
        #Add column with systematic type (normalization or shape)
        lam = lambda x: systtypelist[arguments.channel][x] if x in systtypelist[arguments.channel] else ''
        result.insert(0,' ',result.index.map(lam))
        #Printout MC (rate and systematics) block to file
        print >> arguments.outfile, result

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
        parser.add_argument('--observable', help="observable",default='bdt')
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
