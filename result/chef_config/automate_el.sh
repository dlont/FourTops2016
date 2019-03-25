python ../chef_histogram.py ./plots_el/plotprops.txt Craneen__El ./plots_el ./plots_el/plotlist_other.txt --lumi 35.84 --Datalist ./plots_el/plotlist_Data.txt --preselection ./plots_el/preselection_normal.txt --weighting ./plots_el/weighting.txt --systematics ./plots_el/systematics.txt
python ../chef_histogram.py ./plots_el/plotprops.txt Craneen__El ./plots_el/ttll ./plots_el/plotlist_ttll.txt --lumi 35.84 --preselection ./plots_el/preselection_ttll.txt --weighting ./plots_el/weighting.txt --systematics ./plots_el/systematics.txt
python ../chef_histogram.py ./plots_el/plotprops.txt Craneen__El ./plots_el/ttcc ./plots_el/plotlist_ttcc.txt --lumi 35.84 --preselection ./plots_el/preselection_ttcc.txt --weighting ./plots_el/weighting.txt --systematics ./plots_el/systematics.txt
python ../chef_histogram.py ./plots_el/plotprops.txt Craneen__El ./plots_el/ttbb ./plots_el/plotlist_ttbb.txt --lumi 35.84 --preselection ./plots_el/preselection_ttbb.txt --weighting ./plots_el/weighting.txt --systematics ./plots_el/systematics.txt
#
python ../chef_plot.py ./plots_el/plotprops_overflow.txt plots_el/2018-07-1355/8J4M plots_el/histogram_list.txt --DataHist plots_el/hist_Data.root --DataName "Single e" --preselection --weighting plots_el/weighting.txt --lumi 35.84 --outputName plots_el/hist_single_electron_overflow_fixrange.root --systematics plots_el/systematics.txt
python ../chef_plot.py ./plots_el/plotprops_no_overflow.txt plots_el/2018-07-1355/8J4M plots_el/histogram_list.txt --DataHist plots_el/hist_Data.root --DataName "Single e" --preselection --weighting plots_el/weighting.txt --lumi 35.84 --outputName plots_el/hist_single_electron_noOverflow_fixrange.root --systematics plots_el/systematics.txt --noOverflow
