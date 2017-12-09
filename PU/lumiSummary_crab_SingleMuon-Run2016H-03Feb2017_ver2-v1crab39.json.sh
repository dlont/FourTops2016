#!/bin/bash
#PBS -q localgrid
#PBS -l walltime=4:00:00
# setting up your code and your env
source /user/dlontkov/.bash_profile
cd /user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016
eval `scramv1 runtime -sh`

# want you really want to do!!

/storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/PU/producePU.zsh /storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/PU/Freya_crab_jsons/lumiSummary_crab_SingleMuon-Run2016H-03Feb2017_ver2-v1crab39.json Run2016H-03Feb2017_ver2-v1crab39
