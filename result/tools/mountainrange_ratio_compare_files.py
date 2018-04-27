#!/usr/bin/env python

"""
Script for mountain range plots with post-fit uncertainties from combine
"""

import re
import os
import sys
import time
import argparse
import logging
import json
import pprint

import ROOT as rt
import array

import tdrstyle
import CMS_lumi

colors = [        
        413,
        7,
        610,
        633,
]

def fillsingle(hist_master, rootfile, histograms):
	logging.debug( 'fillsingle()' )
	stitch_edge_bins = []
	previous_stitch_bin = 0
	hist = None
	for ihist,name in enumerate(histograms):
		hist = rootfile.Get(name.encode('ascii'))
		nbins = hist.GetNbinsX()
		logging.debug( '{} {} {}'.format(ihist,name,nbins) )
		stitch_edge_bins.append(previous_stitch_bin + nbins)
		for ibin in range(1,nbins+1):
			#print name, nbins, ihist, ibin, previous_stitch_bin+ibin
			hist_master.SetBinContent(previous_stitch_bin+ibin,hist.GetBinContent(ibin))
			hist_master.SetBinError(previous_stitch_bin+ibin,hist.GetBinError(ibin))
		previous_stitch_bin+=nbins
		
	hist_master.SetTitle('{};{};{}'.format(hist.GetTitle(),hist.GetXaxis().GetTitle(),hist.GetYaxis().GetTitle()))	
	#print stitch_edge_bins
	return stitch_edge_bins

def fillsingle_data(gr_master, rootfile, graphs, hist_template, blind=None):
	if hist_template is None:
		print "ERROR!!!"
		sys.exit(1)

	previous_stitch_bin = 0
	gr = None
	for igr,name in enumerate(graphs):
		gr = rootfile.Get(name.encode('ascii'))
		if gr.InheritsFrom('TH1'): 
			gr.SetBinErrorOption(rt.TH1.kPoisson)
			gr = rt.TGraphAsymmErrors(gr)
		nbins = gr.GetN()
		ylist = gr.GetY()
		yhi   = gr.GetEYhigh()
		ylo   = gr.GetEYlow()
		if blind is not None:
			for cat in str(blind).split(','):
				if cat in name.encode('ascii'):
					ylist = [0] * nbins
					yhi = [0] * nbins
					ylo = [0] * nbins
					break
		for ibin in range(1,nbins+1):
			#print nbins, igr, ibin, previous_stitch_bin+ibin
			bincenter = hist_template.GetBinCenter(igr*nbins+ibin)
			gr_master.SetPoint(previous_stitch_bin+ibin-1,bincenter,ylist[ibin-1])
			gr_master.SetPointError(previous_stitch_bin+ibin-1,0.,0.,ylo[ibin-1],yhi[ibin-1])
		previous_stitch_bin+=nbins
			
	gr_master.SetTitle('{};{};{}'.format(gr.GetTitle(),gr.GetXaxis().GetTitle(),gr.GetYaxis().GetTitle()))	
	return

def fillstack(stack, hist_template, rootfile, histograms):
	master_hists = []
	for isource in range(0,len(histograms[0])):
		name  = 'source'+str(isource)
		clone = hist_template.Clone(name)
		print "name:", name
		print "color ",isource, ":", colors[isource]
		clone.SetFillColor( colors[isource] )
		clone.SetLineColor( colors[isource] )
		clone.SetMarkerColor( colors[isource] )
		master_hists.append(clone)
		clone.Reset()
	print 'Length of master_hists: ', len(master_hists)
	print 'Length of muntaintrange sources: ', len(histograms)
	previous_stitch_bin = 0
	for ichannel,channel_hists in enumerate(histograms):
		nbins = 0
		for isource,name in enumerate(channel_hists):
			hist = rootfile.Get(name.encode('ascii'))
			logging.debug('processing stack hist: %s' % name)
			if not hist: 
				logging.warning('ACHTUNG!!! Histogram %s not found. Check input!!!' % name)
				continue
			nbins = hist.GetNbinsX()
			for ibin in range(1,nbins+1):
				logging.debug('processing stack hist: %s, source: %s' % (name, isource))
				master_hists[isource].SetBinContent(previous_stitch_bin+ibin,hist.GetBinContent(ibin))
				master_hists[isource].SetBinError(previous_stitch_bin+ibin,hist.GetBinError(ibin))
		previous_stitch_bin+=nbins
	for hist in master_hists:
		stack.Add(hist,'hist')
	return

