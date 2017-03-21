
#!/bin/bash 
if [[ -n $1 ]] #check if variable is not empty
then
    if [[ $1 == "test" ]]
    then
	cd test
	for f in ./submit_$2*.sh
	do
		until qsub $f 
		do
			echo "Retrying!"
			echo "$f" >> qsub.log.`date +%m_%d_%Y`	
	   		sleep 0.2
		done
	done
	cd -
    else
	cd output
        for f in ../submit_$1*.sh
        do
		until qsub $f 
		do
			echo "Retrying!"
			echo "$f" >> qsub.log.`date +%m_%d_%Y`	
	   		sleep 0.2
		done
        done
        cd -
    fi

else
    cd output
    for f in ../submit*.sh
    do
		until qsub $f 
		do
			echo "Retrying!"
			echo "$f" >> qsub.log.`date +%m_%d_%Y`	
	   		sleep 0.2
		done
    done
    cd -
fi
