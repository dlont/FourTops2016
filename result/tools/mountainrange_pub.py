#!/usr/bin/env python

"""
Script for mountain range plots with post-fit uncertainties from combine
"""

import gc
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
		if isinstance(gr, rt.TH1): 
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
		#legend.SetHeader(kwargs['legend']['header'])
		header = rt.TLatex()
		header.DrawLatexNDC(0.2,0.85,kwargs['legend']['header'])

	if canvas is not None:
		legend.SetNColumns(4)
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

def draw_subhist_separators(c,stitch_edge_bins,binmapping,labels,conf,hist_template):

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

        ycoord = conf['ypos']
	
	for item, isep in enumerate(separator_bins):
		x = hist_template.GetBinLowEdge(isep)+hist_template.GetBinWidth(isep)
		#ymin = hist_template.GetYaxis().GetXmin()
		ymin = hist_template.GetMinimum()
		ymax = hist_template.GetMaximum()
		#print x, hist_template.GetMaximum()
		l = rt.TLine(x,ymin,x,ymax); l.SetLineColor(rt.kBlack); l.SetLineWidth(2)
		l.Draw()
	
		if isinstance(labels,list):
			tex = rt.TLatex()
                        if 'size' in conf: tex.SetTextSize(conf['size'])
                        else: tex.SetTextSize(0.045)
			tex.SetTextAlign(32)
			#tex.SetTextAngle(45)
			cxmin=c.GetLeftMargin()
			cxmax=1.-c.GetRightMargin()
			cymin=c.GetXlowNDC()
			xmax = hist_template.GetXaxis().GetXmax()
			xmin = hist_template.GetXaxis().GetXmin()
                        if isinstance(labels[item],list) and len(labels[item])>1: x = labels[item][1]
			xndc= cxmin + (x - xmin)/(xmax - xmin) * (cxmax - cxmin)
			#xndc= c.GetLeftMargin()
			print isep,xndc,ycoord,labels[item][0]
			tex.DrawLatexNDC(xndc-0.05,ycoord,labels[item][0])
			if (item == len(separator_bins)-1): 
                            if isinstance(labels[item+1],list) and len(labels[item+1])>1: 
                                x = labels[item+1][1]
			        xndc= cxmin + (x - xmin)/(xmax - xmin) * (cxmax - cxmin)
                                tex.DrawLatexNDC(xndc-0.05,ycoord,labels[item+1][0])
                            else: 
                                tex.DrawLatexNDC(cxmax-0.05,ycoord,labels[item+1][0])
	
def draw_chi2_ndf(c,chi2,ndf):
	c.cd()
	text = '#chi^{{2}}/NDF = {0:.2f}/{1:d}, p-val={2:.2f}'.format(chi2,int(ndf),rt.TMath.Prob(chi2, int(ndf)))
	tex = rt.TLatex()
	tex.SetTextAngle(90)
	tex.DrawLatexNDC(0.99,0.2,text)
	