def binmap(totalhist=None, sighist=None, datagr=None):
	nonemptybinid = set()

	global_nbins = totalhist.GetNbinsX()

	if totalhist is not None:
		nbins = global_nbins
		for ibin in range(1,nbins+1):
			if totalhist.GetBinContent(ibin) > 1.E-05: nonemptybinid.add(ibin)
			#else: totalhist.Print("all"); break
	if sighist is not None:
                nbins = global_nbins
                for ibin in range(1,nbins+1):
                        if sighist.GetBinContent(ibin) > 1.E-05: nonemptybinid.add(ibin)
			#else: sighist.Print("all"); break

	if datagr is not None:
                nbins = global_nbins
		ylist = datagr.GetY()
                for ibin in range(1,nbins+1):
                        if ylist[ibin-1] > 1.E-05: nonemptybinid.add(ibin)
			#else: datagr.Print("all"); break

	#create a map between old and new bin numbers
	print nonemptybinid
	nonemptybinid_list = list(nonemptybinid)
	nonemptybinid_list.sort()
	print nonemptybinid_list
	nonemptybin_map = dict()
 	for i in range(0,len(nonemptybinid_list)): nonemptybin_map[nonemptybinid_list[i]] = i+1

	return nonemptybin_map


def noemptybins(hist, nonemptybin_map):

	title = "%s;%s;%s" % (hist.GetTitle(),hist.GetXaxis().GetTitle(),hist.GetYaxis().GetTitle())
	new_hist = rt.TH1F(hist.GetName()+'_mountain', title, len(nonemptybin_map), -0.5, len(nonemptybin_map)-0.5)
	new_hist.SetFillColor(hist.GetFillColor())
	
	logging.debug("non empty bins")
	for ibin in range(1,hist.GetNbinsX()+1):
		if ibin in nonemptybin_map: 
			new_hist.SetBinContent(	nonemptybin_map[ibin], hist.GetBinContent(ibin) )
			new_hist.SetBinError(	nonemptybin_map[ibin], hist.GetBinError(ibin) )
	return new_hist

def noemptybins_data(gr, nonemptybin_map, hist_template):

	new_gr = rt.TGraphAsymmErrors(len(nonemptybin_map))
	new_gr.SetMarkerStyle(20)
	
	logging.debug("non empty bins")
	ylist = gr.GetY()
	yhi   = gr.GetEYhigh()
	ylo   = gr.GetEYlow()
	for ibin in range(1,gr.GetN()+1):
		if ibin in nonemptybin_map: 
			x = hist_template.GetBinCenter(nonemptybin_map[ibin])
			y = ylist[ibin-1]
			eyh = yhi[ibin-1]
			eyl = ylo[ibin-1]
			new_gr.SetPoint(nonemptybin_map[ibin]-1,x,y)	#change here to remove slope
			new_gr.SetPointError(nonemptybin_map[ibin]-1,0.,0.,eyl,eyh)

	return new_gr

