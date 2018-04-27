import os, sys
from subprocess import call, Popen, PIPE
from email.mime.text import MIMEText

#call(["ls", "-l"])

MYEMAIL = 'denys.lontkovskyi@vub.be'
SENDMAILPATH = '/usr/sbin/sendmail'

def notify_success(sample, **kwargs):
    msg = MIMEText("Test message\n")
    msg._payload += "N Success: {0}\nN Fail: {1}".format(kwargs.get('success',-1),kwargs.get('fail',-1))
    msg["To"] = MYEMAIL
    msg["Subject"] = "Sample {0}. Succeded!".format(sample)
    p = Popen([SENDMAILPATH, "-t", "-oi"], stdin=PIPE)
    p.communicate(msg.as_string())
    #print msg.as_string()

def notify_fail(sample, **kwargs):
    msg = MIMEText("N Success: {0}\nN Fail: {1}".format(kwargs.get('success',-1),kwargs.get('fail',-1)))
    msg["To"] = MYEMAIL
    msg["Subject"] = "Sample {0}. Failed!".format(sample)
    p = Popen([SENDMAILPATH, "-t", "-oi"], stdin=PIPE)
    p.communicate(msg.as_string())

def notify_fail_merge(sample, output, **kwargs):
    msg = MIMEText(output)
    msg["To"] = MYEMAIL
    msg["Subject"] = "Merging of sample {0} files failed!".format(sample)
    p = Popen([SENDMAILPATH, "-t", "-oi"], stdin=PIPE)
    p.communicate(msg.as_string())