def main(arguments):

	#Apply TDR style
	tdrstyle.setTDRStyle()

	#Manipulate python garbage collection
	rt.TLegend.__init__._creates = False
	rt.TLine.__init__._creates = False
	
	#Modify hatch bands
	#rt.gStyle.SetHatchesLineWidth(2)

	hatchStyle = 3013
	hatchColor = rt.kBlack

	inputrootfile = rt.TFile.Open(arguments.infile, 'READ')
	jsondic = None
	with open(arguments.config_json) as json_data:
		jsondic = json.load(json_data)
		logging.debug(pprint.pformat(jsondic))
	
	#count number of bins for mountain range plot
	nbins = 0
	logging.debug( '%s: %s' % ('signal',jsondic['signal']) )
	for hist_name in jsondic['signal']:
		logging.debug( 'hist %s' % (hist_name) )
		hist = inputrootfile.Get(hist_name.encode('ascii'))
		nb = hist.GetNbinsX()
		logging.debug( 'hist %s, nbins=%s' % (hist_name, nb) )
		nbins += nb
	logging.info('Mountain range plot nbins: ' + str(nbins))	

	#create individual histograms for signal, background and data that will be added to the stack plot
	#clone entries and uncertainties from individual search regions to the master histograms
	
	#Signal
	hist_sig = rt.TH1F('hist_sig',arguments.distrib_title,nbins,1.,float(nbins))
	stitch_edges = fillsingle(hist_sig, inputrootfile, jsondic['signal'])

	#Background
        hist_st = rt.THStack('hist_st','background stack;Bin id;events')
	fillstack(hist_st, hist_sig, inputrootfile, jsondic['stack'])

	#Total bg with uncertainties
	#prefit shapes and unc
	hist_bg_prefit_unc = rt.TH1F('hist_bg_prefit_unc',arguments.distrib_title,nbins,1.,float(nbins))
	hist_bg_prefit_unc.SetFillStyle(0)
	hist_bg_prefit_unc.SetLineColor(rt.kBlue)
	hist_bg_prefit_unc.GetXaxis().SetLabelSize(0)
        fillsingle(hist_bg_prefit_unc, inputrootfile, jsondic['prefitbg'])
	#postfit shapes and unc
	hist_bg_unc = rt.TH1F('hist_bg_unc',arguments.distrib_title,nbins,1.,float(nbins))
	#hist_bg_unc.SetFillStyle(3144)
	hist_bg_unc.SetFillStyle(hatchStyle)
	hist_bg_unc.SetFillColor(hatchColor)
	hist_bg_unc.SetLineColor(hatchColor)
	hist_bg_unc.GetXaxis().SetLabelSize(0)
        fillsingle(hist_bg_unc, inputrootfile, jsondic['totalbg'])

	#Data if ublinded
	gr_data = None
	if 'data' in jsondic:
		gr_data = rt.TGraphAsymmErrors(nbins)
		fillsingle_data(gr_data, inputrootfile, jsondic['data'],hist_sig,arguments.blind)
	if gr_data:
		gr_data.SetMarkerStyle(20)	


	binmapping = binmap(hist_bg_unc, hist_sig, gr_data)
	logging.info( "Bin mapping:")
	logging.info(pprint.pformat( binmapping ) )

	hist_bg_unc_noempty = noemptybins(hist_bg_unc, binmapping); 
	hist_bg_unc_noempty.SetMarkerSize(0)
	hist_bg_unc_noempty.SetFillStyle(hatchStyle); 
	hist_bg_unc_noempty.SetFillColor(hatchColor);
	hist_bg_unc_noempty.SetLineWidth(0)
	
	hist_sig_noempty    = noemptybins(hist_sig, binmapping); 
	hist_sig_noempty.Scale(arguments.scale_signal)
	hist_sig_noempty.SetLineColor(hatchColor); 
	hist_sig_noempty.SetLineWidth(2)
        
	hist_st_noempty = rt.THStack('hist_st_mountain','background stack;Bin id;events')
	for hist in hist_st.GetHists():
		hist_noempty = noemptybins(hist, binmapping)
		hist_noempty.SetLineWidth(2)
		hist_noempty.SetLineColor(hist_noempty.GetFillColor())
		hist_st_noempty.Add(hist_noempty,'hist')
	
	hist_bg_prefit_unc_noempty = noemptybins(hist_bg_prefit_unc, binmapping); 
	#hist_bg_prefit_unc_noempty.SetMarkerSize(0); 
	hist_bg_prefit_unc_noempty.SetMarkerStyle(27); 
	hist_bg_prefit_unc_noempty.SetFillStyle(0); 
	hist_bg_prefit_unc_noempty.GetXaxis().SetLabelSize(0); 
	hist_bg_prefit_unc_noempty.GetYaxis().SetTitleSize(0.07); 
	hist_bg_prefit_unc_noempty.GetYaxis().SetTitleOffset(0.8);  
	#hist_bg_prefit_unc_noempty.GetXaxis().SetTitleSize(0.07); 
	hist_bg_prefit_unc_noempty.GetXaxis().SetTitleSize(0.0); 
	hist_bg_prefit_unc_noempty.GetXaxis().SetTitleOffset(0.7)

	gr_data_noempty = None
	if gr_data: gr_data_noempty = noemptybins_data(gr_data, binmapping, hist_noempty) 


	rt.gStyle.SetOptStat(0)
	c1 = rt.TCanvas('c1')
	hist_bg_prefit_unc.Draw("E2")
	hist_st.Draw("same")
	hist_bg_prefit_unc.Draw("E2 same")
	hist_bg_unc.Draw("E2 same")
	hist_sig.Draw("same")
	if gr_data: gr_data.Draw("same pe")
	#c1.SetLogy()
	c1.RedrawAxis()
	#c1.Print('hist1.png')

	c = rt.TCanvas('c',"CMS",5,45,1000,750)
	if arguments.is_ratio and gr_data:
		c.Divide(1,3)
		c.cd(3)
		rt.gPad.SetPad(0.,0.,1.,0.1)
		c.cd(2)
		rt.gPad.SetPad(0.,0.1,1.,0.375);rt.gPad.SetFillStyle(4000)
		c.cd(1)
		rt.gPad.SetPad(0.,0.3,1.,1.);rt.gPad.SetFillStyle(4000)
	hist_bg_prefit_unc_noempty.Draw("E2")
	ymin = hist_bg_prefit_unc_noempty.GetMinimum()
	ymax = 10.*hist_bg_prefit_unc_noempty.GetMaximum()
        ytitle = None
	if "axes" in jsondic:
		if "ymin" in jsondic['axes']: ymin = jsondic['axes']['ymin']
		if "ymax" in jsondic['axes']: ymax = jsondic['axes']['ymax']
                if "ytitle" in jsondic['axes']: 
                    ytitle = jsondic['axes']['ytitle']
	            hist_bg_prefit_unc_noempty.GetYaxis().SetTitle(ytitle)
	hist_bg_prefit_unc_noempty.SetAxisRange(ymin, ymax, "Y")
	hist_st_noempty.Draw("same")
	hist_bg_prefit_unc_noempty.Draw("E2 same")
	hist_bg_unc_noempty.Draw("E2 same")
	hist_sig_noempty.Draw("hist same")
	if gr_data_noempty: gr_data_noempty.Draw("same pe")
	draw_legend(canvas=c,legend=jsondic['legend'],data=gr_data_noempty,hist_pre=hist_bg_prefit_unc_noempty,hist_post=hist_bg_unc_noempty,
			hist_tttt=hist_sig_noempty,
			hist_tt=hist_st_noempty.GetHists()[-1],
			hist_rare=hist_st_noempty.GetHists()[-2],
			hist_st=hist_st_noempty.GetHists()[-3],
			hist_ew=hist_st_noempty.GetHists()[-4])
	#draw_bin_labels(c.cd(1),hist_bg_prefit_unc_noempty,jsondic['binlabels']['labels'],jsondic['binlabels']['ypos'],stitch_edges)
	draw_subhist_separators(c.cd(1),stitch_edges,binmapping, jsondic['binlabels']['labels'],jsondic['binlabels'], hist_bg_prefit_unc_noempty)
	rt.gPad.RedrawAxis()

	if arguments.is_ratio and gr_data:
		c.cd(2)
		hist_ratio_unity = hist_bg_unc_noempty.Clone("hist_ratio_unity")
		#hist_ratio_unity = hist_bg_prefit_unc_noempty.Clone("hist_ratio_unity")
		hist_ratio_unity.SetMarkerSize(0)
		if arguments.distrib_title_ratio is not None: hist_ratio_unity.SetTitle(arguments.distrib_title_ratio)
		else:
			motherhistxtitle = hist_bg_unc_noempty.GetXaxis().GetTitle()
			motherhistxtitle = ';Bin id (%s);Data/Pred.' % re.sub(r' \(.*\)', '', motherhistxtitle)
			hist_ratio_unity.SetTitle(motherhistxtitle)
		hist_ratio_unity.GetXaxis().SetTitleSize(0.15)
		hist_ratio_unity.GetXaxis().SetLabelSize(0.0)
		hist_ratio_unity.GetXaxis().SetTickLength(0.12)
		hist_ratio_unity.GetYaxis().SetTitleSize(0.19)
		hist_ratio_unity.GetYaxis().SetTitleOffset(0.26)
		hist_ratio_unity.GetYaxis().SetLabelSize(0.13)
		hist_ratio_unity.GetYaxis().SetLabelOffset(0.01)
		#hist_ratio_unity.GetXaxis().CenterTitle()
		hist_ratio_unity.GetYaxis().CenterTitle()
		hist_ratio_unity.GetYaxis().SetNdivisions(5)
		hist_ratio_unity.Divide(hist_ratio_unity)
		gr_ratio_data = rt.TGraphAsymmErrors()
		gr_ratio_data.SetMarkerStyle(20)
		logging.debug("number of bins/points: %d %d" % (hist_ratio_unity.GetNbinsX(), gr_data_noempty.GetN()))
		chi2,ndf = 0.,0.
		for ibin in range(0,hist_ratio_unity.GetNbinsX()):
			hist_ratio_unity.SetBinContent(ibin+1,0.)
			ydata = gr_data_noempty.GetY()
			xdata = gr_data_noempty.GetX()
			ymc   = hist_bg_unc_noempty.GetBinContent(ibin+1)
			eymc  = hist_bg_unc_noempty.GetBinError(ibin+1)
			eyh   = gr_data_noempty.GetErrorYhigh(ibin)
			eyl   = gr_data_noempty.GetErrorYlow(ibin)
			if ydata[ibin] > 1.E-6:
				#chi2+=(ydata[ibin]-ymc)**2/(((eyh+eyl)/2.)**2.)
				chi2+=(ydata[ibin]-ymc)**2/(((eyh+eyl)/2.)**2.+eymc**2.)
				ndf+=1.
				gr_ratio_data.SetPoint(ibin,xdata[ibin],(ydata[ibin]-ymc)/ymc)
				gr_ratio_data.SetPointError(ibin,0.,0.,eyl/ymc, eyh/ymc)
		#hist_ratio_unity.GetYaxis().SetRangeUser(-0.5,0.5)
		hist_ratio_unity.GetYaxis().SetRangeUser(-1.,1.)
		#hist_ratio_unity.GetYaxis().SetRangeUser(-2.,2.)
		hist_ratio_unity.Draw("hist e2")
		gr_ratio_data.Draw("same pe")
		if arguments.draw_chi2: draw_chi2_ndf(rt.gPad,chi2,ndf)
		if ndf > 0:
			print "chi2/ndf=", chi2,"/",ndf,"=",chi2/ndf
		draw_subhist_separators(c.cd(2),stitch_edges,binmapping, None,jsondic['binlabels'], hist_ratio_unity)
		rt.gPad.RedrawAxis()
			
			

	#hist_bg_prefit_unc_noempty.GetXaxis().SetRangeUser(100.,125.)
	CMS_lumi.CMS_lumi(c.cd(1),4,0)
	if arguments.outfile: 
		c.Print(arguments.outfile+'_lin.'+arguments.extension)
		c.cd(1); rt.gPad.SetLogy(); 
		c.Print(arguments.outfile+'_log.'+arguments.extension)
	else:
		if 'filename' in jsondic: 
			c.Print(arguments.dir+'/'+jsondic['filename']+'_lin.'+arguments.extension)
			c.cd(1); rt.gPad.SetLogy(); 
			c.Print(arguments.dir+'/'+jsondic['filename']+'_log.'+arguments.extension)

	# Extracting p-values from files
	if arguments.gof_data is not None and arguments.gof_toys is not None :
		f_toys = rt.TFile.Open(arguments.gof_toys,"READ")
		t_toys = f_toys.Get("limit")
		f_data = rt.TFile.Open(arguments.gof_data,"READ")
		t_data = f_data.Get("limit")
		stat_data = 100000000.
		for entr in t_data: stat_data = entr.limit
		pval = 0
		for entr in t_toys:
			logging.debug("Toy p-val: %f" % (entr.limit))
			if entr.limit>stat_data: pval+=1
		pval/=t_toys.GetEntries()
		print "Data: ", stat_data 
		print "p-value: ", pval

        return 0


