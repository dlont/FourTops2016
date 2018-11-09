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
import re
pyr.gErrorIgnoreLevel = 0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
    def __init__(self, name, proc, file_up=None, file_down=None, tree_up=None, tree_down=None,xsect_up=-1.,xsect_down=-1.):
        Systematic.__init__(self, name)
        self.syst_mod_up = ""
        self.syst_mod_down = ""
        self.proc = proc
        self.file_up = file_up
        self.tree_up = tree_up
        self.file_down = file_down
        self.tree_down = tree_down
        self.xsect_up = xsect_up
        self.xsect_down = xsect_down
        self.weight_up = 1.
        self.weight_down = 1.
        pass
        
    def get_up_histogram_for_ObservableTH1DFromTree(self,observable):
        syst_hist_name = observable.hist.GetName()
        print "Doing systematics(get_up_histogram_for_ObservableTH1DFromTree): ", syst_hist_name
        #fill observable.hist by name
        if self.tree_up != None:
            if self.proc in syst_hist_name:
                # print self.tree_up
                rule_with_tree_up_eqLumiWeight = observable.extended_rule_including_modifier(observable.get_rule_including_weight(),'*({})'.format(self.weight_up))
                rule_with_tree_up_eqLumiWeight += self.syst_mod_up
                print self.proc, observable.tree_var+">>"+syst_hist_name, rule_with_tree_up_eqLumiWeight
                self.tree_up.Draw(observable.tree_var+">>"+syst_hist_name, rule_with_tree_up_eqLumiWeight, "goff")
            else:
                #observable.get_histogram()
                pass
        else: raise RuntimeError("Tree up is not specified in systematics: {}".format(syst_hist_name))
        pass
    def get_down_histogram_for_ObservableTH1DFromTree(self,observable):
        syst_hist_name = observable.hist.GetName()
        print "Doing systematics(get_down_histogram_for_ObservableTH1DFromTree): ", syst_hist_name
        #fill observable.hist by name
        if self.tree_down != None:
            if self.proc in syst_hist_name:
                # print self.tree_down
                rule_with_tree_down_eqLumiWeight = observable.extended_rule_including_modifier(observable.get_rule_including_weight(),'*({})'.format(self.weight_down))
                rule_with_tree_down_eqLumiWeight += self.syst_mod_down
                print self.proc, observable.tree_var+">>"+syst_hist_name, rule_with_tree_down_eqLumiWeight
                self.tree_down.Draw(observable.tree_var+">>"+syst_hist_name, rule_with_tree_down_eqLumiWeight, "goff")
            else:
                #observable.get_histogram()
                pass
        else: raise RuntimeError("Tree up is not specified in systematics: {}".format(syst_hist_name))
        pass
        # Calculation of systematics for composite object
    def get_up_histogram_for_ObservableTH1WeightedSum(self,observable):
        print "Doing systematics(get_up_histogram_for_ObservableTH1WeightedSum): ", observable.name
        observable.fill_hist()
        pass
    def get_down_histogram_for_ObservableTH1WeightedSum(self,observable):
        print "Doing systematics(get_down_histogram_for_ObservableTH1WeightedSum): ", observable.name
        observable.fill_hist()
        pass

class WeightProcCatSystematic(Systematic):
    def  __init__(self, name, proc_cut, central, upper, lower):
        Systematic.__init__(self, name)
        process_and_cut = proc_cut.split(":")
        process = process_and_cut[0]
        cut = process_and_cut[1]
        self.proc = process
        self.syst_mod_up = "/("+central+")*("+"{}?{}:1.0".format(cut,upper)+")"
        self.syst_mod_down = "/("+central+")*("+"{}?{}:1.0".format(cut,lower)+")"
        pass

    def get_up_histogram_for_ObservableTH1DFromTree(self,observable):
        syst_hist_name = observable.hist.GetName()
        if self.proc in syst_hist_name:
            print "Doing systematics(WeightProcCatSystematic:get_up_histogram_for_ObservableTH1DFromTree): ", syst_hist_name
            #fill observable.hist by name
            rule_including_weight_and_sysup = observable.extended_rule_including_modifier(observable.get_rule_including_weight(),self.syst_mod_up)
            observable.tree.Draw(observable.tree_var+">>"+syst_hist_name, rule_including_weight_and_sysup, "goff")
        else:
            pass
        observable.hist_ready=True
    def get_down_histogram_for_ObservableTH1DFromTree(self,observable):
        syst_hist_name = observable.hist.GetName()
        if self.proc in syst_hist_name:
            print "Doing systematics(WeightProcCatSystematic:get_down_histogram_for_ObservableTH1DFromTree): ", syst_hist_name
            #fill observable.hist by name
            rule_including_weight_and_sysdw = observable.extended_rule_including_modifier(observable.get_rule_including_weight(),self.syst_mod_down)
            observable.tree.Draw(observable.tree_var+">>"+syst_hist_name, rule_including_weight_and_sysdw, "goff")
        else:
            pass
        observable.hist_ready=True
        pass
        # Calculation of systematics for composite object
    def get_up_histogram_for_ObservableTH1WeightedSum(self,observable):
        print "Doing systematics(WeightProcCatSystematic:get_up_histogram_for_ObservableTH1WeightedSum): ", observable.name
        observable.fill_hist()
    def get_down_histogram_for_ObservableTH1WeightedSum(self,observable):
        print "Doing systematics(WeightProcCatSystematic:get_down_histogram_for_ObservableTH1WeightedSum): ", observable.name
        observable.fill_hist()
        
