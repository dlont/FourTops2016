python ../chef_histogram.py ./plots_mu/plotprops.txt Craneen__Mu ./plots_mu ./plots_mu/plotlist_other.txt --lumi 35.84 --Datalist ./plots_mu/plotlist_Data.txt --preselection ./plots_mu/preselection_normal.txt --weighting ./plots_mu/weighting.txt --systematics ./plots_mu/systematics.txt
python ../chef_histogram.py ./plots_mu/plotprops.txt Craneen__Mu ./plots_mu/ttll ./plots_mu/plotlist_ttll.txt --lumi 35.84 --preselection ./plots_mu/preselection_ttll.txt --weighting ./plots_mu/weighting.txt --systematics ./plots_mu/systematics.txt
python ../chef_histogram.py ./plots_mu/plotprops.txt Craneen__Mu ./plots_mu/ttcc ./plots_mu/plotlist_ttcc.txt --lumi 35.84 --preselection ./plots_mu/preselection_ttcc.txt --weighting ./plots_mu/weighting.txt --systematics ./plots_mu/systematics.txt
python ../chef_histogram.py ./plots_mu/plotprops.txt Craneen__Mu ./plots_mu/ttbb ./plots_mu/plotlist_ttbb.txt --lumi 35.84 --preselection ./plots_mu/preselection_ttbb.txt --weighting ./plots_mu/weighting.txt --systematics ./plots_mu/systematics.txt
##
python ../chef_plot.py ./plots_mu/plotprops_overflow.txt plots_mu/2018-07-17-1358 plots_mu/histogram_list.txt --DataHist plots_mu/hist_Data.root --DataName "Single #mu" --preselection --weighting plots_mu/weighting.txt --lumi 35.84 --outputName plots_mu/hist_single_muon_overflow_fixrange.root --systematics plots_mu/systematics.txt
python ../chef_plot.py ./plots_mu/plotprops_no_overflow.txt plots_mu/2018-07-17-1358 plots_mu/histogram_list.txt --DataHist plots_mu/hist_Data.root --DataName "Single #mu" --preselection --weighting plots_mu/weighting.txt --lumi 35.84 --outputName plots_mu/hist_single_muon_noOverflow_fixrange.root --systematics plots_mu/systematics.txt --noOverflow
