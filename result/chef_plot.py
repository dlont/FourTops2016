import argparse

parser = argparse.ArgumentParser(description="Puts together histograms into a nicely formatted plot for you.", epilog="Run chef_histogram.py first in order to obtain the histograms!")
parser.add_argument("plotprops", metavar="plotprops", help="File containing list of attributes you want in a plot (same as chef_histogram.py)")
parser.add_argument("dir", metavar="dir", help="Directory to read histogram files")
parser.add_argument("MClist", metavar="plot_list_MC", help="File containing list of MC histograms you want")
parser.add_argument("--DataHist", metavar="data_histogram", help="File containing Data histogram you want -- Do not use this flag for blind analysis.")
parser.add_argument("--DataName", metavar="data_name", help="Custom data Craneen name")
parser.add_argument("--preselection", nargs='*', help="Choose a collection (or multiple collections) to do plots -- Leave blank to get all categories from file")
parser.add_argument("--weighting", metavar="weighting_list", help="File containing list of weighting schemes you want")
parser.add_argument("--lumi", metavar="luminosity", help="Target luminosity for each histogram -- Overridden if Datalist option is present")
parser.add_argument("--outputName", help="Name of output ROOT file containing all plots.", default="hist_collection")
parser.add_argument("--noLog", help="Disables log plots", action="store_true")
parser.add_argument("--noOverflow", help="Disables overflow bin", action="store_true")
parser.add_argument("--systematics", help="File containing list of central, upper and lower limit of scale factors")

args = parser.parse_args()

import ROOT as pyr
import tdrstyle
import numpy as np
import math

def get_graph_with_errors_from_histograms(central,up,down):
    if central == None or up == None or down == None:
        raise RuntimeError("Supplied histograms are Null! c:{} u:{} d:{}".format(central,up,down))
    number_of_bins = central.GetNbinsX()
    if up.GetNbinsX() != number_of_bins or down.GetNbinsX() != number_of_bins:
        raise RuntimeError("Histograms have different number of bins: c:{}, u:{}, d:{}".format(number_of_bins,up.GetNBinsX(),down.GetNBinsX()))
    gr = pyr.TGraphAsymmErrors(central)
    for bin in range(1,up.GetNbinsX()+1):
        gr.SetPoint(bin-1,central.GetBinCenter(bin),0.)
        exl = -(central.GetBinCenter(bin) - central.GetBinLowEdge(bin))
        exh = central.GetBinLowEdge(bin) - central.GetBinCenter(bin) 
        gr.SetPointError(bin-1,exl,exh,-down.GetBinContent(bin),up.GetBinContent(bin))
    gr.SetFillColor(1)
    gr.SetFillStyle(3004)
    return gr

def drawOverflow(hist):
    #print(type(hist))
    if not type(hist) == pyr.TH1D:
        raise TypeError("drawOverflow accepts TH1D objects only. Sorry.")
    nx = hist.GetNbinsX() + 1
    xbins = []
    for i in range(nx):
        xbins.append(hist.GetBinLowEdge(i+1))
    xbins.append(xbins[nx-1] + hist.GetBinWidth(nx))
    cacheHist = pyr.TH1D(hist.GetName()+"_overflow", hist.GetTitle(), nx, np.asarray(xbins))
    cacheHist.SetXTitle(hist.GetXaxis().GetTitle())
    cacheHist.SetYTitle(hist.GetYaxis().GetTitle())
    
    for i in range(1, nx + 1):
        cacheHist.Fill(cacheHist.GetBinCenter(i), hist.GetBinContent(i))
    cacheHist.Fill(hist.GetBinLowEdge(1) - 1, hist.GetBinContent(0))
    for i in range(nx + 1):
        cacheHist.SetBinError(i, hist.GetBinError(i))

    cacheHist.SetEntries(hist.GetEntries())
    cacheHist.SetFillStyle(hist.GetFillStyle())
    cacheHist.SetFillColor(hist.GetFillColor())
    cacheHist.SetMarkerStyle(hist.GetMarkerStyle())
    cacheHist.SetLineWidth(hist.GetLineWidth())
    cacheHist.SetLineColor(hist.GetLineColor())

    return cacheHist

def styleRatioPlot(hist_ratio, points = True):
    if points:
        hist_ratio.SetLineColor(1)
        hist_ratio.SetMarkerStyle(21)
    hist_ratio.SetMinimum(0.5)
    hist_ratio.SetMaximum(1.5)
    hist_ratio.GetYaxis().SetTitle("data/MC ")
    hist_ratio.GetYaxis().SetTitleSize(0.08)
    hist_ratio.GetYaxis().SetTitleOffset(0.55)
    hist_ratio.GetYaxis().SetLabelSize(0.08)
    hist_ratio.GetYaxis().SetNdivisions(502, False)
    hist_ratio.GetYaxis().SetDecimals(True)

    hist_ratio.GetXaxis().SetLabelSize(0.10)
    hist_ratio.GetXaxis().SetTitleSize(0.10)