def merge_craneens_process(sample,**kwargs):
    
    # working directory
    WORK_DIR='/user/dlontkov/t2016/result'

    sample_craneen_mapping = {}
    sample_craneen_mapping['Data_Run2016B']='Craneen_DataB_Run2_TopTree_Study.root'
    sample_craneen_mapping['Data_Run2016C']='Craneen_DataC_Run2_TopTree_Study.root'
    sample_craneen_mapping['Data_Run2016D']='Craneen_DataD_Run2_TopTree_Study.root'
    sample_craneen_mapping['Data_Run2016E']='Craneen_DataE_Run2_TopTree_Study.root'
    sample_craneen_mapping['Data_Run2016F']='Craneen_DataF_Run2_TopTree_Study.root'
    sample_craneen_mapping['Data_Run2016G']='Craneen_DataG_Run2_TopTree_Study.root'
    sample_craneen_mapping['Data_Run2016H']='Craneen_DataH_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO']='Craneen_ttttNLO_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_fsrup']='Craneen_ttttNLO_fsrup_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_fsrdown']='Craneen_ttttNLO_fsrdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_isrup']='Craneen_ttttNLO_isrup_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_isrdown']='Craneen_ttttNLO_isrdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_totaljesup']='Craneen_ttttNLO_jesup_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_totaljesdown']='Craneen_ttttNLO_jesdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_jerup']='Craneen_ttttNLO_jerup_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_jerdown']='Craneen_ttttNLO_jerdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_SubTotalPileUp_jesup']='Craneen_ttttNLO_SubTotalPileUp_jesup_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_SubTotalPileUp_jesdown']='Craneen_ttttNLO_SubTotalPileUp_jesdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_SubTotalRelative_jesup']='Craneen_ttttNLO_SubTotalRelative_jesup_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_SubTotalRelative_jesdown']='Craneen_ttttNLO_SubTotalRelative_jesdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_SubTotalPt_jesup']='Craneen_ttttNLO_SubTotalPt_jesup_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_SubTotalPt_jesdown']='Craneen_ttttNLO_SubTotalPt_jesdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_SubTotalScale_jesup']='Craneen_ttttNLO_SubTotalScale_jesup_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_SubTotalScale_jesdown']='Craneen_ttttNLO_SubTotalScale_jesdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_SubTotalFlavor_jesup']='Craneen_ttttNLO_SubTotalFlavor_jesup_Run2_TopTree_Study.root'
    sample_craneen_mapping['ttttNLO_SubTotalFlavor_jesdown']='Craneen_ttttNLO_SubTotalFlavor_jesdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_totaljesup']='Craneen_TTJets_powheg_jesup_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_totaljesdown']='Craneen_TTJets_powheg_jesdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_SubTotalPileUp_jesup']='Craneen_TTJets_powheg_SubTotalPileUp_jesup_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_SubTotalPileUp_jesdown']='Craneen_TTJets_powheg_SubTotalPileUp_jesdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_SubTotalRelative_jesup']='Craneen_TTJets_powheg_SubTotalRelative_jesup_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_SubTotalRelative_jesdown']='Craneen_TTJets_powheg_SubTotalRelative_jesdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_SubTotalPt_jesup']='Craneen_TTJets_powheg_SubTotalPt_jesup_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_SubTotalPt_jesdown']='Craneen_TTJets_powheg_SubTotalPt_jesdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_SubTotalScale_jesup']='Craneen_TTJets_powheg_SubTotalScale_jesup_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_SubTotalScale_jesdown']='Craneen_TTJets_powheg_SubTotalScale_jesdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_SubTotalFlavor_jesup']='Craneen_TTJets_powheg_SubTotalFlavor_jesup_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_SubTotalFlavor_jesdown']='Craneen_TTJets_powheg_SubTotalFlavor_jesdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_jerup']='Craneen_TTJets_powheg_SubTotalFlavor_jesup_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_jerdown']='Craneen_TTJets_powheg_SubTotalFlavor_jesdown_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_central']='Craneen_TTJets_powheg_Run2_TopTree_Study.root'
    sample_craneen_mapping['DYJets_50MG']='Craneen_DYJets_50MG_Run2_TopTree_Study.root'
    sample_craneen_mapping['DY1Jets_50MG']='Craneen_DY1Jets_50MG_Run2_TopTree_Study.root'
    sample_craneen_mapping['DY2Jets_50MG']='Craneen_DY2Jets_50MG_Run2_TopTree_Study.root'
    sample_craneen_mapping['DY3Jets_50MG']='Craneen_DY3Jets_50MG_Run2_TopTree_Study.root'
    sample_craneen_mapping['DY4Jets_50MG']='Craneen_DY4Jets_50MG_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_mass1665']='Craneen_TTJets_powheg_mass1665_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_mass1715']='Craneen_TTJets_powheg_mass1715_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_mass1755']='Craneen_TTJets_powheg_mass1755_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_mass1695']='Craneen_TTJets_powheg_mass1695_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_mass1735']='Craneen_TTJets_powheg_mass1735_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_mass1785']='Craneen_TTJets_powheg_mass1785_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_width02']='Craneen_TTJets_powheg_width02_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_width2']='Craneen_TTJets_powheg_width2_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_width8']='Craneen_TTJets_powheg_width8_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_width05']='Craneen_TTJets_powheg_width05_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTJets_powheg_width4']='Craneen_TTJets_powheg_width4_Run2_TopTree_Study.root'
    sample_craneen_mapping['T_tW']='Craneen_T_tW_Run2_TopTree_Study.root'
    sample_craneen_mapping['Tbar_tW']='Craneen_Tbar_tW_Run2_TopTree_Study.root'
    sample_craneen_mapping['T_tch']='Craneen_T_tch_Run2_TopTree_Study.root'
    sample_craneen_mapping['Tbar_tch']='Craneen_Tbar_tch_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTH']='Craneen_TTH_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTZ']='Craneen_TTZ_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTW']='Craneen_TTW_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTTW']='Craneen_TTTW_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTWZ']='Craneen_TTWZ_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTZZ']='Craneen_TTZZ_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTZH']='Craneen_TTZH_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTHH']='Craneen_TTHH_Run2_TopTree_Study.root'
    sample_craneen_mapping['TTTJ']='Craneen_TTTJ_Run2_TopTree_Study.root'

    #sample_craneen_mapping['TTISRScaledown_powheg_p1']='Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root'
    #sample_craneen_mapping['TTFSRScaledown_powheg_p1']='Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root'
    #sample_craneen_mapping['TTISRScaleup_powheg_p1']='Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root'
    #sample_craneen_mapping['TTFSRScaleup_powheg_p1']='Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root'
    #sample_craneen_mapping['TTISRScaledown_powheg_p2']='Craneen_TTISRScaledown_powheg_Run2_TopTree_Study.root'
    #sample_craneen_mapping['TTFSRScaledown_powheg_p2']='Craneen_TTFSRScaledown_powheg_Run2_TopTree_Study.root'
    #sample_craneen_mapping['TTISRScaleup_powheg_p2']='Craneen_TTISRScaleup_powheg_Run2_TopTree_Study.root'
    #sample_craneen_mapping['TTFSRScaleup_powheg_p2']='Craneen_TTFSRScaleup_powheg_Run2_TopTree_Study.root'
    builddir=kwargs.get('builddir',None)
    inputlocation=kwargs.get('inputlocation',None)
    target=sample_craneen_mapping.get(sample,None)
    if builddir and inputlocation and target:
        command='make BUILDDIR={0} INPUTLOCATION={1} {0}/{2}'.format(builddir,inputlocation,target).split()
	#print command
        p = Popen(command,cwd=WORK_DIR,stdout=PIPE,stderr=PIPE)
	stdoutdata, stderrdata = p.communicate()
	if p.returncode != 0:
		output = stdoutdata if stderrdata is None else stdoutdata+'\n'+stderrdata
		#print output
		notify_fail_merge(sample,output)	
		
