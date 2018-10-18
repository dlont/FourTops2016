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
import sys
pyr.gErrorIgnoreLevel = 0

class Systematic:
    def __init__(self,name):
        self.name = name
        self.rule = None
        pass
    def set_propName(self,propName):
        self.propName = propName
    def set_rule(self,rule):
        self.rule = rule
    def get_baseline_name(self,hist_name):
        return hist_name+"_"+self.name
    def get_up_histogram(self):
        pass
    def get_down_histogram(self):
        pass


class TreeSystematic(Systematic):
    def __init__(self, name, proc, tree_up=None, tree_down=None):
        Systematic.__init__(self, name)
        self.syst_mod_up = ""
        self.syst_mod_down = ""
        self.proc = proc
        self.tree_up = tree_up
        self.tree_down = tree_down
        pass
    def get_up_histogram_for_ObservableTH1DFromTree(self,observable):
        syst_hist_name = observable.hist.GetName()
        print "Doing systematics: ", syst_hist_name
        #fill observable.hist by name
        if self.tree_up != None:
            # print self.proc, observable.tree_var+">>"+syst_hist_name, observable.rule+self.syst_mod_up
            if self.proc in syst_hist_name:
                # print self.tree_up
                self.tree_up.Draw(observable.tree_var+">>"+syst_hist_name, observable.rule+self.syst_mod_up, "goff")
            else:
                #observable.get_histogram()
                pass
        else: raise RuntimeError("Tree up is not specified in systematics: {}".format(syst_hist_name))
        pass
    def get_down_histogram_for_ObservableTH1DFromTree(self,observable):
        syst_hist_name = observable.hist.GetName()
        print "Doing systematics: ", syst_hist_name
        #fill observable.hist by name
        if self.tree_down != None:
            # print self.proc, observable.tree_var+">>"+syst_hist_name, observable.rule+self.syst_mod_down
            if self.proc in syst_hist_name:
                # print self.tree_down
                self.tree_down.Draw(observable.tree_var+">>"+syst_hist_name, observable.rule+self.syst_mod_down, "goff")
            else:
                #observable.get_histogram()
                pass
        else: raise RuntimeError("Tree up is not specified in systematics: {}".format(syst_hist_name))
        pass
        # Calculation of systematics for composite object
    def get_up_histogram_for_ObservableTH1WeightedSum(self,observable):
        print "Doing systematics: ", observable.name
        observable.fill_hist()
    def get_down_histogram_for_ObservableTH1WeightedSum(self,observable):
        print "Doing systematics: ", observable.name
        observable.fill_hist()

class WeightSystematic(Systematic):
    def __init__(self, name, central, upper, lower):
        Systematic.__init__(self, name)
        self.syst_mod_up = "/("+central+")*("+upper+")"
        self.syst_mod_down = "/("+central+")*("+lower+")"
        pass

    def get_up_histogram_for_ObservableTH1DFromTree(self,observable):
        syst_hist_name = observable.hist.GetName()
        print "Doing systematics: ", syst_hist_name
        #fill observable.hist by name
        observable.tree.Draw(observable.tree_var+">>"+syst_hist_name, observable.rule+self.syst_mod_up, "goff")
        pass
    def get_down_histogram_for_ObservableTH1DFromTree(self,observable):
        syst_hist_name = observable.hist.GetName()
        print "Doing systematics: ", syst_hist_name
        #fill observable.hist by name
        observable.tree.Draw(observable.tree_var+">>"+syst_hist_name, observable.rule+self.syst_mod_down, "goff")
        pass
        # Calculation of systematics for composite object
    def get_up_histogram_for_ObservableTH1WeightedSum(self,observable):
        print "Doing systematics: ", observable.name
        observable.fill_hist()
    def get_down_histogram_for_ObservableTH1WeightedSum(self,observable):
        print "Doing systematics: ", observable.name
        observable.fill_hist()

