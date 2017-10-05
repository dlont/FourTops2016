#!/bin/bash

folderwithmergedcraneens=plots_mu_topptnonjw_v2
prefix=ARCcomments
targetvar=''
########################################
#              MUON CARDS/POSTFIT PLOTS
########################################
#for targetvar in LeptonPt NjetsW multitopness HTb HTH HTX SumJetMassX 1stjetpt 2ndjetpt 5thjetpt 6thjetpt csvJetcsv3 csvJetcsv4
for targetvar in 1stjetpt jetpt
do
	echo "$targetvar"
	targetdir=$prefix/$folderwithmergedcraneens\_$targetvar
	mkdir $targetdir
	for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` $targetdir/`basename $i`;done
	make -t -j card_mu.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$targetdir/ DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu TARGETVAR=$targetvar
	rm $targetdir/Hist*.root
	make -j card_mu.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$targetdir/ DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu TARGETVAR=$targetvar
done
