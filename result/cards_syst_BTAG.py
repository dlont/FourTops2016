from centralweight import centralweight
def cut_BTAG1(cut_string,search_scheme='9J3M,10J3M'):
	cut_BTAG = [
			#btagWeightCSVLF UP,
	("allSF_btagWeightCSVLFUp", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVLFUp", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVLFUp", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVLFUp", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVLFUp", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVLFUp", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVLFUp", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVLFUp", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVLFUp", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVLFUp", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVLFUp", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVLFUp", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),

	#btagWeightCSVLF DOWN
	("allSF_btagWeightCSVLFDown", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVLFDown", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVLFDown", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVLFDown", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVLFDown", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVLFDown", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVLFDown", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVLFDown", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVLFDown", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVLFDown", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVLFDown", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVLFDown", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),

	]
	if search_scheme == '9J3M,10J3M':
		cut_BTAG += [
			("9J3M_btagWeightCSVLFUp", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVLFUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVLFDown", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVLFDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
		]
	elif search_scheme == '9J4M,10J4M':
		cut_BTAG += [
			("9J3M_btagWeightCSVLFUp", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVLFUp", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVLFUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVLFUp", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[3]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVLFDown", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVLFDown", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVLFDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVLFDown", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[4]".format(cut_string,centralweight))
		]
	return cut_BTAG
def cut_BTAG2(cut_string,search_scheme='9J3M,10J3M'):
	cut_BTAG = [
	#btagWeightCSVHF UP,
	("allSF_btagWeightCSVHFUp", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVHFUp", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVHFUp", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVHFUp", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVHFUp", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVHFUp", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVHFUp", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVHFUp", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVHFUp", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVHFUp", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVHFUp", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVHFUp", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),

	#btagWeightCSVHF DOWN
	("allSF_btagWeightCSVHFDown", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVHFDown", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVHFDown", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVHFDown", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVHFDown", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVHFDown", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVHFDown", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVHFDown", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVHFDown", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVHFDown", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVHFDown", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVHFDown", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),

	]
	if search_scheme == '9J3M,10J3M':
		cut_BTAG += [
			("9J3M_btagWeightCSVHFUp", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVHFUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVHFDown", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVHFDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
		]
	elif search_scheme == '9J4M,10J4M':
		cut_BTAG += [
			("9J3M_btagWeightCSVHFUp", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVHFUp", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVHFUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVHFUp", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[5]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVHFDown", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVHFDown", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVHFDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVHFDown", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[6]".format(cut_string,centralweight))
		]
	return cut_BTAG
def cut_BTAG3(cut_string,search_scheme='9J3M,10J3M'):
	cut_BTAG = [
		#btagWeightCSVHFStats1 UP,
	("allSF_btagWeightCSVHFStats1Up", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVHFStats1Up", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVHFStats1Up", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVHFStats1Up", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVHFStats1Up", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVHFStats1Up", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVHFStats1Up", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVHFStats1Up", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVHFStats1Up", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVHFStats1Up", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVHFStats1Up", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVHFStats1Up", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),

	#btagWeightCSVHFStats1 DOWN
	("allSF_btagWeightCSVHFStats1Down", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVHFStats1Down", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVHFStats1Down", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVHFStats1Down", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVHFStats1Down", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVHFStats1Down", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVHFStats1Down", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVHFStats1Down", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVHFStats1Down", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVHFStats1Down", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVHFStats1Down", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVHFStats1Down", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
	]
	if search_scheme == '9J3M,10J3M':
		cut_BTAG += [
			("9J3M_btagWeightCSVHFStats1Up", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVHFStats1Up", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVHFStats1Down", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVHFStats1Down", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
		]
	elif search_scheme == '9J4M,10J4M':
		cut_BTAG += [
			("9J3M_btagWeightCSVHFStats1Up", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVHFStats1Up", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVHFStats1Up", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVHFStats1Up", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[7]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVHFStats1Down", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVHFStats1Down", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVHFStats1Down", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVHFStats1Down", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[8]".format(cut_string,centralweight))
		]
	return cut_BTAG
def cut_BTAG4(cut_string,search_scheme='9J3M,10J3M'):
	cut_BTAG = [
	#btagWeightCSVHFStats2 UP,
	("allSF_btagWeightCSVHFStats2Up", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVHFStats2Up", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVHFStats2Up", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVHFStats2Up", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVHFStats2Up", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVHFStats2Up", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVHFStats2Up", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVHFStats2Up", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVHFStats2Up", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVHFStats2Up", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVHFStats2Up", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVHFStats2Up", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),

	#btagWeightCSVHFStats2 DOWN
	("allSF_btagWeightCSVHFStats2Down", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVHFStats2Down", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVHFStats2Down", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVHFStats2Down", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVHFStats2Down", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVHFStats2Down", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVHFStats2Down", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVHFStats2Down", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVHFStats2Down", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVHFStats2Down", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVHFStats2Down", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVHFStats2Down", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
	]
	if search_scheme == '9J3M,10J3M':
		cut_BTAG += [
			("9J3M_btagWeightCSVHFStats2Up", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVHFStats2Up", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVHFStats2Down", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVHFStats2Down", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
		]
	elif search_scheme == '9J4M,10J4M':
		cut_BTAG += [
			("9J3M_btagWeightCSVHFStats2Up", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVHFStats2Up", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVHFStats2Up", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVHFStats2Up", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[9]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVHFStats2Down", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVHFStats2Down", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVHFStats2Down", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVHFStats2Down", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[10]".format(cut_string,centralweight))
		]
	return cut_BTAG
def cut_BTAG5(cut_string,search_scheme='9J3M,10J3M'):
	cut_BTAG = [
		#btagWeightCSVLFStats1 UP,
	("allSF_btagWeightCSVLFStats1Up", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVLFStats1Up", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVLFStats1Up", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVLFStats1Up", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVLFStats1Up", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVLFStats1Up", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVLFStats1Up", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVLFStats1Up", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVLFStats1Up", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVLFStats1Up", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVLFStats1Up", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVLFStats1Up", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
	#btagWeightCSVLFStats1 DOWN
	("allSF_btagWeightCSVLFStats1Down", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVLFStats1Down", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVLFStats1Down", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVLFStats1Down", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVLFStats1Down", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVLFStats1Down", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVLFStats1Down", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVLFStats1Down", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVLFStats1Down", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVLFStats1Down", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVLFStats1Down", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVLFStats1Down", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
	]
	if search_scheme == '9J3M,10J3M':
		cut_BTAG += [
			("9J3M_btagWeightCSVLFStats1Up", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVLFStats1Up", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVLFStats1Down", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVLFStats1Down", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
		]
	elif search_scheme == '9J4M,10J4M':
		cut_BTAG += [
			("9J3M_btagWeightCSVLFStats1Up", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVLFStats1Up", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVLFStats1Up", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVLFStats1Up", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[11]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVLFStats1Down", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVLFStats1Down", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVLFStats1Down", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVLFStats1Down", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[12]".format(cut_string,centralweight))
		]
	return cut_BTAG
def cut_BTAG6(cut_string,search_scheme='9J3M,10J3M'):
	cut_BTAG = [
	#btagWeightCSVLFStats2 UP,
	("allSF_btagWeightCSVLFStats2Up", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVLFStats2Up", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVLFStats2Up", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVLFStats2Up", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVLFStats2Up", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVLFStats2Up", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVLFStats2Up", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVLFStats2Up", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVLFStats2Up", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVLFStats2Up", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVLFStats2Up", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVLFStats2Up", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
	#btagWeightCSVLFStats2 DOWN
	("allSF_btagWeightCSVLFStats2Down", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVLFStats2Down", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVLFStats2Down", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVLFStats2Down", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVLFStats2Down", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVLFStats2Down", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVLFStats2Down", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVLFStats2Down", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVLFStats2Down", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVLFStats2Down", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVLFStats2Down", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVLFStats2Down", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
	]
	if search_scheme == '9J3M,10J3M':
		cut_BTAG += [
			("9J3M_btagWeightCSVLFStats2Up", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVLFStats2Up", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVLFStats2Down", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVLFStats2Down", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
		]
	elif search_scheme == '9J4M,10J4M':
		cut_BTAG += [
			("9J3M_btagWeightCSVLFStats2Up", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVLFStats2Up", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVLFStats2Up", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVLFStats2Up", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[13]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVLFStats2Down", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVLFStats2Down", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVLFStats2Down", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVLFStats2Down", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[14]".format(cut_string,centralweight))
		]
	return cut_BTAG
def cut_BTAG7(cut_string,search_scheme='9J3M,10J3M'):
	cut_BTAG = [
		#btagWeightCSVCFErr1 UP,
	("allSF_btagWeightCSVCFErr1Up", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVCFErr1Up", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVCFErr1Up", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVCFErr1Up", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVCFErr1Up", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVCFErr1Up", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVCFErr1Up", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVCFErr1Up", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVCFErr1Up", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVCFErr1Up", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVCFErr1Up", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVCFErr1Up", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
	#btagWeightCSVCFErr1 DOWN
	("allSF_btagWeightCSVCFErr1Down", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVCFErr1Down", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVCFErr1Down", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVCFErr1Down", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVCFErr1Down", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVCFErr1Down", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVCFErr1Down", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVCFErr1Down", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVCFErr1Down", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVCFErr1Down", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVCFErr1Down", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVCFErr1Down", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
	]
	if search_scheme == '9J3M,10J3M':
		cut_BTAG += [
			("9J3M_btagWeightCSVCFErr1Up", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVCFErr1Up", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVCFErr1Down", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVCFErr1Down", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
		]
	elif search_scheme == '9J4M,10J4M':
		cut_BTAG += [
			("9J3M_btagWeightCSVCFErr1Up", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVCFErr1Up", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVCFErr1Up", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVCFErr1Up", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[15]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVCFErr1Down", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVCFErr1Down", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVCFErr1Down", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVCFErr1Down", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[16]".format(cut_string,centralweight))
		]
	return cut_BTAG
def cut_BTAG8(cut_string,search_scheme='9J3M,10J3M'):
	cut_BTAG = [
	#btagWeightCSVCFErr2 UP,
	("allSF_btagWeightCSVCFErr2Up", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVCFErr2Up", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVCFErr2Up", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVCFErr2Up", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVCFErr2Up", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVCFErr2Up", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVCFErr2Up", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVCFErr2Up", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVCFErr2Up", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVCFErr2Up", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVCFErr2Up", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVCFErr2Up", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
	#btagWeightCSVCFErr2 DOWN
	("allSF_btagWeightCSVCFErr2Down", "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),

	("6J2M_btagWeightCSVCFErr2Down", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
	("6J3M_btagWeightCSVCFErr2Down", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
	("6J4M_btagWeightCSVCFErr2Down", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
	("7J2M_btagWeightCSVCFErr2Down", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
	("7J3M_btagWeightCSVCFErr2Down", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
	("7J4M_btagWeightCSVCFErr2Down", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
	("8J2M_btagWeightCSVCFErr2Down", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
	("8J3M_btagWeightCSVCFErr2Down", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
	("8J4M_btagWeightCSVCFErr2Down", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
	("9J2M_btagWeightCSVCFErr2Down", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
	("10J2M_btagWeightCSVCFErr2Down", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
	]
	if search_scheme == '9J3M,10J3M':
		cut_BTAG += [
			("9J3M_btagWeightCSVCFErr2Up", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVCFErr2Up", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVCFErr2Down", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVCFErr2Down", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
		]
	elif search_scheme == '9J4M,10J4M':
		cut_BTAG += [
			("9J3M_btagWeightCSVCFErr2Up", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVCFErr2Up", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVCFErr2Up", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVCFErr2Up", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[17]".format(cut_string,centralweight)),
			("9J3M_btagWeightCSVCFErr2Down", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
			("9J4M_btagWeightCSVCFErr2Down", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
			("10J3M_btagWeightCSVCFErr2Down", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight)),
			("10J4M_btagWeightCSVCFErr2Down", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[18]".format(cut_string,centralweight))
		]
	return cut_BTAG