class WeightSystematicShapeOnly(WeightSystematic):
    def __init__(self, name, central, upper, lower):
        WeightSystematic.__init__(self, name, central, upper, lower)  
        self.normalization_histogram = None  
    # def get_up_histogram(self,hist_name):
    #     WeightSystematic.get_up_histogram(self,hist_name)
    #     syst_hist_name = self.get_baseline_name(hist_name)+"_up"
    #     hist = pyr.gDirectory.Get(syst_hist_name)
    #     hist_central = pyr.gROOT.Get(hist_name)
    #     # print "Looking for central histogram: ", hist_name
    #     if hist_central != None:
    #         # print hist, hist_central
    #         # hist_central.Print()
    #         numerator   = hist.Integral()
    #         denominator = hist_central.Integral()
    #         if denominator>0: hist.Scale(numerator/denominator)
    #     else: 
    #         raise RuntimeError('Cannot retrieve central histogram for systematics rescaling: {}'.format(hist_name))
    #     pass
    # def get_down_histogram(self,hist_name):
    #     WeightSystematic.get_up_histogram(self,hist_name)
    #     syst_hist_name = self.get_baseline_name(hist_name)+"_down"
    #     hist = pyr.gDirectory.Get(syst_hist_name)
    #     hist_central = pyr.gROOT.Get(hist_name)
    #     # print "Looking for central histogram: ", hist_name
    #     if hist_central != None:
    #         # print hist, hist_central
    #         # hist_central.Print()
    #         numerator   = hist.Integral()
    #         denominator = hist_central.Integral()
    #         if denominator>0: hist.Scale(numerator/denominator)
    #     else: 
    #         raise RuntimeError('Cannot retrieve central histogram for systematics rescaling: {}'.format(hist_name))
    #     pass

    def set_central_histogram_for_normalization(self, hist):
        self.normalization_histogram = hist

    def get_up_histogram_for_ObservableTH1DFromTree(self,observable):
        syst_hist_name = observable.hist.GetName()
        print "Doing systematics: ", syst_hist_name
        #fill observable.hist by name
        observable.tree.Draw(observable.tree_var+">>"+syst_hist_name, observable.rule+self.syst_mod_up, "goff")
        pass
    def get_down_histogram_for_ObservableTH1DFromTree(self,observable):
        syst_hist_name = observable.hist.GetName()
        print "Doing systematics: ", syst_hist_name
        #fill observable.hist by name
        observable.tree.Draw(observable.tree_var+">>"+syst_hist_name, observable.rule+self.syst_mod_down, "goff")
        pass

    # Calculation of systematics for composite object
    def get_up_histogram_for_ObservableTH1WeightedSum(self,observable):
        syst_hist_name = observable.name
        print "Doing systematics: ", syst_hist_name
        observable.fill_hist()
        if self.normalization_histogram.Integral() > 0: 
            observable.hist.Scale(self.normalization_histogram.Integral()/observable.hist.Integral())
        pass
    def get_down_histogram_for_ObservableTH1WeightedSum(self,observable):
        syst_hist_name = observable.name
        print "Doing systematics: ", syst_hist_name
        observable.fill_hist()
        if self.normalization_histogram.Integral() > 0: 
            observable.hist.Scale(self.normalization_histogram.Integral()/observable.hist.Integral())
        pass

class Observable:
    def __init__(self,name,hist=None):
        self.name = name
        self.units = None
        self.entry_units = None
        self.hist = hist
        pass

    def apply_syst(self,syst):
        pass

    def get_histogram(self):
        return self.hist
        pass

