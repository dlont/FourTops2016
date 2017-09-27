

def trgcuts(tree_name):
	trigger_cuts = ''
	if 'Mu' in tree_name:
	        trigger_cuts = "((HLT_IsoMu24==1||HLT_IsoTkMu24==1)  && met > 50 && fabs(LeptonEta)<2.1 )"
	        #trigger_cuts = "(HLT_PFHT400_SixJet30_DoubleBTagCSV_p056==1)"
	        #trigger_cuts = "(HLT_Mu15_IsoVVVL_BTagCSV_p067_PFHT400==1)"
	elif 'El' in tree_name:
	        trigger_cuts = "((HLT_Ele32_eta2p1_WPTight_Gsf==1) &&  met > 50 && HT > 450 && fabs(LeptonEta)<=2.1 )"
	        #trigger_cuts = "(HLT_PFHT400_SixJet30_DoubleBTagCSV_p056==1)"
	        #trigger_cuts = "(HLT_Ele15_IsoVVVL_PFHT350_PFMET50==1)"
	
	
	#########################
	#trigger_cuts = ''
	#if 'Mu' in tree_name:
	#	trigger_cuts = "((HLT_IsoMu24==1||HLT_IsoTkMu24==1) && nJets>=7 && HT > 450 && met > 50)"
	#	#trigger_cuts = "(HLT_PFHT400_SixJet30_DoubleBTagCSV_p056==1)"
	#	#trigger_cuts = "(HLT_Mu15_IsoVVVL_BTagCSV_p067_PFHT400==1)"
	#elif 'El' in tree_name:
	#	#trigger_cuts = "((HLT_Ele32_eta2p1_WPTight_Gsf==1) && HT > 450 && met > 50)"
	#	trigger_cuts = "((HLT_Ele32_eta2p1_WPTight_Gsf==1) && nJets>7 && HT > 450 && met > 50)"
	#	#trigger_cuts = "(HLT_PFHT400_SixJet30_DoubleBTagCSV_p056==1)"
	#	#trigger_cuts = "(HLT_Ele15_IsoVVVL_PFHT350_PFMET50==1)"

	return trigger_cuts
