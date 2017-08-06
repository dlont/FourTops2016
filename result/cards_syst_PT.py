def cut_PT(cut_string):
	cut_PT = [
	#PT UP
	("6J2M_TTPTUp", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	("6J3M_TTPTUp", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	("6J4M_TTPTUp", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	("7J2M_TTPTUp", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	("7J3M_TTPTUp", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	("7J4M_TTPTUp", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	("8J2M_TTPTUp", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	("8J3M_TTPTUp", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	("8J4M_TTPTUp", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	("9J2M_TTPTUp", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	("9J3M_TTPTUp", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	("9J4M_TTPTUp", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	("10J2M_TTPTUp", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	("10J3M_TTPTUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	("10J4M_TTPTUp", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[1]".format(cut_string)),
	#PT DOWN
	("6J2M_TTPTDown", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string)),
	("6J3M_TTPTDown", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string)),
	("6J4M_TTPTDown", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string)),
	("7J2M_TTPTDown", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string)),
	("7J3M_TTPTDown", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string)),
	("7J4M_TTPTDown", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string)),
	("8J2M_TTPTDown", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string)),
	("8J3M_TTPTDown", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string)),
	("8J4M_TTPTDown", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string)),
	("9J2M_TTPTDown", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string)),
	("9J3M_TTPTDown", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string)),
	("9J4M_TTPTDown", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string)),
	("10J2M_TTPTDown", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string)),
	("10J3M_TTPTDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string)),
	("10J4M_TTPTDown", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]*toprewunc[2]".format(cut_string))
	]
	return cut_PT