if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('infile', help="Input file")
        parser.add_argument('-o', '--outfile', help="Output file")
	parser.add_argument('-r', '--ratio', help="Make ratio plot", dest='is_ratio', action='store_true')
        parser.add_argument('-j', '--config-json', help="JSON configuration file")
        parser.add_argument('-e', '--extension', help="Plot file extension (.C, .root, .png, .pdf)", default='png')
        parser.add_argument('--dir', help="Plots output directory", default='./')
        parser.add_argument('--blind', help="Blind datapoints from these categories [CAT1,CAT2]", default=None, type=str)
        parser.add_argument('--scale-signal', help="Scale signal", default=1., type=float)
        parser.add_argument('--gof-toys', help="ROOT file with GOF toys for p-value calculation", default=None)
        parser.add_argument('--gof-data', help="ROOT file with observed p-value", default=None)
        parser.add_argument('--distrib-title', help="Histogram title settings", default=';;Events')
        parser.add_argument('--distrib-title-ratio', help="Ratio histogram title settings", default=None)
        parser.add_argument('--draw-chi2', help="Plot chi2 on the plot", dest='draw_chi2', action='store_true', default=False)
        #parser.add_argument('--distrib-title-ratio', help="Ratio histogram title settings", default=';Bin id (D_{t#bar{t}t#bar{t}}^{lj});Rel. diff.')
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
