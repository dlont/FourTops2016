#!/bin/bash
#PBS -q localgrid
#PBS -l walltime=3:00:00
# setting up your code and your env
source /user/dlontkov/.bash_profile
cd /user/dlontkov/CMSSW_8_0_21/src/TopBrussels/FourTops2016
eval `scramv1 runtime -sh`

# want you really want to do!!

