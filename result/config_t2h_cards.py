# Configuration file for tree2hists
# Created Nov 13, 2016.
try:
    ## the normal way to import from rootplot
    from rootplot.tree2hists import RootTree, Plot
except ImportError:
    ## special import for CMSSW installations of rootplot
    from PhysicsTools.PythonAnalysis.rootplot.tree2hists import RootTree, Plot
from array import array      # to allow making Float_t arrays for ROOT hists
from math import pi
from ROOT import TH1F, TH2F  # import other kinds of hists as neeeded
import sys

inputfile=str(sys.argv[2])
output_filename=str(sys.argv[3])
tree_name=str(sys.argv[4])
scalefactor=float(sys.argv[5])
systematic=str(sys.argv[6])
target=str(sys.argv[7])

print 'Using input file: ' + inputfile
print 'Output file: ' + inputfile
print 'Systematic source: ' + systematic
print 'Target variable: ' + target

trigger_cuts = ''
if 'Mu' in tree_name:
        trigger_cuts = "((HLT_IsoMu24==1||HLT_IsoTkMu24==1)  && met > 50 && fabs(LeptonEta)<2.1 )"
        #trigger_cuts = "(HLT_PFHT400_SixJet30_DoubleBTagCSV_p056==1)"
        #trigger_cuts = "(HLT_Mu15_IsoVVVL_BTagCSV_p067_PFHT400==1)"
elif 'El' in tree_name:
        trigger_cuts = "((HLT_Ele32_eta2p1_WPTight_Gsf==1) &&  met > 50 && HT > 450 && fabs(LeptonEta)<=2.1 )"
        #trigger_cuts = "(HLT_PFHT400_SixJet30_DoubleBTagCSV_p056==1)"
        #trigger_cuts = "(HLT_Ele15_IsoVVVL_PFHT350_PFMET50==1)"

list_of_files = [RootTree(str(tree_name), fileName=inputfile, scale=scalefactor, cuts="")]

cut_for_all_files = ""

# All plots are made for each "cut set".
# A "cut set" is 3 things: folder name to store hists in, string to add to hist titles, and cuts for these hists.
# Let cut_sets = [] to make all plots.

cut_sets = []
if 'PU' in systematic:
    from cards_syst_PU import cut_PU
    cut_sets = cut_PU('&&'+trigger_cuts)
elif 'PT' in systematic:
    from cards_syst_PT import cut_PT
    cut_sets = cut_PT('&&'+trigger_cuts)  
elif 'BTAG' in systematic:
    from cards_syst_BTAG import cut_BTAG
    cut_sets = cut_BTAG('&&'+trigger_cuts)  
elif 'BJCOR' in systematic:
    from cards_syst_BTAG_JES import cut_BTAG_JES
    cut_sets = cut_BTAG_JES(systematic, '&&'+trigger_cuts)  
elif 'JE' in systematic:
    from cards_syst_JEC import getJECCutSets
    cut_sets = getJECCutSets(systematic, '&&'+trigger_cuts)
elif 'MEScale' in systematic:
    from cards_syst_ME import getMECutSets
    cut_sets = getMECutSets(systematic, '&&'+trigger_cuts)
elif 'PDF' in systematic:
    from cards_syst_PDF import getPDFCutSets
    cut_sets = getPDFCutSets(systematic, '&&'+trigger_cuts)
elif 'HDAMP' in systematic and 'ALT' not in systematic:
    from cards_syst_HDAMP import getHDAMPCutSets
    cut_sets = getHDAMPCutSets(systematic, '&&'+trigger_cuts)
elif 'HDAMPALT' in systematic:
    from cards_syst_HDAMP_alt import getHDAMPAltCutSets
    cut_sets = getHDAMPCutSets(systematic, '&&'+trigger_cuts)
elif 'ISR' in systematic:
    from cards_syst_IFSRUE import getIFSRUECutSets
    cut_sets = getIFSRUECutSets(systematic, '&&'+trigger_cuts)
elif 'FSR' in systematic:
    from cards_syst_IFSRUE import getIFSRUECutSets
    cut_sets = getIFSRUECutSets(systematic, '&&'+trigger_cuts)
elif 'UE' in systematic:
    from cards_syst_IFSRUE import getIFSRUECutSets
    cut_sets = getIFSRUECutSets(systematic, '&&'+trigger_cuts)
elif 'heavyFlav' in systematic:
    from cards_syst_TTX import getTTXCutSets
    cut_sets = getTTXCutSets(systematic, '&&'+trigger_cuts)
#    (weight7"barrel15to20", "(|#eta|<1.45weight7, 15<E_{T}<20)", "et>15&&et<20&&abs(eta)<1.45"),
#    ("barrel20to30", "(|#eta|<1.45, 20<E_{T}<30)", "et>20&&et<30&&abs(eta)<1.45"),
#    ("endcap15to20", "(1.7<|#eta|<2.5, 15<E_{T}<20)", "et>15&&et<20&&abs(eta)>1.7&&abs(eta)<2.5"),
#    ("endcap20to30", "(1.7<|#eta|<2.5, 20<E_{T}<30)", "et>20&&et<30&&abs(eta)>1.7&&abs(eta)<2.5")


# Define histograms to plot
bins_et     = array("f", [15.0, 20.0, 30.0, 50.0, 80.0, 120.0]) # example custom bins
from listofplots_cards import targetvar
list_of_plots = [targetvar(target)]