class ObservableTH1DFromTree(Observable):
    def __init__(self,name,propNBins,propLowerBound,propHigherBound,tree=None,tree_var=None,rule=None):
        Observable.__init__(self,name)
        self.hist = pyr.TH1D(name, "", propNBins, propLowerBound, propHigherBound)
        self.hist.SetDirectory(pyr.gROOT)
        pyr.SetOwnership(self.hist,False)
        self.hist.Sumw2()
        self.tree = tree
        self.tree_var = tree_var
        self.rule = rule
        self.hist_ready = False
    
    def apply_syst(self,syst,direction='up'):
        if direction=='up':
            syst.get_up_histogram_for_ObservableTH1DFromTree(self)
        elif direction=='down':
            syst.get_down_histogram_for_ObservableTH1DFromTree(self)
        self.hist_ready = True
        pass
    
    def fill_hist(self):
        if not self.hist_ready:
            self.tree.Draw(self.tree_var+">>"+self.name, self.rule, "goff")
            # print "Filling histogram! ", self.name
            # self.hist.Print()
            self.hist_ready = True
    def get_histogram(self):
        if not self.hist_ready: self.fill_hist()
        return self.hist

        # hist_central = pyr.gROOT.Get(hist_name)
        # pass

class ObservableTH1WeightedSum(Observable):
    def __init__(self,name):
        Observable.__init__(self,name)
        self.observables_and_weights = []
        self.hist = None
        self.hist_ready = False

    def apply_syst(self,syst,direction='up'):
        if direction=='up':
            syst.get_up_histogram_for_ObservableTH1WeightedSum(self)
        elif direction=='down':
            syst.get_down_histogram_for_ObservableTH1WeightedSum(self)
        self.hist_ready = True
        pass

    def fill_hist(self):
        if not self.hist_ready:
            if len(self.observables_and_weights)>0:
                self.hist = self.observables_and_weights[0][0].get_histogram().Clone(self.name)
                self.hist.SetDirectory(pyr.gROOT)
                pyr.SetOwnership(self.hist,False)
                self.hist.Reset()
                self.hist.Sumw2()
            else: raise RuntimeError('List of observables for weighted sum is empty: {}'.format(self.observables_and_weights))

            for obs, weight in self.observables_and_weights:
                # obs.get_histogram().Print('all')
                self.hist.Add(obs.get_histogram(),weight)

            self.hist_ready = True
    def get_histogram(self):
        if not self.hist_ready:
            self.fill_hist()
            
        return self.hist
        # pass

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


