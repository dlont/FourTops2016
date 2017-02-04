def getJECCutSets(systematic):
    syst, var = '',''
    if 'JES' in systematic.upper():
        syst = 'JES'
    elif 'JER' in systematic.upper():
        syst = 'JER'
    else:
        print 'Unrecognised systematic', systematic
    if 'UP' in systematic.upper():
        var = 'Up'
    elif 'DOWN' in systematic.upper():
        var = 'Down'
    else: 
        print 'Unrecognised systematic', systematic
    cut_sets = [
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