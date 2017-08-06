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
        rt.TH1.__init__._creates = False
        rt.TH2.__init__._creates = False
        rt.TLegend.__init__._creates = False

	other_cuts = '((HLT_IsoMu24==1||HLT_IsoTkMu24==1) && nJets>6)'


	rt.gStyle.SetOptStat(0)
	rt.gStyle.SetOptTitle(0)

	conf = arguments.config_json
	file_data = rt.TFile.Open(conf['data'][0],"READ")
	tree_data = file_data.Get(arguments.tree)
	
	c = rt.TCanvas('c','c1',5,45,800,500);c.Divide(3,1)

	c.cd(1)
	hA = rt.TH2F("hA","A;lepton isolation;MET (GeV)",50,0.,5.0,100,0.,1000)
	hB = rt.TH2F("hB","B;lepton isolation;MET (GeV)",50,0.,5.0,100,0.,1000)
	hC = rt.TH2F("hC","C;lepton isolation;MET (GeV)",50,0.,5.0,100,0.,1000)
	hD = rt.TH2F("hD","D;lepton isolation;MET (GeV)",50,0.,5.0,100,0.,1000)
	tree_data.Draw("met:leptonIso>>hA","{}*(met>50 && leptonIso<0.15 && {})*ScaleFactor*SFtrig*GenWeight".format(conf['data'][1],other_cuts),""); 
	tree_data.Draw("met:leptonIso>>hB","{}*(met<50 && leptonIso<0.15 && {})*ScaleFactor*SFtrig*GenWeight".format(conf['data'][1],other_cuts),""); 
	tree_data.Draw("met:leptonIso>>hC","{}*(met>50 && leptonIso>0.15 && {})*ScaleFactor*SFtrig*GenWeight".format(conf['data'][1],other_cuts),""); 
	tree_data.Draw("met:leptonIso>>hD","{}*(met<50 && leptonIso>0.15 && {})*ScaleFactor*SFtrig*GenWeight".format(conf['data'][1],other_cuts),""); 
	hA.SetTitle("A {0:.1f}".format(hA.Integral()))
	hB.SetTitle("B {0:.1f}".format(hB.Integral()))
	hC.SetTitle("C {0:.1f}".format(hC.Integral()))
	hD.SetTitle("D {0:.1f}".format(hD.Integral()))
	DATA = {"A":hA.Integral(), "B":hB.Integral(), "C":hC.Integral(), "D":hD.Integral()}
	hA.SetFillColor(rt.kBlue+1)
	hB.SetFillColor(rt.kRed+2)
	hC.SetFillColor(rt.kGreen+1)
	hD.SetFillColor(rt.kMagenta-1)
	hA.Draw("box");
	hB.Draw("box same");
	hC.Draw("box same");
	hD.Draw("box same");
        #print 'Data integral {}'.format(sum([hA.Integral(),hB.Integral(),hC.Integral(),hD.Integral()]))
        #print 'Data integral {}'.format(sum([hA.Integral(),hC.Integral()]))

	hA.GetXaxis().SetRangeUser(0.,0.4)
	hA.GetYaxis().SetRangeUser(0.,200.)

	leg1 = rt.TLegend(0.1,0.1,0.89,0.49,'Data')
	leg1.AddEntry(hA); leg1.AddEntry(hB); leg1.AddEntry(hC); leg1.AddEntry(hD);
	leg1.SetNColumns(1); leg1.SetBorderSize(0)

	c.cd(2)
	hA_sum = rt.TH2F("hA_{}".format('sum'),"A;lepton isolation;MET (GeV)",50,0.,2.5,100,0.,1000)
	hB_sum = rt.TH2F("hB_{}".format('sum'),"B;lepton isolation;MET (GeV)",50,0.,2.5,100,0.,1000)
	hC_sum = rt.TH2F("hC_{}".format('sum'),"C;lepton isolation;MET (GeV)",50,0.,2.5,100,0.,1000)
	hD_sum = rt.TH2F("hD_{}".format('sum'),"D;lepton isolation;MET (GeV)",50,0.,2.5,100,0.,1000)
	hA_sum.SetFillColor(rt.kBlue+1)
	hB_sum.SetFillColor(rt.kRed+2)
	hC_sum.SetFillColor(rt.kGreen+1)
	hD_sum.SetFillColor(rt.kMagenta-1)
	for elem in conf['MC']:
		file_mc = rt.TFile.Open(conf['MC'][elem][0],"READ")
		tree_mc = file_mc.Get(arguments.tree)
		hA_mc = rt.TH2F("hA_{}".format(elem),"A;lepton isolation;MET (GeV)",50,0.,2.5,100,0.,1000)
		hB_mc = rt.TH2F("hB_{}".format(elem),"B;lepton isolation;MET (GeV)",50,0.,2.5,100,0.,1000)
		hC_mc = rt.TH2F("hC_{}".format(elem),"C;lepton isolation;MET (GeV)",50,0.,2.5,100,0.,1000)
		hD_mc = rt.TH2F("hD_{}".format(elem),"D;lepton isolation;MET (GeV)",50,0.,2.5,100,0.,1000)
		tree_mc.Draw("met:leptonIso>>hA_{}".format(elem),"{}*(met>50 && leptonIso<0.15 &&{})*ScaleFactor*SFtrig*GenWeight".format(conf['MC'][elem][1],other_cuts),""); 
		tree_mc.Draw("met:leptonIso>>hB_{}".format(elem),"{}*(met<50 && leptonIso<0.15 &&{})*ScaleFactor*SFtrig*GenWeight".format(conf['MC'][elem][1],other_cuts),""); 
		tree_mc.Draw("met:leptonIso>>hC_{}".format(elem),"{}*(met>50 && leptonIso>0.15 &&{})*ScaleFactor*SFtrig*GenWeight".format(conf['MC'][elem][1],other_cuts),""); 
		tree_mc.Draw("met:leptonIso>>hD_{}".format(elem),"{}*(met<50 && leptonIso>0.15 &&{})*ScaleFactor*SFtrig*GenWeight".format(conf['MC'][elem][1],other_cuts),""); 
		hA_sum.Add(hA_mc.Clone())
		hB_sum.Add(hB_mc.Clone())
		hC_sum.Add(hC_mc.Clone())
		hD_sum.Add(hD_mc.Clone())
		
	hA_sum.SetTitle("A {0:.1f}".format(hA_sum.Integral())); 
	hB_sum.SetTitle("B {0:.1f}".format(hB_sum.Integral())); 
	hC_sum.SetTitle("C {0:.1f}".format(hC_sum.Integral())); 
	hD_sum.SetTitle("D {0:.1f}".format(hD_sum.Integral())); 
	MC = {"A":hA_sum.Integral(), "B":hB_sum.Integral(), "C":hC_sum.Integral(), "D":hD_sum.Integral()}
	hA_sum.Draw("box");
	hB_sum.Draw("box same");
	hC_sum.Draw("box same");
	hD_sum.Draw("box same");
	hA_sum.GetXaxis().SetRangeUser(0.,0.4)
	hA_sum.GetYaxis().SetRangeUser(0.,200.)

	leg2 = rt.TLegend(0.1,0.5,0.89,0.89,'non QCD MC')
	leg2.AddEntry(hA_sum); leg2.AddEntry(hB_sum); leg2.AddEntry(hC_sum); leg2.AddEntry(hD_sum);
	leg2.SetNColumns(1); leg2.SetBorderSize(0)


	c.cd(3)
	leg1.Draw()
	leg2.Draw()

	#Transfer factor calculation
	print "{:<10}".format(""),'{0:>10}{1:>10}{2:>10}{3:>10}'.format('A','B','C','D')
	print "{:<10}".format("DATA"),"{0:10.1f}{1:10.1f}{2:10.1f}{3:10.1f}".format(DATA["A"], DATA["B"], DATA["C"], DATA["D"])
	print "{:<10}".format("non QCD MC"),"{0:10.1f}{1:10.1f}{2:10.1f}{3:10.1f}".format(MC["A"], MC["B"], MC["C"], MC["D"])
	print "After non-QCD subtraction"
	DATA_QCD = {}
	for key in DATA: DATA_QCD[key]=DATA[key]-MC[key]
	print "{:<10}".format("DATA"),"{0:10.1f}{1:10.1f}{2:10.1f}{3:10.1f}".format(DATA_QCD["A"], DATA_QCD["B"], DATA_QCD["C"], DATA_QCD["D"])
	
	
	c.Print(arguments.format)

        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('-o', '--outfile', help="Output file")
        parser.add_argument('-j', '--config-json', type=json.loads, help="JSON configuration file")
        parser.add_argument('-t', '--tree', help="Tree name")
        parser.add_argument('-f', '--format', help="ROOT canvas print format", default='.png')
        parser.add_argument('-b', help="ROOT batch mode", dest='isBatch', action='store_true')
        parser.add_argument('-i', help="ROOT interactive mode", dest='isInteractive', action='store_true')
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
