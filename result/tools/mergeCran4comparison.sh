#!/bin/bash

# Merge Craneen files for comparison with Lana's output
# date: 19 April 2016

# Specify folder with files to merge
inputfolder=""
if [[ -n $1 ]] #check if variable is not empty
then
	inputfolder=$1
	echo "Craneens from $inputfolder will be merged"
else
	echo "Usage: mergeCran4comparison [FOLDER] [CRAN LIST]"
fi

# Specify the list of output Craneens
outputsumcraneens=$2
if [[ -n $2 ]] #check if variable is not empty
then
        outputsumcraneens=$2
        echo "Sum Craneens from the file $outputsumcraneens were requested"
	echo "List of requested files"
	cat $outputsumcraneens
else
        echo "Usage: mergeCran4comparison [FOLDER] [CRAN LIST]"
fi

# Check whether 'hadd' is available
#eval testhadd=$(which hadd|grep "no hadd")
#if [[ -n testhadd ]] #check if variable is not empty
#then
#	echo ""
#else
#        echo "hadd was not found. Stopping!"
#	exit
#fi

#################################################
#             Merging ROOT files
#################################################

# Loop over lines in the input list
while read filename; do
  #echo $filename
	eval "filestomergewildcard=\$(echo \$filename | sed -e \"s/Run2_TopTree_Study/\*/g\")"
	#ls $filename $inputfolder/$filestomergewildcard
	echo hadd $filename $inputfolder/$filestomergewildcard
	hadd $filename $inputfolder/$filestomergewildcard
done < $outputsumcraneens

