def getMECutSets(syst):
    cut_sets = [
        #central
        ("6J2M_{0}Up".format(syst), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2)*ScaleFactor*Max$(abs(weight))"),
        ("6J3M_{0}Up".format(syst), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3)*ScaleFactor*Max$(abs(weight))"),
        ("6J4M_{0}Up".format(syst), "Njet=6, nMtags=4",  "(nJets==6 && nMtags==4)*ScaleFactor*Max$(abs(weight))"),
        ("7J2M_{0}Up".format(syst), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2)*ScaleFactor*Max$(abs(weight))"),
        ("7J3M_{0}Up".format(syst), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3)*ScaleFactor*Max$(abs(weight))"),
        ("7J4M_{0}Up".format(syst), "Njet=7, nMtags=4",  "(nJets==7 && nMtags==4)*ScaleFactor*Max$(abs(weight))"),
        ("8J2M_{0}Up".format(syst), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2)*ScaleFactor*Max$(abs(weight))"),
        ("8J3M_{0}Up".format(syst), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3)*ScaleFactor*Max$(abs(weight))"),
        ("8J4M_{0}Up".format(syst), "Njet=8, nMtags=4",  "(nJets==8 && nMtags==4)*ScaleFactor*Max$(abs(weight))"),
        ("9J2M_{0}Up".format(syst), "Njet=9+, nMtags=2", "(nJets>=9 && nMtags==2)*ScaleFactor*Max$(abs(weight))"),
        ("9J3M_{0}Up".format(syst), "Njet=9+, nMtags=3", "(nJets>=9 && nMtags==3)*ScaleFactor*Max$(abs(weight))"),
        ("9J4M_{0}Up".format(syst), "Njet=9+, nMtags=4", "(nJets>=9 && nMtags==4)*ScaleFactor*Max$(abs(weight))"),
        ("6J2M_{0}Down".format(syst), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2)*ScaleFactor*Min$(abs(weight))"),
        ("6J3M_{0}Down".format(syst), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3)*ScaleFactor*Min$(abs(weight))"),
        ("6J4M_{0}Down".format(syst), "Njet=6, nMtags=4",  "(nJets==6 && nMtags==4)*ScaleFactor*Min$(abs(weight))"),
        ("7J2M_{0}Down".format(syst), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2)*ScaleFactor*Min$(abs(weight))"),
        ("7J3M_{0}Down".format(syst), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3)*ScaleFactor*Min$(abs(weight))"),
        ("7J4M_{0}Down".format(syst), "Njet=7, nMtags=4",  "(nJets==7 && nMtags==4)*ScaleFactor*Min$(abs(weight))"),
        ("8J2M_{0}Down".format(syst), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2)*ScaleFactor*Min$(abs(weight))"),
        ("8J3M_{0}Down".format(syst), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3)*ScaleFactor*Min$(abs(weight))"),
        ("8J4M_{0}Down".format(syst), "Njet=8, nMtags=4",  "(nJets==8 && nMtags==4)*ScaleFactor*Min$(abs(weight))"),
        ("9J2M_{0}Down".format(syst), "Njet=9+, nMtags=2", "(nJets>=9 && nMtags==2)*ScaleFactor*Min$(abs(weight))"),
        ("9J3M_{0}Down".format(syst), "Njet=9+, nMtags=3", "(nJets>=9 && nMtags==3)*ScaleFactor*Min$(abs(weight))"),
        ("9J4M_{0}Down".format(syst), "Njet=9+, nMtags=4", "(nJets>=9 && nMtags==4)*ScaleFactor*Min$(abs(weight))")
    ]
    return cut_sets