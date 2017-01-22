
#!/bin/bash 

sleepinterval=0.2

if [[ -n $1 ]] #check if variable is not empty
then
    if [[ $1 == "test" ]]
    then
	cd test
	for f in ./submit_$2*.sh
	do
	    qsub $f || echo "qsub $f" >> qsub.log.`date +%m_%d_%Y`
	    sleep $sleepinterval
	done
	cd -
    else
	cd output
        for f in ../submit_$1*.sh
        do
            qsub $f || echo "qsub $f" >> qsub.log.`date +%m_%d_%Y`
	    sleep $sleepinterval
        done
        cd -
    fi

else
    cd output
    for f in ../submit*.sh
    do
	qsub $f || echo "qsub $f" >> qsub.log.`date +%m_%d_%Y`
	sleep $sleepinterval
    done
    cd -

fi
