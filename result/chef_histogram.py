import argparse

parser = argparse.ArgumentParser(description="Cooks some histograms from Craneen files for you.")
parser.add_argument("plotprops", metavar="plotprops", help="File containing list of attributes you want in a plot")
parser.add_argument("treename", metavar="tree_name", help="Tree name you want from Craneen file")
parser.add_argument("dir", metavar="dir", help="Directory to store new histogram files")
parser.add_argument("MClist", metavar="plot_list_MC", help="File containing list of MC Craneen files you want")
parser.add_argument("--Datalist", metavar="plot_list_Data", help="File containing list of Data files you want -- Do not use this flag for blind analysis.")
parser.add_argument("--preselection", metavar="preselection_file", help="File containing list of preselection cuts you want")
parser.add_argument("--weighting", metavar="weighting_list", help="File containing list of weighting schemes you want")
parser.add_argument("--lumi", metavar="luminosity", help="Target luminosity for each histogram -- Overrides luminosity from Datalist option")
parser.add_argument("--systematics", help="File containing list of central, upper and lower limit of scale factors")

args = parser.parse_args()

import ROOT as pyr
import time
pyr.gErrorIgnoreLevel = 0

def checkOp(event, key, op, value):
    if op == "==":    return getattr(event, key) == value
    elif op == "!=":  return getattr(event, key) != value
    elif op == ">":   return getattr(event, key) > value
    elif op == "<":   return getattr(event, key) < value
    elif op == ">=":  return getattr(event, key) >= value
    elif op == "<=":  return getattr(event, key) <= value
    elif op == "a==": return abs(getattr(event, key)) == value
    elif op == "a!=": return abs(getattr(event, key)) != value
    elif op == "a>=": return abs(getattr(event, key)) >= value
    elif op == "a<=": return abs(getattr(event, key)) <= value
    elif op == "a>":  return abs(getattr(event, key)) > value
    elif op == "a<":  return abs(getattr(event, key)) < value
    else: return True

delimiter = "======================================"

plotlist_MC_file = open(args.MClist)
plotlist_MC_list = plotlist_MC_file.readlines()

blind = False
if args.Datalist != None:
    plotlist_Data_file = open(args.Datalist)
    plotlist_Data_list = plotlist_Data_file.readlines()
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

print delimiter
print "Properties to be plotted"
print plotprops_list

preselection_list = []
if args.preselection != None:
    preselection_file = open(args.preselection)
    for line in preselection_file.readlines():
        if "###" in line:
            break
        name = line.split()[0]
        configs = " ".join(line.split()[1:])
        preselection_list.append((name, configs))
else:
    preselection_list.append(("all", []))

print delimiter
print "Preselection catergories"
print preselection_list

forced_preselection_list = {}
if args.preselection != None:
    preselection_file = open(args.preselection)
    force_read_start = False
    for line in preselection_file.readlines():
        if not force_read_start:
            if "###" in line:
                force_read_start = True
        else:
            filename = line.split()[0]
            configs = " ".join(line.split()[1:])
            forced_preselection_list[filename] = configs

print delimiter
print "Forced criteria"
print forced_preselection_list

tree_name = args.treename
save_dir = args.dir

weighting_scheme = []
if args.weighting != None:
    weighting_file = open(args.weighting)
    for line in weighting_file.readlines():
        name = line.split()[0]
        rule = " ".join(line.split()[1:])
        weighting_scheme.append([name, rule])
else:
    weighting_scheme.append(["NormalWeight", "ScaleFactor*GenWeight*SFtrig"])

print delimiter
print "Weighting schemes"
print weighting_scheme

systematic_list = []
if args.systematics != None:
    systematic_file = open(args.systematics)
    for line in systematic_file.readlines():
        name = line.split()[0]
        central = line.split()[1]
        upper = line.split()[2]
        lower = line.split()[3]
        systematic_list.append((name, central, upper, lower))
    #if len(systematic_list) > 1:
    #    all_central = "*".join([central for name, central, upper, lower in systematic_list])
    #    all_upper = "*".join([upper for name, central, upper, lower in systematic_list])
    #    all_lower = "*".join([lower for name, central, upper, lower in systematic_list])
    #    systematic_list.append(("All systematic errors", all_central, all_upper, all_lower))

print delimiter
print "Systematic list"
print systematic_list

#raw_input()

