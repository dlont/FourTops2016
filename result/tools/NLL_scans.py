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
        rt.TLegend.__init__._creates = False
        rt.TLatex.__init__._creates = False
        rt.TText.__init__._creates = False
        rt.TLegendEntry.__init__._creates = False
        rt.TH1.__init__._creates = False


	conf = arguments.config_json

	sl_fit   =conf['sl_fit']; print sl_fit
	dl_fit   =conf['dl_fit']
	combo_fit=conf['combo_fit']

	file_sl    = rt.TFile.Open(conf['sl'],'READ')
	tree_sl    = file_sl.Get('limit')
	file_dl    = rt.TFile.Open(conf['dl'],'READ')
	tree_dl    = file_dl.Get('limit')
	file_combo = rt.TFile.Open(conf['combo'],'READ')
	tree_combo = file_combo.Get('limit')

	c = rt.TCanvas('NLL_scan','CMS',5,45,600,600)

	tree_sl.Draw('deltaNLL:r','','LP')
	gr_sl = c.FindObject("Graph").Clone("gr_sl"); gr_sl.RemovePoint(0)
	tree_sl.Draw('r:deltaNLL','r>1','LP')
	spline_pos_gr_sl = c.FindObject("Graph").Clone("spline_pos_gr_sl"); spline_pos_gr_sl.RemovePoint(0)
	tree_sl.Draw('r:deltaNLL','r<1','LP')
	spline_neg_gr_sl = c.FindObject("Graph").Clone("spline_neg_gr_sl"); spline_neg_gr_sl.RemovePoint(0)
	x_pos_sl = spline_pos_gr_sl.Eval(0.5); x_pos_sl = abs(x_pos_sl - 1.); 
	x_neg_sl = spline_neg_gr_sl.Eval(0.5); x_neg_sl = abs(1. - x_neg_sl);
	print x_pos_sl, x_neg_sl
	gr_sl.SetLineWidth(2); gr_sl.SetLineColor(rt.kBlue+2); 
	gr_sl.SetTitle("l+jets, r={0}^{{+{1}}}_{{-{2}}}".format(1.,round(x_pos_sl,2), round(x_neg_sl,2) if x_neg_sl<1. else 1.))

	tree_dl.Draw('deltaNLL:r','','LP')
	gr_dl = c.FindObject("Graph").Clone("gr_dl"); gr_dl.RemovePoint(0)
	tree_dl.Draw('r:deltaNLL','r>1','LP')
	spline_pos_gr_dl = c.FindObject("Graph").Clone("spline_pos_gr_dl"); spline_pos_gr_dl.RemovePoint(0)
	tree_dl.Draw('r:deltaNLL','r<1','LP')
	spline_neg_gr_dl = c.FindObject("Graph").Clone("spline_neg_gr_dl"); spline_neg_gr_dl.RemovePoint(0)
	x_pos_dl = spline_pos_gr_dl.Eval(0.5); x_pos_dl = abs(x_pos_dl - 1.); 
	x_neg_dl = spline_neg_gr_dl.Eval(0.5); x_neg_dl = abs(1. - x_neg_dl);
	print x_pos_dl, x_neg_dl
	gr_dl.SetLineWidth(2); gr_dl.SetLineColor(rt.kGreen+2); 
	gr_dl.SetTitle("OS ll+jets, r={0}^{{+{1}}}_{{-{2}}}".format(1.,round(x_pos_dl,2), round(x_neg_dl,2) if x_neg_dl <1. else 1.))

	tree_combo.Draw('deltaNLL:r','','LP')
	gr_combo = c.FindObject("Graph").Clone("gr_combo"); gr_combo.RemovePoint(0)
	tree_combo.Draw('r:deltaNLL','r>1','LP')
	spline_pos_gr_combo = c.FindObject("Graph").Clone("spline_pos_gr_combo"); 
	tree_combo.Draw('r:deltaNLL','r<1','LP')
	spline_neg_gr_combo = c.FindObject("Graph").Clone("spline_neg_gr_combo"); 
	x_pos_combo = spline_pos_gr_combo.Eval(0.5); x_pos_combo = abs(x_pos_combo - 1.); 
	x_neg_combo = spline_neg_gr_combo.Eval(0.5); x_neg_combo = abs(1. - x_neg_combo);
	print x_pos_combo, x_neg_combo
	gr_combo.SetLineWidth(2); gr_combo.SetLineColor(rt.kRed+2); 
	gr_combo.SetTitle("Combined, r={0}^{{+{1}}}_{{-{2}}}".format(1.,round(x_pos_combo,2), round(x_neg_combo,2) if x_neg_combo<1. else 1.))

	mg = rt.TMultiGraph()
	mg.SetTitle(";#mu;#Delta NLL(#mu)")
	mg.Add(gr_sl)
	mg.Add(gr_dl)
	mg.Add(gr_combo)
	mg.Draw("A")
	mg.GetXaxis().SetRangeUser(0.,3.)
	mg.GetYaxis().SetTitleOffset(1.2)

	leg = c.BuildLegend(0.2,0.6,0.5,0.89)
	leg.SetHeader("Expected sensitivity")
	leg.SetBorderSize(0); 
	leg.SetFillStyle(0)
	#leg.SetEntrySeparation(2)

	line = rt.TLine(0.,0.5,3.,0.5); line.SetLineStyle(2); line.SetLineWidth(2)
	line.Draw()
	tex = rt.TLatex()
	tex.DrawLatex(0.3,0.45,'68% CL')

	c.Print(arguments.format)

        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        #parser.add_argument('-o', '--outfile', help="Output file")
        parser.add_argument('-f', '--format', default='.png', help="Output file format (.root, .png, .pdf)")
        parser.add_argument('-j', '--config-json', type=json.loads, help="JSON configuration file")
        parser.add_argument('-b', dest='is_root_batch', action='store_true', default=False, help="ROOT batch mode")
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