class WeightSystematic(Systematic):
    def __init__(self, name, central, upper, lower):
        Systematic.__init__(self, name)
        self.syst_mod_up = "/("+central+")*("+upper+")"
        self.syst_mod_down = "/("+central+")*("+lower+")"
        pass

    def get_up_histogram_for_ObservableTH1DFromTree(self,observable):
        syst_hist_name = observable.hist.GetName()
        print "Doing systematics(WeightSystematic:get_up_histogram_for_ObservableTH1DFromTree): ", syst_hist_name
        #fill observable.hist by name
        rule_including_weight_and_sysup = observable.extended_rule_including_modifier(observable.get_rule_including_weight(),self.syst_mod_up)
        observable.tree.Draw(observable.tree_var+">>"+syst_hist_name, rule_including_weight_and_sysup, "goff")
        observable.hist_ready=True
        pass
    def get_down_histogram_for_ObservableTH1DFromTree(self,observable):
        syst_hist_name = observable.hist.GetName()
        print "Doing systematics(WeightSystematic:get_up_histogram_for_ObservableTH1DFromTree): ", syst_hist_name
        #fill observable.hist by name
        rule_including_weight_and_sysdw = observable.extended_rule_including_modifier(observable.get_rule_including_weight(),self.syst_mod_down)
        observable.tree.Draw(observable.tree_var+">>"+syst_hist_name, rule_including_weight_and_sysdw, "goff")
        observable.hist_ready=True
        pass
        # Calculation of systematics for composite object
    def get_up_histogram_for_ObservableTH1WeightedSum(self,observable):
        print "Doing systematics(WeightSystematic:get_up_histogram_for_ObservableTH1WeightedSum): ", observable.name
        observable.fill_hist()
    def get_down_histogram_for_ObservableTH1WeightedSum(self,observable):
        print "Doing systematics(WeightSystematic:get_down_histogram_for_ObservableTH1WeightedSum): ", observable.name
        observable.fill_hist()

