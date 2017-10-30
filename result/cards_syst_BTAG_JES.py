from centralweight import centralweight
def cut_BTAG_JES(systematic,cut_string):
    cut_sets = []
    syst, var = 'btagWeightCSVJES',''
    if 'UP' in systematic.upper():
        var = 'Up'
	cut_sets = [
	       ("allSF_{0}{1}".format(syst,var), "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),

	       ("6J2M_{0}{1}".format(syst,var), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),
	       ("6J3M_{0}{1}".format(syst,var), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),
	       ("6J4M_{0}{1}".format(syst,var), "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),
	       ("7J2M_{0}{1}".format(syst,var), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),
	       ("7J3M_{0}{1}".format(syst,var), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),
	       ("7J4M_{0}{1}".format(syst,var), "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),
	       ("8J2M_{0}{1}".format(syst,var), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),
	       ("8J3M_{0}{1}".format(syst,var), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),
	       ("8J4M_{0}{1}".format(syst,var), "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),
	       ("9J2M_{0}{1}".format(syst,var), "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),
	       ("9J3M_{0}{1}".format(syst,var), "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),
	       ("9J4M_{0}{1}".format(syst,var), "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),
	       ("10J2M_{0}{1}".format(syst,var), "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),
	       ("10J3M_{0}{1}".format(syst,var), "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight)),
	       ("10J4M_{0}{1}".format(syst,var), "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[1]".format(cut_string,centralweight))
	]
    elif 'DOWN' in systematic.upper():
        var = 'Down'
	cut_sets = [
	       ("allSF_{0}{1}".format(syst,var), "inclusive",  "(1 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),

	       ("6J2M_{0}{1}".format(syst,var), "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),
	       ("6J3M_{0}{1}".format(syst,var), "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),
	       ("6J4M_{0}{1}".format(syst,var), "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),
	       ("7J2M_{0}{1}".format(syst,var), "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),
	       ("7J3M_{0}{1}".format(syst,var), "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),
	       ("7J4M_{0}{1}".format(syst,var), "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),
	       ("8J2M_{0}{1}".format(syst,var), "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),
	       ("8J3M_{0}{1}".format(syst,var), "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),
	       ("8J4M_{0}{1}".format(syst,var), "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),
	       ("9J2M_{0}{1}".format(syst,var), "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),
	       ("9J3M_{0}{1}".format(syst,var), "Njet=9, nMtags=3",  "(nJets==9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),
	       ("9J4M_{0}{1}".format(syst,var), "Njet=9, nMtags=4",  "(nJets==9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),
	       ("10J2M_{0}{1}".format(syst,var), "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),
	       ("10J3M_{0}{1}".format(syst,var), "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight)),
	       ("10J4M_{0}{1}".format(syst,var), "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}/csvrsw[0]*csvrsw[2]".format(cut_string,centralweight))
	]
    else:
        print 'Unrecognised systematic', systematic
	
    return cut_sets
