def cut_BTAG_JES(systematic,cut_string):
    cut_sets = []
    syst, var = 'btagWeightCSVJES',''
    if 'UP' in systematic.upper():
        var = 'Up'
	cut_sets = [
	       ("6J2M_{0}{1}".format(syst,var), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string)),
	       ("6J3M_{0}{1}".format(syst,var), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string)),
	       ("6J4M_{0}{1}".format(syst,var), "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string)),
	       ("7J2M_{0}{1}".format(syst,var), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string)),
	       ("7J3M_{0}{1}".format(syst,var), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string)),
	       ("7J4M_{0}{1}".format(syst,var), "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string)),
	       ("8J2M_{0}{1}".format(syst,var), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string)),
	       ("8J3M_{0}{1}".format(syst,var), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string)),
	       ("8J4M_{0}{1}".format(syst,var), "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string)),
	       ("9J2M_{0}{1}".format(syst,var), "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string)),
	       ("9J3M_{0}{1}".format(syst,var), "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string)),
	       ("9J4M_{0}{1}".format(syst,var), "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string)),
	       ("10J2M_{0}{1}".format(syst,var), "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string)),
	       ("10J3M_{0}{1}".format(syst,var), "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string)),
	       ("10J4M_{0}{1}".format(syst,var), "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[1]".format(cut_string))
	]
    elif 'DOWN' in systematic.upper():
        var = 'Down'
	cut_sets = [
	       ("6J2M_{0}{1}".format(syst,var), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string)),
	       ("6J3M_{0}{1}".format(syst,var), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string)),
	       ("6J4M_{0}{1}".format(syst,var), "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string)),
	       ("7J2M_{0}{1}".format(syst,var), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string)),
	       ("7J3M_{0}{1}".format(syst,var), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string)),
	       ("7J4M_{0}{1}".format(syst,var), "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string)),
	       ("8J2M_{0}{1}".format(syst,var), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string)),
	       ("8J3M_{0}{1}".format(syst,var), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string)),
	       ("8J4M_{0}{1}".format(syst,var), "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string)),
	       ("9J2M_{0}{1}".format(syst,var), "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string)),
	       ("9J3M_{0}{1}".format(syst,var), "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string)),
	       ("9J4M_{0}{1}".format(syst,var), "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string)),
	       ("10J2M_{0}{1}".format(syst,var), "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string)),
	       ("10J3M_{0}{1}".format(syst,var), "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string)),
	       ("10J4M_{0}{1}".format(syst,var), "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig/csvrsw[0]*csvrsw[2]".format(cut_string))
	]
    else:
        print 'Unrecognised systematic', systematic
	
    return cut_sets
