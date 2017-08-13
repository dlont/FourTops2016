#!/bin/bash

folderwithmergedcraneens=plots_mu_toppt
targetvar=''
########################################
#              MUON CARDS/POSTFIT PLOTS
########################################
for targetvar in LeptonPt NjetsW multitopness HTb HTH HTX SumJetMassX 1stjetpt 2ndjetpt 5thjetpt 6thjetpt csvJetcsv3 csvJetcsv4
do
	echo "$targetvar"
	mkdir $folderwithmergedcraneens\_$targetvar
	for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` $folderwithmergedcraneens\_$targetvar/`basename $i`;done
	make -t -j card_mu.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$folderwithmergedcraneens\_$targetvar/ DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu TARGETVAR=$targetvar
	rm $folderwithmergedcraneens\_$targetvar/Hist*.root
	make -j card_mu.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$folderwithmergedcraneens\_$targetvar/ DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu TARGETVAR=$targetvar
done
