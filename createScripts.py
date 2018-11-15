import xml.etree.cElementTree as ET
import subprocess
import time
import os
import glob
from shutil import copyfile
from datetime import datetime
# libray to copy files
import shutil 


# Define time variable 
now = datetime.now()
dd = str(now.day)
mm = str(now.month)
yyyy = str(now.year)
hh = str(now.hour)
mn= str(now.minute)

# make a data string. Pick one of the two above 
#date = dd+"_"+mm+"_"+yyyy+"_"+hh+"h"+mn+"min"
date = dd+"_"+mm+"_"+yyyy
#date = dd+"_"+mm+"_"+yyyy+"noTrig"


# pick one of the following
#channels = ["Mu2016","El2016","Syst2016Mu","Syst2016El"] # muon and electron channels central and systematics files
#channels = ["Mu2016","Syst2016Mu"]		# muon channel central and systematics files
#channels = ["El2016","Syst2016El"]		# electron channel central and systematics files
#channels = ["Mu2016","El2016"] 		# both electron and muon channel files
channels = ['Syst2016Mu','Syst2016El']		# Systematic MC electron and muon files
#channels = ["El2016"]				# only electron files
#channels = ["CutBasedEl2016"]			# only electron files with cutbased selection
#channels = ["Mu2016"]				# only muon files

channel_outfolder_map = {'Mu2016':'Mu2016', 'El2016':'El2016', 'CutBasedEl2016':'El2016', 'Syst2016Mu':'Mu2016', 'Syst2016El':'El2016'}

