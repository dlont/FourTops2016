def cut_PAGPT(cut_string):
	cut_PT = [
	#PT UP
	("6J2M_TTPAGPTUp", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	("6J3M_TTPAGPTUp", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	("6J4M_TTPAGPTUp", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	("7J2M_TTPAGPTUp", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	("7J3M_TTPAGPTUp", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	("7J4M_TTPAGPTUp", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	("8J2M_TTPAGPTUp", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	("8J3M_TTPAGPTUp", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	("8J4M_TTPAGPTUp", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	("9J2M_TTPAGPTUp", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	("9J3M_TTPAGPTUp", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	("9J4M_TTPAGPTUp", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	("10J2M_TTPAGPTUp", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	("10J3M_TTPAGPTUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	("10J4M_TTPAGPTUp", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig".format(cut_string)),
	#PT DOWN
	("6J2M_TTPAGPTDown", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string)),
	("6J3M_TTPAGPTDown", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string)),
	("6J4M_TTPAGPTDown", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string)),
	("7J2M_TTPAGPTDown", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string)),
	("7J3M_TTPAGPTDown", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string)),
	("7J4M_TTPAGPTDown", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string)),
	("8J2M_TTPAGPTDown", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string)),
	("8J3M_TTPAGPTDown", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string)),
	("8J4M_TTPAGPTDown", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string)),
	("9J2M_TTPAGPTDown", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string)),
	("9J3M_TTPAGPTDown", "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string)),
	("9J4M_TTPAGPTDown", "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string)),
	("10J2M_TTPAGPTDown", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string)),
	("10J3M_TTPAGPTDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string)),
	("10J4M_TTPAGPTDown", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/toprewunc[0]".format(cut_string))
	]
	return cut_PT
