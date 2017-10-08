#!/bin/bash
set -x

folderwithmergedcraneens=plots_el_toppt
targetvar=''
########################################
#              ELECTRON CARDS/POSTFIT PLOTS
########################################
for targetvar in LeptonPt NjetsW multitopness HTb HTH HTX SumJetMassX 1stjetpt 2ndjetpt 5thjetpt 6thjetpt csvJetcsv3 csvJetcsv4
do
	echo "$targetvar"
	targetdir=$prefix\_$targetvar
	mkdir $targetdir
	for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` $targetdir/`basename $i`;done
	make -t -j card_el.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$targetdir/ DATALABEL:=Single\ e TREENAME=Craneen__El TARGETVAR=$targetvar
	rm $targetdir/Hist*.root
	make -j card_el.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$targetdir/ DATALABEL:=Single\ e TREENAME=Craneen__El TARGETVAR=$targetvar
done
set +x
