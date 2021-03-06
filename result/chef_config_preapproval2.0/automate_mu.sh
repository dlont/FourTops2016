#!/bin/bash
set -o xtrace
# python ../chef_histogram.py ./plots_mu/plotprops.txt Craneen__Mu ./plots_mu      ./plots_mu/plotlist_other.txt --lumi 35.84 --preselection ./plots_mu/preselection_normal.txt --weighting ./plots_mu/weighting.txt --systematics ./plots_mu/systematics.txt  --Datalist ./plots_mu/plotlist_Data.txt
# python ../chef_histogram.py ./plots_mu/plotprops.txt Craneen__Mu ./plots_mu/ttll ./plots_mu/plotlist_ttll.txt  --lumi 35.84 --preselection ./plots_mu/preselection_ttll.txt   --weighting ./plots_mu/weighting.txt --systematics ./plots_mu/systematics.txt
# python ../chef_histogram.py ./plots_mu/plotprops.txt Craneen__Mu ./plots_mu/ttcc ./plots_mu/plotlist_ttcc.txt  --lumi 35.84 --preselection ./plots_mu/preselection_ttcc.txt   --weighting ./plots_mu/weighting.txt --systematics ./plots_mu/systematics.txt
# python ../chef_histogram.py ./plots_mu/plotprops.txt Craneen__Mu ./plots_mu/ttbb ./plots_mu/plotlist_ttbb.txt  --lumi 35.84 --preselection ./plots_mu/preselection_ttbb.txt   --weighting ./plots_mu/weighting.txt --systematics ./plots_mu/systematics.txt
##
dir_name=plots_mu_paper_postCWR_pt35/2019-05-07
mkdir $dir_name
python ../chef_plot_v2.py --no-entries ./plots_mu_paper_postCWR_pt35/plotprops_overflow.txt    $dir_name plots_mu_paper_postCWR_pt35/histogram_list.txt --DataHist plots_mu_paper_postCWR_pt35/hist_Data.root --DataName "Single lepton: #mu" --preselection --weighting plots_mu_paper_postCWR_pt35/weighting.txt --lumi 35.84 --outputName plots_mu_paper_postCWR_pt35/hist_single_muon_overflow_fixrange.root --systematics plots_mu_paper_postCWR_pt35/systematics.txt
python ../chef_plot_v2.py --no-entries ./plots_mu_paper_postCWR_pt35/plotprops_no_overflow.txt $dir_name plots_mu_paper_postCWR_pt35/histogram_list.txt --DataHist plots_mu_paper_postCWR_pt35/hist_Data.root --DataName "Single lepton: #mu" --preselection --weighting plots_mu_paper_postCWR_pt35/weighting.txt --lumi 35.84 --outputName plots_mu_paper_postCWR_pt35/hist_single_muon_noOverflow_fixrange.root --systematics plots_mu_paper_postCWR_pt35/systematics.txt --noOverflow
set +o xtrace