# loop over channels
for chan in channels:
    print "\nSearching list of sample used for ", chan, " channel!"
    # getting the appropriate xml file
    if chan == "Mu2016":
        #tree = ET.ElementTree(file='config/FullMuonTopTrees80_v12.xml')
        tree = ET.ElementTree(file='config/FullMuonTopTrees80_v12_nomasswidth.xml')
    elif chan == "El2016":
        #tree = ET.ElementTree(file='config/FullElectronTopTrees80_v12.xml')
        tree = ET.ElementTree(file='config/FullElectronTopTrees80_v12_nomasswidth.xml')
    elif chan == "CutBasedEl2016":
        tree = ET.ElementTree(file='config/FullElectronTopTrees80_v12_nomasswidth_cutbased.xml')
    elif chan == "Syst2016Mu":
        tree = ET.ElementTree(file='config/SystMuonTopTrees80_v9.xml')
    elif chan == "Syst2016El":
        tree = ET.ElementTree(file='config/SystElectronTopTrees80_v9.xml')
    else:
        print "Channel '", chan , "' is not a correct channel name. No tree has been loaded!"
        sys.exit()

    root = tree.getroot()
    datasets = root.find('datasets')
    print "found  "  + str(len(datasets)) + " datasets"

    
    # create new dirs if not already existing
    if not os.path.exists("SubmitScripts/"+date):
        os.makedirs("SubmitScripts/"+date)
    if not os.path.exists("SubmitScripts/"+date+"/"+chan):
        os.makedirs("SubmitScripts/"+date+"/"+chan)
    if not os.path.exists("SubmitScripts/"+date+"/"+chan+"/output"):
        os.makedirs("SubmitScripts/"+date+"/"+chan+"/output")
    if not os.path.exists("SubmitScripts/"+date+"/"+chan+"/test"):
        os.makedirs("SubmitScripts/"+date+"/"+chan+"/test")

    # copy the submitAll macro
    copyfile("SubmitAll.sh","SubmitScripts/"+date+"/"+chan+"/SubmitAll.sh")

    
    # list of variables 
    topTrees = []
    listOfFiles = []
    listOfScratchFiles = []
    listOfTmpDirFiles = []
    CopyCmdlistOfFiles = []
    files_str=""
    scractFiles_str=''
    tmpdirFiles_str=""
    FilePerJob=0 # add dccap...
    addPrefix=True
    N_processed=0
    
    # loop over all the dataset with add="1"
    for d in datasets:
        if d.attrib['add'] == '1':
            print "found dataset to be added..." + str(d.attrib['name'])
            if "Dilep" in chan:
                commandString = "./MACRO "+str(d.attrib['name'])+" "+str(d.attrib['title'])+" "+str(d.attrib['add'])+" "+str(d.attrib['color'])+" "+str(d.attrib['ls'])+" "+str(d.attrib['lw'])+" "+str(d.attrib['normf'])+" "+str(d.attrib['EqLumi'])+" "+str(d.attrib['xsection'])+" "+str(d.attrib['PreselEff'])
            else:
		jes = ''
		if 'totaljesup' in str(d.attrib['name']):
			jes = '--fourtops_jes=Total_up'
		elif 'totaljesdown' in str(d.attrib['name']):
			jes = '--fourtops_jes=Total_down'
		elif 'SubTotalPileUp_jesup' in str(d.attrib['name']):
			jes = '--fourtops_jes=SubTotalPileUp_up'
		elif 'SubTotalPileUp_jesdown' in str(d.attrib['name']):
			jes = '--fourtops_jes=SubTotalPileUp_down'
		elif 'SubTotalRelative_jesup' in str(d.attrib['name']):
			jes = '--fourtops_jes=SubTotalRelative_up'
		elif 'SubTotalRelative_jesdown' in str(d.attrib['name']):
			jes = '--fourtops_jes=SubTotalRelative_down'
		elif 'SubTotalPt_jesup' in str(d.attrib['name']):
			jes = '--fourtops_jes=SubTotalPt_up'
		elif 'SubTotalPt_jesdown' in str(d.attrib['name']):
			jes = '--fourtops_jes=SubTotalPt_down'
		elif 'SubTotalScale_jesup' in str(d.attrib['name']):
			jes = '--fourtops_jes=SubTotalScale_up'
		elif 'SubTotalScale_jesdown' in str(d.attrib['name']):
			jes = '--fourtops_jes=SubTotalScale_down'
		elif 'SubTotalFlavor_jesup' in str(d.attrib['name']):
			jes = '--fourtops_jes=SubTotalFlavor_up'
		elif 'SubTotalFlavor_jesdown' in str(d.attrib['name']):
			jes = '--fourtops_jes=SubTotalFlavor_down'
		
		jer = ''
		if 'jerup' in str(d.attrib['name']):
                        jer = '--fourtops_jer=up'
                elif 'jerdown' in str(d.attrib['name']):
                        jer = '--fourtops_jer=down'
		

                commandString = 'GLOG_log_dir=/scratch/$PBS_JOBID/ ./FourTops'\
		+' --dataset_name="{}"'.format(str(d.attrib['name'])) \
		+' --dataset_title="{}"'.format(str(d.attrib['title']))\
		+' --dataset_color={}'.format(str(d.attrib['color']))\
		+' --dataset_linestyle={}'.format(str(d.attrib['ls']))\
		+' --dataset_linewidth={}'.format(str(d.attrib['lw']))\
		+' --dataset_norm_factor={}'.format(str(d.attrib['normf']))\
		+' --dataset_eq_lumi={}'.format(str(d.attrib['EqLumi']))\
		+' --dataset_cross_section={}'.format(str(d.attrib['xsection']))\
		+' --dataset_preselection_eff={}'.format(str(d.attrib['PreselEff']))

		if 'CUTBASED' in str(d.attrib['name']):
			commandString = commandString + ' --fourtops_eleid="CUT"'
            topTrees = glob.glob(d.attrib['filenames'])

	    #print topTrees

            # setting the number of file per job depending whether it is data sample or not
            # this ca be tweaked
            if "Data" in str(d.attrib['name']):
                FilePerJob=10
            elif "tttt" in str(d.attrib['name']):
                FilePerJob=1
            else:
                FilePerJob=4

            # create a test job for each dataset
            # create a file for this job 
            filenameTest="SubmitScripts/"+date+"/"+chan+"/test"+"/submit_"+str(d.attrib['name'])+"_"+"Test"+".sh"
            # copy a skeleton file that set up the code environment, the wall time and the queue 
            shutil.copyfile("submitTestSkeleton.sh", filenameTest)
            # append to the file the actual command 
            outfileTest = open (filenameTest, 'a')
            if not len(topTrees) == 0:
		print >> outfileTest, './FourTops --version '
                print >> outfileTest, commandString, '--nevents=1000 --input_files="dcap://maite.iihe.ac.be'+topTrees[0], '" ', '--fourtops_channel="{}"'.format(chan), jes, jer 
		# copy output of the ntupler to /pnfs
		print >> outfileTest, 'export PNFS_OUTPUT_DIR=$PNFS_OUTPUT_DIR/test/{}'.format(channel_outfolder_map[chan])
		print >> outfileTest, 'echo "$FOURTOPS_OUTFILE" -> "$PNFS_OUTPUT_DIR"'
		print >> outfileTest, 'gfal-mkdir -p {}'.format('$PNFS_OUTPUT_DIR')
		print >> outfileTest, 'gfal-copy $FOURTOPS_OUTFILE $PNFS_OUTPUT_DIR'
            N_job = 0
            N_file = 1
            remainder= len(topTrees)%FilePerJob