delimiter = "======================================"

plotlist_MC_file = open(args.MClist)
plotlist_MC_list = plotlist_MC_file.readlines()

blind = False
if args.DataHist != None:
    plotlist_Data_file = open(args.DataHist)
else:
    print delimiter
    print "Blind analysis activated"
    blind = True

plotprops_file = open(args.plotprops)
plotprops_list = []
for line in plotprops_file.readlines():
    propname = line.split()[0]
    nbins = int(line.split()[1])
    lowbound = float(line.split()[2])
    highbound = float(line.split()[3])
    propdesc = " ".join(line.split()[4:])
    plotprops_list.append((propname, nbins, lowbound, highbound, propdesc))

open_dir = args.dir

mc_colour_collection = []
mcName = ""

if args.lumi != None:
    targetLumi = float(args.lumi)
else:
    targetLumi = 1.

for line in plotlist_MC_list:
    mcFileName = line.split()[0]
    mcSet = line.split()[1]
    mcName = " ".join(line.split()[2:-1])
    mcColour = int(line.split()[-1])
    mc_colour_collection.append((mcFileName, mcSet, mcName, mcColour))

print mc_colour_collection

if not blind: histfile_data = pyr.TFile(args.DataHist)
print "histfile_data: ",histfile_data
preselection_list = []
if args.preselection != None:
    if args.preselection != []:
        preselection_list = args.preselection
    else:
        histfile_sample = pyr.TFile(mc_colour_collection[0][0])
        for key in histfile_sample.GetListOfKeys():
            if key.GetClassName() == "TDirectoryFile":
                preselection_list.append(key.GetName())
        histfile_sample.Close()
else:
    preselection_list = ["all"]

print delimiter
print "Preselection: "
print preselection_list

weighting_scheme = []
if args.weighting != None:
    weighting_file = open(args.weighting)
    for line in weighting_file.readlines():
        name = line.split()[0]
        weighting_scheme.append(name)
else:
    weighting_scheme.append("NoWeights")

dataset_name = "Data"
if args.DataName != None:
    dataset_name = args.DataName

draw_syst = False
syst_list = []
if args.systematics != None:
    with open(args.systematics) as systfile:
        for line in systfile.readlines():
            columns_entries = line.split()
            name,sys_type = columns_entries[0],columns_entries[1]
            if '#' not in name: syst_list.append(name)  # skip commented out systematics entries
    draw_syst = True

if draw_syst:
    print delimiter
    print "Drawing systematic errors in ratio plot with following systs:"
    print syst_list

