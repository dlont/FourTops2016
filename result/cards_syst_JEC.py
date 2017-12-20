from centralweight import centralweight
def getJECCutSets(systematic, cut_string):
    syst, var = '',''
    if 'JES' in systematic.upper():
        syst = 'JES'
    elif 'SUBTOTALSCALEJEC' in systematic.upper():
	syst = 'SubTotalScaleJES'
    elif 'SUBTOTALRELATIVEJEC' in systematic.upper():
	syst = 'SubTotalRelativeJES'
    elif 'SUBTOTALPTJEC' in systematic.upper():
	syst = 'SubTotalPtJES'
    elif 'SUBTOTALPILEJEC' in systematic.upper():
	syst = 'SubTotalPileUpJES'
    elif 'SUBTOTALFLAVORJEC' in systematic.upper():
	syst = 'SubTotalFlavorJES'
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
        ("allSF_{0}{1}".format(syst,var), "inclusive",  "(1 {0})*{1}".format(cut_string,centralweight)),

        ("6J2M_{0}{1}".format(syst,var), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
        ("6J3M_{0}{1}".format(syst,var), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
        ("6J4M_{0}{1}".format(syst,var), "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
        ("7J2M_{0}{1}".format(syst,var), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
        ("7J3M_{0}{1}".format(syst,var), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
        ("7J4M_{0}{1}".format(syst,var), "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
        ("8J2M_{0}{1}".format(syst,var), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
        ("8J3M_{0}{1}".format(syst,var), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
        ("8J4M_{0}{1}".format(syst,var), "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
        ("9J2M_{0}{1}".format(syst,var), "Njet=9, nMtags=2", "(nJets==9 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
        ("9J3M_{0}{1}".format(syst,var), "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
        ("9J4M_{0}{1}".format(syst,var), "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
        ("10J2M_{0}{1}".format(syst,var), "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
        ("10J3M_{0}{1}".format(syst,var), "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
        ("10J4M_{0}{1}".format(syst,var), "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}".format(cut_string,centralweight))
    ]
    return cut_sets
