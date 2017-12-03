# Son 06 Nov 2016 16:13:34 CET

```
cd build
cmake -DTopBrussels_SOURCE_DIR=/user/dlontkov/CMSSW_8_0_21/src/TopBrussels -DCMAKE_BUILD_TYPE=Debug -DCMAKE_CXX_FLAGS="-g2" ..
```

**List/count batch jobs without header**

```
qstat -u dlontkov| tail -n+6
qstat -u dlontkov| tail -n+6|wc -l
```
**Remove batch output files in the test folder**
```
rm *.e* *.o*
```


# Mon 07 Nov 2016 01:13:05 CET
**Environment to XML parsing**
```
export|awk '{print $3}'|awk -F'=' '{printf "<variable name=\"%s\" value=%s/>\n", $1,$2}'
```



# Son 13 Nov 2016 21:15:32 CET

## Plotting with rootplot

tree2hist template
```
tree2hist
```
Afterwards modify created configuration file `t2h_config.py`

```
for i in *.py;do  tree2hists $i;done
rootplot -f --data=1 --ratio-split=2 --overflow  -n Hists_data.root Hists_TT.root Hists_TTTT.root
```

## Data sample lumi
https://twiki.cern.ch/twiki/bin/viewauth/CMS/CMSTopBrussels13TeVSamplesBookkeeping

/pnfs/iihe/cms/store/user/fblekman/TopTree/CMSSW_80X_v1-Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON_NoL1T/TTP-CMSSW_80X_v1-Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON_NoL1T--GT-80X_dataRun2_ICHEP16_repro_v0/*/*/*/*/TOPTREE_*.root

Freya's lumi values for repro_v3 (I use repro_v0 so far, that has to be changed)


|Sample|          2016B|           2016C|           2016D|           2016E|           2016F|           2016G|           2016H|           SUM (mb^-1)|
|------|---------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------------|
|**repro_v3**|
|SingleMuon|      5840063059.395|  2523447696.817|  4275320129.305|  3839184008.312|  2898669614.585|  7383952466.412|  8283713045.538| 35044350020.364|
|**repro_v0**|
|SingleMuon|      5208746535.071|  2448756618.041|  4201921158.859|  4049732039.245|  3147822524.876|  7554453625.468|  5476961519.179| 32088394020.739|


## Equivalent lumi for different samples
TTTT (0.0092 pb)
/pnfs/iihe/cms/store/user/fblekman/TopTree/CMSSW_80X_v1/TTP-CMSSW_80X_v1--GT-80X_mcRun2_asymptotic_2016_miniAODv2_v1/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/*/*/*/TOPTREE_*.root

TT (831.76 pb)
/pnfs/iihe/cms/store/user/fblekman/TopTree/CMSSW_80X_v1/TTP-CMSSW_80X_v1--GT-80X_mcRun2_asymptotic_2016_miniAODv2_v1/TT_TuneCUETP8M1_13TeV-powheg-pythia8/*/*/*/TOPTREE_*.root

TT scale (831.76 pb)
/pnfs/iihe/cms/store/user/fblekman/TopTree/CMSSW_80X_v1/TTP-CMSSW_80X_v1--GT-80X_mcRun2_asymptotic_2016_miniAODv2_v1/TT_TuneCUETP8M1_13TeV-powheg-scale*-pythia8/*/*/*/TOPTREE_*.root

['ttttNLO', 989025L, 107502717.39130434]
['TTJets_powheg', 274957326L, 330572.9128594787]
['TTScaledown_powheg', 9942427L, 11953.48057131865]
['TTScaleup_powheg', 9933327L, 11942.5399153602]


## Normalisation factors
___repro_v3___

TT (35044350020.364/330572000000.9128594787=0.01525945942)

___repro_0___

TT (32088394020.739/330572000000.9128594787=0.09706930417775973)

TTTT (32088394020.739/107502717391304.34=0.0002984891433389437)

Control plots with correct normalisation and labels (except for TTTT)
```
rootplot -f --data=3 --logy --overflow --scale=0.09706930417775973,0.0002984891433389437,1 --legend-entries='t#bar{t},t#bar{t}t#bar{t},CMS (33/fb)' Hists_TT.root Hists_TTTT.root Hists_data.root
```

# Mon 14 Nov 2016 01:23:56 CET
```
for i in *_t2h.py;do  tree2hists $i;done
```

Using make
```
make plots
```


# Son 20 Nov 2016 19:41:16 CET
Run with updated Muon trigger (80X) (tag v0.0.1) 

## Merge output

```
source ../../tools/mergeCran4comparison.sh ../Craneens_Mu/Craneens20_11_2016/ ../../tools/listCran
```

Normalisation factors calculated above were incorect because decimal point was incorrectly placed!
330572000000.9128594787 should be  330572912859.4787
Below is proper calculation

**Data lumi**
SingleMuon B+C+D+E+F+G+H

35044350020.364 (mb-1)

SingleElectron B+C+D+E+F+G+H

34045653292.636 (mb-1)

**Normalisation factors MC**

__repro_v3__

TT (35044350020.364/330572912859.4787=0.10601095448876295)

TTTT (35044350020.364/107502717391304.34=0.00032598571339182407)

## Summing numbers in column using AWK

```
grep preTrig submit_TTJets_powheg_*.o*|awk '{print $2}'|awk '{sum += $1} END {print sum}'
```


# Mon 28 Nov 2016 19:35:39 CET

**For debugging with valgrind**

```
GLOG_log_dir="." valgrind --tool=memcheck --show-possibly-lost=no --suppressions=$ROOTSYS/etc/valgrind-root.supp --leak-check=full --log-file=log ./FourTops  TTJets_powheg t\bar{t}+jets_powheg 1 633 0 2 1 330572.9128594787 831.76 0.0 -input_files="/pnfs/iihe/cms/store/user/fblekman/TopTree/CMSSW_80X_v1/TTP-CMSSW_80X_v1--GT-80X_mcRun2_asymptotic_2016_miniAODv2_v1/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_8M113TeVpowhegpythia8RunIISpring16MiniAODv2PUSpring1680XmcRun2asymptotic2016miniAODv2v0ext4v1crab28/161028_095239/0001/TOPTREE_1000.root"   -fourtops_channel="Mu2016"
```

commit: d80cbac5bc4af23af616667e5c4866a848ae137a
These fixes should remove stale file problem when mutliple files produce same output Craneens


# Mon 28 Nov 2016 21:27:18 CET
**Launching with tag v0.0.2**

It was found that several jobs crashed. These jobs corresponded to leftovers from naive arg parsing times. Crashes should be fix after cleaning submit folder.

# Die 29 Nov 2016 01:34:46 CET
**Updated build command**
```
cd build
cmake -DTopBrussels_SOURCE_DIR=/user/dlontkov/CMSSW_8_0_21/src/TopBrussels -DCMAKE_BUILD_TYPE=Debug ..
```

**Merge root output ntuples**
```bash
source ../../../tools/mergeCran4comparison.sh . ../../../tools/listCran
```

---
# Mit 30 Nov 2016 02:07:56 CET
**Updated event numbers for samples from commit 59bfb68** <br>
['ttttNLO', 989025L, 107502717.39130434] <br>
['TTJets_powheg_central', 92925926L, 111722.04241608156] <br>
['TTScaledown_powheg', 9942427L, 11953.48057131865] <br>
['TTScaleup_powheg', 9933327L, 11942.5399153602] <br>
['T_tW', 998400L, 28044.94382022472] <br>
['Tbar_tW', 985000L, 27668.539325842696] <br>
['WJets', 99514498L, 1617.4381237200532] <br>

**FourTops version master - v0.0.3 - 1bacbc7 - 2016-11-29 12:14:24 +0100 - RELEASE**

The content of **output/Craneen*/Craneens30_11_2016** contains the first set of **reference** ntuples produced using 

**Single muon (Craneens_Mu)**
```bash
-rw-r--r-- 1 dlontkov localusers 28864030  1. Dez  02:08 Craneen_Data_Run2_TopTree_Study.root
-rw-r--r-- 1 dlontkov localusers 16839543  1. Dez  02:08 Craneen_ttttNLO_Run2_TopTree_Study.root
-rw-r--r-- 1 dlontkov localusers 77923989  1. Dez  02:08 Craneen_TTJets_powheg_Run2_TopTree_Study.root
-rw-r--r-- 1 dlontkov localusers  9060477  1. Dez  02:08 Craneen_TTScaleup_powheg_Run2_TopTree_Study.root
-rw-r--r-- 1 dlontkov localusers  9280267  1. Dez  02:08 Craneen_TTScaledown_powheg_Run2_TopTree_Study.root
-rw-r--r-- 1 dlontkov localusers   304522  1. Dez  02:08 Craneen_T_tW_Run2_TopTree_Study.root
-rw-r--r-- 1 dlontkov localusers   317211  1. Dez  02:08 Craneen_Tbar_tW_Run2_TopTree_Study.root
-rw-r--r-- 1 dlontkov localusers   798772  1. Dez  02:08 Craneen_WJets_Run2_TopTree_Study.root
```
**Single electron (Craneens_El)**
```bash
-rw-r--r-- 1 dlontkov localusers 17429999  1. Dez  02:16 Craneen_Data_Run2_TopTree_Study.root
-rw-r--r-- 1 dlontkov localusers 11404748  1. Dez  02:16 Craneen_ttttNLO_Run2_TopTree_Study.root
-rw-r--r-- 1 dlontkov localusers 51660245  1. Dez  02:16 Craneen_TTJets_powheg_Run2_TopTree_Study.root
-rw-r--r-- 1 dlontkov localusers  6039905  1. Dez  02:16 Craneen_TTScaleup_powheg_Run2_TopTree_Study.root
-rw-r--r-- 1 dlontkov localusers  6087078  1. Dez  02:16 Craneen_TTScaledown_powheg_Run2_TopTree_Study.root
-rw-r--r-- 1 dlontkov localusers   221246  1. Dez  02:16 Craneen_T_tW_Run2_TopTree_Study.root
-rw-r--r-- 1 dlontkov localusers   236494  1. Dez  02:16 Craneen_Tbar_tW_Run2_TopTree_Study.root
-rw-r--r-- 1 dlontkov localusers   741107  1. Dez  02:16 Craneen_WJets_Run2_TopTree_Study.root
```
---
## Reference ROOT ntuples (tag v0.0.3)
**commit**: `2e6330b34256091af5c3e69e03f1fdd39ca24ff4`
**path**: `test/data/backward/Craneens_*`
---


