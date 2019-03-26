# FourTops2016
2016 data analysis repository
## Prerequisites 

Let's call the root folder where the codes will be installed, i.e. 

0. about 1Gb space
1. autotools (present at T2_BE_IIHE and lxplus)
2. Higgs combine (https://cms-hcomb.gitbooks.io/combine/content/)
3. There should exist  `~/lib` folder for files from different packages (```mkdir ~/lib```)
  * **NOTE:** `~/lib` should be added to `$LD_LIBRARY_PATH` (```export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/lib```)
4. CMSSW environment has to be 

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
# if intalling on lxplus
# rsync -r username@mshort.iihe.ac.be:~dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/TopTreeAnalysisBase  TopBrussels
cd TopBrussels/TopTreeAnalysisBase
make -j
cd -

git clone https://github.com/dlont/FourTops2016.git --single-branch -b master TopBrussels/FourTops2016
cd TopBrussels/FourTops2016
cp ana/src/VecTLorentzVector_rdict.pcm ~/lib

cd rootplot
export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/TopBrussels/FourTops2016/rootplot/lib/python2.7/site-packages
python setup.py develop --prefix=$CMSSW_BASE/src/TopBrussels/FourTops2016/rootplot
cd -

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
cp -d $CMSSW_BASE/src/TopBrussels/FourTops2016/glog/lib/*.so* ~/lib
cd -

mkdir build; cd build
cmake .. -DTopBrussels_SOURCE_DIR=$CMSSW_BASE/src/TopBrussels -DCMAKE_INSTALL_PREFIX=$CMSSW_BASE/src/TopBrussels/FourTops2016
make -j; make install
cd -
```
## Testing
```

mkdir output
./FourTops --dataset_name="TTJetsFilt_powheg_central" --dataset_title="t\bar{t}+jets_powheg" --dataset_color=633 --dataset_linestyle=0 --dataset_linewidth=2 --dataset_norm_factor=1 --dataset_eq_lumi=1. --dataset_cross_section=831.76 --dataset_preselection_eff=1.0 --nevents=10000 --input_files="dcap://maite.iihe.ac.be/pnfs/iihe/cms/store/user/fblekman/TopTree/CMSSW_80X_v12/TTP-CMSSW_80X_v12--GT-80X_mcRun2_asymptotic_2016_TrancheIV_v8/TTToSemiLepton_HT500Njet9_TuneCUETP8M2T4_13TeV-powheg-pythia8/crab_P8M2T413TeVpowhegpythia8RunIISummer16MiniAODv2PUMoriond1780XmcRun2asymptotic2016TrancheIVv6v1crab292/180403_190034/0000/TOPTREE_100.root "  --fourtops_channel="Mu2016" -is_local_output

# if at lxplus
# rsync --progress username@mshort.iihe.ac.be:/pnfs/iihe/cms/store/user/fblekman/TopTree/CMSSW_80X_v12/TTP-CMSSW_80X_v12--GT-80X_mcRun2_asymptotic_2016_TrancheIV_v8/TTToSemiLepton_HT500Njet9_TuneCUETP8M2T4_13TeV-powheg-pythia8/crab_P8M2T413TeVpowhegpythia8RunIISummer16MiniAODv2PUMoriond1780XmcRun2asymptotic2016TrancheIVv6v1crab292/180403_190034/0000/TOPTREE_100.root .
#./FourTops --dataset_name="TTJetsFilt_powheg_central" --dataset_title="t\bar{t}+jets_powheg" --dataset_color=633 --dataset_linestyle=0 --dataset_linewidth=2 --dataset_norm_factor=1 --dataset_eq_lumi=1. --dataset_cross_section=831.76 --dataset_preselection_eff=1.0 --nevents=10000 --input_files="TOPTREE_100.root "  --fourtops_channel="Mu2016" -is_local_output
```
### This should make small output craneen in the output folder

## Using existing craneens for datacards and fits
```
mkdir result/plots_el_filt
mkdir result/plots_mu_filt
cp -s /user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_el_filt/Cran* result/plots_el_filt
cp -s /user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt/Cran* result/plots_mu_filt
cd result
```

### Compare data and systematic templates histogram
```
#short help command
python $CMSSW_BASE/src/TopBrussels/FourTops2016/result/tools/compare_hist_files/compare.py  --usage

#example usage for comparison of btag templates. Input path for histogram files in the _cff.py has to be modified accordingly
python $CMSSW_BASE/src/TopBrussels/FourTops2016/result/tools/compare_hist_files/compare.py -c $CMSSW_BASE/src/TopBrussels/FourTops2016/result/tools/compare_hist_files/config/conf_btag_JES_cff.py -b --dir ./ -o btag_jes -e png,pdf
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

### Adding friend tree with new MVA python discriminator to existing craneen
One need a disciminator that is stored in a pickle (.p) file. This .p file will be read by the python script which creates the friend branch.
Short usage information
```
python ../../tools/addfriend_freya_njets_nonjetsw.py --usage
```
Example processing of existing craneen file named ../../final_unblinding/50bins/plots_mu/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root. Since the improved dicriminants were trained independently in different jet multiplicity categories, the pickle files that have to be used in different jet categories are provided via .json dictionary **(-j flag)**.
```
python ../../tools/addfriend_freya_njets_nonjetsw.py -j '{"10j":"../../../MVA/Freyas/noNjetsW/BDTAdaBoost_njets10_400_2.p", "9j":"../../../MVA/Freyas/noNjetsW/BDTAdaBoost_njets9_400_2.p", "8j":"../../../MVA/Freyas/noNjetsW/BDTAdaBoost_njets8_400_2.p", "7j":"../../../MVA/Freyas/noNjetsW/BDTAdaBoost_njets7_40_2.p"}' -s Craneen__Mu -f BDT9and10jetsplitNoNjw ../../final_unblinding/50bins/plots_mu/Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root
```

