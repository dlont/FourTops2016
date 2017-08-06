#!/bin/bash

folderwithmergedcraneens=plots_mu_toppt
targetvar=''
########################################
#              MUON CARDS/POSTFIT PLOTS
########################################
#mkdir plots_mu_toppt_LeptonPt
#for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` plots_mu_toppt_LeptonPt/`basename $i`;done
#
#mkdir plots_mu_toppt_NjetsW
#for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` plots_mu_toppt_NjetsW/`basename $i`;done
#
#mkdir plots_mu_toppt_multitopness
#for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` plots_mu_toppt_multitopness/`basename $i`;done
#make -t -j card_mu.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=plots_mu_toppt_multitopness/ DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu TARGETVAR=multitopness
#rm plots_mu_toppt_multitopness/Hist*.root
#make -j card_mu.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=plots_mu_toppt_multitopness/ DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu TARGETVAR=multitopness

#folderwithmergedcraneens=plots_mu_toppt
#targetvar=HTb
#mkdir plots_mu_toppt_$targetvar
#for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` plots_mu_toppt_$targetvar/`basename $i`;done
#make -t -j card_mu.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=plots_mu_toppt_$targetvar/ DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu TARGETVAR=$targetvar
#rm plots_mu_toppt_$targetvar/Hist*.root
#make -j card_mu.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=plots_mu_toppt_$targetvar/ DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu TARGETVAR=$targetvar


#for targetvar in HTb HTH HTX SumJetMassX 1stjetpt 2ndjetpt 5thjetpt 6thjetpt csvJetcsv3 csvJetcsv4
folderwithmergedcraneens=plots_mu_toppt
for targetvar in HTH HTX SumJetMassX 1stjetpt 2ndjetpt 5thjetpt 6thjetpt csvJetcsv3 csvJetcsv4
do
	echo "$targetvar"
	mkdir $folderwithmergedcraneens\_$targetvar
	for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` $folderwithmergedcraneens\_$targetvar/`basename $i`;done
	make -t -j card_mu.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$folderwithmergedcraneens\_$targetvar/ DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu TARGETVAR=$targetvar
	rm $folderwithmergedcraneens\_$targetvar/Hist*.root
	make -j card_mu.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$folderwithmergedcraneens\_$targetvar/ DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu TARGETVAR=$targetvar
done