## List files in sorted order
```
cat submit_TTJets_powheg_central_*|grep RAWAOD|grep -o "TOPTREE_[0-9]*"|sort | uniq -d
```


Mon 05 Dez 2016 03:37:54 CET
Add bookkeeping tree

tag v0.0.4


Fre 09 Dez 2016 04:17:59 CET
plotting
make plots_el INPUTLOCATION=../test/data/backward/Craneens_El/  TREENAME=Craneen__El DATALABEL=Single\ e
make plots_mu INPUTLOCATION=../test/data/backward/Craneens_Mu/  TREENAME=Craneen__Mu DATALABEL=Single\ \#mu



Son 11 Dez 2016 03:02:26 CET
# Testing script
```
root -b -l test/plotComparison.C\(\"./output/Craneens_Mu/Craneens30_11_2016/Craneen_TTJets_powheg_Run2_TopTree_Study.root\"\,\"test/data/backward/Craneens_Mu/Craneen_TTJets_powheg_Run2_TopTree_Study.root\"\,\"Craneen__Mu\"\)
```


Mit 14 Dez 2016 00:36:04 CET
#Pileup reweighting

* Reference page https://twiki.cern.ch/twiki/bin/view/CMSPublic/Step1TagAndProbe

@lxplus
cmsrel CMSSW_7_4_1_patch4
cd CMSSW_7_4_1_patch4/src
cmsenv
git cms-addpkg RecoLuminosity/LumiDB
scram b -j
voms-proxy-init -voms cms
source producePU.zsh


Die 10 Jan 2017 21:23:36 CET
['ttttNLO', 989025L, 107502717.39130434]
['TTJets_powheg_central', 92925926L, 111722.04241608156]
['TTScaledown_powheg', 9942427L, 11675.956219980506]
['TTScaleup_powheg', 9933327L, 12377.052183014355]
['T_tW', 998400L, 28044.94382022472]
['Tbar_tW', 985000L, 27668.539325842696]
['WJets', 99514498L, 1617.4381237200532]


Muon
['Data_Run2016B-ReReco', 153007286L, 153007286.0]
['Data_Run2016C-ReReco', 64528905L, 64528905.0]
['Data_Run2016D-ReReco', 96017782L, 96017782.0]
['Data_Run2016E-ReReco', 0L, 0.0]
['Data_Run2016E-ReReco', 86679163L, 86679163.0]
['Data_Run2016F-ReReco', 65033768L, 65033768.0]
['Data_Run2016G-ReReco', 0L, 0.0]
['Data_Run2016G-ReReco', 147871216L, 147871216.0]
['Data_Run2016H-PromptRecoV2', 4389808L, 4389808.0]
SUM: 617527928L



Don 19 Jan 2017 17:02:08 CET
Summer16 samples
['ttttNLO', 2455937L, 266949673.91304347]
['TTJets_powheg_central', 77337597L, 92980.6638934308]
['TTJets_amcnlo_central', 42593710L, 51209.134846590365]
['TTFSRScaledown_powheg', 29139830L, 35033.9400788689]
['TTFSRScaleup_powheg', 26010154L, 31271.224872559393]
['TTISRScaledown_powheg', 29915304L, 35966.26911609118]
['TTISRScaleup_powheg', 58682125L, 70551.75170722324]
['TTUETunedown_powheg', 27737808L, 33348.33124939886]
['TTUETuneup_powheg', 29194459L, 35099.61888044628]
['T_tW', 6946349L, 195122.1629213483]
['Tbar_tW', 6826465L, 191754.63483146066]
['WJets', 29047710L, 472.1208919806261]
['DYJets_50MG', 47930047L, 23864.791376219877]
['TTHbb', 3735442L, -3735442.0]
['TTZQQ', 749386L, -749386.0]
['TTZLL', 1992407L, -1992407.0]
['TTWLN', 2160135L, -2160135.0]
['TTWQQ', 833282L, -833282.0]


Fre 20 Jan 2017 00:09:43 CET
rootplot installation instructions

see http://pythonhosted.org/rootplot/

```
$ export PYTHONPATH=$PYTHONPATH:/storage_mnt/storage/user/dlontkov/CMSSW_8_0_21/src/TopBrussels/FourTops2016/rootplot/lib/python2.7/site-packages/ 
$ hg clone http://bitbucket.org/klukas/rootplot
$ cd rootplot
$ python setup.py develop --prefix=/storage_mnt/storage/user/dlontkov/CMSSW_8_0_21/src/TopBrussels/FourTops2016/rootplot
$ hg pull http://bitbucket.org/klukas/rootplot
$ hg update
```


Plotting commands
make -j plots_el INPUTLOCATION=/storage_mnt/storage/user/dlontkov/CMSSW_8_0_21/src/TopBrussels/FourTops2016/output/Craneens_El/Craneens20_1_2017 BUILDDIR=plots_el TREENAME=Craneen__El DATALABEL=Single\ e

make -j  plots_mu INPUTLOCATION=/storage_mnt/storage/user/dlontkov/CMSSW_8_0_21/src/TopBrussels/FourTops2016/output/Craneens_Mu/Craneens19_1_2017 BUILDDIR=plots_mu TREENAME=Craneen__Mu DATALABEL=Single\ \#mu

Electon data events
['Data_Run2016B-ReReco', 237020067L, 237020067.0]
['Data_Run2016C-ReReco', 93219591L, 93219591.0]
['Data_Run2016D-ReReco', 146306673L, 146306673.0]
['Data_Run2016E-ReReco', 112041101L, 112041101.0]
['Data_Run2016F-ReReco', 70142300L, 70142300.0]
['Data_Run2016G-ReReco', 151991012L, 151991012.0]
['Data_Run2016H-PromptRecoV2', 123214902L, 123214902.0]
['Data_Run2016H-PromptRecoV3', 3189653L, 3189653.0]
TOTAL: 937125299
Muon
['Data_Run2016B-ReReco', 153007286L, 153007286.0]
['Data_Run2016C-ReReco', 64528905L, 64528905.0]
['Data_Run2016D-ReReco', 96017782L, 96017782.0]
['Data_Run2016E-ReReco', 86679163L, 86679163.0]
['Data_Run2016F-ReReco', 65033768L, 65033768.0]
['Data_Run2016G-ReReco', 147871216L, 147871216.0]
['Data_Run2016H-PromptRecoV2', 166660757L, 166660757.0]
['Data_Run2016H-PromptRecoV3', 4389808L, 4389808.0]
TOTAL: 784188685


TTTT negative weight fraction
negative weight NormFactor (posttrig): 0.44206
negative weight NormFactor (pretrig): 0.449449



Sam 21 Jan 2017 00:38:41 CET

tag v0.0.9pudown is a special tag for M17 analysis with the corrections described in 
https://docs.google.com/presentation/d/1MtTtEbT5QSpP8rcazfXWDO4vHs00xfsAfpryrdcI3Os/edit#slide=id.g191c4d4b66_0_140
and central pile-up SF replaced by down variation SFPU in the event level SF



#To make combine cards
```
cd result
make -n cards INPUTLOCATION=plots_mu
```


Son 22 Jan 2017 04:49:56 CET
To create combine cards
python tools/cards.py -o cards_mu/card.txt --channel=mu --data plots_mu/Hists_data.root --debug --source '{"TTTT":"plots_mu/Hists_TTTT.root", "TT":"plots_mu/Hists_SYST.root", "EW":"plots_mu/Hists_WJets.root", "ST":"plots_mu/Hists_T.root"}' --observable=bdt

or using make

make -n cards_mu BUILDDIR=plots_mu


Son 22 Jan 2017 19:22:40 CET
tag v0.0.10pudown is a start for moving towards more convenient (array-based) data structure for jets, ME weights, etc. Still in this tag central PU weight is replaced by its downward variation



# Die 24 Jan 2017 20:23:46 CET

## Extapolation of 2015 Single Lepton results (see record # Die 24 Jan 2017 19:28:15 CET in /user/dlontkov/CMSSW_7_4_7/src/combine2016_tttt/LOG)

 -- Asymptotic -- 
Expected  2.5%: r < 1.4818
Expected 16.0%: r < 1.9994
Expected 50.0%: r < 2.8203
Expected 84.0%: r < 3.9782
Expected 97.5%: r < 5.3971

This has to be compared to 

 -- Asymptotic -- 
Expected  2.5%: r < 2.0332
Expected 16.0%: r < 3.4510
Expected 50.0%: r < 6.4062
Expected 84.0%: r < 12.5859
Expected 97.5%: r < 19.4266


# Sam 28 Jan 2017 23:19:44 CET
CSVRS systematic studies code is at
/user/dlontkov/TOPCMSSW_7_6_3/src/TopBrussels/FourTops


# Son 05 Feb 2017 01:37:45 CET
Updated Muon (split by period), electron, Lumi and JEC according to Kevin's code

Hacked btagging corrections file to add light flavour to the mujets measurement (copy of incl)
e.g.
0, incl, central, 2, 0, 2.4, 20, 1000, 0, 1," ""1.13904+-0.000594946*x+1.97303e-06*x*x+-1.38194e-09*x*x*x"" "
0, incl, mujets, 2, 0, 2.4, 20, 1000, 0, 1," ""1.13904+-0.000594946*x+1.97303e-06*x*x+-1.38194e-09*x*x*x"" "
1, incl, central, 2, 0, 2.4, 20, 1000, 0, 1," ""1.0589+0.000382569*x+-2.4252e-07*x*x+2.20966e-10*x*x*x"" "
1, incl, mujets, 2, 0, 2.4, 20, 1000, 0, 1," ""1.0589+0.000382569*x+-2.4252e-07*x*x+2.20966e-10*x*x*x"" "
2, incl, central, 2, 0, 2.4, 20, 1000, 0, 1," ""0.971945+163.215/(x*x)+0.000517836*x"" "
2, incl, mujets, 2, 0, 2.4, 20, 1000, 0, 1," ""0.971945+163.215/(x*x)+0.000517836*x"" "



