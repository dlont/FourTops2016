from centralweight import centralweight
def getPDFCutSets(syst,cut_string,search_scheme='9J3M,10J3M'):
    cut_sets = [
        #central
        ("allSF_{0}Up".format(syst), "inclusive",  "(1 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
        ("allSF_{0}Down".format(syst), "inclusive",  "(1 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),

        ("6J2M_{0}Up".format(syst), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
        ("6J3M_{0}Up".format(syst), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
        ("6J4M_{0}Up".format(syst), "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
        ("7J2M_{0}Up".format(syst), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
        ("7J3M_{0}Up".format(syst), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
        ("7J4M_{0}Up".format(syst), "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
        ("8J2M_{0}Up".format(syst), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
        ("8J3M_{0}Up".format(syst), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
        ("8J4M_{0}Up".format(syst), "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
        ("9J2M_{0}Up".format(syst), "Njet=9, nMtags=2", "(nJets==9 && nMtags==2 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
        ("10J2M_{0}Up".format(syst), "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),

        ("6J2M_{0}Down".format(syst), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
        ("6J3M_{0}Down".format(syst), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
        ("6J4M_{0}Down".format(syst), "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
        ("7J2M_{0}Down".format(syst), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
        ("7J3M_{0}Down".format(syst), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
        ("7J4M_{0}Down".format(syst), "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
        ("8J2M_{0}Down".format(syst), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
        ("8J3M_{0}Down".format(syst), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
        ("8J4M_{0}Down".format(syst), "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
        ("9J2M_{0}Down".format(syst), "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
        ("10J2M_{0}Down".format(syst), "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
    ]
    if search_scheme == '9J3M,10J3M':
            cut_sets += [
            ("9J3M_{0}Up".format(syst), "Njet=9, nMtags=3", "(nJets==9 && nMtags>=3 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
            ("10J3M_{0}Up".format(syst), "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
            ("9J3M_{0}Down".format(syst), "Njet=9, nMtags=3",  "(nJets==9 && nMtags>=3 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
            ("10J3M_{0}Down".format(syst), "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
		]
    elif search_scheme == '9J4M,10J4M':
            cut_sets += [
            ("9J3M_{0}Up".format(syst), "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
            ("9J4M_{0}Up".format(syst), "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
            ("10J3M_{0}Up".format(syst), "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
            ("10J4M_{0}Up".format(syst), "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}*Max$(abs(pdfw))".format(cut_string,centralweight)),
            ("9J3M_{0}Down".format(syst), "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
            ("9J4M_{0}Down".format(syst), "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
            ("10J3M_{0}Down".format(syst), "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight)),
            ("10J4M_{0}Down".format(syst), "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}*Min$(abs(pdfw))".format(cut_string,centralweight))
		]
    return cut_sets

