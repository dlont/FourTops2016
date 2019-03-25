#!/usr/bin/env python

"""A simple python script template.
"""

import os
import sys
import time
import argparse
import logging

import ROOT

from histtransformer import histProcessor
import scaleunc

rec_counter = 1

def addsysunc(target,nominal,scaleup,scaledown):
	global rec_counter
	#gain time, do not add the objects in the list in memory
	status = ROOT.TH1.AddDirectoryStatus();
	ROOT.TH1.AddDirectory(ROOT.kFALSE);

	ROOT.gDirectory.Print()
	full_path = target.GetPath()
	path = str(target.GetPath()).split(':/',1)[1]

	nominal.cd(path)

	ROOT.gDirectory.Print()
	# loop over all keys in this directory
	for key in ROOT.gDirectory.GetListOfKeys():
		obj = key.ReadObj()
		if (obj.IsA().InheritsFrom( ROOT.TH1.Class() )):
	 		nominal.cd( path )
	 		keynom = ROOT.gDirectory.GetListOfKeys().FindObject(obj.GetName())
			hnom = keynom.ReadObj()

			# renorm/fact scale variation envelope
			

			scaleup.cd( path )
	 		key1 = ROOT.gDirectory.GetListOfKeys().FindObject(obj.GetName())
         		h1 = key1.ReadObj()
	 		scaledown.cd( path )
	 		key2 = ROOT.gDirectory.GetListOfKeys().FindObject(obj.GetName())
			h2 = key2.ReadObj()
            		if (key1 and key2):
				for ibin in range(1,obj.GetNbinsX()+1):
					obj.SetBinError(ibin,rec_counter*100.*obj.GetBinError(ibin))
	       			h1.Print()
	       			h2.Print()
               			del h1
               			del h2
          
		elif ( obj.IsA().InheritsFrom( ROOT.TDirectory.Class() ) ):
			print "Found subdirectory ", obj.GetName() 
			scaledown.cd(obj.GetName())
			scaleup.cd(obj.GetName())
			nominal.cd(obj.GetName())
			target.cd()
			target.mkdir(obj.GetName())
		        target.cd(obj.GetName())
			newdir = ROOT.gDirectory
			rec_counter+=1
         		addsysunc( newdir, nominal, scaleup, scaledown )

      		else:
	        	print "Unknown object type, name: ", obj.GetName(), " title: ", obj.GetTitle()

		if ( obj.IsA().InheritsFrom( ROOT.TH1.Class() ) ):
			target.cd(full_path)
			obj.Write( key.GetName() )

	#save modifications to target file
	target.SaveSelf(ROOT.kTRUE);
	ROOT.TH1.AddDirectory(status);

def main(arguments):

    	print(args)

	file_target = ROOT.TFile.Open(args.outfile[0],'RECREATE')
	file_nominal = ROOT.TFile.Open(args.nominal[0],'READ')
	#file_isrscaleup = ROOT.TFile.Open(args.isrscaleup[0],'READ')
	#file_isrscaledown = ROOT.TFile.Open(args.isrscaledown[0],'READ')
	#addsysunc(file_target,file_nominal,file_isrscaleup,file_isrscaledown)

	scaleProc = scaleunc.scaleUncProcessor(file_nominal)
	trafo = histProcessor(target=file_target, proc=scaleProc)
	trafo.process()

	return 0

if __name__ == '__main__':
        start_time = time.time()

    	parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    	parser.add_argument('--uecaleup', help="UE Scale up histogram file", nargs=1)
    	parser.add_argument('--uescaledown', help="UE Scale down histogram file", nargs=1)
    	parser.add_argument('--fsrscaleup', help="FS Scale up histogram file", nargs=1)
    	parser.add_argument('--fsrscaledown', help="FS Scale down histogram file", nargs=1)
    	parser.add_argument('--isrscaleup', help="IS Scale up histogram file", nargs=1)
    	parser.add_argument('--isrscaledown', help="IS Scale down histogram file", nargs=1)
    	parser.add_argument('--nominal', help="Nominal histogram file", nargs=1)
    	parser.add_argument('-o', '--outfile', help="Output file",nargs=1)
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

	logging.basicConfig(level=args.loglevel)

        logging.info( time.asctime() )
	exitcode = main(args)
        logging.info( time.asctime() )
        logging.info( 'TOTAL TIME IN MINUTES:' + str((time.time() - start_time) / 60.0))
    	sys.exit(exitcode)