class WeightSystematicShapeOnly(WeightSystematic):
    def __init__(self, name, central, upper, lower):
        WeightSystematic.__init__(self, name, central, upper, lower)  
        self.normalization_histogram = None  

    def set_central_histogram_for_normalization(self, hist):
        self.normalization_histogram = hist

    def get_up_histogram_for_ObservableTH1DFromTree(self,observable):
        syst_hist_name = observable.hist.GetName()
        print "Doing systematics: ", syst_hist_name
        #fill observable.hist by name
        rule_including_weight_and_sysup = observable.extended_rule_including_modifier(observable.get_rule_including_weight(),self.syst_mod_up)
        observable.tree.Draw(observable.tree_var+">>"+syst_hist_name, rule_including_weight_and_sysup, "goff")
        pass
    def get_down_histogram_for_ObservableTH1DFromTree(self,observable):
        syst_hist_name = observable.hist.GetName()
        print "Doing systematics: ", syst_hist_name
        #fill observable.hist by name
        rule_including_weight_and_sysdw = observable.extended_rule_including_modifier(observable.get_rule_including_weight(),self.syst_mod_down)
        observable.tree.Draw(observable.tree_var+">>"+syst_hist_name, rule_including_weight_and_sysdw, "goff")
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
    def __init__(self,name,hist,tree=None,tree_var=None,rule=None,weight=1.):
        Observable.__init__(self,name)
        self.hist = hist
        self.hist.SetDirectory(pyr.gROOT)
        pyr.SetOwnership(self.hist,False)
        self.hist.Sumw2()
        self.tree = tree
        self.tree_var = tree_var
        self.rule = rule
        self.weight = weight
        self.hist_ready = False

    @classmethod
    def fromuniform(cls,name,propNBins,propLowerBound,propHigherBound,tree=None,tree_var=None,rule=None,weight=1.):
        hist = pyr.TH1D(name, "", propNBins, propLowerBound, propHigherBound)
        return cls(name,hist,tree,tree_var,rule,weight)

    @classmethod
    def fromhisttemplate(cls,hist_template,tree=None,tree_var=None,rule=None,weight=1.)
        hist = hist_template.Clone(name)
        return cls(name,hist,tree,tree_var,rule,weight)        

    def fromnonuniform(cls,name,propNBins,binEdgeList,tree=None,tree_var=None,rule=None,weight=1.):
        hist = pyr.TH1D(name, "", propNBins, binEdgeList)
        return cls(name,hist,tree,tree_var,rule,weight)
    
    def apply_syst(self,syst,direction='up'):
        if direction=='up':
            syst.get_up_histogram_for_ObservableTH1DFromTree(self)
        elif direction=='down':
            syst.get_down_histogram_for_ObservableTH1DFromTree(self)
        self.hist_ready = True
        pass
    
    def extended_rule_including_modifier(self, rule, modifier):
        return rule+modifier

    def get_rule_including_weight(self):
        return self.extended_rule_including_modifier(self.rule, "*(" + str(self.weight) + ')')

    def fill_hist(self):
        if not self.hist_ready:
            rule_including_weight = self.get_rule_including_weight()
            self.tree.Draw(self.tree_var+">>"+self.name, rule_including_weight, "goff")
            print "Filling histogram! (ObservableTH1DFromTree:fill_hist) ", self.name
            # self.hist.Print()
            self.hist_ready = True
    def get_histogram(self):
        if not self.hist_ready: self.fill_hist()
        return self.hist


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
    lowbound = 6.5
    highbound = 10.5
    binning_scheme = line.split()[2]
    print binning_scheme
    if 'uniform' in binning_scheme:
        pattern = re.compile("\(.+\)")
        obsrange = pattern.findall(binning_scheme)[0]
        lowbound = float(obsrange.split(',')[0][1:])
        highbound = float(obsrange.split(',')[1][0:-1])
    propdesc = " ".join(line.split()[3:])
    plotprops_list.append((propname, nbins, lowbound, highbound, propdesc))

