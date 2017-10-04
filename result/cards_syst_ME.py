from centralweight import centralweight
def getMECutSets(syst,cut_string):
    cut_sets = [
        #central
        ("6J2M_{0}Up".format(syst), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("6J3M_{0}Up".format(syst), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("6J4M_{0}Up".format(syst), "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("7J2M_{0}Up".format(syst), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("7J3M_{0}Up".format(syst), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("7J4M_{0}Up".format(syst), "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("8J2M_{0}Up".format(syst), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("8J3M_{0}Up".format(syst), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("8J4M_{0}Up".format(syst), "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("9J2M_{0}Up".format(syst), "Njet=9, nMtags=2", "(nJets==9 && nMtags==2 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("9J3M_{0}Up".format(syst), "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("9J4M_{0}Up".format(syst), "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("10J2M_{0}Up".format(syst), "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("10J3M_{0}Up".format(syst), "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("10J4M_{0}Up".format(syst), "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}*Max$(abs(weight))".format(cut_string,centralweight)),
        ("6J2M_{0}Down".format(syst), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight)),
        ("6J3M_{0}Down".format(syst), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight)),
        ("6J4M_{0}Down".format(syst), "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight)),
        ("7J2M_{0}Down".format(syst), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight)),
        ("7J3M_{0}Down".format(syst), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight)),
        ("7J4M_{0}Down".format(syst), "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight)),
        ("8J2M_{0}Down".format(syst), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight)),
        ("8J3M_{0}Down".format(syst), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight)),
        ("8J4M_{0}Down".format(syst), "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight)),
        ("9J2M_{0}Down".format(syst), "Njet=9, nMtags=2", "(nJets==9 && nMtags==2 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight)),
        ("9J3M_{0}Down".format(syst), "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight)),
        ("9J4M_{0}Down".format(syst), "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight)),
        ("10J2M_{0}Down".format(syst), "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight)),
        ("10J3M_{0}Down".format(syst), "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight)),
        ("10J4M_{0}Down".format(syst), "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}*Min$(abs(weight))".format(cut_string,centralweight))
    ]
    return cut_sets
