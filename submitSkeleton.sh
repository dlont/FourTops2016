#!/bin/bash
#PBS -q localgrid
#PBS -l walltime=8:00:00
# setting up your code and your env
source /user/dlontkov/.bash_profile
cd /user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016
eval `scramv1 runtime -sh`

#These ENV variables are needed for gfal-copy of the output of FourTops ntupler (defaults are overriden by the FourTops application)
export X509_USER_PROXY=/user/$USER/x509up_u$(id -u $USER)
export PNFS_OUTPUT_DIR=srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/dlontkov/clusteroutput/v0.0.42cutflow
export FOURTOPS_OUTFILE=/scratch/$PBS_JOBID/Cran*.root

# want you really want to do!!

