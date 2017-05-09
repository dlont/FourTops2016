def cut_PU(cut_string):
	cut_PU = [
	#PU UP
	("6J2M_PUUp", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	("6J3M_PUUp", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	("6J4M_PUUp", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	("7J2M_PUUp", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	("7J3M_PUUp", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	("7J4M_PUUp", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	("8J2M_PUUp", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	("8J3M_PUUp", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	("8J4M_PUUp", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	("9J2M_PUUp", "Njet=9, nMtags=2", "(nJets==9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	("9J3M_PUUp", "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	("9J4M_PUUp", "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	("10J2M_PUUp", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	("10J3M_PUUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	("10J4M_PUUp", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_up".format(cut_string)),
	#PU DOWN
	("6J2M_PUDown", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string)),
	("6J3M_PUDown", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string)),
	("6J4M_PUDown", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string)),
	("7J2M_PUDown", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string)),
	("7J3M_PUDown", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string)),
	("7J4M_PUDown", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string)),
	("8J2M_PUDown", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string)),
	("8J3M_PUDown", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string)),
	("8J4M_PUDown", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string)),
	("9J2M_PUDown", "Njet=9, nMtags=2", "(nJets==9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string)),
	("9J3M_PUDown", "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string)),
	("9J4M_PUDown", "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string)),
	("10J2M_PUDown", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string)),
	("10J3M_PUDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string)),
	("10J4M_PUDown", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/SFPU*SFPU_down".format(cut_string))
	]
	return cut_PU