def draw_legend(**kwargs):
	"""
	Add legend to the canvas
	"""

	logging.debug("draw_legend() arguments")
	logging.debug(pprint.pformat(kwargs))

	canvas = None
	legend = None
	if 'canvas' in kwargs: canvas = kwargs['canvas']
	if 'legend' in kwargs: 
		if 'coord' in kwargs['legend']:
			coords = kwargs['legend']['coord']
			logging.debug('legend coordinates: %s %s %s %s' % (coords[0],coords[1],coords[2],coords[3]))
			legend = rt.TLegend(coords[0],coords[1],coords[2],coords[3])
	else: legend = rt.TLegend(0.6,0.75,0.9,0.9)

	datagr = None
	if 'data' in kwargs: datagr = kwargs['data']
	
	if 'header' in kwargs['legend']:
		legend.SetHeader(kwargs['legend']['header'])

	if canvas is not None:
		legend.SetNColumns(3)
		legend.SetBorderSize(0)
		#legend.SetFillStyle(0)

		if datagr: legend.AddEntry(datagr,"Data",'pe')
		if 'hist_tt' in kwargs: 
			hist_tt = kwargs['hist_tt']
			legend.AddEntry(hist_tt,"t#bar{t}",'lf')
		if 'hist_st' in kwargs:
			hist_st = kwargs['hist_st']
                        legend.AddEntry(hist_st,"tX",'lf')
		if 'hist_ew' in kwargs:
			hist_ew = kwargs['hist_ew']
                        legend.AddEntry(hist_ew,"EW",'lf')	#for slepton
                        #legend.AddEntry(hist_ew,"DY",'lf')	#for dilepton
		if 'hist_rare' in kwargs:
			hist_rare = kwargs['hist_rare']
                        legend.AddEntry(hist_rare,"Rare",'lf')
		if 'hist_tttt' in kwargs:
			hist_tttt = kwargs['hist_tttt']
			legend.AddEntry(hist_tttt,"t#bar{t}t#bar{t}",'lf')
		if 'hist_pre' in kwargs:
			hist_pre = kwargs['hist_pre']
			legend.AddEntry(hist_pre,"Prefit unc.","fe")
		if 'hist_post' in kwargs:
			hist_post = kwargs['hist_post']
			legend.AddEntry(hist_post,"Postfit unc.","fe")
		canvas.cd(3)
		legend.Draw()

def draw_bin_labels(c,masterhist,labels,ycoord,edges=None):
	'''
	Add labels below the X axis
	'''
	tex = rt.TLatex()
	tex.SetTextSize(0.025)
	tex.SetTextAlign(31)
	c.cd()

	if isinstance(labels,dict):
		for entry in labels:
			x = masterhist.GetBinCenter(int(entry))
			print labels[entry], x
			xmax = masterhist.GetXaxis().GetXmax()
			xmin = masterhist.GetXaxis().GetXmin()
			xndc=(x - xmin)/(xmax - xmin)
			tex.DrawLatexNDC(xndc,ycoord,labels[entry])
	if isinstance(labels,list):
		for entry,label in enumerate(labels):
			x = masterhist.GetBinCenter(edges[entry])
			print labels[entry], x
			xmax = masterhist.GetXaxis().GetXmax()
			xmin = masterhist.GetXaxis().GetXmin()
			xndc=(x - xmin)/(xmax - xmin)
			tex.DrawLatexNDC(xndc,ycoord,label)