# Son 05 Feb 2017 13:21:22 CET
to make test of histogram compatibility

```
make -j test TARGET=../result/plots_mu REFERENCE=../result/history/30_01_2017/plots_mu
```

Don 27 Apr 2017 14:05:16 CEST

Trigger efficiency calculation

`python trgeff/trgeff.py plots_mu_jethtstream_sixjettrig/Craneen_Data_Run2_TopTree_Study.root --tree-name=Craneen__Mu --variable-name=LeptonPt --triggers=HLT_PFHT400_SixJet30_DoubleBTagCSV_p056:"HLT_IsoMu24||HLT_IsoTkMu24" -o HLT_IsoMu24_OR_HLT_IsoTkMu24_data.root`


Sam 29 Apr 2017 10:53:11 CEST
Pileup comparison
Need Freya's crab lumi files
cd PU
producePU.zsh [NAME OF THE CRAB LUMI JSON] [OUTPUTFILE/HIST suffix]

producePU.zsh uses official input (GOLDEN/SILVER) json --inputLumiJSON=INPUTLUMIJSON

/storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/PU/producePU.zsh /storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/PU/Freya_crab_jsons/lumiSummary_crab_SingleMuon-Run2016F-03Feb2017-v1crab37.json Run2016F-03Feb2017-v1crab37

Event yields histogram
cd result/

#single lepton stream
python -i datayields.py '{"B":["plots_mu_B/Craneen_Data_Run2_TopTree_Study.root","Craneen__Mu",5743725979.478], "C":["plots_mu_C/Craneen_Data_Run2_TopTree_Study.root","Craneen__Mu",2573399420.069 ], "D":["plots_mu_D/Craneen_Data_Run2_TopTree_Study.root","Craneen__Mu",4248383597.366], "E":["plots_mu_E/Craneen_Data_Run2_TopTree_Study.root","Craneen__Mu",4008375931.882], "F":["plots_mu_F/Craneen_Data_Run2_TopTree_Study.root","Craneen__Mu",3101618412.335], "G":["plots_mu_G/Craneen_Data_Run2_TopTree_Study.root","Craneen__Mu",7540487735.974], "H":["plots_mu_H/Craneen_Data_Run2_TopTree_Study.root","Craneen__Mu",8605689861.909]}' yields.root:mu24

#jetht stream
python -i datayields.py '{"B":["plots_mu_jethtstream_sixjettrig_B/Craneen_Data_Run2_TopTree_Study.root","Craneen__Mu",5743725979.478], "C":["plots_mu_jethtstream_sixjettrig_C/Craneen_Data_Run2_TopTree_Study.root","Craneen__Mu",2573399420.069 ], "D":["plots_mu_jethtstream_sixjettrig_D/Craneen_Data_Run2_TopTree_Study.root","Craneen__Mu",4248383597.366], "E":["plots_mu_jethtstream_sixjettrig_E/Craneen_Data_Run2_TopTree_Study.root","Craneen__Mu",4008375931.882], "F":["plots_mu_jethtstream_sixjettrig_F/Craneen_Data_Run2_TopTree_Study.root","Craneen__Mu",3101618412.335], "G":["plots_mu_jethtstream_sixjettrig_G/Craneen_Data_Run2_TopTree_Study.root","Craneen__Mu",7540487735.974], "H":["plots_mu_jethtstream_sixjettrig_H/Craneen_Data_Run2_TopTree_Study.root","Craneen__Mu",8605689861.909]}' yields.root:jetht


#How to plot systematics comparison
python -b sysplot.py -b ~/CMSSW_8_0_21/src/TopBrussels/FourTops2016/result/v6JECapplied/plots_mu/Hists_TT_CARDS.root -j JES.json -r ~/CMSSW_8_0_21/src/TopBrussels/FourTops2016/result/v6JECapplied/plots_mu/Hists_TT_CARDS.root -f .png


#Trigger efficiency calculation for SingleElectron trigger HLT_Ele32_eta2p1_WPTight_Gsf
python ../trgeff/trgeff.py plots_el/Craneen_TTJets_powheg_Run2_TopTree_Study.root --tree-name=Craneen__El --variable-name=LeptonPt --triggers=HLT_PFHT400_SixJet30_DoubleBTagCSV_p056:"HLT_Ele32_eta2p1_WPTight_Gsf" -o HLT_Ele32_eta2p1_WPTight_Gsf_mcJETHT_pt.root


Tue 09 May 2017 11:52:23 PM CEST
Friend tree afterburner with MVA recalcualtion

python tools/addfriend_bdt.py plots_mu/Craneen_ttttNLO_Run2_TopTree_Study.root -w ../weights_Mu29Aug400trees_5MinNodeSize_20nCuts_3MaxDepth_5adaboostbeta_adaBoost_alphaSTune_noMinEvents/MasterMVA_SingleMuon_29Aug400trees_5MinNodeSize_20nCuts_3MaxDepth_5adaboostbeta_adaBoost_alphaSTune_noMinEvents_BDT.weights.xml  -s Craneen__Mu -f BDT2



Fri 19 May 2017 11:06:22 AM CEST
Dump latex source for control plots
python ../latex/texplotspage.py -j singlemuoncp.json log/allSF/


Fri 19 May 2017 11:49:50 PM CEST

Friend tree afterburner with MVA recalcualtion for all craneens in the folder
for i in plots_mu/Craneen_*.root; do python tools/addfriend_bdt.py -o $i -s Craneen__Mu -f bdt_paper -w ../MVA/weights_Mu29Aug400trees_5MinNodeSize_20nCuts_3MaxDepth_5adaboostbeta_adaBoost_alphaSTune_noMinEvents/MasterMVA_SingleMuon_29Aug400trees_5MinNodeSize_20nCuts_3MaxDepth_5adaboostbeta_adaBoost_alphaSTune_noMinEvents_BDT.weights.xml $i;done


Sat 20 May 2017 10:55:17 AM CEST
Impacts
text2workspace.py card_mu.txt
combineTool.py -M Impacts -d card_mu.root --doInitialFit -m 125
combineTool.py -M Impacts -d card_mu.root --doFits -m 125 --parallel 4
combineTool.py -M Impacts -d card_mu.root -o impacts_mu.json -m 125
plotImpacts.py -i impacts_mu.json -o impacts_mu


Thu 25 May 2017 01:08:09 AM CEST
Rescale shape systematics
python tools/renormsysshapes.py plots_mu/Hists_TTTT_CARDS.root -r plots_mu/Hists_TTTT.root -t bdt -d -s MEScale



Sat 27 May 2017 12:06:33 AM CEST
TO run over alternative TT samples (e.g. powheg-herwig)
make -j card_mu.txt ERA=full INPUTLOCATION=/pnfs/iihe/cms/store/user/dlontkov/backup/t2016/tag_v0.0.21/Craneens_Mu/Craneens22_5_2017/ BUILDDIR=plots_mu DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu FORMAT=png TTCENTRAL=powheg_herwig


Sat 27 May 2017 11:58:47 AM CEST
Prepare bigsub and smallsub scripts
for i in ../*El*/submit*.sh;do echo qsub $i;done > bigsub.txt
for i in ../*Mu*/submit*.sh;do echo qsub $i;done > bigsub.txt
grep -v MET bigsub.txt |grep -v JETHT|grep -v herwig_je


