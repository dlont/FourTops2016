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
