#!/bin/bash
set -o xtrace
# python ../chef_histogram.py ./plots_el_paper_postCWR/plotprops.txt Craneen__El ./plots_el_paper_postCWR      ./plots_el_paper_postCWR/plotlist_other.txt --lumi 35.84 --preselection ./plots_el_paper_postCWR/preselection_normal.txt --weighting ./plots_el_paper_postCWR/weighting.txt --systematics ./plots_el_paper_postCWR/systematics.txt --Datalist ./plots_el_paper_postCWR/plotlist_Data.txt 
# python ../chef_histogram.py ./plots_el_paper_postCWR/plotprops.txt Craneen__El ./plots_el_paper_postCWR/ttll ./plots_el_paper_postCWR/plotlist_ttll.txt  --lumi 35.84 --preselection ./plots_el_paper_postCWR/preselection_ttll.txt   --weighting ./plots_el_paper_postCWR/weighting.txt --systematics ./plots_el_paper_postCWR/systematics.txt
# python ../chef_histogram.py ./plots_el_paper_postCWR/plotprops.txt Craneen__El ./plots_el_paper_postCWR/ttcc ./plots_el_paper_postCWR/plotlist_ttcc.txt  --lumi 35.84 --preselection ./plots_el_paper_postCWR/preselection_ttcc.txt   --weighting ./plots_el_paper_postCWR/weighting.txt --systematics ./plots_el_paper_postCWR/systematics.txt
# python ../chef_histogram.py ./plots_el_paper_postCWR/plotprops.txt Craneen__El ./plots_el_paper_postCWR/ttbb ./plots_el_paper_postCWR/plotlist_ttbb.txt  --lumi 35.84 --preselection ./plots_el_paper_postCWR/preselection_ttbb.txt   --weighting ./plots_el_paper_postCWR/weighting.txt --systematics ./plots_el_paper_postCWR/systematics.txt
##
dir_name=plots_el_paper_postCWR/2019-05-04-2111
mkdir $dir_name
python ../chef_plot_v2.py --no-entries ./plots_el_paper_postCWR/plotprops_overflow.txt    $dir_name plots_el_paper_postCWR/histogram_list.txt --DataHist plots_el_paper_postCWR/hist_Data.root --DataName "Single lepton: e" --preselection --weighting plots_el_paper_postCWR/weighting.txt --lumi 35.84 --outputName plots_el_paper_postCWR/hist_single_electron_overflow_fixrange.root   --systematics plots_el_paper_postCWR/systematics.txt
python ../chef_plot_v2.py --no-entries ./plots_el_paper_postCWR/plotprops_no_overflow.txt $dir_name plots_el_paper_postCWR/histogram_list.txt --DataHist plots_el_paper_postCWR/hist_Data.root --DataName "Single lepton: e" --preselection --weighting plots_el_paper_postCWR/weighting.txt --lumi 35.84 --outputName plots_el_paper_postCWR/hist_single_electron_noOverflow_fixrange.root --systematics plots_el_paper_postCWR/systematics.txt --noOverflow
set +o xtrace