Sat 03 Jun 2017 09:55:45 AM CEST
Expected limit optimisation
cp ../long_and_denys_2016/datacard* .
cp ../long_and_denys_2016/shapefile* .
cp ~/t2016/result/card_el.txt ~/t2016/result/card_mu.txt .
mkdir plots_el plots_mu
cp ~/t2016/result/plots_mu/*CARDS* ~/t2016/result/plots_mu/Hists_data.root plots_mu
cp ~/t2016/result/plots_el/*CARDS* ~/t2016/result/plots_el/Hists_data.root plots_el
cp /user/dlontkov/t2016/result/plots_el/Hists_EW.root plots_el
cp /user/dlontkov/t2016/result/plots_mu/Hists_EW.root plots_mu
cp /user/dlontkov/t2016/result/plots_el/Hists_T.root plots_el
cp /user/dlontkov/t2016/result/plots_mu/Hists_T.root plots_mu
cp /user/dlontkov/t2016/result/plots_el/Hists_TT_RARE.root plots_el
cp /user/dlontkov/t2016/result/plots_mu/Hists_TT_RARE.root plots_mu

combineCards.py EL=card_el.txt MU=card_mu.txt > combo_sl.txt
combineCards.py EL=card_el.txt MU=card_mu.txt MUMU=datacardMuMu_BDT_DilepCombined22ndJune2016_13TeVHadTop_JS.txt ELEL=datacardElEl_BDT_DilepCombined22ndJune2016_13TeVHadTop_JS.txt MUEL=datacardMuEl_BDT_DilepCombined22ndJune2016_13TeVHadTop_JS.txt  > combo.txt

combine -M MaxLikelihoodFit combo.txt -t -1 --expectSignal=1 --robustFit=1
combine -M ProfileLikelihood combo.txt -t -1 --expectSignal=1 --significance
combine -M Asymptotic --run blind combo.txt


Tue 06 Jun 2017 10:10:58 PM CEST
Jet split training (add jet multiplicity-dependent tree)

python addfriend_freya_njets.py -j '{"10j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets10_100_2.p","9j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets9_100_2.p","8j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets8_300_2.p","7j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets6_500_2.p"}' -s Craneen__Mu -f BDTjetsplit ../plots_mu/Craneen_ttttNLO_Run2_TopTree_Study.root

for i in ../plots_el/Craneen_*.root;do echo python ../tools/addfriend_freya_njets.py -j "'"'{"10j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets10_100_2.p","9j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets9_100_2.p","8j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets8_300_2.p","7j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets6_500_2.p"}'"'" -s Craneen__El -f BDTjetsplit $i|cat submitSkeleton.sh - > sub_`basename $i .root`.sh;done

for i in ../plots_mu/Craneen_*.root;do echo python ../tools/addfriend_freya_njets.py -j "'"'{"10j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets10_100_2.p","9j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets9_100_2.p","8j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets8_300_2.p","7j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets6_500_2.p"}'"'" -s Craneen__Mu -f BDTjetsplit $i|cat submitSkeleton.sh - > sub_`basename $i .root`.sh;done

# 9to10 jet split
for i in ../plots_el/Craneen_*.root;do echo python ../tools/addfriend_freya_njets.py -j "'"'{"10j":"../../MVA/Freyas/9to10jetsplitting/BDTAdaBoost_250_2.p","9j":"../../MVA/Freyas/9to10jetsplitting/BDTAdaBoost_250_2.p","8j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets8_300_2.p","7j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets6_500_2.p"}'"'" -s Craneen__El -f BDT9and10jetsplit $i|cat submitSkeleton.sh - > sub_`basename $i .root`.sh;done

for i in ../plots_mu/Craneen_*.root;do echo python ../tools/addfriend_freya_njets.py -j "'"'{"10j":"../../MVA/Freyas/9to10jetsplitting/BDTAdaBoost_250_2.p","9j":"../../MVA/Freyas/9to10jetsplitting/BDTAdaBoost_250_2.p","8j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets8_300_2.p","7j":"../../MVA/Freyas/individualnjtraining/BDTAdaBoost_njets6_500_2.p"}'"'" -s Craneen__Mu -f BDT9and10jetsplit $i|cat submitSkeleton.sh - > sub_`basename $i .root`.sh;done


Fri 09 Jun 2017 02:22:47 PM CEST
Mask channels
#Single electron
text2workspace.py card_el.txt  --channel-masks
combine card_el.root  -M Asymptotic --run blind --setPhysicsModelParameters mask_el7J2M=1,mask_el7J3M=1,mask_el7J4M=1
## With nuissance freezing
combine card_el.root  -M Asymptotic --run blind --setPhysicsModelParameters mask_el7J2M=1,mask_el7J3M=1,mask_el7J4M=1,TTTTISR=0.,TTTTFSR=0. --freezeNuisances TTTTISR,TTTTFSR
#Single and dilepton combined
text2workspace.py combo.txt --channel-masks
combine combo.root -M Asymptotic --setPhysicsModelParameters mask_EL_el7J2M=1,mask_EL_el7J3M=1,mask_EL_el7J4M=1


#Sat 17 Jun 2017 07:57:30 PM CEST
##Signal injection test
for i in {1..20};do combine -M MaxLikelihoodFit combo_sl.root -t -1 --expectSignal=$i --rMax=50 --robustFit=1|grep "Best fit"|awk -v var="$i" '{print var" "$4" "$5}';done
python linearity.py

##Postfit mountainrange plot
python mountainrange.py -j mountain_mu.json  mlfit.root


#Sun 18 Jun 2017 01:03:16 AM CEST
cd test;make report_TTJets_unbinned.pdf TARGET=../output/Craneens_Mu/Craneens15_6_2017 REFERENCE=../output/Craneens_Mu/Craneens14_6_2017/ref;cd -
cd test;make report_TTTT_unbinned.pdf TARGET=../output/Craneens_Mu/Craneens14_6_2017 REFERENCE=../output/Craneens_Mu/Craneens14_6_2017/ref;cd -


#Sat 24 Jun 2017 05:01:57 PM CEST
## 2d mass plots
python tools/mass2dplots.py -s plots_mu_tritop/Craneen_ttttNLO_Run2_TopTree_Study.root -g plots_mu_tritop/Craneen_TTJets_powheg_Run2_TopTree_Study.root -t Craneen__Mu -o mass_plots.png -b

## POWHEG fake tag multiplicity studies
python tools/ttbbfakes.py plots_mu/Craneen_TTJets_powheg_Run2_TopTree_Study.root -t Craneen__Mu -o fake_ttbb.png -b

## ABCD
# muon channel
python ABCD.py -j '{"data":"/storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/output/Craneens_Mu/Craneens25_6_2017/merged/Craneen_Data_Run2016_Run2_TopTree_Study.root"}' -t Craneen__Mu -b

python tools/ABCD.py -j '{"data":["plots_mu_ABCD/Craneen_Data_Run2_TopTree_Study.root",1.0], "MC":{"TT":["plots_mu_ABCD/Craneen_TTJets_powheg_Run2_TopTree_Study.root",0.193716347452], "DY1":["plots_mu_ABCD/Craneen_DY1Jets_50MG_Run2_TopTree_Study.root",0.059297982638], "DY2":["plots_mu_ABCD/Craneen_DY2Jets_50MG_Run2_TopTree_Study.root",0.182288730249],"DY3":["plots_mu_ABCD/Craneen_DY3Jets_50MG_Run2_TopTree_Study.root",0.0589828180267], "DY4":["plots_mu_ABCD/Craneen_DY4Jets_50MG_Run2_TopTree_Study.root",0.00299991762558], "W1":["plots_mu_ABCD/Craneen_W1Jets_Run2_TopTree_Study.root",7.49748867091], "W2":["plots_mu_ABCD/Craneen_W2Jets_Run2_TopTree_Study.root",3.74154234029], "W3":["plots_mu_ABCD/Craneen_W3Jets_Run2_TopTree_Study.root",2.03671725612], "W4":["plots_mu_ABCD/Craneen_W4Jets_Run2_TopTree_Study.root",2.04812850961], "STTW":["plots_mu_ABCD/Craneen_T_tW_Run2_TopTree_Study.root",1.28582690024], "STBARTW":["plots_mu_ABCD/Craneen_Tbar_tW_Run2_TopTree_Study.root",1.27777900214], "STTCH":["plots_mu_ABCD/Craneen_T_tch_Run2_TopTree_Study.root",0.813137512367], "STBARTCH":["plots_mu_ABCD/Craneen_Tbar_tch_Run2_TopTree_Study.root",0.73840459982], "TTW":["plots_mu_ABCD/Craneen_TTW_Run2_TopTree_Study.root",0.00314013867289], "TTZ":["plots_mu_ABCD/Craneen_TTZ_Run2_TopTree_Study.root",0.00257810454647], "TTH":["plots_mu_ABCD/Craneen_TTH_Run2_TopTree_Study.root",0.000170315610139]}}' -t Craneen__Mu -b



Sun 30 Jul 2017 09:15:51 PM CEST
for i in `grep -L "End of" *.o*`; do ../../resubmit.sh -f $i -o ~/t2016/output/Craneens_Mu/Craneens29_7_2017/ -s ~/t2016/SubmitScripts/2_7_2017/Mu2016/; done


Mon 31 Jul 2017 07:52:51 PM CEST
Generate scripts for adding exta mvas on cluster
cd /user/dlontkov/t2016/result/addfriend/Mu
../generate_jobs.sh -s ../submitSkeleton.sh ../../plots_mu_toppt/"Cran*".root
for i in *.sh;do qsub $i;done



Wed 02 Aug 2017 01:07:09 PM CEST

for i in plots_mu_toppt/Cran*.root; do echo ln -s `readlink -f $i` plots_mu_toppt_LeptonPt/`basename $i`;done
for i in plots_el_toppt/Cran*.root; do echo ln -s `readlink -f $i` plots_el_toppt_LeptonPt/`basename $i`;done



# Wed Aug 23 07:46:41 CEST 2017
resubmit crashed jobs
for i in `grep -IirnL "End of" *.o*`;do ../../../../resubmit.sh  -o /user/dlontkov/t2016/output/Craneens_Mu/Craneens21_8_2017/ -s ../.. -f $i;done


# Mon Aug 28 10:35:41 CEST 2017
## Signal to background ratio tables

+ Make json files with signal and background rates
```
muons:
python /storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/result/tools/SBratio.py -o SB.json --caption='pT>30 GeV' --channel=mu --data Hists_data.root  --source '{"NP_overlay_ttttNLO":"Hists_TTTT_CARDS.root", "ttbarTTX":"Hists_TT_CARDS.root", "EW":"Hists_EW.root", "ST_tW":"Hists_T.root", "TTRARE":"Hists_TT_RARE.root"}' --observable=bdt
electrons:
python /storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/result/tools/SBratio.py -o SB.json --caption='pT>30 GeV' --channel=el --data Hists_data.root  --source '{"NP_overlay_ttttNLO":"Hists_TTTT_CARDS.root", "ttbarTTX":"Hists_TT_CARDS.root", "EW":"Hists_EW.root", "ST_tW":"Hists_T.root", "TTRARE":"Hists_TT_RARE.root"}' --observable=bdt
```
+ Parse json output from previous steps into tables
```
python /storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/result/tools/parseSBratio.py -f tex SB_1.json SB_2.json
```

Example output:
python /storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/result/tools/parseSBratio.py -f tex plots_el_topptnonjw_lowbpt/SB.json plots_el_topptnonjw/SB.json

Search category     &        BG rate&    Signal rate&      S/B ratio&        BG rate&    Signal rate&      S/B ratio\\
el8J2M              &        1485.82&           1.66&        0.00111&        1373.05&           1.68&        0.00123\\
el8J3M              &         399.47&           1.26&        0.00316&         331.11&           1.17&        0.00354\\
el8J4M              &          73.39&           0.47&        0.00643&          54.99&           0.41&        0.00753\\
el9J2M              &         446.82&           1.25&        0.00280&         410.21&           1.23&        0.00299\\
el9J3M              &         152.00&           0.98&        0.00647&         127.58&           0.89&        0.00701\\
el9J4M              &          35.02&           0.44&        0.01263&          25.49&           0.38&        0.01495\\
el10J2M             &         174.16&           1.10&        0.00631&         159.52&           1.08&        0.00680\\
el10J3M             &          65.42&           0.94&        0.01444&          54.78&           0.82&        0.01501\\
el10J4M             &          15.73&           0.55&        0.03528&          10.88&           0.47&        0.04332\\

python /storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/result/tools/parseSBratio.py -f tex plots_mu_topptnonjw_lowbpt/SB.json plots_mu_topptnonjw/SB.json
Search category     &        BG rate&    Signal rate&      S/B ratio&        BG rate&    Signal rate&      S/B ratio\\
mu7J2M              &        6219.78&           2.51&        0.00040&        5732.48&           2.59&        0.00045\\
mu7J3M              &        1357.77&           1.65&        0.00121&        1148.11&           1.57&        0.00137\\
mu7J4M              &         205.71&           0.55&        0.00269&         162.67&           0.49&        0.00302\\
mu8J2M              &        2276.40&           2.60&        0.00114&        2094.27&           2.60&        0.00124\\
mu8J3M              &         614.91&           1.97&        0.00320&         510.56&           1.83&        0.00358\\
mu8J4M              &         114.03&           0.73&        0.00640&          87.08&           0.63&        0.00723\\
mu9J2M              &         708.68&           1.81&        0.00255&         643.86&           1.76&        0.00273\\
mu9J3M              &         230.63&           1.56&        0.00675&         185.53&           1.44&        0.00778\\
mu9J4M              &          47.46&           0.66&        0.01390&          33.99&           0.58&        0.01696\\
mu10J2M             &         257.34&           1.63&        0.00635&         235.59&           1.56&        0.00660\\
mu10J3M             &          88.94&           1.45&        0.01633&          72.58&           1.33&        0.01828\\
mu10J4M             &          27.79&           0.81&        0.02931&          21.77&           0.67&        0.03070\\



Tue Sep 19 18:57:39 CEST 2017
Impacts
combineTool.py -M Impacts -d combo_topptnonjw_v1/datacard_muel_nomcstat.root --doInitialFit -m 125 -t -1 --expectSignal=1 --robustFit=1
combineTool.py -M Impacts -d combo_topptnonjw_v1/datacard_muel_nomcstat.root --doFits -m 125 --parallel 4 -t -1 --expectSignal=1 --robustFit=1 
combineTool.py -M Impacts -d combo_topptnonjw_v1/datacard_muel_nomcstat.root -o impacts_combined_elmu.json -m 125 -t -1 --expectSignal=1 --robustFit=1 
plotImpacts.py -i impacts_combined_elmu.json -o impacts_combined_elmu



# Wed  Sep 27 23:20:21 CEST 2017
mkdir plots_mu_topptnonjw_v1/png plots_mu_topptnonjw_v1/pdf
make -j  plots_mu INPUTLOCATION=plots_mu_topptnonjw_v1 BUILDDIR=plots_mu_topptnonjw_v1 TREENAME=Craneen__Mu DATALABEL=Single\ \#mu FORMAT=png
rm -rf plots_mu_topptnonjw_v1/png/l*; mv plots_mu_topptnonjw_v1/l* plots_mu_topptnonjw_v1/png
make -j  plots_mu INPUTLOCATION=plots_mu_topptnonjw_v1 BUILDDIR=plots_mu_topptnonjw_v1 TREENAME=Craneen__Mu DATALABEL=Single\ \#mu FORMAT=pdf
rm -rf plots_mu_topptnonjw_v1/pdf/l*; mv plots_mu_topptnonjw_v1/l* plots_mu_topptnonjw_v1/pdf
make -j card_mu.txt INPUTLOCATION=plots_mu_topptnonjw_v1 BUILDDIR=plots_mu_topptnonjw_v1 TREENAME=Craneen__Mu DATALABEL=Single\ \#mu FORMAT=png
make -j sysplots BUILDDIR=plots_mu_topptnonjw_v1 FORMAT=png
make -j sysplotsnorm BUILDDIR=plots_mu_topptnonjw_v1 FORMAT=png
make -j sysplots BUILDDIR=plots_mu_topptnonjw_v1 FORMAT=pdf
make -j sysplotsnorm BUILDDIR=plots_mu_topptnonjw_v1 FORMAT=pdf

mkdir plots_el_topptnonjw_v1/png plots_el_topptnonjw_v1/pdf
make -j  plots_el INPUTLOCATION=plots_el_topptnonjw_v1 BUILDDIR=plots_el_topptnonjw_v1 TREENAME=Craneen__El DATALABEL=Single\ el FORMAT=png
rm -rf plots_el_topptnonjw_v1/pdf/l*; mv plots_el_topptnonjw_v1/l* plots_el_topptnonjw_v1/png
make -j  plots_el INPUTLOCATION=plots_el_topptnonjw_v1 BUILDDIR=plots_el_topptnonjw_v1 TREENAME=Craneen__El DATALABEL=Single\ el FORMAT=pdf
mv plots_el_topptnonjw_v1/l* plots_el_topptnonjw_v1/pdf
make -j card_el.txt INPUTLOCATION=plots_el_topptnonjw_v1 BUILDDIR=plots_el_topptnonjw_v1 TREENAME=Craneen__El DATALABEL=Single\ el FORMAT=png
make -j sysplots BUILDDIR=plots_el_topptnonjw_v1 FORMAT=png
make -j sysplots BUILDDIR=plots_el_topptnonjw_v1 FORMAT=pdf

mkdir plots_topptnonjw_v1/png plots_topptnonjw_v1/pdf
make -j mergechannelsplots BUILDDIR=plots_topptnonjw_v1 BUILDDIR_EL=plots_el_topptnonjw_v1 BUILDDIR_MU=plots_mu_topptnonjw_v1
make -j  plots_mu INPUTLOCATION=plots_topptnonjw_v1 BUILDDIR=plots_topptnonjw_v1 DATALABEL=Single\ l FORMAT=png
mv plots_topptnonjw_v1/l* plots_topptnonjw_v1/png
make -j  plots_mu INPUTLOCATION=plots_topptnonjw_v1 BUILDDIR=plots_topptnonjw_v1 DATALABEL=Single\ l FORMAT=pdf
mv plots_topptnonjw_v1/l* plots_topptnonjw_v1/pdf

mkdir plots_topptnonjw_v1
make -j datacard_elmu.txt BUILDDIR=plots_topptnonjw_v1 BUILDDIR_EL=plots_el_topptnonjw_v1 BUILDDIR_MU=plots_mu_topptnonjw_v1
make -j plots_topptnonjw_v1/datacard_elmu.root BUILDDIR=plots_topptnonjw_v1 BUILDDIR_EL=plots_el_topptnonjw_v1 BUILDDIR_MU=plots_mu_topptnonjw_v1
make -j impacts_combined_elmu_blind.pdf BUILDDIR=plots_topptnonjw_v1
make -j limits BUILDDIR=plots_topptnonjw_v1 BUILDDIR_EL=plots_el_topptnonjw_v1 BUILDDIR_MU=plots_mu_topptnonjw_v1 FORMAT=txt
make -j combinechecks BUILDDIR=plots_topptnonjw_v1 BUILDDIR_EL=plots_el_topptnonjw_v1 BUILDDIR_MU=plots_mu_topptnonjw_v1


# Sun Oct  1 10:43:15 CEST 2017
mkdir plots_mu_topptnonjw_v2
mkdir plots_mu_topptnonjw_v2/png plots_mu_topptnonjw_v2/pdf
make -j  plots_mu INPUTLOCATION=plots_mu_topptnonjw_v2/ BUILDDIR=plots_mu_topptnonjw_v2 TREENAME=Craneen__Mu DATALABEL=Single\ \#mu FORMAT=png


# Sun Oct  1 23:17:33 CEST 2017
################################### SUPERIMPORTANT ################################
mybtag branch changes always have to be merged into master CMSSW_80X because master branch has different electron definition!!!!!
################################### SUPERIMPORTANT ################################


# Tue Nov 14 04:16:29 CET 2017
command to run limit with mc stats and limits without stepping 
In order to reduce the number of Barlow-Beeston parameters do
	*4M autoMCstats 1

combine -M AsymptoticLimits final_unblinding/50bins/datacard_elmu.root --run both --rRelAcc=0.0000000001 --rAbsAcc=0.0000000001  --minosAlgo=bisection  --cminDefaultMinimizerType=Minuit2 --X-rtd MINIMIZER_analytic

## Combine Long's and my datacards
combineCards.py MU=final_unblinding/50bins/plots_mu/card_mu.txt EL=final_unblinding/50bins/plots_el/card_el.txt MUMU=final_unblinding/longs/datacardMuMu_BDT_MuMu18thSep2017_13TeVHadTop_JTS.txt ELEL=final_unblinding/longs/datacardElEl_BDT_ElEl18thSep2017_13TeVHadTop_JTS.txt MUEL=final_unblinding/longs/datacardMuEl_BDT_MuEl18thSep2017_13TeVHadTop_JTS.txt > final_unblinding/combo.txt


## r scans
combine -M MultiDimFit --robustFit=1 --rMax=3 -t -1 --expectSignal=1 --saveNLL --algo grid -n _dl --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --freezeParameter lumiscale --setParameters lumiscale=1. final_unblinding/longs/dilepton_lumiscale.txt --points 200

combine -M MultiDimFit --robustFit=1 --rMax=3 -t -1 --expectSignal=1 --saveNLL --algo grid -n _sl --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --freezeParameter lumiscale --setParameters lumiscale=1. final_unblinding/50bins/datacard_elmu_lumiscale.txt --points 200

combine -M MultiDimFit --robustFit=1 --rMax=3 -t -1 --expectSignal=1 --saveNLL --algo grid -n _combo --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --freezeParameter lumiscale --setParameters lumiscale=1. final_unblinding/combo_lumiscale.txt  --points 200

python NLL_scans.py -f .pdf -j '{"sl":"higgsCombine_sl.MultiDimFit.mH120.root","dl":"higgsCombine_dl.MultiDimFit.mH120.root","combo":"higgsCombine_combo.MultiDimFit.mH120.root", "sl_fit":[1.0,2.47,-1.0],"dl_fit":[1.0,1.74,-1.0],"combo_fit":[1.0,1.34,-1.0]}' -b


# Thu Nov 16 14:16:35 CET 2017
## SL, OS, SS combination
make -f Makefile_comb.mk final_combination/fullcombo.root BUILDDIR=final_combination BUILDDIR_EL=final_unblinding/50bins/plots_el BUILDDIR_MU=final_unblinding/50bins/plots_mu BUILDDIR_OS=final_unblinding/longs BUILDDIR_SS=~/CMSSW_7_4_7/src/SS_2017/uaf-8.t2.ucsd.edu/fourtop_combination_17Aug2017

All systematics uncorrelated
combine -M Asymptotic --run blind final_unblinding/full_combo.txt

Expected  2.5%: r < 0.7819
Expected 16.0%: r < 1.0972
Expected 50.0%: r < 1.6406
Expected 84.0%: r < 2.5104
Expected 97.5%: r < 3.7206

# JES correlated

## OS combination
make -n -f Makefile_comb.mk final_unblinding/longs/jes_total/datacard_os.txt  BUILDDIR=final_combination BUILDDIR_SL=final_unblinding/50bins/  BUILDDIR_EL=final_unblinding/50bins/plots_el BUILDDIR_MU=final_unblinding/50bins/plots_mu BUILDDIR_OS=final_unblinding/longs/jes_total BUILDDIR_SS=~/CMSSW_7_4_7/src/SS_2017/uaf-8.t2.ucsd.edu/fourtop_combination_17Aug2017

make -f Makefile_comb.mk final_combination/fullcombo_cor.root BUILDDIR=final_combination BUILDDIR_SL=final_unblinding/50bins/  BUILDDIR_EL=final_unblinding/50bins/plots_el BUILDDIR_MU=final_unblinding/50bins/plots_mu BUILDDIR_OS=final_unblinding/longs/jes_total BUILDDIR_SS=~/CMSSW_7_4_7/src/SS_2017/uaf-8.t2.ucsd.edu/fourtop_combination_17Aug2017

 -- AsymptoticLimits ( CLs ) --
Expected  2.5%: r < 0.7670
Expected 16.0%: r < 1.0829
Expected 50.0%: r < 1.6094
Expected 84.0%: r < 2.4433
Expected 97.5%: r < 3.5633


# Fri Nov 17 12:06:07 CET 2017
individual systematics stack
python tools/plot_stack_syst.py -b final_unblinding/50bins/plots_mu/Hists_TTTT_CARDS.root final_unblinding/50bins/unblinded

# Sat Nov 18 17:00:09 CET 2017
# Mountain range plots for all systematic sources

combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters JER --setParameters JER=-1 -n _jer_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters JER --setParameters JER=+1 -n _jer_up --out final_unblinding/50bins/unblinded --saveShapes

combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters PU --setParameters PU=-1 -n _PU_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters PU --setParameters PU=+1 -n _PU_up --out final_unblinding/50bins/unblinded --saveShapes

combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters TTJets_PDF --setParameters TTJets_PDF=-1 -n _ttpdf_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters TTJets_PDF --setParameters TTJets_PDF=+1 -n _ttpdf_up --out final_unblinding/50bins/unblinded --saveShapes


TTPT
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters TTPT --setParameters TTPT=-1 -n _ttpt_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters TTPT --setParameters TTPT=+1 -n _ttpt_up --out final_unblinding/50bins/unblinded --saveShapes

heavyFlav
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters heavyFlav --setParameters heavyFlav=-1 -n _hf_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters heavyFlav --setParameters heavyFlav=+1 -n _hf_up --out final_unblinding/50bins/unblinded --saveShapes

ttMEScale
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters ttMEScale --setParameters ttMEScale=-1 -n _ttme_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters ttMEScale --setParameters ttMEScale=+1 -n _ttme_up --out final_unblinding/50bins/unblinded --saveShapes

ttttMEScale
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters TTTTMEScale --setParameters TTTTMEScale=-1 -n _ttttme_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters TTTTMEScale --setParameters TTTTMEScale=+1 -n _ttttme_up --out final_unblinding/50bins/unblinded --saveShapes

btagWeightCSVCFErr1
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVCFErr1 --setParameters btagWeightCSVCFErr1=-1 -n _CFErr1_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVCFErr1 --setParameters btagWeightCSVCFErr1=+1 -n _CFErr1_up --out final_unblinding/50bins/unblinded --saveShapes

btagWeightCSVCFErr2
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVCFErr2 --setParameters btagWeightCSVCFErr2=-1 -n _CFErr2_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVCFErr2 --setParameters btagWeightCSVCFErr2=+1 -n _CFErr2_up --out final_unblinding/50bins/unblinded --saveShapes

btagWeightCSVHF
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVHF --setParameters btagWeightCSVHF=-1 -n _CSVHF_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVHF --setParameters btagWeightCSVHF=+1 -n _CSVHF_up --out final_unblinding/50bins/unblinded --saveShapes
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHF_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHF_down.root --outfile longhist_btCSVHF --sysname=CSVHF -b

btagWeightCSVHFStats1
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVHFStats1 --setParameters btagWeightCSVHFStats1=-1 -n _CSVHFStats1_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVHFStats1 --setParameters btagWeightCSVHFStats1=+1 -n _CSVHFStats1_up --out final_unblinding/50bins/unblinded --saveShapes

btagWeightCSVHFStats2
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVHFStats2 --setParameters btagWeightCSVHFStats2=-1 -n _CSVHFStats2_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVHFStats2 --setParameters btagWeightCSVHFStats2=+1 -n _CSVHFStats2_up --out final_unblinding/50bins/unblinded --saveShapes

btagWeightCSVJES
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVJES --setParameters btagWeightCSVJES=-1 -n _CSVJES_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVJES --setParameters btagWeightCSVJES=+1 -n _CSVJES_up --out final_unblinding/50bins/unblinded --saveShapes

btagWeightCSVLF
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVLF --setParameters btagWeightCSVLF=-1 -n _CSVLF_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVLF --setParameters btagWeightCSVLF=+1 -n _CSVLF_up --out final_unblinding/50bins/unblinded --saveShapes

btagWeightCSVLFStats1
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVLFStats1 --setParameters btagWeightCSVLFStats1=-1 -n _CSVLFStats1_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVLFStats1 --setParameters btagWeightCSVLFStats1=+1 -n _CSVLFStats1_up --out final_unblinding/50bins/unblinded --saveShapes

btagWeightCSVLFStats2
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVLFStats2 --setParameters btagWeightCSVLFStats2=-1 -n _CSVLFStats2_down --out final_unblinding/50bins/unblinded --saveShapes
combine -M FitDiagnostics final_unblinding/50bins/datacard_elmu_total_jes.root --skipBOnlyFit --freezeParameters btagWeightCSVLFStats2 --setParameters btagWeightCSVLFStats2=+1 -n _CSVLFStats2_up --out final_unblinding/50bins/unblinded --saveShapes

#python plotting Electron channel

python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_jes_up.root final_unblinding/50bins/unblinded/fitDiagnostics_jes_down.root -b --sysname=JES --outfile=longhist_jes
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_PU_up.root final_unblinding/50bins/unblinded/fitDiagnostics_PU_down.root --outfile longhist_pu --sysname=PU -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_ttpdf_up.root final_unblinding/50bins/unblinded/fitDiagnostics_ttpdf_down.root --outfile longhist_ttpdf --sysname=ttPDF -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_ttpt_up.root final_unblinding/50bins/unblinded/fitDiagnostics_ttpt_down.root --outfile longhist_ttpt --sysname=ttPT -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_hf_up.root final_unblinding/50bins/unblinded/fitDiagnostics_hf_down.root --outfile longhist_hf --sysname=HF -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_ttme_up.root final_unblinding/50bins/unblinded/fitDiagnostics_ttme_down.root --outfile longhist_ttme --sysname=ttME -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr1_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr1_down.root --outfile longhist_btCFErr1 --sysname=CFErr1 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr2_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr2_down.root --outfile longhist_btCFErr2 --sysname=CFErr2 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats1_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats1_down.root --outfile longhist_CSVHFStats1 --sysname=CSVHFStats1 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats2_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats2_down.root --outfile longhist_CSVHFStats2 --sysname=CSVHFStats2 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVJES_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVJES_down.root --outfile longhist_CSVJES --sysname=CSVJES -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLF_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLF_down.root --outfile longhist_CSVLF --sysname=CSVLF -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats1_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats1_down.root --outfile longhist_CSVLFStats1 --sysname=CSVLFStats1 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats2_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats2_down.root --outfile longhist_CSVLFStats2 --sysname=CSVLFStats2 -b

#python plotting Muon channel

python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_jes_up.root final_unblinding/50bins/unblinded/fitDiagnostics_jes_down.root -b --sysname=JES --outfile=longhist_jes
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_PU_up.root final_unblinding/50bins/unblinded/fitDiagnostics_PU_down.root --outfile longhist_pu --sysname=PU -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_ttpdf_up.root final_unblinding/50bins/unblinded/fitDiagnostics_ttpdf_down.root --outfile longhist_ttpdf --sysname=ttPDF -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_ttpt_up.root final_unblinding/50bins/unblinded/fitDiagnostics_ttpt_down.root --outfile longhist_ttpt --sysname=ttPT -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_hf_up.root final_unblinding/50bins/unblinded/fitDiagnostics_hf_down.root --outfile longhist_hf --sysname=HF -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_ttme_up.root final_unblinding/50bins/unblinded/fitDiagnostics_ttme_down.root --outfile longhist_ttme --sysname=ttME -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr1_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr1_down.root --outfile longhist_btCFErr1 --sysname=CFErr1 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr2_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr2_down.root --outfile longhist_btCFErr2 --sysname=CFErr2 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats1_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats1_down.root --outfile longhist_CSVHFStats1 --sysname=CSVHFStats1 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats2_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats2_down.root --outfile longhist_CSVHFStats2 --sysname=CSVHFStats2 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVJES_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVJES_down.root --outfile longhist_CSVJES --sysname=CSVJES -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLF_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLF_down.root --outfile longhist_CSVLF --sysname=CSVLF -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats1_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats1_down.root --outfile longhist_CSVLFStats1 --sysname=CSVLFStats1 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats2_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats2_down.root --outfile longhist_CSVLFStats2 --sysname=CSVLFStats2 -b

#python plotting Electron channel

python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_jes_up.root final_unblinding/50bins/unblinded/fitDiagnostics_jes_down.root -b --sysname=JES --outfile=longhist_signal_jes
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_PU_up.root final_unblinding/50bins/unblinded/fitDiagnostics_PU_down.root --outfile longhist_signal_pu --sysname=PU -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_ttttme_up.root final_unblinding/50bins/unblinded/fitDiagnostics_ttttme_down.root --outfile longhist_signal_ttttme --sysname=ttttME -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr1_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr1_down.root --outfile longhist_signal_btCFErr1 --sysname=CFErr1 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr2_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr2_down.root --outfile longhist_signal_btCFErr2 --sysname=CFErr2 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats1_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats1_down.root --outfile longhist_signal_CSVHFStats1 --sysname=CSVHFStats1 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats2_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats2_down.root --outfile longhist_signal_CSVHFStats2 --sysname=CSVHFStats2 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVJES_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVJES_down.root --outfile longhist_signal_CSVJES --sysname=CSVJES -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLF_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLF_down.root --outfile longhist_signal_CSVLF --sysname=CSVLF -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats1_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats1_down.root --outfile longhist_signal_CSVLFStats1 --sysname=CSVLFStats1 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_el.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats2_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats2_down.root --outfile longhist_signal_CSVLFStats2 --sysname=CSVLFStats2 -b

#python plotting Muon channel

python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_jes_up.root final_unblinding/50bins/unblinded/fitDiagnostics_jes_down.root -b --sysname=JES --outfile=longhist_signal_jes
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_PU_up.root final_unblinding/50bins/unblinded/fitDiagnostics_PU_down.root --outfile longhist_signal_pu --sysname=PU -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_ttttme_up.root final_unblinding/50bins/unblinded/fitDiagnostics_ttttme_down.root --outfile longhist_signal_ttttme --sysname=ttttME -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr1_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr1_down.root --outfile longhist_signal_btCFErr1 --sysname=CFErr1 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr2_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CFErr2_down.root --outfile longhist_signal_btCFErr2 --sysname=CFErr2 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats1_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats1_down.root --outfile longhist_signal_CSVHFStats1 --sysname=CSVHFStats1 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats2_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVHFStats2_down.root --outfile longhist_signal_CSVHFStats2 --sysname=CSVHFStats2 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVJES_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVJES_down.root --outfile longhist_signal_CSVJES --sysname=CSVJES -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLF_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLF_down.root --outfile longhist_signal_CSVLF --sysname=CSVLF -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats1_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats1_down.root --outfile longhist_signal_CSVLFStats1 --sysname=CSVLFStats1 -b
python tools/mountainrange_ratio_variant2.py -j tools/mountainrangeratio_configs/mountain_fitdiag_signal_mu.json -r final_unblinding/50bins/unblinded/fitDiagnostics_jes_central.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats2_up.root final_unblinding/50bins/unblinded/fitDiagnostics_CSVLFStats2_down.root --outfile longhist_signal_CSVLFStats2 --sysname=CSVLFStats2 -b


#Mon Nov 20 07:20:04 CET 2017
##Limits with different binning

combine -M MaxLikelihoodFit -d final_unblinding/10bins/datacard_elmu_total_jes.root --setPhysicsModelParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=1,mask_MU_mu8J3M=1,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=1,mask_EL_el8J3M=1,mask_EL_el8J2M=0  --rMax=100 --rMin=0 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --initFromBonly --robustFit=1
Best fit r: 9.99201e-14  -9.99201e-14/+100  (68% CL)
nll S+B -> -99.7984  nll B -> -101.488

combine -M MaxLikelihoodFit -d final_unblinding/10bins/datacard_elmu_total_jes.root --setPhysicsModelParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=0,mask_MU_mu8J3M=0,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=0,mask_EL_el8J3M=0,mask_EL_el8J2M=0  --rMax=100 --rMin=-10 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --initFromBonly --robustFit=1
Best fit r: 1.05476  -11.0548/+98.9452  (68% CL)
nll S+B -> -114.824  nll B -> -116.482

combine -M Asymptotic -d final_unblinding/10bins/datacard_elmu_total_jes.root --setPhysicsModelParameters mask_MU_mu10J4M=0,mask_MU_mu10J3M=0,mask_MU_mu10J2M=0,mask_MU_mu9J4M=0,mask_MU_mu9J3M=0,mask_MU_mu9J2M=0,mask_MU_mu8J4M=0,mask_MU_mu8J3M=0,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=0,mask_EL_el10J3M=0,mask_EL_el10J2M=0,mask_EL_el9J4M=0,mask_EL_el9J3M=0,mask_EL_el9J2M=0,mask_EL_el8J4M=0,mask_EL_el8J3M=0,mask_EL_el8J2M=0  --rMax=100 --rMin=-10 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic

 -- Asymptotic -- 
Observed Limit: r < 14.2461
Expected  2.5%: r < 4.8278
Expected 16.0%: r < 6.5410
Expected 50.0%: r < 9.2578
Expected 84.0%: r < 13.1325
Expected 97.5%: r < 18.1193

*blind*
 -- Asymptotic -- 
Expected  2.5%: r < 4.4125
Expected 16.0%: r < 5.9228
Expected 50.0%: r < 8.3984
Expected 84.0%: r < 11.9804
Expected 97.5%: r < 16.6939

combine -M MaxLikelihoodFit -d final_unblinding/25bins/datacard_elmu_total_jes.root --setPhysicsModelParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=1,mask_MU_mu8J3M=1,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=1,mask_EL_el8J3M=1,mask_EL_el8J2M=0  --rMax=100 --rMin=0 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --initFromBonly --robustFit=1
Best fit r: 0.0463339  -0.0463339/+99.9537  (68% CL)
nll S+B -> -99.3509  nll B -> -102.474

combine -M MaxLikelihoodFit -d final_unblinding/25bins/datacard_elmu_total_jes.root --setPhysicsModelParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=0,mask_MU_mu8J3M=0,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=0,mask_EL_el8J3M=0,mask_EL_el8J2M=0  --rMax=100 --rMin=-10 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --initFromBonly --robustFit=1

combine -M Asymptotic -d final_unblinding/25bins/datacard_elmu_total_jes.root --setPhysicsModelParameters mask_MU_mu10J4M=0,mask_MU_mu10J3M=0,mask_MU_mu10J2M=0,mask_MU_mu9J4M=0,mask_MU_mu9J3M=0,mask_MU_mu9J2M=0,mask_MU_mu8J4M=0,mask_MU_mu8J3M=0,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=0,mask_EL_el10J3M=0,mask_EL_el10J2M=0,mask_EL_el9J4M=0,mask_EL_el9J3M=0,mask_EL_el9J2M=0,mask_EL_el8J4M=0,mask_EL_el8J3M=0,mask_EL_el8J2M=0  --rMax=100 --rMin=-10 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic


*blind*
Expected  2.5%: r < 3.8111
Expected 16.0%: r < 5.1570
Expected 50.0%: r < 7.3633
Expected 84.0%: r < 10.6212
Expected 97.5%: r < 14.8968

combine -M Asymptotic -d final_unblinding/25bins/datacard_elmu_total_jes.root --setPhysicsModelParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=1,mask_MU_mu8J3M=1,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=1,mask_EL_el8J3M=1,mask_EL_el8J2M=0  --rMax=100 --rMin=0 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic
*aposteriory* CR


combine -M MaxLikelihoodFit -d final_unblinding/50bins/datacard_elmu_total_jes.root --setPhysicsModelParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=0,mask_MU_mu8J3M=0,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=0,mask_EL_el8J3M=0,mask_EL_el8J2M=0  --rMax=100 --rMin=-10 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --initFromBonly --robustFit=1
Best fit r: 15.0172  -25.0172/+84.9828  (68% CL)
nll S+B -> -129.43  nll B -> -128.624
*blind*
 -- Asymptotic -- 
Expected  2.5%: r < 6.9999
Expected 16.0%: r < 9.5773
Expected 50.0%: r < 13.9453
Expected 84.0%: r < 20.5601
Expected 97.5%: r < 28.6669
*aposteriory*
 -- Asymptotic -- 
Observed Limit: r < 37.3739
Expected  2.5%: r < 7.1619
Expected 16.0%: r < 10.0282
Expected 50.0%: r < 14.7266
Expected 84.0%: r < 21.8293
Expected 97.5%: r < 30.8846


combine -M Asymptotic -d final_unblinding/50bins/datacard_elmu_total_jes.root --setPhysicsModelParameters mask_MU_mu10J4M=0,mask_MU_mu10J3M=0,mask_MU_mu10J2M=0,mask_MU_mu9J4M=0,mask_MU_mu9J3M=0,mask_MU_mu9J2M=0,mask_MU_mu8J4M=0,mask_MU_mu8J3M=0,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=0,mask_EL_el10J3M=0,mask_EL_el10J2M=0,mask_EL_el9J4M=0,mask_EL_el9J3M=0,mask_EL_el9J2M=0,mask_EL_el8J4M=0,mask_EL_el8J3M=0,mask_EL_el8J2M=0  --rMax=100 --rMin=-10 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic

 -- Asymptotic -- 
Observed Limit: r < 18.2750
Expected  2.5%: r < 3.7745
Expected 16.0%: r < 5.2081
Expected 50.0%: r < 7.5195
Expected 84.0%: r < 10.9065
Expected 97.5%: r < 15.2511

*blind*
 -- Asymptotic -- 
Expected  2.5%: r < 3.1809
Expected 16.0%: r < 4.4081
Expected 50.0%: r < 6.3867
Expected 84.0%: r < 9.4162
Expected 97.5%: r < 13.2853


combine -M Asymptotic -d final_unblinding/50bins/datacard_elmu_total_jes.root --setPhysicsModelParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=1,mask_MU_mu8J3M=1,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=1,mask_EL_el8J3M=1,mask_EL_el8J2M=0  --rMax=100 --rMin=0 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic
Observed Limit: r < 39.6393
Expected  2.5%: r < 8.7062
Expected 16.0%: r < 12.7191
Expected 50.0%: r < 19.2969
Expected 84.0%: r < 29.0655
Expected 97.5%: r < 42.1371

combine -M MaxLikelihoodFit -d final_unblinding/50bins/datacard_elmu_total_jes.root --setPhysicsModelParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=1,mask_MU_mu8J3M=1,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=1,mask_EL_el8J3M=1,mask_EL_el8J2M=0  --rMax=100 --rMin=0 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --initFromBonly --robustFit=1
Best fit r: 2.76754  -2.76754/+97.2325  (68% CL)







############
python tools/mountainrange_pub.py -j tools/mountainrange_configs/mountain_mu_pub_tttt10_prefit_combo.json final_unblinding/50bins/unblinded_all/mlfit.root -r -b -e png; python tools/mountainrange_pub.py -j tools/mountainrange_configs/mountain_mu_pub_tttt9_prefit_combo.json final_unblinding/50bins/unblinded_all/mlfit.root -r -b -e png; python tools/mountainrange_pub.py -j tools/mountainrange_configs/mountain_mu_pub_tttt8_prefit_combo.json final_unblinding/50bins/unblinded_all/mlfit.root -r -b -e png; python tools/mountainrange_pub.py -j tools/mountainrange_configs/mountain_mu_pub_tttt7_prefit_combo.json final_unblinding/50bins/unblinded_all/mlfit.root -r -b -e png;############
python tools/mountainrange_pub.py -j tools/mountainrange_configs/mountain_el_pub_tttt10_prefit_combo.json final_unblinding/50bins/unblinded_all/mlfit.root -r -b -e png; python tools/mountainrange_pub.py -j tools/mountainrange_configs/mountain_el_pub_tttt9_prefit_combo.json final_unblinding/50bins/unblinded_all/mlfit.root -r -b -e png; python tools/mountainrange_pub.py -j tools/mountainrange_configs/mountain_el_pub_tttt8_prefit_combo.json final_unblinding/50bins/unblinded_all/mlfit.root -r -b -e png;

###################### Free floating normalization

# Sun Nov 26 17:52:04 CET 2017
## Prefit and postfit normalizations
python tools/postfitnorm.py final_unblinding/50bins/unblinded_all/fitDiagnostics_no10j3m.root

# Tue Nov 28 21:16:35 CET 2017
combine -M MaxLikelihoodFit -d final_unblinding/50bins/datacard_elmu_total_jes.root --setPhysicsModelParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=0,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=1,mask_MU_mu8J4M=1,mask_MU_mu8J3M=1,mask_MU_mu8J2M=1,mask_MU_mu7J4M=1,mask_MU_mu7J3M=1,mask_MU_mu7J2M=1,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=1,mask_EL_el8J4M=1,mask_EL_el8J3M=1,mask_EL_el8J2M=1  --rMax=100 --rMin=0 --cminDefaultMinimizerType=Minuit1 --X-rtd MINIMIZER_analytic --freezeNuisances scale_nj6d8s,scale_nj6d9s,scale_nj7d10s,TTJets_norm,ttMEScale,TTJets_HDAMP,TTJets_PDF,heavyFlav,tttt_norm,TTTTMEScale,ST_tW_norm,EW_norm,TTRARE_norm,lumi,PU,JES,JER,leptonSFMu,leptonSFEl,TTISR,TTFSR,TTUE,TTPT,TTTTISR,TTTTFSR,btagWeightCSVJES,btagWeightCSVHF,btagWeightCSVLF,btagWeightCSVHFStats1,btagWeightCSVHFStats2,btagWeightCSVLFStats1,btagWeightCSVLFStats2,btagWeightCSVCFErr1,btagWeightCSVCFErr2,TTJets_norm10 -v2 -S0

# Wed Nov 29 02:18:28 CET 2017
combine -M FitDiagnostics -d final_unblinding/50bins/datacard_elmu_total_jes.root --setParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=1,mask_MU_mu8J4M=0,mask_MU_mu8J3M=1,mask_MU_mu8J2M=1,mask_MU_mu7J4M=1,mask_MU_mu7J3M=1,mask_MU_mu7J2M=1,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=1,mask_EL_el8J4M=1,mask_EL_el8J3M=1,mask_EL_el8J2M=1  --rMax=100 --rMin=0 --cminDefaultMinimizerType=Minuit1 --X-rtd MINIMIZER_analytic --freezeParameters scale_nj6d9s,scale_nj7d10s

# fixing MC stats parameters
combine -M MaxLikelihoodFit -d final_unblinding/50bins/datacard_elmu_total_jes.root --setPhysicsModelParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=1,mask_MU_mu8J4M=0,mask_MU_mu8J3M=1,mask_MU_mu8J2M=1,mask_MU_mu7J4M=1,mask_MU_mu7J3M=1,mask_MU_mu7J2M=1,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=1,mask_EL_el8J4M=1,mask_EL_el8J3M=1,mask_EL_el8J2M=1  --rMax=100 --rMin=0 --cminDefaultMinimizerType=Minuit2 --X-rtd MINIMIZER_analytic --freezeNuisances r,scale_nj6d9s,scale_nj7d10s,rgx{'prop.*'} --robustFit=1 --cminPreScan --cminSingleNuisFit --saveShapes --saveWithUncertainties --saveNormalizations -n _mu84_bg_only

############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
```
combine -M Asymptotic -d final_unblinding/50bins/datacard_elmu_total_jes.root --setParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=1,mask_MU_mu8J4M=1,mask_MU_mu8J3M=0,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=1,mask_EL_el8J4M=1,mask_EL_el8J3M=0,mask_EL_el8J2M=0  --rMax=50 --rMin=0 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --freezeParameters scale_nj6d9s,scale_nj7d10s,rgx{'prop.*'} --picky
```
 -- AsymptoticLimits ( CLs ) --
Observed Limit: r < 33.3652
Expected  2.5%: r < 12.5418
Expected 16.0%: r < 16.9820
Expected 50.0%: r < 24.1406
Expected 84.0%: r < 34.6292
Expected 97.5%: r < 47.8080
```
combine -M FitDiagnostics -d final_unblinding/50bins/datacard_elmu_total_jes.root --setParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=1,mask_MU_mu8J4M=1,mask_MU_mu8J3M=0,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=1,mask_EL_el8J4M=1,mask_EL_el8J3M=0,mask_EL_el8J2M=0  --rMax=50 --rMin=0 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --freezeParameters scale_nj6d9s,scale_nj7d10s,rgx{'prop.*'}
```
 --- FitDiagnostics ---
Best fit r: 12.3447  -12.3447/+10.4649  (68% CL)
```
combine -M Significance -d final_unblinding/50bins/datacard_elmu_total_jes.root --setParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=1,mask_MU_mu8J4M=1,mask_MU_mu8J3M=0,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=1,mask_EL_el8J4M=1,mask_EL_el8J3M=0,mask_EL_el8J2M=0  --rMax=50 --rMin=0 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --freezeParameters scale_nj6d9s,scale_nj7d10s,rgx{'prop.*'}
```
 -- Significance -- 
Significance: 1.26143

```
combine -M Asymptotic -d final_unblinding/50bins/datacard_elmu_total_jes.root --setParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=1,mask_MU_mu8J3M=0,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=1,mask_EL_el8J3M=0,mask_EL_el8J2M=0  --rMax=50 --rMin=0 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --freezeParameters scale_nj7d10s,rgx{'prop.*'}
```
 -- AsymptoticLimits ( CLs ) --
Observed Limit: r < 26.5895
Expected  2.5%: r < 10.0708
Expected 16.0%: r < 13.6924
Expected 50.0%: r < 19.5312
Expected 84.0%: r < 28.0950
Expected 97.5%: r < 38.8532

### observed hybrid limit
```
combine -M HybridNew --LHCmode LHC-limits -d final_unblinding/50bins/datacard_elmu_total_jes.root --setParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=1,mask_MU_mu8J3M=0,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=1,mask_EL_el8J3M=0,mask_EL_el8J2M=0  --rMax=50 --rMin=0 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --freezeParameters scale_nj7d10s,rgx{'prop.*'} --rAbsAcc=1 --rRelAcc=0.2
```
Limit: r < 28.0428 +/- 2.5 @ 95% CL

### expected median limit (takes about 20 mins)
```
combine -M HybridNew --LHCmode LHC-limits -d final_unblinding/50bins/datacard_elmu_total_jes.root --setParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=1,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=0,mask_MU_mu8J4M=1,mask_MU_mu8J3M=0,mask_MU_mu8J2M=0,mask_MU_mu7J4M=0,mask_MU_mu7J3M=0,mask_MU_mu7J2M=0,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=0,mask_EL_el8J4M=1,mask_EL_el8J3M=0,mask_EL_el8J2M=0  --rMax=50 --rMin=0 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --freezeParameters scale_nj7d10s,rgx{'prop.*'} --rAbsAcc=1 --rRelAcc=0.2 --expectedFromGrid=0.5
```
 -- Hybrid New -- 
Limit: r < 19.664 +/- 1.61944 @ 95% CL


#################### Hybrid significance ##########################
step 1:
combine -M HybridNew -d final_unblinding/50bins/datacard_elmu_total_jes.root --setParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=0,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=1,mask_MU_mu8J4M=1,mask_MU_mu8J3M=1,mask_MU_mu8J2M=1,mask_MU_mu7J4M=1,mask_MU_mu7J3M=1,mask_MU_mu7J2M=1,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=1,mask_EL_el8J4M=1,mask_EL_el8J3M=1,mask_EL_el8J2M=1  --rMax=50 --rMin=0 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --LHCmode LHC-significance  --saveToys --fullBToys --saveHybridResult -T 500 -i 1 -s -1

step 2:
combine -M HybridNew -d final_unblinding/50bins/datacard_elmu_total_jes.root --setParameters mask_MU_mu10J4M=1,mask_MU_mu10J3M=0,mask_MU_mu10J2M=1,mask_MU_mu9J4M=1,mask_MU_mu9J3M=1,mask_MU_mu9J2M=1,mask_MU_mu8J4M=1,mask_MU_mu8J3M=1,mask_MU_mu8J2M=1,mask_MU_mu7J4M=1,mask_MU_mu7J3M=1,mask_MU_mu7J2M=1,mask_EL_el10J4M=1,mask_EL_el10J3M=1,mask_EL_el10J2M=1,mask_EL_el9J4M=1,mask_EL_el9J3M=1,mask_EL_el9J2M=1,mask_EL_el8J4M=1,mask_EL_el8J3M=1,mask_EL_el8J2M=1  --rMax=50 --rMin=0 --cminDefaultMinimizerType=Minuit --X-rtd MINIMIZER_analytic --LHCmode LHC-significance  --readHybridResult --toysFile higgsCombineTest.HybridNew.mH120.-1302417571.roo