def draw_subhist_separators(c,stitch_edge_bins,binmapping,labels,ycoord,hist_template):

	mappedbins = binmapping.keys()
	mappedbins.sort()
	mapped_edge_bins = []
	for edge in stitch_edge_bins:
		mappededge = -1
		for mb in mappedbins:
			if mb <= edge: mappededge = mb
			else:
				mapped_edge_bins.append(mappededge)
				break
	separator_bins = [binmapping[x] for x in mapped_edge_bins]

	logging.debug( "Stitching bins:" )
	logging.debug(pprint.pformat( stitch_edge_bins ) )
	print pprint.pformat( stitch_edge_bins )
	logging.debug( "Separator bins:" )
	logging.debug(pprint.pformat( separator_bins ) )

	c.cd()
	
	for item, isep in enumerate(separator_bins):
		x = hist_template.GetBinLowEdge(isep)+hist_template.GetBinWidth(isep)
		ymin = hist_template.GetYaxis().GetXmin()
		ymax = hist_template.GetMaximum()
		#print x, hist_template.GetMaximum()
		l = rt.TLine(x,ymin,x,ymax); l.SetLineColor(rt.kBlack); l.SetLineWidth(2)
		l.Draw()
	
		if isinstance(labels,list):
			tex = rt.TLatex()
			tex.SetTextSize(0.030)
			tex.SetTextAlign(32)
			tex.SetTextAngle(45)
			cxmin=c.GetLeftMargin()
			cxmax=1.-c.GetRightMargin()
			cymin=c.GetXlowNDC()
			xmax = hist_template.GetXaxis().GetXmax()
			xmin = hist_template.GetXaxis().GetXmin()
			xndc= cxmin + (x - xmin)/(xmax - xmin) * (cxmax - cxmin)
			#xndc= c.GetLeftMargin()
			print isep,xndc,ycoord,labels[item]
			tex.DrawLatexNDC(xndc,ycoord,labels[item])
			if (item == len(separator_bins)-1): tex.DrawLatexNDC(cxmax,ycoord,labels[item+1])
	
def draw_chi2_ndf(c,chi2,ndf):
	c.cd()
	text = '#chi^{{2}}/NDF = {0:.2f}/{1:d}, p-val={2:.2f}'.format(chi2,int(ndf),rt.TMath.Prob(chi2, int(ndf)))
	tex = rt.TLatex()
	tex.SetTextAngle(90)
	tex.DrawLatexNDC(0.99,0.2,text)
	
def transformh(h,xmin):
	hnew = rt.TH1D(h.GetName()+'_new',h.GetTitle(),h.GetNbinsX(),xmin,xmin+h.GetXaxis().GetXmax())
	return hnew

