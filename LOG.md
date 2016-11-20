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
Sample          2016B           2016C           2016D           2016E           2016F           2016G           2016H           SUM (mb^-1)
repro_v3
SingleMuon      5840063059.395  2523447696.817  4275320129.305  3839184008.312  2898669614.585  7383952466.412  8283713045.538 35044350020.364
repro_v0
SingleMuon      5208746535.071  2448756618.041  4201921158.859  4049732039.245  3147822524.876  7554453625.468  5476961519.179 32088394020.739


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
repro_v3
TT (35044350020.364/330572000000.9128594787=0.01525945942)
repro_0
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


