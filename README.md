# FourTops2016
2016 data analysis repository
## Prerequisites 
1. autotools (present at T2_BE_IIHE but not available at lxplus)

## Installation
0. a) Create CMSSW development area
0. b) Install TTP/TTAB
1. Download [FourTop2016] (https://github.com/dlont/FourTops2016) code
2. Download [gflags] (https://github.com/gflags/gflags)
3. Download [glog] (https://github.com/google/glog)
4. Optional. Download [StatTest](https://github.com/andreadotti/StatTest)

cmsrel CMSSW_8_0_26_patch1
cd CMSSW_8_0_26_patch1/src
cmsenv

git clone http://github.com/TopBrussels/TopTreeProducer --branch CMSSW_80X --single-branch TopBrussels/TopTreeProducer
cd TopBrussels/TopTreeProducer/src
make
cd -

git clone http://github.com/TopBrussels/TopTreeAnalysisBase --branch CMSSW_80X --single-branch TopBrussels/TopTreeAnalysisBase
cd TopBrussels/TopTreeAnalysisBase/
#Repalace Tools/*/BTagWeigtTools*
make -j
cd -

git lfs clone https://github.com/dlont/FourTops2016.git --single-branch TopBrussels/FourTops2016
cd TopBrussels/FourTops2016

git clone https://github.com/gflags/gflags.git gflags-install
cd gflags-install
git checkout tags/v2.2.0
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$CMSSW_BASE/src/TopBrussels/FourTops2016/gflags
make -j
make install
cd $CMSSW_BASE/src/TopBrussels/FourTops2016

git clone https://github.com/google/glog.git glog-install
cd glog-install
git checkout tags/v0.3.3
./configure --prefix=$CMSSW_BASE/src/TopBrussels/FourTops2016/glog
make
make install
cd -

mkdir build; cd build
cmake .. -DTopBrussels_SOURCE_DIR=$CMSSW_BASE/src/TopBrussels -DCMAKE_INSTALL_PREFIX=$CMSSW_BASE/src/TopBrussels/FourTops2016
make -j; make install
cd -

git clone https://github.com/dlont/FourTops2016.git --single-branch -b split_tthz_ttwxy_combined TopBrussels/FourTops2016


----------------------------
scramv1 project -n FourTops_8_0_26_patch1 CMSSW CMSSW_8_0_26_patch1
cd FourTops_8_0_26_patch1/src
cmsenv

git clone http://github.com/TopBrussels/TopTreeProducer --branch CMSSW_80X --single-branch TopBrussels/TopTreeProducer
cd TopBrussels/TopTreeProducer/src
make
cd -

cd TopBrussels
cp -a -f ~/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/TopTreeAnalysisBase  .
#git clone http://github.com/TopBrussels/TopTreeAnalysisBase --branch CMSSW_80X --single-branch TopBrussels/TopTreeAnalysisBase
#cd TopBrussels/TopTreeAnalysisBase/
##Repalace Tools/*/BTagWeigtTools*
#make -j
cd -

git clone https://github.com/dlont/FourTops2016.git --single-branch -b split_tthz_ttwxy_combined TopBrussels/FourTops2016
cd TopBrussels/FourTops2016
git fetch --tags
git checkout tags/v0.0.38patch1 -b v0.0.38patch1

git clone https://github.com/gflags/gflags.git gflags-install
cd gflags-install
git checkout tags/v2.2.0
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$CMSSW_BASE/src/TopBrussels/FourTops2016/gflags
make -j
make install
cd -
cd ..


git clone https://github.com/google/glog.git glog-install
cd glog-install
git checkout tags/v0.3.3
./configure --prefix=$CMSSW_BASE/src/TopBrussels/FourTops2016/glog
make
make install
cd -

mkdir build; cd build
cmake .. -DTopBrussels_SOURCE_DIR=$CMSSW_BASE/src/TopBrussels -DCMAKE_INSTALL_PREFIX=$CMSSW_BASE/src/TopBrussels/FourTops2016
make -j; make install
cd -

## Testing

mkdir output

./FourTops --dataset_name="TTJetsFilt_powheg_central" --dataset_title="t\bar{t}+jets_powheg" --dataset_color=633 --dataset_linestyle=0 --dataset_linewidth=2 --dataset_norm_factor=1 --dataset_eq_lumi=1. --dataset_cross_section=831.76 --dataset_preselection_eff=1.0 --nevents=1000 --input_files="dcap://maite.iihe.ac.be/pnfs/iihe/cms/store/user/fblekman/TopTree/CMSSW_80X_v12/TTP-CMSSW_80X_v12--GT-80X_mcRun2_asymptotic_2016_TrancheIV_v8/TTToSemiLepton_HT500Njet9_TuneCUETP8M2T4_13TeV-powheg-pythia8/crab_P8M2T413TeVpowhegpythia8RunIISummer16MiniAODv2PUMoriond1780XmcRun2asymptotic2016TrancheIVv6v1crab292/180403_190034/0000/TOPTREE_100.root "  --fourtops_channel="Mu2016" -is_local_output
