# FourTops2016
2016 data analysis repository

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



