from centralweight import centralweight
def cut_PT(cut_string):
	cut_PT = [
	#PT UP
	("6J2M_TTWRONGPTUp", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("6J3M_TTWRONGPTUp", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("6J4M_TTWRONGPTUp", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("7J2M_TTWRONGPTUp", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("7J3M_TTWRONGPTUp", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("7J4M_TTWRONGPTUp", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("8J2M_TTWRONGPTUp", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("8J3M_TTWRONGPTUp", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("8J4M_TTWRONGPTUp", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("9J2M_TTWRONGPTUp", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("9J3M_TTWRONGPTUp", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("9J4M_TTWRONGPTUp", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("10J2M_TTWRONGPTUp", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("10J3M_TTWRONGPTUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	("10J4M_TTWRONGPTUp", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[1]".format(cut_string,centralweight)),
	#PT DOWN
	("6J2M_TTWRONGPTDown", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("6J3M_TTWRONGPTDown", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("6J4M_TTWRONGPTDown", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("7J2M_TTWRONGPTDown", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("7J3M_TTWRONGPTDown", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("7J4M_TTWRONGPTDown", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("8J2M_TTWRONGPTDown", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("8J3M_TTWRONGPTDown", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("8J4M_TTWRONGPTDown", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("9J2M_TTWRONGPTDown", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("9J3M_TTWRONGPTDown", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("9J4M_TTWRONGPTDown", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("10J2M_TTWRONGPTDown", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("10J3M_TTWRONGPTDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight)),
	("10J4M_TTWRONGPTDown", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/toprewunc[0]*toprewunc[2]".format(cut_string,centralweight))
	]
	return cut_PT
