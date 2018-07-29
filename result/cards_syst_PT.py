from centralweight import centralweight
def cut_PT(cut_string,search_scheme='9J3M,10J3M'):
	cut_PT = [
	#PT UP
	("allSF_TTPTUp", "inclusive",  "(1 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),

	("6J2M_TTPTUp", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("6J3M_TTPTUp", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("6J4M_TTPTUp", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("7J2M_TTPTUp", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("7J3M_TTPTUp", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("7J4M_TTPTUp", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("8J2M_TTPTUp", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("8J3M_TTPTUp", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("8J4M_TTPTUp", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("9J2M_TTPTUp", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("10J2M_TTPTUp", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),

	#PT DOWN
	("allSF_TTPTDown", "inclusive",  "(1 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),

	("6J2M_TTPTDown", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("6J3M_TTPTDown", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("6J4M_TTPTDown", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("7J2M_TTPTDown", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("7J3M_TTPTDown", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("7J4M_TTPTDown", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("8J2M_TTPTDown", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("8J3M_TTPTDown", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("8J4M_TTPTDown", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("9J2M_TTPTDown", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("10J2M_TTPTDown", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),

	]
	if search_scheme == '9J3M,10J3M':
		cut_PT += 
		[
			("9J3M_TTPTUp", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
			("10J3M_TTPTUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),	
			("9J3M_TTPTDown", "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
			("10J3M_TTPTDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
		]
	elif search_scheme == '9J4M,10J4M':
		cut_PT += 
		[
			("9J3M_TTPTUp", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
			("9J4M_TTPTUp", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
			("10J3M_TTPTUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
			("10J4M_TTPTUp", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
			("9J3M_TTPTDown", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
			("9J4M_TTPTDown", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
			("10J3M_TTPTDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
			("10J4M_TTPTDown", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
		]
	return cut_PT
