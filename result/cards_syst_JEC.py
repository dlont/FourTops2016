def getJECCutSets(systematic):
    if systematic.upper() == 'JESUP':
        syst, var = 'JES', 'Up'
    elif systematic.upper() == 'JESDOWN':
        syst, var = 'JES', 'Down'
    elif systematic.upper() == 'JERUP':
        syst, var = 'JER', 'Up'
    elif systematic.upper() == 'JERDOWN':
        syst, var = 'JER', 'Down'
    else: pass
    cut_sets = [
        #central
        ("6J2M_{0}{1}".format(syst,var), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2)*ScaleFactor"),
        ("6J3M_{0}{1}".format(syst,var), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3)*ScaleFactor"),
        ("6J4M_{0}{1}".format(syst,var), "Njet=6, nMtags=4",  "(nJets==6 && nMtags==4)*ScaleFactor"),
        ("7J2M_{0}{1}".format(syst,var), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2)*ScaleFactor"),
        ("7J3M_{0}{1}".format(syst,var), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3)*ScaleFactor"),
        ("7J4M_{0}{1}".format(syst,var), "Njet=7, nMtags=4",  "(nJets==7 && nMtags==4)*ScaleFactor"),
        ("8J2M_{0}{1}".format(syst,var), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2)*ScaleFactor"),
        ("8J3M_{0}{1}".format(syst,var), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3)*ScaleFactor"),
        ("8J4M_{0}{1}".format(syst,var), "Njet=8, nMtags=4",  "(nJets==8 && nMtags==4)*ScaleFactor"),
        ("9J2M_{0}{1}".format(syst,var), "Njet=9+, nMtags=2", "(nJets>=9 && nMtags==2)*ScaleFactor"),
        ("9J3M_{0}{1}".format(syst,var), "Njet=9+, nMtags=3", "(nJets>=9 && nMtags==3)*ScaleFactor"),
        ("9J4M_{0}{1}".format(syst,var), "Njet=9+, nMtags=4", "(nJets>=9 && nMtags==4)*ScaleFactor")
    ]
    return cut_sets