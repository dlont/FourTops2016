#!/bin/bash
set -o xtrace
# python ../chef_histogram.py ./plots_el_paperV25/plotprops.txt Craneen__El ./plots_el_paperV25      ./plots_el_paperV25/plotlist_other.txt --lumi 35.84 --preselection ./plots_el_paperV25/preselection_normal.txt --weighting ./plots_el_paperV25/weighting.txt --systematics ./plots_el_paperV25/systematics.txt --Datalist ./plots_el_paperV25/plotlist_Data.txt 
# python ../chef_histogram.py ./plots_el_paperV25/plotprops.txt Craneen__El ./plots_el_paperV25/ttll ./plots_el_paperV25/plotlist_ttll.txt  --lumi 35.84 --preselection ./plots_el_paperV25/preselection_ttll.txt   --weighting ./plots_el_paperV25/weighting.txt --systematics ./plots_el_paperV25/systematics.txt
# python ../chef_histogram.py ./plots_el_paperV25/plotprops.txt Craneen__El ./plots_el_paperV25/ttcc ./plots_el_paperV25/plotlist_ttcc.txt  --lumi 35.84 --preselection ./plots_el_paperV25/preselection_ttcc.txt   --weighting ./plots_el_paperV25/weighting.txt --systematics ./plots_el_paperV25/systematics.txt
# python ../chef_histogram.py ./plots_el_paperV25/plotprops.txt Craneen__El ./plots_el_paperV25/ttbb ./plots_el_paperV25/plotlist_ttbb.txt  --lumi 35.84 --preselection ./plots_el_paperV25/preselection_ttbb.txt   --weighting ./plots_el_paperV25/weighting.txt --systematics ./plots_el_paperV25/systematics.txt
##
dir_name=plots_el_paperV25/2019-01-31-1259
mkdir $dir_name
python ../chef_plot_v2.py ./plots_el_paperV25/plotprops_overflow.txt    $dir_name plots_el_paperV25/histogram_list.txt --DataHist plots_el_paperV25/hist_Data.root --DataName "Single lepton: e" --preselection --weighting plots_el_paperV25/weighting.txt --lumi 35.84 --outputName plots_el_paperV25/hist_single_electron_overflow_fixrange.root   --systematics plots_el_paperV25/systematics.txt
python ../chef_plot_v2.py ./plots_el_paperV25/plotprops_no_overflow.txt $dir_name plots_el_paperV25/histogram_list.txt --DataHist plots_el_paperV25/hist_Data.root --DataName "Single lepton: e" --preselection --weighting plots_el_paperV25/weighting.txt --lumi 35.84 --outputName plots_el_paperV25/hist_single_electron_noOverflow_fixrange.root --systematics plots_el_paperV25/systematics.txt --noOverflow
set +o xtrace
