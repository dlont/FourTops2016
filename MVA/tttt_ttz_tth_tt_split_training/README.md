# Build instructions

#Debug

```bash
mkdir build; cd !$;
cmake .. -DTopBrussels_SOURCE_DIR=/storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels -DCMAKE_BUILD_TYPE=Debug
make; make install
```

#Release

```bash
mkdir build; cd !$;
cmake .. -DTopBrussels_SOURCE_DIR=/storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels -DCMAKE_BUILD_TYPE=Release
make; make install
```

#Usage
```
./MVATrainer --background_craneens /user/dlontkov/t2016/result/final_unblinding/rare_tthz_ttwxy_merge_50bins/plots_mu/Craneen_TTJets_powheg_Run2_TopTree_Study.root,/user/dlontkov/t2016/result/final_unblinding/rare_tthz_ttwxy_merge_50bins/plots_mu/Craneen_TTH_Run2_TopTree_Study.root,/user/dlontkov/t2016/result/final_unblinding/rare_tthz_ttwxy_merge_50bins/plots_mu/Craneen_TTZ_Run2_TopTree_Study.root --signal_craneens=/user/dlontkov/t2016/result/final_unblinding/rare_tthz_ttwxy_merge_50bins/plots_mu/Craneen_ttttNLO_Run2_TopTree_Study.root
```