if not blind:
    targetLumi = 0.
    for line in plotlist_Data_list:
        targetLumi += float(line.split()[-1])

    print delimiter
    print "Starting data histogram"
    outfile_data = pyr.TFile(save_dir+"/"+"hist_Data.root", "RECREATE")
    
    for condition_name, condition_rules in preselection_list:
        outfile_data.cd()
        pyr.gDirectory.mkdir(condition_name)
        
    pyr.gROOT.cd()
    collection_histograms = {}
    for prop in plotprops_list:
        propName = prop[0]
        propNBins = prop[1]
        propLowerBound = prop[2]
        propHigherBound = prop[3]
        
        weight_histograms = {}
        for weight in weighting_scheme:
            weightName = weight[0]
            #weight_histograms[weightName] = pyr.TH2D("hist_Data_"+propName+"_"+weightName, "Data "+weightName, propNBins, propLowerBound, propHigherBound, len(preselection_list), 0., float(len(preselection_list)))
            presel_histograms = {}
            for presel, binNum in zip(preselection_list,range(1, len(preselection_list)+1)):
                preselName = presel[0]
                #weight_histograms[weightName].GetYaxis().SetBinLabel(binNum, preselName)
                presel_histograms[preselName] = pyr.TH1D("hist_Data_"+propName+"_"+weightName+"_"+preselName, "", propNBins, propLowerBound, propHigherBound)
                presel_histograms[preselName].SetDirectory(pyr.gROOT)
            weight_histograms[weightName] = presel_histograms
        collection_histograms[propName] = weight_histograms

    for line in plotlist_Data_list:
        startTime = time.time()
        craneen = pyr.TFile(line.split()[0])
        tree = getattr(craneen, tree_name)
        print "Starting "+line.split()[0]+" with "+str(tree.GetEntries()) + " events"
        pyr.gROOT.cd()
        for preselName, preselRules in preselection_list:
            #print "plotting "+preselName
            for prop in plotprops_list:
                propName = prop[0]
                #print "plotting "+propName
                for weightName, weightRule in weighting_scheme:
                    #print "plotting "+weightName
                    rule_cache = '(' + preselRules + ')'
                    #rule_cache += "*(" + weightRule +")"
                    tree.Draw(propName+">>+"+"hist_Data_"+propName+"_"+weightName+"_"+preselName, rule_cache, "goff")

                    #pyr.gDirectory.ls()
                    #raw_input()
#         count = 1
#         for event in tree:
#             print "\rProcessing event " + str(count),
#             count += 1
#             for preselName, preselRules in preselection_list:
#                 fillThis = True
#                 for key, op, value in preselRules:
#                     #if op == "==":    fillThis = fillThis and getattr(event, key) == value
#                     #elif op == "!=":  fillThis = fillThis and getattr(event, key) != value
#                     #elif op == ">":   fillThis = fillThis and getattr(event, key) > value
#                     #elif op == "<":   fillThis = fillThis and getattr(event, key) < value
#                     #elif op == ">=":  fillThis = fillThis and getattr(event, key) >= value
#                     #elif op == "<=":  fillThis = fillThis and getattr(event, key) <= value
#                     #elif op == "a==": fillThis = fillThis and abs(getattr(event, key)) == value
#                     #elif op == "a!=": fillThis = fillThis and abs(getattr(event, key)) != value
#                     #elif op == "a>=": fillThis = fillThis and abs(getattr(event, key)) >= value
#                     #elif op == "a<=": fillThis = fillThis and abs(getattr(event, key)) <= value
#                     #elif op == "a>":  fillThis = fillThis and abs(getattr(event, key)) > value
#                     #elif op == "a<":  fillThis = fillThis and abs(getattr(event, key)) < value
#                     fillThis = fillThis and checkOp(event, key, op, value)
#                 if fillThis:
#                     for prop in plotprops_list:
#                         for weight in weighting_scheme:
#                             propName = prop[0]
#                             weightName = weight[0]
#                             collection_histograms[propName][weightName].Fill(getattr(event, propName), preselName, 1.
        endTime = time.time()
        print "\rCompleted in {:.2f} seconds. ({:.2f} events/second)".format(endTime-startTime, tree.GetEntries()/(endTime-startTime))

    for presel, preselNum in zip(preselection_list, range(1, len(preselection_list)+1)):
        preselName = presel[0]
        outfile_data.cd(preselName)
        for prop in plotprops_list:
            propName = prop[0]
            for weightName, weightRule in weighting_scheme:
                hist = collection_histograms[propName][weightName][preselName].Clone()
                #print hist.GetEntries()
                hist.Write()
#     outfile_data.cd()
#     for presel in preselection_list:
#         for prop in plotprops_list:
#             for weight in weighting_scheme:
#                 propName = prop[0]
#                 weightName = weight[0]
#                 collection_histograms[propName][weightName][preselName].Write()
    outfile_data.Close()

if args.lumi != None:
    targetLumi = float(args.lumi)
else:
    if blind: targetLumi = 1.

mc_collection = {}
cachelist = []
mcName = ""

print delimiter
print "Compiling dictionary of MC sets"

for line in plotlist_MC_list:
    if "###" in line or "##!" in line:
        if len(cachelist) != 0:
            mc_collection[mcName] = cachelist
        mcName = " ".join(line.split()[1])
        cachelist = []
    elif "!!!" in line:
        mc_collection[mcName] = cachelist
        break
    else:
        cachelist.append((line.split()[0], float(line.split()[1])))

