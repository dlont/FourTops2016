def getHDAMPCutSets(syst,cut_string):
    cut_sets = [
        #central
        ("6J2M_{0}Up".format(syst), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("6J3M_{0}Up".format(syst), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("6J4M_{0}Up".format(syst), "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("7J2M_{0}Up".format(syst), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("7J3M_{0}Up".format(syst), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("7J4M_{0}Up".format(syst), "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("8J2M_{0}Up".format(syst), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("8J3M_{0}Up".format(syst), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("8J4M_{0}Up".format(syst), "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("9J2M_{0}Up".format(syst), "Njet=9, nMtags=2", "(nJets==9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("9J3M_{0}Up".format(syst), "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("9J4M_{0}Up".format(syst), "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("10J2M_{0}Up".format(syst), "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("10J3M_{0}Up".format(syst), "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("10J4M_{0}Up".format(syst), "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig*Max$(abs(hdampw))".format(cut_string)),
        ("6J2M_{0}Down".format(syst), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string)),
        ("6J3M_{0}Down".format(syst), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string)),
        ("6J4M_{0}Down".format(syst), "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string)),
        ("7J2M_{0}Down".format(syst), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string)),
        ("7J3M_{0}Down".format(syst), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string)),
        ("7J4M_{0}Down".format(syst), "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string)),
        ("8J2M_{0}Down".format(syst), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string)),
        ("8J3M_{0}Down".format(syst), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string)),
        ("8J4M_{0}Down".format(syst), "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string)),
        ("9J2M_{0}Down".format(syst), "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string)),
        ("9J3M_{0}Down".format(syst), "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string)),
        ("9J4M_{0}Down".format(syst), "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string)),
        ("10J2M_{0}Down".format(syst), "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string)),
        ("10J3M_{0}Down".format(syst), "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string)),
        ("10J4M_{0}Down".format(syst), "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {})*ScaleFactor*GenWeight*SFtrig*Min$(abs(hdampw))".format(cut_string))
    ]
    return cut_sets

