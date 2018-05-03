# FourTops2016
2016 data analysis repository
## Prerequisites 
1. autotools (present at T2_BE_IIHE but not available at lxplus)
2. Higgs combine (https://cms-hcomb.gitbooks.io/combine/content/)
3. There should be 

## Installation outline
0. a) Create CMSSW development area
0. b) Install TTP/TTAB
1. Download [FourTop2016] (https://github.com/dlont/FourTops2016) code
2. Download [gflags] (https://github.com/gflags/gflags)
3. Download [glog] (https://github.com/google/glog)
4. Optional. Download [StatTest](https://github.com/andreadotti/StatTest)

----------------------------

## Installation steps
```
scramv1 project -n FourTops_8_0_26_patch1 CMSSW CMSSW_8_0_26_patch1
cd FourTops_8_0_26_patch1/src
cmsenv

git clone http://github.com/TopBrussels/TopTreeProducer --branch CMSSW_80X --single-branch TopBrussels/TopTreeProducer
cd TopBrussels/TopTreeProducer/src
make
cd -

cp -a -f ~dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/TopTreeAnalysisBase  TopBrussels/TopTreeAnalysisBase
#git clone http://github.com/TopBrussels/TopTreeAnalysisBase --branch CMSSW_80X --single-branch TopBrussels/TopTreeAnalysisBase
cd TopBrussels/TopTreeAnalysisBase
make -j
cd -

git clone https://github.com/dlont/FourTops2016.git --single-branch -b master TopBrussels/FourTops2016
cd TopBrussels/FourTops2016

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
```
## Testing
```
mkdir output

./FourTops --dataset_name="TTJetsFilt_powheg_central" --dataset_title="t\bar{t}+jets_powheg" --dataset_color=633 --dataset_linestyle=0 --dataset_linewidth=2 --dataset_norm_factor=1 --dataset_eq_lumi=1. --dataset_cross_section=831.76 --dataset_preselection_eff=1.0 --nevents=1000 --input_files="dcap://maite.iihe.ac.be/pnfs/iihe/cms/store/user/fblekman/TopTree/CMSSW_80X_v12/TTP-CMSSW_80X_v12--GT-80X_mcRun2_asymptotic_2016_TrancheIV_v8/TTToSemiLepton_HT500Njet9_TuneCUETP8M2T4_13TeV-powheg-pythia8/crab_P8M2T413TeVpowhegpythia8RunIISummer16MiniAODv2PUMoriond1780XmcRun2asymptotic2016TrancheIVv6v1crab292/180403_190034/0000/TOPTREE_100.root "  --fourtops_channel="Mu2016" -is_local_output
```
### This should make small output craneen in the output folder

## Using existing craneens for datacards and fits
```
cp -a /user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_el_filt result
cp -a /user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt result
cd result
```
### Make datacards
```
make -j card_el.txt INPUTLOCATION=plots_el_filt BUILDDIR=plots_el_filt TREENAME=Craneen__El DATALABEL=Single\ e
make -j card_mu.txt INPUTLOCATION=plots_mu_filt BUILDDIR=plots_mu_filt TREENAME=Craneen__Mu DATALABEL=Single\ \#mu
make -j datacard_elmu.txt BUILDDIR_EL=plots_el_filt BUILDDIR_MU=plots_mu_filt BUILDDIR=.
```
### Convert datacards to root format
```
text2workspace.py --channel-masks plots_el_filt/card_el.txt
text2workspace.py --channel-masks plots_mu_filt/card_mu.txt
text2workspace.py --channel-masks datacard_elmu.txt
```

### Fits and limits
```
combine -M FitDiagnostics datacard_elmu.root --saveShapes --saveWithUncertainties --saveNormalizations --X-rtd MINIMIZER_analytic # this command produces fitDiagnostics.root file with pre-(post-)fit templates, etc. This file is used as input for pulls, correlations, plots
combine -M AsimptoticLimits datacard_elmu.root --X-rtd MINIMIZER_analytic
```
### In order to blind a channel
```
combine -M FitDiagnostics datacard_elmu.root --X-rtd MINIMIZER_analytic --setParameters mask_EL_el10J3M=1 
```
### Pulls
```
python tools/nuispulls/diffNuisances_denys.py fitDiagnostics.root -g pulls.root
python tools/nuispulls/plot_nuis_pulls.py pulls.root -o pulls -e pdf
```
### Correlations
```
python tools/corrmatrix/plot_corr_matrix.py fitDiagnostics.root -e pdf
```
### Post-fit BDT plots
```
python tools/mountainrange/mountainrange_pub_raresplit.py fitDiagnostics.root conf.json -b -r -e pdf,png --dir ./
```