for mcset in mc_collection.keys():
    print "Starting " + mcset + " histogram set"
    outfile_mc = pyr.TFile(save_dir+"/"+"hist_"+mcset+".root", "RECREATE")
    for condition_name, condition_rules in preselection_list:
        outfile_mc.cd()
        pyr.gDirectory.mkdir(condition_name)
    
    collection_histograms = {}
    systematic_histograms = []
    for prop in plotprops_list:
        propName = prop[0]
        propNBins = prop[1]
        propLowerBound = prop[2]
        propHigherBound = prop[3]

        weight_histograms = {}
        for weight in weighting_scheme:
            weightName = weight[0]
            presel_histograms = {}
            for presel in preselection_list:
                preselName = presel[0]
                presel_histograms[preselName] = pyr.TH1D("hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName, "", propNBins, propLowerBound, propHigherBound)
                presel_histograms[preselName].SetDirectory(pyr.gROOT)
                for syst in systematic_list:
                    syst_name = syst[0]
                    presel_histograms[preselName+"_"+syst_name+"_up"] = pyr.TH1D("hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName+"_"+syst_name+"_up", "", propNBins, propLowerBound, propHigherBound)
                    presel_histograms[preselName+"_"+syst_name+"_up"].SetDirectory(pyr.gROOT)
                    #print presel_histograms[preselName+"_"+syst_name+"_up"]
                    presel_histograms[preselName+"_"+syst_name+"_down"] = pyr.TH1D("hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName+"_"+syst_name+"_down", "", propNBins, propLowerBound, propHigherBound)
                    presel_histograms[preselName+"_"+syst_name+"_down"].SetDirectory(pyr.gROOT)
                    #print presel_histograms[preselName+"_"+syst_name+"_down"]
            weight_histograms[weightName] = presel_histograms
        collection_histograms[propName] = weight_histograms
    #pyr.gROOT.ls()
    #raw_input()
    
    for mcfilename, xsect in mc_collection[mcset]:
        craneen = pyr.TFile(mcfilename)
        tree = getattr(craneen, tree_name)
        print "Starting " + mcfilename + " with " + str(tree.GetEntries()) + " events"
        #bookEvents = 0.
        #for event in craneen.bookkeeping:
        #    bookEvents += event.Genweight
        hist_countbook = pyr.TH1D("count_book", "", 1, 0., 2.)
        craneen.bookkeeping.Draw("1>>count_book", "Genweight", "goff")
        bookEvents = hist_countbook.Integral()
        if abs(bookEvents) < 0.1:
            bookEvents = craneen.bookkeeping.GetEntries()
        print "Events in bookkeeping (Integral) : {}".format(bookEvents)
        print "Events in bookkeeping (GetEvents): {}".format(craneen.bookkeeping.GetEntries())
        del hist_countbook
        startTime = time.time()
        pyr.gROOT.cd()
        for preselName, preselRules in preselection_list:
            for prop in plotprops_list:
                propName = prop[0]
                for weightName, weightRule in weighting_scheme:
                    rule_cache = '(' + preselRules + ')'
                    if mcfilename in forced_preselection_list.keys():
                        rule_cache = rule_cache + " && (" + forced_preselection_list[mcfilename] + ')'
                    rule_cache = '(' + rule_cache + ")*(" + weightRule + ")*(" + str(targetLumi*xsect/bookEvents) + ')'
                    print "Plotting normal histograms"
                    tree.Draw(propName+">>+"+"hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName, rule_cache, "goff")
                    #print propName+">>+"+"hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName
                    #print rule_cache
                    #treeweight = tree.GetW()
                    #treevalue = tree.GetV1()
                    #outtreeweight = open(save_dir+"/weights_"+mcset+"_"+propName+"_"+weightName+"_"+preselName+".txt", "w")
                    #for i in range(tree.GetSelectedRows()):
                    #    outtreeweight.write("{}{:20.9f}{:20.9f}\n".format(i, treevalue[i], treeweight[i]))
                    #outtreeweight.close()
                    for syst in systematic_list:
                        syst_mod_up = "/("+syst[1]+")*("+syst[2]+")"
                        syst_mod_down = "/("+syst[1]+")*("+syst[3]+")"
                        syst_factor = syst[1]
                        syst_name = syst[0]
                        print "Plotting " + syst_name + ", upper case"
                        tree.Draw(propName+">>+"+"hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName+"_"+syst_name+"_up", rule_cache+syst_mod_up, "goff")
                        #print collection_histograms[propName][weightName][preselName+"_"+syst_factor+"_up"]
                        #collection_histograms[propName][weightName][preselName+"_"+syst_factor+"_up"].Draw()
                        #pyr.gROOT.ls()
                        #raw_input()
                        print "Plotting " + syst_name + ", lower case"
                        tree.Draw(propName+">>+"+"hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName+"_"+syst_name+"_down", rule_cache+syst_mod_down, "goff")
                        #print collection_histograms[propName][weightName][preselName+"_"+syst_factor+"_down"]
                        #collection_histograms[propName][weightName][preselName+"_"+syst_factor+"_down"].Draw()
                        #raw_input()
#         count = 1
#         for event in tree:
#             print "\rProcessing event " + str(count),
#             count += 1
#             passForcing = True
#             if mcfilename in forced_preselection_list.keys():
#                 for key, op, value in forced_preselection_list[mcfilename]:
#                     #if op == "==":    passForcing = passForcing and getattr(event, key) == value
#                     #elif op == "!=":  passForcing = passForcing and getattr(event, key) != value
#                     #elif op == ">":   passForcing = passForcing and getattr(event, key) > value
#                     #elif op == "<":   passForcing = passForcing and getattr(event, key) < value
#                     #elif op == ">=":  passForcing = passForcing and getattr(event, key) >= value
#                     #elif op == "<=":  passForcing = passForcing and getattr(event, key) <= value
#                     #elif op == "a==": passForcing = passForcing and abs(getattr(event, key)) == value
#                     #elif op == "a!=": passForcing = passForcing and abs(getattr(event, key)) != value
#                     #elif op == "a>=": passForcing = passForcing and abs(getattr(event, key)) >= value
#                     #elif op == "a<=": passForcing = passForcing and abs(getattr(event, key)) <= value
#                     #elif op == "a>":  passForcing = passForcing and abs(getattr(event, key)) > value
#                     #elif op == "a<":  passForcing = passForcing and abs(getattr(event, key)) < value
#                     passForcing = passForcing and checkOp(event, key, op, value)
#             if passForcing:
#                 for preselName, preselRules in preselection_list:
#                     fillThis = True
#                     for key, op, value in preselRules:
#                         #if op == "==":    fillThis = fillThis and getattr(event, key) == value
#                         #elif op == "!=":  fillThis = fillThis and getattr(event, key) != value
#                         #elif op == ">":   fillThis = fillThis and getattr(event, key) > value
#                         #elif op == "<":   fillThis = fillThis and getattr(event, key) < value
#                         #elif op == ">=":  fillThis = fillThis and getattr(event, key) >= value
#                         #elif op == "<=":  fillThis = fillThis and getattr(event, key) <= value
#                         #elif op == "a==": fillThis = fillThis and abs(getattr(event, key)) == value
#                         #elif op == "a!=": fillThis = fillThis and abs(getattr(event, key)) != value
#                         #elif op == "a>=": fillThis = fillThis and abs(getattr(event, key)) >= value
#                         #elif op == "a<=": fillThis = fillThis and abs(getattr(event, key)) <= value
#                         #elif op == "a>":  fillThis = fillThis and abs(getattr(event, key)) > value
#                         #elif op == "a<":  fillThis = fillThis and abs(getattr(event, key)) < value
#                         fillThis = fillThis and checkOp(event, key, op, value)
#                     if fillThis:
#                         for prop in plotprops_list:
#                             propName = prop[0]
#                             eventweight = 1.
#                             for weightName, weightNumerator, weightDenominator in weighting_scheme:
#                                 for n in weightNumerator:
#                                     eventweight *= getattr(event, n)
#                                 for d in weightDenominator:
#                                     if getattr(event, d) != 0: eventweight = eventweight / getattr(event, d)
#                                 collection_histograms[propName][weightName].Fill(getattr(event, propName), preselName, eventweight * targetLumi * xsect / bookEvents)
        endTime = time.time()
        print "\rCompleted in {:.2f} seconds. ({:.2f} events/second)".format(endTime-startTime, tree.GetEntries()/(endTime-startTime))

    for presel, preselNum in zip(preselection_list, range(1, len(preselection_list)+1)):
        preselName = presel[0]
        outfile_mc.cd(preselName)
        for prop in plotprops_list:
            propName = prop[0]
            for weightName, weightRule in weighting_scheme:
                hist = collection_histograms[propName][weightName][preselName].Clone()
                hist.Write()
                for syst in systematic_list:
                    syst_name = syst[0]
                    hist = collection_histograms[propName][weightName][preselName+"_"+syst_name+"_up"].Clone()
                    hist.Write()
                    hist = collection_histograms[propName][weightName][preselName+"_"+syst_name+"_down"].Clone()
                    hist.Write()
#     outfile_mc.cd()
#     for prop in plotprops_list:
#         for weight in weighting_scheme:
#             propName = prop[0]
#             weightName = weight[0]
#             collection_histograms[propName][weightName][preselName].Write()
    outfile_mc.Close()