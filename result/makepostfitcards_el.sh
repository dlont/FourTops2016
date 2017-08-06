#!/bin/bash

folderwithmergedcraneens=plots_el_toppt
targetvar=''
########################################
#              ELECTRON CARDS/POSTFIT PLOTS
########################################
#targetvar=LeptonPt
#mkdir $folderwithmergedcraneens\_$targetvar
#for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` $folderwithmergedcraneens\_$targetvar/`basename $i`;done
#make -t -j card_el.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$folderwithmergedcraneens\_$targetvar/ DATALABEL:=Single\ \#el TREENAME=Craneen__El TARGETVAR=$targetvar
#rm $folderwithmergedcraneens\_$targetvar/Hist*.root
#make -j card_el.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$folderwithmergedcraneens\_$targetvar/ DATALABEL:=Single\ \#el TREENAME=Craneen__El TARGETVAR=$targetvar
#
#targetvar=NjetsW
#mkdir $folderwithmergedcraneens\_$targetvar
#for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` $folderwithmergedcraneens\_$targetvar/`basename $i`;done
#make -t -j card_el.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$folderwithmergedcraneens\_$targetvar/ DATALABEL:=Single\ \#el TREENAME=Craneen__El TARGETVAR=$targetvar
#rm $folderwithmergedcraneens\_$targetvar/Hist*.root
#make -j card_el.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$folderwithmergedcraneens\_$targetvar/ DATALABEL:=Single\ \#el TREENAME=Craneen__El TARGETVAR=$targetvar
#
#targetvar=multitopness
#mkdir $folderwithmergedcraneens\_$targetvar
#for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` $folderwithmergedcraneens\_$targetvar/`basename $i`;done
#make -t -j card_el.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$folderwithmergedcraneens\_$targetvar/ DATALABEL:=Single\ \#el TREENAME=Craneen__El TARGETVAR=$targetvar
#rm $folderwithmergedcraneens\_$targetvar/Hist*.root
#make -j card_el.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$folderwithmergedcraneens\_$targetvar/ DATALABEL:=Single\ \#el TREENAME=Craneen__El TARGETVAR=$targetvar
#
#targetvar=HTb
#targetvar=HTH
#targetvar=SumJetMassX
#targetvar=HTX
#targetvar=csvJetcsv4
#targetvar=1stjetpt
#targetvar=2ndjetpt
#targetvar=5thjetpt
#targetvar=6thjetpt

for targetvar in HTH HTX SumJetMassX 1stjetpt 2ndjetpt 5thjetpt 6thjetpt csvJetcsv3 csvJetcsv4
do
	echo "$targetvar"
	mkdir $folderwithmergedcraneens\_$targetvar
	for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` $folderwithmergedcraneens\_$targetvar/`basename $i`;done
	make -t -j card_el.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$folderwithmergedcraneens\_$targetvar/ DATALABEL:=Single\ e TREENAME=Craneen__El TARGETVAR=$targetvar
	rm $folderwithmergedcraneens\_$targetvar/Hist*.root
	make -j card_el.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=$folderwithmergedcraneens\_$targetvar/ DATALABEL:=Single\ e TREENAME=Craneen__El TARGETVAR=$targetvar
done
