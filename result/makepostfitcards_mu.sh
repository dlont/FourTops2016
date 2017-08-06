#!/bin/bash

folderwithmergedcraneens=plots_mu_toppt
targetvar=''
########################################
#              MUON CARDS/POSTFIT PLOTS
########################################
mkdir plots_mu_toppt_LeptonPt
for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` plots_mu_toppt_LeptonPt/`basename $i`;done

mkdir plots_mu_toppt_NjetsW
for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` plots_mu_toppt_NjetsW/`basename $i`;done

mkdir plots_mu_toppt_multitopness
for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` plots_mu_toppt_multitopness/`basename $i`;done
make -t -j card_mu.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=plots_mu_toppt_multitopness/ DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu TARGETVAR=multitopness
rm plots_mu_toppt_multitopness/Hist*.root
make -j card_mu.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=plots_mu_toppt_multitopness/ DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu TARGETVAR=multitopness

folderwithmergedcraneens=plots_mu_toppt
targetvar=HTb
mkdir plots_mu_toppt_$targetvar
for i in $folderwithmergedcraneens/Cran*.root; do ln -s `readlink -f $i` plots_mu_toppt_$targetvar/`basename $i`;done
make -t -j card_mu.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=plots_mu_toppt_$targetvar/ DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu TARGETVAR=$targetvar
rm plots_mu_toppt_$targetvar/Hist*.root
make -j card_mu.txt ERA=full INPUTLOCATION=$folderwithmergedcraneens BUILDDIR=plots_mu_toppt_$targetvar/ DATALABEL:=Single\ \#mu TREENAME=Craneen__Mu TARGETVAR=$targetvar