#            print "remainder is", remainder
            
#            print "len(topTrees) is ", len(topTrees)
            # loop over all the root files 
            for f in range(0,len(topTrees)):
#                print "file number ", f , " is : ", topTrees[f]

                # Combine multiple root files in a single job
                listOfFiles.append(topTrees[f])
		# intermediate copy to scratch space
                #CopyCmdlistOfFiles.append("dccp dcap://maite.iihe.ac.be"+topTrees[f]+" /$TMPDIR/TOPTREE_"+str(f)+".root")
                #listOfScratchFiles.append(" /scratch/$PBS_JOBID/TOPTREE_"+str(f)+".root")
                #listOfTmpDirFiles.append(" /$TMPDIR/TOPTREE_"+str(f)+".root")

		# read input directly from dcache
                listOfTmpDirFiles.append("dcap://maite.iihe.ac.be"+topTrees[f]+",")
                
#                print CopyCmdlistOfFiles[0]
                
                # if the number of files is big enough, create one job with the list of files
                if (len(listOfFiles) == FilePerJob) or ((len(topTrees)- N_job * FilePerJob <= FilePerJob) and (len(listOfFiles) == remainder) ):
#                    print "len(listOfFiles) is ", len(listOfFiles) 

                    # create a file for this job
                    filename="SubmitScripts/"+date+"/"+chan+"/submit_"+str(d.attrib['name'])+"_"+str(N_job*FilePerJob+1)+"to"+str(N_job*FilePerJob+len(listOfFiles))+".sh"
                    #a copy a skeleton file that set up the code environment, the wall time and the queue
                    shutil.copyfile("submitSkeleton.sh", filename)

                    # add one copy cmd per file in that job
                    outfile = open (filename, 'a')

                    # run on the files
                    print >> outfile, "# now run on the file copied under /$TMPDIR/ "
		    print >> outfile, './FourTops --version '
                    print >> outfile, commandString, '--input_files="{}"'.format(''.join(listOfTmpDirFiles)) , ' ', '--fourtops_channel="{}"'.format(chan), \
						     jes, jer, '--jobid="{}"'.format('$PBS_JOBID')
		    # copy output of the ntupler to /pnfs
		    print >> outfile, 'export PNFS_OUTPUT_DIR=$PNFS_OUTPUT_DIR/{}'.format(channel_outfolder_map[chan])
		    print >> outfile, 'echo "$FOURTOPS_OUTFILE" -> "$PNFS_OUTPUT_DIR"'
		    print >> outfile, 'gfal-mkdir -p {}'.format('$PNFS_OUTPUT_DIR')
		    print >> outfile, 'gfal-copy $FOURTOPS_OUTFILE $PNFS_OUTPUT_DIR'

                    # cleaning
                    listOfFiles=[]
                    listOfScratchFiles=[]
                    CopyCmdlistOfFiles=[]
                    listOfTmpDirFiles =[]
                    files_str=""
                    scractFiles_str=""

                    N_job=N_job+1
#                    print N_job * FilePerJob
#                    print "Number of processed file is ", N_processed

                N_file=N_file+1



#                print lisfOflisOfFiles
                
# moving the newly created dir
#os.chdir("SubmitScripts/"+chan+"/"+date)