outcanvasfile = pyr.TFile(args.outputName,"RECREATE")
for propline in plotprops_list:
    propName = propline[0]
    propDesc = propline[-1]
    for cat in preselection_list:
        for weight in weighting_scheme:
            canvas = pyr.TCanvas(propName + '_' + cat + '_' + weight, propName + '_' + cat + '_' + weight, 750, 750)
            legend = pyr.TLegend(0.5, 0.75, 0.9, 0.9)
            legend.SetNColumns(2)
            legend.SetHeader("Single lepton: {}".format(dataset_name))
            if not blind:
                print "Looking for hist: ", cat+'/'+"hist_Data_"+propName+'_'+weight+'_'+cat
                hist_data = histfile_data.Get(cat+'/'+"hist_Data_"+propName+'_'+weight+'_'+cat).Clone()
                if not args.noOverflow:
                    hist_data = drawOverflow(hist_data)
                else:
                    hist_data.Sumw2()
                hist_data.SetMarkerStyle(20)
                hist_data.SetMarkerColor(1)
                legend.AddEntry(hist_data, "Data " + " (" + "{:.0f}".format(hist_data.Integral()) + " entries)")
                # legend.AddEntry(hist_data, dataset_name + " (" + "{:.1f}".format(hist_data.Integral()) + ")")
                
            hist_mc_stack = pyr.THStack()
            hist_line = None
            hist_line_name = ""
            hist_upper_unc = {}
            hist_lower_unc = {}
            for mcfile, mcset, mcName, mc_colour in mc_colour_collection:
                histfile_mc = pyr.TFile(mcfile)
                print mcfile
                print histfile_mc
                histfile_mc.ls(cat)
                pyr.gROOT.cd()
                print mcfile
                print cat+'/'+"hist_"+mcset+'_'+propName+'_'+weight+'_'+cat
                hist_mc = histfile_mc.Get(cat+'/'+"hist_"+mcset+'_'+propName+'_'+weight+'_'+cat).Clone(cat+'/'+"hist_"+mcName+'_'+propName+'_'+weight+'_'+cat)
                if not args.noOverflow:
                    hist_mc = drawOverflow(hist_mc)
                if draw_syst:
                    for syst_name in syst_list:
                        print cat+'/'+"hist_"+mcset+'_'+propName+'_'+weight+'_'+cat+"_"+syst_name+"_up"
                        if syst_name not in hist_upper_unc.keys():
                            print cat+'/'+"hist_"+mcset+'_'+propName+'_'+weight+'_'+cat+"_"+syst_name+"_up"
                            hist_upper_unc[syst_name] = histfile_mc.Get(cat+'/'+"hist_"+mcset+'_'+propName+'_'+weight+'_'+cat+"_"+syst_name+"_up").Clone(propName+'_'+weight+'_'+cat+"_"+syst_name+"_up")
                            hist_upper_unc[syst_name].SetDirectory(pyr.gROOT)
                        else:
                            hist_upper_unc[syst_name].Add(histfile_mc.Get(cat+'/'+"hist_"+mcset+'_'+propName+'_'+weight+'_'+cat+"_"+syst_name+"_up"))
                        print cat+'/'+"hist_"+mcset+'_'+propName+'_'+weight+'_'+cat+"_"+syst_name+"_down"
                        if syst_name not in hist_lower_unc.keys():
                            hist_lower_unc[syst_name] = histfile_mc.Get(cat+'/'+"hist_"+mcset+'_'+propName+'_'+weight+'_'+cat+"_"+syst_name+"_down").Clone(propName+'_'+weight+'_'+cat+"_"+syst_name+"_down")
                            hist_lower_unc[syst_name].SetDirectory(pyr.gROOT)
                        else:
                            hist_lower_unc[syst_name].Add(histfile_mc.Get(cat+'/'+"hist_"+mcset+'_'+propName+'_'+weight+'_'+cat+"_"+syst_name+"_down"))
                if mc_colour != 1:
                    hist_mc.SetFillColor(mc_colour)
                    hist_mc.SetMarkerStyle(1)
                    hist_mc.SetMarkerSize(0)
                    hist_mc.SetLineWidth(0)
                    hist_mc_stack.Add(hist_mc)
                    legend.AddEntry(hist_mc, mcName + " (" + "{:.0f}".format(hist_mc.Integral()) + " entries)")
                    # legend.AddEntry(hist_mc, mcName + " (" + "{:.1f}".format(hist_mc.Integral()) + ")")
                else:
                    pyr.gROOT.cd()
                    hist_line = hist_mc.Clone()
                    hist_line.SetFillStyle(0)
                    hist_line.SetLineWidth(3)
                    hist_line.SetLineColor(1)
                    hist_line.SetMarkerStyle(0)
                    hist_line_name = mcName
            legend.AddEntry(hist_line, hist_line_name + " (" + "{:.0f}".format(hist_line.Integral()) + ")")
            # legend.AddEntry(hist_line, hist_line_name + " (" + "{:.1f}".format(hist_line.Integral()) + ")")

            canvas.cd()
            if not blind:
                pad1 = pyr.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
                pad1.SetBottomMargin(0)
                pad1.Draw()
                pad1.cd()
                
            if not args.noLog: pyr.gPad.SetLogy(True)
            #print "Now drawing"
            hist_mc_stack.Draw("hist")
            hist_mc_stack.GetYaxis().SetTitle("Events/{:0.2f}".format(round(hist_mc_stack.GetStack().Last().GetBinWidth(1), 2)))
            hist_mc_stack.SetTitle(cat)
            #print "hist_mc_stack.GetYaxis()"
            #hist_mc_stack.GetYaxis().SetRangeUser(max(hist_line.GetMinimum(), 0.), hist_mc_stack.GetMaximum()*10.)
            hist_mc_stack.SetMinimum(0.01)
            hist_mc_stack.SetMaximum(hist_mc_stack.GetMaximum()*20.)
            if blind: hist_mc_stack.GetXaxis().SetTitle(propDesc)
            hist_line.Draw("hist same")
            #print "hist_line.GetYaxis()"
            #hist_line.GetYaxis().SetRangeUser(max(hist_line.GetMinimum(), 0.), hist_mc_stack.GetMaximum()*10.)
            hist_line.SetMinimum(0.01)
            hist_line.SetMaximum(hist_mc_stack.GetMaximum()*20.)
            #print hist_data
            if not blind: 
                hist_data.Draw("same")
                #print "hist_data.GetYaxis()"
                #hist_data.GetYaxis().SetRangeUser(max(hist_line.GetMinimum(), 0.), hist_mc_stack.GetMaximum()*10.)
                hist_data.SetMinimum(0.1)
                hist_data.SetMaximum(hist_mc_stack.GetMaximum()*20.)
            legend.Draw()

            if blind:
                hist_mc_stack.GetXaxis().SetLabelSize(0.03)
                hist_mc_stack.GetXaxis().SetTitleSize(0.03)

            if not args.noOverflow:
                overflowPosX = hist_line.GetBinCenter(hist_line.GetNbinsX()) + hist_line.GetBinWidth(hist_line.GetNbinsX())*0.2
                overflowPosY = hist_mc_stack.GetMaximum()/10.

                overflowText = pyr.TText(overflowPosX, overflowPosY, "Overflow")
                overflowText.SetTextAngle(90)
                overflowText.SetTextFont(42)
                overflowText.SetTextSize(0.05)
                overflowText.Draw()

            pyr.gPad.Modified()
            pyr.gPad.Update()

            if not blind:
                canvas.cd()
                pad2 = pyr.TPad("pad2", "pad2", 0, 0.01, 1, 0.3)
                pad2.SetTopMargin(0)
                pad2.SetBottomMargin(0.2)
                pad2.SetGridy()
                pad2.Draw()
                pad2.cd()
                pyr.gStyle.SetHistTopMargin(0)

                if draw_syst:
                    hist_highline_unc = hist_upper_unc[syst_list[0]].Clone(propName+'_'+weight+'_'+cat+"_"+"_lineup")
                    hist_lowline_unc  = hist_lower_unc[syst_list[0]].Clone(propName+'_'+weight+'_'+cat+"_"+"_linedown")

                    for i in range(hist_highline_unc.GetNbinsX()+2):
                        cache_up = 0.
                        cache_down = 0.
                        cache_central = hist_mc_stack.GetStack().Last().GetBinContent(i)
                        for syst in syst_list:
                            cache_up   += (hist_upper_unc[syst].GetBinContent(i) - cache_central)**2
                            cache_down += (hist_lower_unc[syst].GetBinContent(i) - cache_central)**2
                        cache_up = math.sqrt(cache_up)
                        cache_down = -math.sqrt(cache_down)
                        hist_highline_unc.SetBinContent(i, cache_up)
                        hist_lowline_unc.SetBinContent(i, cache_down)
                    
                    if not args.noOverflow:
                        hist_highline_unc = drawOverflow(hist_highline_unc)
                        hist_lowline_unc = drawOverflow(hist_lowline_unc)

                    hist_highline_unc.Divide(hist_mc_stack.GetStack().Last())
                    hist_lowline_unc.Divide(hist_mc_stack.GetStack().Last())
                    gr_errors = get_graph_with_errors_from_histograms(hist_mc_stack.GetStack().Last(),hist_highline_unc,hist_lowline_unc)

                    hist_unc_stack = pyr.THStack()
                    hist_unc_stack.SetMinimum(-0.999)
                    hist_unc_stack.SetMaximum(+0.999)

                    hist_ratio = hist_data.Clone("hist_ratio")
                    hist_ratio.SetLineColor(1)
                    hist_ratio.Add(hist_mc_stack.GetStack().Last(),-1.)
                    hist_ratio.Divide(hist_mc_stack.GetStack().Last())
                    hist_ratio.SetMarkerStyle(21)
                    # hist_ratio.Draw("ep same")
                    # hist_ratio.GetXaxis().SetTitle(propDesc)
                    styleRatioPlot(hist_ratio)
                    hist_unc_stack.Add(hist_ratio)

                    hist_unc_stack.Draw("nostack")
                    gr_errors.Draw("PE2")
                    gr_errors.Print("All")

                    hist_unc_stack.GetYaxis().SetTitle("(Data-MC)/MC ")
                    hist_unc_stack.GetYaxis().SetTitleSize(0.08)
                    hist_unc_stack.GetYaxis().SetTitleOffset(0.55)
                    hist_unc_stack.GetYaxis().SetLabelSize(0.08)
                    hist_unc_stack.GetYaxis().SetNdivisions(502, False)
                    hist_unc_stack.GetYaxis().SetDecimals(True)

                    hist_unc_stack.GetXaxis().SetLabelSize(0.10)
                    hist_unc_stack.GetXaxis().SetTitleSize(0.10)
                    hist_unc_stack.GetXaxis().SetTitle(propDesc)
                    if 'Number of' in hist_unc_stack.GetXaxis().GetTitle():
                        hist_unc_stack.GetXaxis().SetNdivisions(500, False)

                    #raw_input()

            
            if not blind:
                pad1.cd()
            else:
                canvas.cd()
            tdrstyle.cmsPrel(targetLumi*1000, 13., False, True, sp=0, textScale=1., xoffset=0., thisIsPrelim=True)

            #raw_input()
            canvas.SaveAs(open_dir+"/hist_"+propName+"_"+cat+'_'+weight+".png")
            outcanvasfile.cd()
            canvas.Write()
            canvas.Close()