# Disable garbage collection for this list of objects
pyr.TCanvas.__init__._creates = False
pyr.TFile.__init__._creates = False
pyr.TH1.__init__._creates = False
pyr.TH2.__init__._creates = False
pyr.THStack.__init__._creates = False
pyr.TGraph.__init__._creates = False
pyr.TMultiGraph.__init__._creates = False
pyr.TList.__init__._creates = False
pyr.TCollection.__init__._creates = False
pyr.TIter.__init__._creates = False

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
        columns_entries = line.split()
        name = columns_entries[0]
        sys_type = columns_entries[1]
        if '#' not in name: 
            if sys_type.lower() == 'weight':
                central = columns_entries[2]
                upper = columns_entries[3]
                lower = columns_entries[4]
                systematic_list.append(WeightSystematic(name, central, upper, lower))
            elif sys_type.lower() == 'weightshapeonly':
                central = columns_entries[2]
                upper = columns_entries[3]
                lower = columns_entries[4]
                systematic_list.append(WeightSystematicShapeOnly(name, central, upper, lower))
            elif sys_type.lower() == 'samples':
                proc    = columns_entries[2]
                central = columns_entries[3]
                file_tree_weight_str = columns_entries[4].split(":")
                craneen_up = pyr.TFile.Open(file_tree_weight_str[0],"READ")
                tree_up = getattr(craneen_up, file_tree_weight_str[1])

                file_tree_weight_str = columns_entries[5].split(":")
                craneen_down = pyr.TFile.Open(file_tree_weight_str[0],"READ")
                tree_down = getattr(craneen_down, file_tree_weight_str[1])
                systematic_list.append(TreeSystematic(name, proc, tree_up=tree_up, tree_down=tree_down))
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
                obs_name = "hist_Data_"+propName+"_"+weightName+"_"+preselName
                presel_histograms[preselName] = ObservableTH1WeightedSum(obs_name)
                # presel_histograms[preselName] = Observable(obs_name,hist=pyr.TH1D("hist_Data_"+propName+"_"+weightName+"_"+preselName, "", propNBins, propLowerBound, propHigherBound))
                # presel_histograms[preselName].get_histogram().SetDirectory(pyr.gROOT)
            weight_histograms[weightName] = presel_histograms
        collection_histograms[propName] = weight_histograms

    for line in plotlist_Data_list:
        startTime = time.time()
        craneen_file_name = line.split()[0]
        craneen = pyr.TFile(craneen_file_name)
        tree = getattr(craneen, tree_name)
        pyr.SetOwnership(tree,False)
        print "Starting "+line.split()[0]+" with "+str(tree.GetEntries()) + " events"
        pyr.gROOT.cd()
        for preselName, preselRules in preselection_list:
            #print "plotting "+preselName
            for prop in plotprops_list:
                propName = prop[0]
                propNBins = prop[1]
                propLowerBound = prop[2]
                propHigherBound = prop[3]
                #print "plotting "+propName
                for weightName, weightRule in weighting_scheme:
                    #print "plotting "+weightName
                    rule_cache = '(' + preselRules + ')'
                    #rule_cache += "*(" + weightRule +")"
                    obs_name = "hist_"+craneen_file_name.split('/')[-1]+"_Data_"+propName+"_"+weightName+"_"+preselName
                    obs = ObservableTH1DFromTree(obs_name, propNBins, propLowerBound, propHigherBound,
                                                   tree=tree, tree_var=propName, rule=rule_cache)
                    print "***"*10              # I have to keep this because data is 
                    obs.get_histogram().Print() # not filled when it is absent
                    print "***"*10
                    collection_histograms[propName][weightName][preselName].observables_and_weights.append((obs,1.0))
                    # print presel_histograms[preselName].observables_and_weights
                    # tree.Draw(propName+">>+"+"hist_Data_"+propName+"_"+weightName+"_"+preselName, rule_cache, "goff")

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
                hist = collection_histograms[propName][weightName][preselName].get_histogram().Clone()
                hist.Print('all')
                print hist.GetEntries()
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
        mcName = "".join(line.split()[1])
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
                obs_name = "hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName
                presel_histograms[preselName] = ObservableTH1WeightedSum(obs_name)
                for syst in systematic_list:
                    # syst_name = syst.name
                    presel_histograms[preselName+"_"+syst.name+"_up"] = ObservableTH1WeightedSum(obs_name+'_'+syst.name+"_up")
                    # presel_histograms[preselName+"_"+syst.name+"_up"] = Observable(obs_name+'_'+syst.name,hist=pyr.TH1D("hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName+"_"+syst_name+"_up", "", propNBins, propLowerBound, propHigherBound))
                    # presel_histograms[preselName+"_"+syst.name+"_up"].get_histogram().SetDirectory(pyr.gROOT)
                    #print presel_histograms[preselName+"_"+syst_name+"_up"]
                    presel_histograms[preselName+"_"+syst.name+"_down"] = ObservableTH1WeightedSum(obs_name+'_'+syst.name+"_down")
                    # presel_histograms[preselName+"_"+syst.name+"_down"] = Observable(obs_name+'_'+syst.name,hist=pyr.TH1D("hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName+"_"+syst_name+"_down", "", propNBins, propLowerBound, propHigherBound))
                    # presel_histograms[preselName+"_"+syst.name+"_down"].get_histogram().SetDirectory(pyr.gROOT)
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
                propNBins = prop[1]
                propLowerBound = prop[2]
                propHigherBound = prop[3]
                for weightName, weightRule in weighting_scheme:
                    rule_cache = '(' + preselRules + ')'
                    if mcfilename in forced_preselection_list.keys():
                        rule_cache = rule_cache + " && (" + forced_preselection_list[mcfilename] + ')'
                    rule_cache = '(' + rule_cache + ")*(" + weightRule + ")*(" + str(targetLumi*xsect/bookEvents) + ')'
                    print "Plotting normal histograms"

                    obs_name = "hist_"+mcfilename.split('/')[-1]+'_'+mcset+"_"+propName+"_"+weightName+"_"+preselName
                    obs = ObservableTH1DFromTree(obs_name, propNBins, propLowerBound, propHigherBound,
                                                   tree=tree, tree_var=propName, rule=rule_cache)
                    print "***"*10              # I have to keep this printout otherwise data is not filled
                    obs.get_histogram().Print() # this is not normal and has to be fixed
                    print "***"*10              # sad
                    collection_histograms[propName][weightName][preselName].observables_and_weights.append((obs,1.0))

                    # tree.Draw(propName+">>+"+"hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName, rule_cache, "goff")
                    print "Central histogram: ", "hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName
                    #print propName+">>+"+"hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName
                    #print rule_cache
                    #treeweight = tree.GetW()
                    #treevalue = tree.GetV1()
                    #outtreeweight = open(save_dir+"/weights_"+mcset+"_"+propName+"_"+weightName+"_"+preselName+".txt", "w")
                    #for i in range(tree.GetSelectedRows()):
                    #    outtreeweight.write("{}{:20.9f}{:20.9f}\n".format(i, treevalue[i], treeweight[i]))
                    #outtreeweight.close()
                    for syst in systematic_list:
                        #resolve dependencies
                        # if isinstance(syst,WeightSystematic):
                            # syst.set_tree(tree)
                        # else: pass
                        obs_name = "hist_"+mcfilename.split('/')[-1]+'_'+mcset+"_"+propName+"_"+weightName+"_"+preselName+'_'+syst.name+"_up"
                        obs_up = ObservableTH1DFromTree(obs_name, propNBins, propLowerBound, propHigherBound,
                                                   tree=tree, tree_var=propName, rule=rule_cache)
                        obs_up.apply_syst(syst,direction='up')
                        obs_up.get_histogram().Print()
                        collection_histograms[propName][weightName][preselName+"_"+syst.name+"_up"].observables_and_weights.append((obs_up,1.0))
                        obs_name = "hist_"+mcfilename.split('/')[-1]+'_'+mcset+"_"+propName+"_"+weightName+"_"+preselName+'_'+syst.name+"_down"
                        obs_down = ObservableTH1DFromTree(obs_name, propNBins, propLowerBound, propHigherBound,
                                                   tree=tree, tree_var=propName, rule=rule_cache)
                        obs_down.apply_syst(syst,direction='down')
                        obs_down.get_histogram().Print()
                        collection_histograms[propName][weightName][preselName+"_"+syst.name+"_down"].observables_and_weights.append((obs_down,1.0))
                        # syst.set_propName(propName)
                        # syst.set_rule(rule_cache)
                        # hist_name = "hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName
                        # syst.get_down_histogram(hist_name)
                        # syst.get_up_histogram(hist_name)


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
                hist = collection_histograms[propName][weightName][preselName].get_histogram().Clone()
                hist.Write()
                for syst in systematic_list:
                    syst_name = syst.name
                    if isinstance(syst,WeightSystematicShapeOnly): syst.set_central_histogram_for_normalization(collection_histograms[propName][weightName][preselName].get_histogram())
                    obs_up = collection_histograms[propName][weightName][preselName+"_"+syst_name+"_up"]
                    obs_up.apply_syst(syst,direction='up')
                    hist = collection_histograms[propName][weightName][preselName+"_"+syst_name+"_up"].get_histogram().Clone()
                    hist.Write()

                    obs_down = collection_histograms[propName][weightName][preselName+"_"+syst_name+"_down"]
                    obs_down.apply_syst(syst,direction='down')
                    hist = collection_histograms[propName][weightName][preselName+"_"+syst_name+"_down"].get_histogram().Clone()
                    hist.Write()
#     outfile_mc.cd()
#     for prop in plotprops_list:
#         for weight in weighting_scheme:
#             propName = prop[0]
#             weightName = weight[0]
#             collection_histograms[propName][weightName][preselName].Write()
    outfile_mc.Close()