def main(arguments):

	colors = [rt.kRed+1,rt.kBlue+1,rt.kGreen+1,rt.kMagenta+1]

	#Apply TDR style
	tdrstyle.setTDRStyle()

	#Manipulate python garbage collection
	rt.TLegend.__init__._creates = False
	rt.TLine.__init__._creates = False
	rt.TH1.__init__._creates = False
	
	#Modify hatch bands
	#rt.gStyle.SetHatchesLineWidth(2)

	hatchStyle = 3013
	hatchColor = rt.kBlack

	inputrootfiles = [rt.TFile.Open(f, 'READ') for f in arguments.infile] 
	referencefile  = rt.TFile.Open(arguments.ratio_reference, 'READ')
	print inputrootfiles, referencefile
	jsondic = None
	with open(arguments.config_json) as json_data:
		jsondic = json.load(json_data)
		logging.debug(pprint.pformat(jsondic))

	#nbins
	nbins=0; rangex=0.;
        for hname in jsondic['prefitbg']:
		h = referencefile.Get(hname.encode('ascii','ignore'))
		nbins += h.GetNbinsX()
		rangex+= h.GetXaxis().GetXmax()
	print nbins, rangex

	longhist_rat = None
	if arguments.ratio_reference is not None:
		#ratio
		longhist = rt.TH1D("reference_"+referencefile.GetName(),"",nbins,0.,rangex)
		xmin = 0
		for hname in jsondic['reference']:
			h = referencefile.Get(hname.encode('ascii','ignore'))
			for ibin in range(1,h.GetNbinsX()+1):
				longhist.SetBinContent(xmin+ibin,h.GetBinContent(ibin))
			xmin += h.GetNbinsX()
		longhist_rat = longhist

	#prefit
	longhistfromfiles_pre = []
	for item,f in enumerate(inputrootfiles):
		longhist = rt.TH1D("prefit_"+f.GetName(),"",nbins,0.,rangex)
		longhist.SetLineColor(colors[item])
		longhist.SetLineWidth(1)
		xmin = 0
		for hname in jsondic['prefitbg']:
			h = f.Get(hname.encode('ascii','ignore'))
			for ibin in range(1,h.GetNbinsX()+1):
				longhist.SetBinContent(xmin+ibin,h.GetBinContent(ibin))
			xmin += h.GetNbinsX()
			
		longhistfromfiles_pre.append(longhist)
	#postfit
	longhistfromfiles_post = []
	for item,f in enumerate(inputrootfiles):
		longhist = rt.TH1D("postfit_"+f.GetName(),"",nbins,0.,rangex)
		longhist.SetLineColor(colors[item])
		longhist.SetLineStyle(2)
		longhist.SetLineWidth(1)
		xmin = 0
		if 'postfitbg' in jsondic:
			for hname in jsondic['postfitbg']:
				h = f.Get(hname)
				for ibin in range(1,h.GetNbinsX()+1):
					longhist.SetBinContent(xmin+ibin,h.GetBinContent(ibin))
				xmin += h.GetNbinsX()
			
		longhistfromfiles_post.append(longhist)

	c = rt.TCanvas()

	if arguments.ratio_reference is not None:
		c.Divide(1,2)
	
	c.cd(1)
	longhist_rat.Draw()
	print longhistfromfiles_pre, longhistfromfiles_post
	for h in longhistfromfiles_pre:
		h.Draw("same")
	for h in longhistfromfiles_post:
		h.Draw("same")

	leg = rt.TLegend(0.6,0.6,0.89,0.89)
	leg.SetBorderSize(0)
	for h in longhistfromfiles_pre: leg.AddEntry(h,h.GetName(),'l')
	for h in longhistfromfiles_post: leg.AddEntry(h,h.GetName(),'l')
	leg.Draw()

	longhistfromfiles_pre_rat = []
	longhistfromfiles_post_rat = []
	if arguments.ratio_reference is not None:
		c.cd(2)
		unitline = longhist_rat.Clone("uniline")
		unitline.Divide(longhist_rat)
		unitline.Draw()
		unitline.GetYaxis().SetTitle("Ratio wrt top pT prefit")
		unitline.GetYaxis().CenterTitle()
		unitline.GetYaxis().SetRangeUser(0.5,1.5)
		#longhist_rat.Divide(longhist_rat)
		#longhist_rat.Draw()
		for h in longhistfromfiles_pre:
			c.cd(2)
			hrat = h.Clone("rat_"+h.GetName())
			hrat.Divide(longhist_rat)
       			hrat.Draw("same")
			longhistfromfiles_pre_rat.append(hrat)
        	for h in longhistfromfiles_post:
			c.cd(2)
			hrat = h.Clone("rat_"+h.GetName())
			hrat.Divide(longhist_rat)
                	hrat.Draw("same")
			longhistfromfiles_post_rat.append(hrat)



	if 'filename' in jsondic: c.Print(arguments.dir+'/'+jsondic['filename']+'_lin.'+arguments.extension)
	c.cd(1); rt.gPad.SetLogy(); CMS_lumi.CMS_lumi(c.cd(1),4,0)
	if 'filename' in jsondic: c.Print(arguments.dir+'/'+jsondic['filename']+'_log.'+arguments.extension)


        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('infile', nargs='+', help="Input file")
        parser.add_argument('-o', '--outfile', help="Output file")
        parser.add_argument('-r', '--ratio-reference', help="FILE for the denominator in the ratio plot")
        parser.add_argument('-j', '--config-json', help="JSON configuration file")
        parser.add_argument('-e', '--extension', help="Plot file extension (.C, .root, .png, .pdf)", default='png')
        parser.add_argument('--dir', help="Plots output directory", default='./')
        parser.add_argument('-b', help="ROOT batch mode", dest='isBatch', action='store_true')

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
