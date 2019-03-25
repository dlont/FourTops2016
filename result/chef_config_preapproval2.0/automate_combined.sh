#!/bin/bash
set -o xtrace
#source automate_mu.sh
#source automate_el.sh
##
dir_name=plots_combined/`date +%F-%H%M`
mkdir $dir_name

#merge muons and electrons
hadd -f plots_combined/hist_Data.root          plots_mu/hist_Data.root        plots_el/hist_Data.root
#hadd -f plots_combined/hist_TTXY.root          plots_mu/hist_TTXY.root        plots_el/hist_TTXY.root
hadd -f plots_combined/hist_TTW_XY.root          plots_mu/hist_TTW_XY.root        plots_el/hist_TTW_XY.root
hadd -f plots_combined/hist_TTV.root           plots_mu/hist_TTV.root         plots_el/hist_TTV.root
#hadd -f plots_combined/hist_TTH.root           plots_mu/hist_TTH.root         plots_el/hist_TTH.root
hadd -f plots_combined/hist_TTH_Z.root           plots_mu/hist_TTH_Z.root         plots_el/hist_TTH_Z.root
hadd -f plots_combined/hist_EW.root            plots_mu/hist_EW.root          plots_el/hist_EW.root
hadd -f plots_combined/hist_Single-top.root    plots_mu/hist_Single-top.root  plots_el/hist_Single-top.root
hadd -f plots_combined/ttll/hist_ttbar.root    plots_mu/ttll/hist_ttbar.root  plots_el/ttll/hist_ttbar.root
hadd -f plots_combined/ttcc/hist_ttbar.root    plots_mu/ttcc/hist_ttbar.root  plots_el/ttcc/hist_ttbar.root
hadd -f plots_combined/ttbb/hist_ttbar.root    plots_mu/ttbb/hist_ttbar.root  plots_el/ttbb/hist_ttbar.root
hadd -f plots_combined/hist_tttt.root          plots_mu/hist_tttt.root        plots_el/hist_tttt.root

python ../chef_plot_v2.py ./plots_combined/plotprops_overflow.txt    $dir_name plots_combined/histogram_list.txt --DataHist plots_combined/hist_Data.root --DataName "Single lepton: e+#mu" --preselection --weighting plots_combined/weighting.txt --lumi 35.84 --outputName plots_combined/hist_combined_overflow_fixrange.root --systematics plots_combined/systematics.txt
python ../chef_plot_v2.py ./plots_combined/plotprops_no_overflow.txt $dir_name plots_combined/histogram_list.txt --DataHist plots_combined/hist_Data.root --DataName "Single lepton: e+#mu" --preselection --weighting plots_combined/weighting.txt --lumi 35.84 --outputName plots_combined/hist_combined_noOverflow_fixrange.root --systematics plots_combined/systematics.txt --noOverflow
set +o xtrace
