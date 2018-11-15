from centralweight import centralweight
def cut_PU(cut_string,search_scheme='9J3M,10J3M'):
	cut_PU = [
	#PU UP
	("allSF_PUUp", "inclusive",  "(1 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),

	("6J2M_PUUp", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
	("6J3M_PUUp", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
	("6J4M_PUUp", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
	("7J2M_PUUp", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
	("7J3M_PUUp", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
	("7J4M_PUUp", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
	("8J2M_PUUp", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
	("8J3M_PUUp", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
	("8J4M_PUUp", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
	("9J2M_PUUp", "Njet=9, nMtags=2", "(nJets==9 && nMtags==2 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
	("10J2M_PUUp", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
	#PU DOWN
	("allSF_PUDown", "inclusive",  "(1 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),

	("6J2M_PUDown", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
	("6J3M_PUDown", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
	("6J4M_PUDown", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
	("7J2M_PUDown", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
	("7J3M_PUDown", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
	("7J4M_PUDown", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
	("8J2M_PUDown", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
	("8J3M_PUDown", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
	("8J4M_PUDown", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
	("9J2M_PUDown", "Njet=9, nMtags=2", "(nJets==9 && nMtags==2 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
	("10J2M_PUDown", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
	]
	if search_scheme == '9J3M,10J3M':
		cut_PU += [
			("9J3M_PUUp", "Njet=9, nMtags=3", "(nJets==9 && nMtags>=3 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
			("10J3M_PUUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
			("9J3M_PUDown", "Njet=9, nMtags=3", "(nJets==9 && nMtags>=3 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
			("10J3M_PUDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
		]
	elif search_scheme == '9J4M,10J4M':
		cut_PU += [
			("9J3M_PUUp", "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
			("9J4M_PUUp", "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
			("10J3M_PUUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
			("10J4M_PUUp", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/SFPU*SFPU_up".format(cut_string,centralweight)),
			("9J3M_PUDown", "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
			("9J4M_PUDown", "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
			("10J3M_PUDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
			("10J4M_PUDown", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/SFPU*SFPU_down".format(cut_string,centralweight)),
		]
	return cut_PU
