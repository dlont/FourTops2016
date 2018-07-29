from centralweight import centralweight
def getHDAMPAltCutSets(syst,cut_string,search_scheme='9J3M,10J3M'):
    if 'UP' in syst.upper():
        var = 'Up'
    elif 'DOWN' in syst.upper():
        var = 'Down'
    else: 
        print 'Unrecognised systematic', systematic
    cut_sets = [
        ("allSF_TTJets_HDAMP{1}".format(syst,var), "inclusive",  "(1 {0})*{1}".format(cut_string,centralweight)),

        ("6J2M_TTJets_HDAMP{1}".format(syst,var), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
        ("6J3M_TTJets_HDAMP{1}".format(syst,var), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
        ("6J4M_TTJets_HDAMP{1}".format(syst,var), "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
        ("7J2M_TTJets_HDAMP{1}".format(syst,var), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
        ("7J3M_TTJets_HDAMP{1}".format(syst,var), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
        ("7J4M_TTJets_HDAMP{1}".format(syst,var), "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
        ("8J2M_TTJets_HDAMP{1}".format(syst,var), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
        ("8J3M_TTJets_HDAMP{1}".format(syst,var), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
        ("8J4M_TTJets_HDAMP{1}".format(syst,var), "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
        ("9J2M_TTJets_HDAMP{1}".format(syst,var), "Njet=9, nMtags=2", "(nJets==9 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
        ("10J2M_TTJets_HDAMP{1}".format(syst,var), "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
    ]
    if search_scheme == '9J3M,10J3M':
        cut_sets += 
        [
        ("9J3M_TTJets_HDAMP{1}".format(syst,var), "Njet=9, nMtags=3", "(nJets==9 && nMtags>=3 {0})*{1}".format(cut_string,centralweight)),
        ("10J3M_TTJets_HDAMP{1}".format(syst,var), "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}".format(cut_string,centralweight)),
        ]
    elif search_scheme == '9J4M,10J4M':
        cut_sets += 
        [
        ("9J3M_TTJets_HDAMP{1}".format(syst,var), "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
        ("9J4M_TTJets_HDAMP{1}".format(syst,var), "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
        ("10J3M_TTJets_HDAMP{1}".format(syst,var), "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
        ("10J4M_TTJets_HDAMP{1}".format(syst,var), "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}".format(cut_string,centralweight))
        ]
    return cut_sets

