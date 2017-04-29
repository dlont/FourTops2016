#!/bin/bash

# +- 5% variations
# cross section source: https://twiki.cern.ch/twiki/bin/viewauth/CMS/POGRecipesICHEP2016
# 69.2
xsec=("65740.00" "69200" "72660.00")
tag=("Down" "Nom" "Up")

idx=0
for i in ${xsec[@]}
do
echo $i "pileup$2"${tag[${idx}]} Pileup$2${tag[${idx}]}.root
 pileupCalc.py -i $1 \
--inputLumiJSON /storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/PU/pileup_latest.txt \
--calcMode observed \
--minBiasXsec ${i} \
--maxPileupBin 100 \
--numPileupBins 100 \
--pileupHistName "pileup$2"${tag[${idx}]} \
 /storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/PU/PileupObs$2${tag[${idx}]}.root
idx=$(($idx+1))
done