print delimiter
print "Properties to be plotted"
print plotprops_list
# sys.exit(1)
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
            elif sys_type.lower() == 'weightproccat':
                proc_cut    = columns_entries[2]
                central = columns_entries[3]
                upper = columns_entries[4]
                lower = columns_entries[5]
                systematic_list.append(WeightProcCatSystematic(name, proc_cut, central, upper, lower))
            elif sys_type.lower() == 'samples':
                proc    = columns_entries[2]
                central = columns_entries[3]
                file_tree_weight_str = columns_entries[4].split(":")
                craneen_up = pyr.TFile.Open(file_tree_weight_str[0],"READ")
                tree_up = getattr(craneen_up, file_tree_weight_str[1])
                xsect_up = float(file_tree_weight_str[2])

                file_tree_weight_str = columns_entries[5].split(":")
                craneen_down = pyr.TFile.Open(file_tree_weight_str[0],"READ")
                tree_down = getattr(craneen_down, file_tree_weight_str[1])
                xsect_down = float(file_tree_weight_str[2])
                systematic_list.append(TreeSystematic(name, proc, file_up=craneen_up, file_down=craneen_down, tree_up=tree_up, tree_down=tree_down, 
                                                                xsect_up=xsect_up, xsect_down=xsect_down))

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
                    obs = ObservableTH1DFromTree.fromuniform(obs_name, propNBins, propLowerBound, propHigherBound,
                                                   tree=tree, tree_var=propName, rule=rule_cache)
                    print "***"*10              # I have to keep this because data is 
                    obs.get_histogram().Print() # not filled when it is absent
                    print "***"*10
                    collection_histograms[propName][weightName][preselName].observables_and_weights.append((obs,1.0))

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
                    presel_histograms[preselName+"_"+syst.name+"_up"] = ObservableTH1WeightedSum(obs_name+'_'+syst.name+"_up")
                    presel_histograms[preselName+"_"+syst.name+"_down"] = ObservableTH1WeightedSum(obs_name+'_'+syst.name+"_down")
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
                    rule_cache = '(' + rule_cache + ")*(" + weightRule + ")"
                    eqLumi = targetLumi*xsect/bookEvents
                    print "Plotting normal histograms"

                    obs_name = "hist_"+mcfilename.split('/')[-1]+'_'+mcset+"_"+propName+"_"+weightName+"_"+preselName
                    obs = ObservableTH1DFromTree.fromuniform(obs_name, propNBins, propLowerBound, propHigherBound,
                                                   tree=tree, tree_var=propName, rule=rule_cache, weight=eqLumi)
                    print "***"*10              # I have to keep this printout otherwise data is not filled
                    obs.get_histogram().Print() # this is not normal and has to be fixed
                    print "***"*10              # sad
                    collection_histograms[propName][weightName][preselName].observables_and_weights.append((obs,1.0))

                    print "Central histogram: ", "hist_"+mcset+"_"+propName+"_"+weightName+"_"+preselName
                    print propName+">>+"+"hist_"+mcfilename.split('/')[-1]+'_'+mcset+"_"+propName+"_"+weightName+"_"+preselName
                    print rule_cache
                    #treeweight = tree.GetW()
                    #treevalue = tree.GetV1()
                    #outtreeweight = open(save_dir+"/weights_"+mcset+"_"+propName+"_"+weightName+"_"+preselName+".txt", "w")
                    #for i in range(tree.GetSelectedRows()):
                    #    outtreeweight.write("{}{:20.9f}{:20.9f}\n".format(i, treevalue[i], treeweight[i]))
                    #outtreeweight.close()
                    for syst in systematic_list:
                        #Up component
                        obs_name = "hist_"+mcfilename.split('/')[-1]+'_'+mcset+"_"+propName+"_"+weightName+"_"+preselName+'_'+syst.name+"_up"
                        obs_up = None
                        if isinstance(syst,TreeSystematic):
                            bookEventsSyst=syst.file_up.Get("bookkeeping").GetEntries()
                            eqLumi = targetLumi*syst.xsect_up/bookEventsSyst
                            obs_up = ObservableTH1DFromTree.fromuniform(obs_name, propNBins, propLowerBound, propHigherBound,
                                                   tree=None, tree_var=propName, rule=rule_cache, weight=eqLumi)
                        else:
                            obs_up = ObservableTH1DFromTree.fromuniform(obs_name, propNBins, propLowerBound, propHigherBound,
                                                   tree=tree, tree_var=propName, rule=rule_cache, weight=eqLumi)
                        obs_up.apply_syst(syst,direction='up')
                        obs_up.get_histogram().Print()
                        collection_histograms[propName][weightName][preselName+"_"+syst.name+"_up"].observables_and_weights.append((obs_up,1.0))
                        #Down component
                        obs_name = "hist_"+mcfilename.split('/')[-1]+'_'+mcset+"_"+propName+"_"+weightName+"_"+preselName+'_'+syst.name+"_down"
                        obs_down = None
                        if isinstance(syst,TreeSystematic):
                            bookEventsSyst=syst.file_down.Get("bookkeeping").GetEntries()
                            eqLumi = targetLumi*syst.xsect_down/bookEventsSyst
                            obs_down = ObservableTH1DFromTree.fromuniform(obs_name, propNBins, propLowerBound, propHigherBound,
                                                   tree=None, tree_var=propName, rule=rule_cache, weight=eqLumi)
                        else: 
                            obs_down = ObservableTH1DFromTree.fromuniform(obs_name, propNBins, propLowerBound, propHigherBound,
                                                   tree=tree, tree_var=propName, rule=rule_cache, weight=eqLumi)
                        obs_down.apply_syst(syst,direction='down')
                        obs_down.get_histogram().Print()
                        collection_histograms[propName][weightName][preselName+"_"+syst.name+"_down"].observables_and_weights.append((obs_down,1.0))

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
                    if isinstance(syst,WeightSystematicShapeOnly): 
                        syst.set_central_histogram_for_normalization(collection_histograms[propName][weightName][preselName].get_histogram())
                    obs_up = collection_histograms[propName][weightName][preselName+"_"+syst_name+"_up"]
                    obs_up.apply_syst(syst,direction='up')
                    hist = collection_histograms[propName][weightName][preselName+"_"+syst_name+"_up"].get_histogram().Clone()
                    hist.Write()

                    obs_down = collection_histograms[propName][weightName][preselName+"_"+syst_name+"_down"]
                    obs_down.apply_syst(syst,direction='down')
                    hist = collection_histograms[propName][weightName][preselName+"_"+syst_name+"_down"].get_histogram().Clone()
                    hist.Write()

    outfile_mc.Close()