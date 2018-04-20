usage="$(basename "$0") [-h] [-f filename] [-o /path/to/output/Craneens/] [-s /path/to/submit/scripts/] -- script to resubmit PBS job given .o file of the chashed one

where:
    -h  show this help text
    -f  name of the output .o file of the crashed job
    -o  path to Craneens
    -s  path to submit_ scirpt files

    Typical usecase:
	> for i in \`grep -L \"End of the program\" *.o* \`; do resubmit.sh -f \$i -o /path/to/output/Craneens/ -s /path/to/submit/scripts/; done

    Useful commands:
	> grep -L \"End of the program\" *.o*|wc -l  #How much jobs failed. Assumes *.o files are in ./
	> grep -l \"End of the program\" *.o*|wc -l  #How much jobs succeeded. Assumes *.o files are in ./
	> ls ../submit_*.sh|wc -l		     #How much submit_*.sh scripts in the parent folder
"

outfile=
path2output=
submitscriptpath=
while getopts ':hf:o:s:' option; do
  case "$option" in
    h) echo "$usage"
       exit
       ;;
    f) outfile=$OPTARG
       ;;
    o) path2output=$OPTARG
       ;;
    s) submitscriptpath=$OPTARG
       ;;
    :) printf "missing argument for -%s\n" "$OPTARG" >&2
       echo "$usage" >&2
       exit 1
       ;;
   \?) printf "illegal option: -%s\n" "$OPTARG" >&2
       echo "$usage" >&2
       exit 1
       ;;
  esac
done
shift "$((OPTIND-1))"

echo "Suspect job: $outfile"
suffix="$(grep "OUTPUT" $outfile|awk '{print $5}')"
echo "Output craneen suffix: $suffix"
rootfile="$(find $path2output -name "*$suffix.root")"

submitscript=$submitscriptpath/${outfile%.*}	#${outfile%.*} removes .oXXXXXXX extension from the output LOG filename
if [ -f $submitscript ]; then
    	echo "Submit script has been found!"
    	echo "qsub $submitscript"
    	echo "qsub $submitscript" >> bigsub-resubmit.txt 

	if [ -d resubmit ]; then
		mv $outfile resubmit
	else
		echo "Create folder: resubmit"
		mkdir resubmit
		mv $outfile resubmit
	fi

	if [[ ! -z "$rootfile" && -f "$rootfile" ]]; then
    		echo "Corrupt output file has been found!"
    		echo "rm $rootfile"
    		rm "$rootfile"
	else
    		echo "Craneen file not found!"
    		echo "$rootfile"
        fi
else
	echo "Submit script $submitscript was not found!"
fi

