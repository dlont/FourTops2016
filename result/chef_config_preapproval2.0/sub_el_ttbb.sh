#!/bin/bash
#PBS -q localgrid
#PBS -l walltime=8:00:00
# setting up your code and your env
source /user/dlontkov/.bash_profile
cd /user/dlontkov/t2016/result/chef_config_preapproval2.0
eval `scramv1 runtime -sh`

#These ENV variables are needed for gfal-copy of the output of FourTops ntupler (defaults are overriden by the FourTops application)
export X509_USER_PROXY=/user/$USER/x509up_u$(id -u $USER)
export PNFS_OUTPUT_DIR=srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/dlontkov/clusteroutput/v0.0.40
export FOURTOPS_OUTFILE=/scratch/$PBS_JOBID/Cran*.root

python ../chef_histogram.py ./plots_el_paperV25/plotprops.txt Craneen__El ./plots_el_paperV25/ttbb ./plots_el_paperV25/plotlist_ttbb.txt  --lumi 35.84 --preselection ./plots_el_paperV25/preselection_ttbb.txt   --weighting ./plots_el_paperV25/weighting.txt --systematics ./plots_el_paperV25/systematics.txt

