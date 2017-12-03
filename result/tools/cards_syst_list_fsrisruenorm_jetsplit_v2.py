from cards_bin_list import binlist

systtypelist = {
'mu':{
'TTJets_norm':'lnN',
#'TTJets_norm8':'lnN',
#'TTJets_norm9':'lnN',
'TTJets_norm10':'lnN',
'ttMEScale':'shape',
'TTJets_HDAMP':'lnN',
'TTJets_PDF':'shape',
'heavyFlav':'shape',
'tttt_norm':'lnN',
'TTTTMEScale':'shape',
'ST_tW_norm':'lnN',
'EW_norm':'lnN',
'TTRARE_norm':'lnN',
'lumi':'lnN',
'PU':'shape',
'SubTotalPileUpJES':'shape',
'SubTotalScaleJES':'shape',
'SubTotalPtJES':'shape',
'SubTotalRelativeJES':'shape',
'JER':'shape',
'leptonSFMu':'lnN',
#{'ScaleH',
#{'heavyFlav',
'TTISR':'lnN',
'TTFSR':'lnN',
'TTUE':'lnN',
'TTPT':'shape',
'TTTTISR':'lnN',
'TTTTFSR':'lnN',
'btagWeightCSVJES':'shape',
'btagWeightCSVHF':'shape',
'btagWeightCSVLF':'shape',
'btagWeightCSVHFStats1':'shape',
'btagWeightCSVHFStats2':'shape',
'btagWeightCSVLFStats1':'shape',
'btagWeightCSVLFStats2':'shape',
'btagWeightCSVCFErr1':'shape',
'btagWeightCSVCFErr2':'shape'
},
'el':{
'TTJets_norm':'lnN',
#'TTJets_norm8':'lnN',
#'TTJets_norm9':'lnN',
'TTJets_norm10':'lnN',
'ttMEScale':'shape',
'TTJets_HDAMP':'lnN',
'TTJets_PDF':'shape',
'heavyFlav':'shape',
'tttt_norm':'lnN',
'TTTTMEScale':'shape',
'ST_tW_norm':'lnN',
'TTRARE_norm':'lnN',
'EW_norm':'lnN',
'lumi':'lnN',
'PU':'shape',
'SubTotalPileUpJES':'shape',
'SubTotalScaleJES':'shape',
'SubTotalPtJES':'shape',
'SubTotalRelativeJES':'shape',
'JER':'shape',
'leptonSFEl':'lnN',
#{'ScaleH',
#{'heavyFlav',
'TTISR':'lnN',
'TTFSR':'lnN',
'TTUE':'lnN',
'TTPT':'shape',
'TTTTISR':'lnN',
'TTTTFSR':'lnN',
'btagWeightCSVJES':'shape',
'btagWeightCSVHF':'shape',
'btagWeightCSVLF':'shape',
'btagWeightCSVHFStats1':'shape',
'btagWeightCSVHFStats2':'shape',
'btagWeightCSVLFStats1':'shape',
'btagWeightCSVLFStats2':'shape',
'btagWeightCSVCFErr1':'shape',
'btagWeightCSVCFErr2':'shape'
}}



na = '-'
lumiunc = 1.025
leptonsf = 1.03

tt7jetbinunc = lambda x: '0.95/1.05' if '7J' in x else '-'
tt8jetbinunc = lambda x: '2.0' if '8J' in x else '-'
tt9jetbinunc = lambda x: '2.0' if '9J' in x else '-'
tt10jetbinunc = lambda x: '1.1' if '10J' in x else '-'
TTJets_norm7_mu_unc  = list(map(tt7jetbinunc, binlist['mu']))
TTJets_norm8_mu_unc  = list(map(tt8jetbinunc, binlist['mu']))
TTJets_norm9_mu_unc  = list(map(tt9jetbinunc, binlist['mu']))
TTJets_norm10_mu_unc = list(map(tt10jetbinunc, binlist['mu']))
TTJets_norm7_el_unc  = list(map(tt7jetbinunc, binlist['el']))
TTJets_norm8_el_unc  = list(map(tt8jetbinunc, binlist['el']))
TTJets_norm9_el_unc  = list(map(tt9jetbinunc, binlist['el']))
TTJets_norm10_el_unc = list(map(tt10jetbinunc, binlist['el']))

def syst_norm_size(rootfiles,ch):

	sysdic = {}
	for sys in ["TTISR","TTFSR","TTUE","TTJets_HDAMP"]:
		syslist = []
		for cat in binlist[ch]:
			cat = cat.replace("mu",""); cat = cat.replace("el","");	#strip prefix
			central = rootfiles['ttbarTTX'].Get(cat+'/bdt')
			sysup   = rootfiles['ttbarTTX'].Get(cat+'_'+sys+'Up/bdt')
			sysdown = rootfiles['ttbarTTX'].Get(cat+'_'+sys+'Down/bdt')
			unc = 1.
			#print cat, sys, central, sysup, sysdown
			if sysdown.Integral()/central.Integral() > 1:
				unc = max(sysdown.Integral()/central.Integral(), sysup.Integral()/central.Integral())
			if sysup.Integral()/central.Integral() < 1:
				unc = min(sysdown.Integral()/central.Integral(), sysup.Integral()/central.Integral())
			if unc < 1. and len(syslist)>0: unc = syslist[-1]
			if sysup.Integral()/central.Integral() > 1 and sysdown.Integral()/central.Integral() < 1:
				unc = ''+str(sysdown.Integral()/central.Integral())+'/'+str(sysup.Integral()/central.Integral())
			syslist.append( unc )
		sysdic[sys] = syslist

	for sys in ["TTTTISR","TTTTFSR"]:
		syslist = []
		for cat in binlist[ch]:
			cat = cat.replace("mu",""); cat = cat.replace("el","");	#strip prefix
			central = rootfiles['NP_overlay_ttttNLO'].Get(cat+'/bdt')
			sysup   = rootfiles['NP_overlay_ttttNLO'].Get(cat+'_'+sys+'Up/bdt')
			sysdown = rootfiles['NP_overlay_ttttNLO'].Get(cat+'_'+sys+'Down/bdt')
			unc = 1.
			#print cat, sys, central, sysup, sysdown
			if sysdown.Integral()/central.Integral() > 1:
				unc = max(sysdown.Integral()/central.Integral(), sysup.Integral()/central.Integral())
			if sysup.Integral()/central.Integral() < 1:
				unc = min(sysdown.Integral()/central.Integral(), sysup.Integral()/central.Integral())
			if unc < 1. and len(syslist)>0: unc = syslist[-1]
			if sysup.Integral()/central.Integral() > 1 and sysdown.Integral()/central.Integral() < 1:
				unc = ''+str(sysdown.Integral()/central.Integral())+'/'+str(sysup.Integral()/central.Integral())
			syslist.append( unc )
		sysdic[sys] = syslist

	syst_norm_size_list_dict = {
'mu':{ 'NP_overlay_ttttNLO' : {
            'TTJets_HDAMP'      :[na         ]*len(binlist['mu']),
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            #'TTJets_norm8'      :[na         ]*len(binlist['mu']),
            #'TTJets_norm9'      :[na         ]*len(binlist['mu']),
            'TTJets_norm10'     :[na         ]*len(binlist['mu']),
            'tttt_norm'         :['0.94/1.05']*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'TTRARE_norm'          :[na         ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'TTISR'             :[na         ]*len(binlist['mu']),
            'TTFSR'             :[na         ]*len(binlist['mu']),
            'TTUE'              :[na         ]*len(binlist['mu']),
            'TTTTISR'           :sysdic['TTTTISR'],
            'TTTTFSR'           :sysdic['TTTTFSR'],
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},
       'ttbarTTX' : {
            'TTJets_HDAMP'      :sysdic['TTJets_HDAMP'],
            'TTJets_norm'       :TTJets_norm7_mu_unc,
            #'TTJets_norm8'      :TTJets_norm8_mu_unc,
            #'TTJets_norm9'      :TTJets_norm9_mu_unc,
            'TTJets_norm10'     :TTJets_norm10_mu_unc,
            'tttt_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'TTRARE_norm'       :[na         ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'TTISR'             :sysdic['TTISR'],
            'TTFSR'             :sysdic['TTFSR'],
            'TTUE'              :sysdic['TTUE'],
            'TTTTISR'           :[na         ]*len(binlist['mu']),
            'TTTTFSR'           :[na         ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},
       'EW' : {
            'TTJets_HDAMP'      :[na         ]*len(binlist['mu']),
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            #'TTJets_norm8'      :[na         ]*len(binlist['mu']),
            #'TTJets_norm9'      :[na         ]*len(binlist['mu']),
            'TTJets_norm10'     :[na         ]*len(binlist['mu']),
            'tttt_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[1.04       ]*len(binlist['mu']),
            'TTRARE_norm'          :[na         ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'TTISR'             :[na         ]*len(binlist['mu']),
            'TTFSR'             :[na         ]*len(binlist['mu']),
            'TTUE'              :[na         ]*len(binlist['mu']),
            'TTTTISR'           :[na         ]*len(binlist['mu']),
            'TTTTFSR'           :[na         ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},     
       'TTRARE' : {
            'TTJets_HDAMP'      :[na         ]*len(binlist['mu']),
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            #'TTJets_norm8'      :[na         ]*len(binlist['mu']),
            #'TTJets_norm9'      :[na         ]*len(binlist['mu']),
            'TTJets_norm10'     :[na         ]*len(binlist['mu']),
            'tttt_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'TTRARE_norm'          :[1.5        ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'TTISR'             :[na         ]*len(binlist['mu']),
            'TTFSR'             :[na         ]*len(binlist['mu']),
            'TTUE'              :[na         ]*len(binlist['mu']),
            'TTTTISR'           :[na         ]*len(binlist['mu']),
            'TTTTFSR'           :[na         ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},     
       'ST_tW' : {
            'TTJets_HDAMP'      :[na         ]*len(binlist['mu']),
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            #'TTJets_norm8'      :[na         ]*len(binlist['mu']),
            #'TTJets_norm9'      :[na         ]*len(binlist['mu']),
            'TTJets_norm10'     :[na         ]*len(binlist['mu']),
            'tttt_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[1.04       ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'TTRARE_norm'          :[na         ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'TTISR'             :[na         ]*len(binlist['mu']),
            'TTFSR'             :[na         ]*len(binlist['mu']),
            'TTUE'              :[na         ]*len(binlist['mu']),
            'TTTTISR'           :[na         ]*len(binlist['mu']),
            'TTTTFSR'           :[na         ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])}, 
},
'el':{ 'NP_overlay_ttttNLO' : {
            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
            'TTJets_norm'       :[na         ]*len(binlist['el']),
            #'TTJets_norm8'      :[na         ]*len(binlist['el']),
            #'TTJets_norm9'      :[na         ]*len(binlist['el']),
            'TTJets_norm10'     :[na         ]*len(binlist['el']),
            'tttt_norm'         :['0.94/1.05']*len(binlist['el']),
            'ST_tW_norm'        :[na         ]*len(binlist['el']),
            'EW_norm'           :[na         ]*len(binlist['el']),
            'TTRARE_norm'          :[na         ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'TTISR'             :[na         ]*len(binlist['el']),
            'TTFSR'             :[na         ]*len(binlist['el']),
            'TTUE'              :[na         ]*len(binlist['el']),
            'TTTTISR'           :sysdic['TTTTISR'],
            'TTTTFSR'           :sysdic['TTTTFSR'],
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])},
       'ttbarTTX' : {
            'TTJets_HDAMP'      :sysdic['TTJets_HDAMP'],
            'TTJets_norm'       :TTJets_norm7_el_unc,
            #'TTJets_norm8'      :TTJets_norm8_el_unc,
            #'TTJets_norm9'      :TTJets_norm9_el_unc,
            'TTJets_norm10'     :TTJets_norm10_el_unc,
            'tttt_norm'         :[na         ]*len(binlist['el']),
            'ST_tW_norm'        :[na         ]*len(binlist['el']),
            'EW_norm'           :[na         ]*len(binlist['el']),
            'TTRARE_norm'          :[na         ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'TTISR'             :sysdic['TTISR'],
            'TTFSR'             :sysdic['TTFSR'],
            'TTUE'              :sysdic['TTUE'],
            'TTTTISR'           :[na         ]*len(binlist['el']),
            'TTTTFSR'           :[na         ]*len(binlist['el']),
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])},
       'EW' : {
            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
            'TTJets_norm'       :[na         ]*len(binlist['el']),
            #'TTJets_norm8'      :[na         ]*len(binlist['el']),
            #'TTJets_norm9'      :[na         ]*len(binlist['el']),
            'TTJets_norm10'     :[na         ]*len(binlist['el']),
            'tttt_norm'         :[na         ]*len(binlist['el']),
            'ST_tW_norm'        :[na         ]*len(binlist['el']),
            'EW_norm'           :[1.04       ]*len(binlist['el']),
            'TTRARE_norm'          :[na         ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'TTISR'             :[na         ]*len(binlist['el']),
            'TTFSR'             :[na         ]*len(binlist['el']),
            'TTUE'              :[na         ]*len(binlist['el']),
            'TTTTISR'           :[na         ]*len(binlist['el']),
            'TTTTFSR'           :[na         ]*len(binlist['el']),
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])},     
       'TTRARE' : {
            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
            'TTJets_norm'       :[na         ]*len(binlist['el']),
            #'TTJets_norm8'      :[na         ]*len(binlist['el']),
            #'TTJets_norm9'      :[na         ]*len(binlist['el']),
            'TTJets_norm10'     :[na         ]*len(binlist['el']),
            'tttt_norm'         :[na         ]*len(binlist['el']),
            'ST_tW_norm'        :[na         ]*len(binlist['el']),
            'EW_norm'           :[na         ]*len(binlist['el']),
            'TTRARE_norm'          :[1.5        ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'TTISR'             :[na         ]*len(binlist['el']),
            'TTFSR'             :[na         ]*len(binlist['el']),
            'TTUE'              :[na         ]*len(binlist['el']),
            'TTTTISR'           :[na         ]*len(binlist['el']),
            'TTTTFSR'           :[na         ]*len(binlist['el']),
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])},     
       'ST_tW' : {
            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
            'TTJets_norm'       :[na         ]*len(binlist['el']),
            #'TTJets_norm8'      :[na         ]*len(binlist['el']),
            #'TTJets_norm9'      :[na         ]*len(binlist['el']),
            'TTJets_norm10'     :[na         ]*len(binlist['el']),
            'tttt_norm'         :[na         ]*len(binlist['el']),
            'ST_tW_norm'        :[1.04       ]*len(binlist['el']),
            'EW_norm'           :[na         ]*len(binlist['el']),
            'TTRARE_norm'          :[na         ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'TTISR'             :[na         ]*len(binlist['el']),
            'TTFSR'             :[na         ]*len(binlist['el']),
            'TTUE'              :[na         ]*len(binlist['el']),
            'TTTTISR'           :[na         ]*len(binlist['el']),
            'TTTTFSR'           :[na         ]*len(binlist['el']),
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])}, }
	}
	return syst_norm_size_list_dict



syst_shape_size_list = {
'mu':{ 'NP_overlay_ttttNLO' : {
            'TTTTMEScale'      :[1.         ]*len(binlist['mu']),
            'ttMEScale'    :[na         ]*len(binlist['mu']),
            'TTJets_PDF'	:[na         ]*len(binlist['mu']),
            'heavyFlav'        :[na         ]*len(binlist['mu']),
            'TTPT'              :[na         ]*len(binlist['mu']),
            'PU'                :[1.         ]*len(binlist['mu']),
            'SubTotalRelativeJES'               :[1.         ]*len(binlist['mu']),
            'SubTotalPtJES'               :[1.         ]*len(binlist['mu']),
            'SubTotalScaleJES'               :[1.         ]*len(binlist['mu']),
            'SubTotalPileUpJES'               :[1.         ]*len(binlist['mu']),
            'JER'               :[1.         ]*len(binlist['mu']),
            'btagWeightCSVJES'  :[1.         ]*len(binlist['mu']),
            'btagWeightCSVHF'   :[1.         ]*len(binlist['mu']),
            'btagWeightCSVLF'   :[1.         ]*len(binlist['mu']),
            'btagWeightCSVHFStats1':[1.         ]*len(binlist['mu']),
            'btagWeightCSVHFStats2':[1.         ]*len(binlist['mu']),
            'btagWeightCSVLFStats1':[1.         ]*len(binlist['mu']),
            'btagWeightCSVLFStats2':[1.         ]*len(binlist['mu']),
            'btagWeightCSVCFErr1':[1.         ]*len(binlist['mu']),
            'btagWeightCSVCFErr2':[1.         ]*len(binlist['mu'])
            },
      'ttbarTTX' : {
            'TTTTMEScale'      :[na         ]*len(binlist['mu']),
            'ttMEScale'    :[1.         ]*len(binlist['mu']),
            'TTJets_PDF'	:[1.         ]*len(binlist['mu']),
            'heavyFlav'        :[1.         ]*len(binlist['mu']),
            'TTPT'              :[1.         ]*len(binlist['mu']),
            'PU'                :[1.         ]*len(binlist['mu']),
            'SubTotalRelativeJES'               :[1.         ]*len(binlist['mu']),
            'SubTotalPtJES'               :[1.         ]*len(binlist['mu']),
            'SubTotalScaleJES'               :[1.         ]*len(binlist['mu']),
            'SubTotalPileUpJES'               :[1.         ]*len(binlist['mu']),
            'JER'               :[1.         ]*len(binlist['mu']),
            'btagWeightCSVJES'  :[1.         ]*len(binlist['mu']),
            'btagWeightCSVHF'   :[1.         ]*len(binlist['mu']),
            'btagWeightCSVLF'   :[1.         ]*len(binlist['mu']),
            'btagWeightCSVHFStats1':[1.         ]*len(binlist['mu']),
            'btagWeightCSVHFStats2':[1.         ]*len(binlist['mu']),
            'btagWeightCSVLFStats1':[1.         ]*len(binlist['mu']),
            'btagWeightCSVLFStats2':[1.         ]*len(binlist['mu']),
            'btagWeightCSVCFErr1':[1.         ]*len(binlist['mu']),
            'btagWeightCSVCFErr2':[1.         ]*len(binlist['mu'])
            },
      'EW' : {
            'TTTTMEScale'      :[na         ]*len(binlist['mu']),
            'ttMEScale'    :[na         ]*len(binlist['mu']),
            'TTJets_PDF'	:[na         ]*len(binlist['mu']),
            'heavyFlav'        :[na         ]*len(binlist['mu']),
            'TTPT'              :[na         ]*len(binlist['mu']),
            'PU'                :[na         ]*len(binlist['mu']),
            'SubTotalRelativeJES'               :[na         ]*len(binlist['mu']),
            'SubTotalPtJES'               :[na         ]*len(binlist['mu']),
            'SubTotalScaleJES'               :[na         ]*len(binlist['mu']),
            'SubTotalPileUpJES'               :[na         ]*len(binlist['mu']),
            'JER'               :[na         ]*len(binlist['mu']),
            'btagWeightCSVJES'  :[na         ]*len(binlist['mu']),
            'btagWeightCSVHF'   :[na         ]*len(binlist['mu']),
            'btagWeightCSVLF'   :[na         ]*len(binlist['mu']),
            'btagWeightCSVHFStats1':[na         ]*len(binlist['mu']),
            'btagWeightCSVHFStats2':[na         ]*len(binlist['mu']),
            'btagWeightCSVLFStats1':[na         ]*len(binlist['mu']),
            'btagWeightCSVLFStats2':[na         ]*len(binlist['mu']),
            'btagWeightCSVCFErr1':[na        ]*len(binlist['mu']),
            'btagWeightCSVCFErr2':[na         ]*len(binlist['mu'])
            },
      'ST_tW' : {
            'TTTTMEScale'      :[na         ]*len(binlist['mu']),
            'ttMEScale'    :[na         ]*len(binlist['mu']),
            'TTJets_PDF'	:[na         ]*len(binlist['mu']),
            'heavyFlav'        :[na         ]*len(binlist['mu']),
            'TTPT'              :[na         ]*len(binlist['mu']),
            'PU'                :[na         ]*len(binlist['mu']),
            'SubTotalRelativeJES'               :[na         ]*len(binlist['mu']),
            'SubTotalPtJES'               :[na         ]*len(binlist['mu']),
            'SubTotalScaleJES'               :[na         ]*len(binlist['mu']),
            'SubTotalPileUpJES'               :[na         ]*len(binlist['mu']),
            'JER'               :[na         ]*len(binlist['mu']),
            'btagWeightCSVJES'  :[na         ]*len(binlist['mu']),
            'btagWeightCSVHF'   :[na         ]*len(binlist['mu']),
            'btagWeightCSVLF'   :[na         ]*len(binlist['mu']),
            'btagWeightCSVHFStats1':[na         ]*len(binlist['mu']),
            'btagWeightCSVHFStats2':[na         ]*len(binlist['mu']),
            'btagWeightCSVLFStats1':[na         ]*len(binlist['mu']),
            'btagWeightCSVLFStats2':[na         ]*len(binlist['mu']),
            'btagWeightCSVCFErr1':[na        ]*len(binlist['mu']),
            'btagWeightCSVCFErr2':[na         ]*len(binlist['mu'])
            },
      'TTRARE' : {
            'TTTTMEScale'      :[na         ]*len(binlist['mu']),
            'ttMEScale'    :[na         ]*len(binlist['mu']),
            'TTJets_PDF'	:[na         ]*len(binlist['mu']),
            'heavyFlav'        :[na         ]*len(binlist['mu']),
            'TTPT'              :[na         ]*len(binlist['mu']),
            'PU'                :[na         ]*len(binlist['mu']),
            'SubTotalRelativeJES'               :[na         ]*len(binlist['mu']),
            'SubTotalPtJES'               :[na         ]*len(binlist['mu']),
            'SubTotalScaleJES'               :[na         ]*len(binlist['mu']),
            'SubTotalPileUpJES'               :[na         ]*len(binlist['mu']),
            'JER'               :[na         ]*len(binlist['mu']),
            'btagWeightCSVJES'  :[na         ]*len(binlist['mu']),
            'btagWeightCSVHF'   :[na         ]*len(binlist['mu']),
            'btagWeightCSVLF'   :[na         ]*len(binlist['mu']),
            'btagWeightCSVHFStats1':[na         ]*len(binlist['mu']),
            'btagWeightCSVHFStats2':[na         ]*len(binlist['mu']),
            'btagWeightCSVLFStats1':[na         ]*len(binlist['mu']),
            'btagWeightCSVLFStats2':[na         ]*len(binlist['mu']),
            'btagWeightCSVCFErr1':[na        ]*len(binlist['mu']),
            'btagWeightCSVCFErr2':[na         ]*len(binlist['mu'])
            },
},
'el':{ 'NP_overlay_ttttNLO' : {
            'TTTTMEScale'      :[1.         ]*len(binlist['el']),
            'ttMEScale'    :[na         ]*len(binlist['el']),
            'TTJets_PDF'	:[na         ]*len(binlist['el']),
            'heavyFlav'        :[na         ]*len(binlist['el']),
            'TTPT'              :[na         ]*len(binlist['el']),
            'PU'                :[1.         ]*len(binlist['el']),
            'SubTotalRelativeJES'               :[1.         ]*len(binlist['el']),
            'SubTotalPtJES'               :[1.         ]*len(binlist['el']),
            'SubTotalScaleJES'               :[1.         ]*len(binlist['el']),
            'SubTotalPileUpJES'               :[1.         ]*len(binlist['el']),
            'JER'               :[1.         ]*len(binlist['el']),
            'btagWeightCSVJES'  :[1.         ]*len(binlist['el']),
            'btagWeightCSVHF'   :[1.         ]*len(binlist['el']),
            'btagWeightCSVLF'   :[1.         ]*len(binlist['el']),
            'btagWeightCSVHFStats1':[1.         ]*len(binlist['el']),
            'btagWeightCSVHFStats2':[1.         ]*len(binlist['el']),
            'btagWeightCSVLFStats1':[1.         ]*len(binlist['el']),
            'btagWeightCSVLFStats2':[1.         ]*len(binlist['el']),
            'btagWeightCSVCFErr1':[1.        ]*len(binlist['el']),
            'btagWeightCSVCFErr2':[1.         ]*len(binlist['el'])
            },
      'ttbarTTX' : {
            'TTTTMEScale'      :[na         ]*len(binlist['el']),
            'ttMEScale'    :[1.         ]*len(binlist['el']),
            'TTJets_PDF'	:[1.         ]*len(binlist['el']),
            'heavyFlav'        :[1.         ]*len(binlist['el']),
            'TTPT'              :[1.         ]*len(binlist['el']),
            'PU'                :[1.         ]*len(binlist['el']),
            'SubTotalRelativeJES'               :[1.         ]*len(binlist['el']),
            'SubTotalPtJES'               :[1.         ]*len(binlist['el']),
            'SubTotalScaleJES'               :[1.         ]*len(binlist['el']),
            'SubTotalPileUpJES'               :[1.         ]*len(binlist['el']),
            'JER'               :[1.         ]*len(binlist['el']),
            'btagWeightCSVJES'  :[1.         ]*len(binlist['el']),
            'btagWeightCSVHF'   :[1.         ]*len(binlist['el']),
            'btagWeightCSVLF'   :[1.         ]*len(binlist['el']),
            'btagWeightCSVHFStats1':[1.         ]*len(binlist['el']),
            'btagWeightCSVHFStats2':[1.         ]*len(binlist['el']),
            'btagWeightCSVLFStats1':[1.         ]*len(binlist['el']),
            'btagWeightCSVLFStats2':[1.         ]*len(binlist['el']),
            'btagWeightCSVCFErr1':[1.        ]*len(binlist['el']),
            'btagWeightCSVCFErr2':[1.         ]*len(binlist['el'])
            },
      'EW' : {
            'TTTTMEScale'      :[na         ]*len(binlist['el']),
            'ttMEScale'    :[na         ]*len(binlist['el']),
            'TTJets_PDF'	:[na         ]*len(binlist['el']),
            'heavyFlav'        :[na         ]*len(binlist['el']),
            'TTPT'              :[na         ]*len(binlist['el']),
            'PU'                :[na         ]*len(binlist['el']),
            'SubTotalRelativeJES'               :[na         ]*len(binlist['el']),
            'SubTotalPtJES'               :[na         ]*len(binlist['el']),
            'SubTotalScaleJES'               :[na         ]*len(binlist['el']),
            'SubTotalPileUpJES'               :[na         ]*len(binlist['el']),
            'JER'               :[na         ]*len(binlist['el']),
            'btagWeightCSVJES'  :[na         ]*len(binlist['el']),
            'btagWeightCSVHF'   :[na         ]*len(binlist['el']),
            'btagWeightCSVLF'   :[na         ]*len(binlist['el']),
            'btagWeightCSVHFStats1':[na         ]*len(binlist['el']),
            'btagWeightCSVHFStats2':[na         ]*len(binlist['el']),
            'btagWeightCSVLFStats1':[na         ]*len(binlist['el']),
            'btagWeightCSVLFStats2':[na         ]*len(binlist['el']),
            'btagWeightCSVCFErr1':[na        ]*len(binlist['el']),
            'btagWeightCSVCFErr2':[na         ]*len(binlist['el'])
            },
      'ST_tW' : {
            'TTTTMEScale'      :[na         ]*len(binlist['el']),
            'ttMEScale'    :[na         ]*len(binlist['el']),
            'TTJets_PDF'	:[na         ]*len(binlist['el']),
            'heavyFlav'        :[na         ]*len(binlist['el']),
            'TTPT'              :[na         ]*len(binlist['el']),
            'PU'                :[na         ]*len(binlist['el']),
            'SubTotalRelativeJES'               :[na         ]*len(binlist['el']),
            'SubTotalPtJES'               :[na         ]*len(binlist['el']),
            'SubTotalScaleJES'               :[na         ]*len(binlist['el']),
            'SubTotalPileUpJES'               :[na         ]*len(binlist['el']),
            'JER'               :[na         ]*len(binlist['el']),
            'btagWeightCSVJES'  :[na         ]*len(binlist['el']),
            'btagWeightCSVHF'   :[na         ]*len(binlist['el']),
            'btagWeightCSVLF'   :[na         ]*len(binlist['el']),
            'btagWeightCSVHFStats1':[na         ]*len(binlist['el']),
            'btagWeightCSVHFStats2':[na         ]*len(binlist['el']),
            'btagWeightCSVLFStats1':[na         ]*len(binlist['el']),
            'btagWeightCSVLFStats2':[na         ]*len(binlist['el']),
            'btagWeightCSVCFErr1':[na        ]*len(binlist['el']),
            'btagWeightCSVCFErr2':[na         ]*len(binlist['el'])
            },
      'TTRARE' : {
            'TTTTMEScale'      :[na         ]*len(binlist['el']),
            'ttMEScale'    :[na         ]*len(binlist['el']),
            'TTJets_PDF'	:[na         ]*len(binlist['el']),
            'heavyFlav'        :[na         ]*len(binlist['el']),
            'TTPT'              :[na         ]*len(binlist['el']),
            'PU'                :[na         ]*len(binlist['el']),
            'SubTotalRelativeJES'               :[na         ]*len(binlist['el']),
            'SubTotalPtJES'               :[na         ]*len(binlist['el']),
            'SubTotalScaleJES'               :[na         ]*len(binlist['el']),
            'SubTotalPileUpJES'               :[na         ]*len(binlist['el']),
            'JER'               :[na         ]*len(binlist['el']),
            'btagWeightCSVJES'  :[na         ]*len(binlist['el']),
            'btagWeightCSVHF'   :[na         ]*len(binlist['el']),
            'btagWeightCSVLF'   :[na         ]*len(binlist['el']),
            'btagWeightCSVHFStats1':[na         ]*len(binlist['el']),
            'btagWeightCSVHFStats2':[na         ]*len(binlist['el']),
            'btagWeightCSVLFStats1':[na         ]*len(binlist['el']),
            'btagWeightCSVLFStats2':[na         ]*len(binlist['el']),
            'btagWeightCSVCFErr1':[na        ]*len(binlist['el']),
            'btagWeightCSVCFErr2':[na         ]*len(binlist['el'])
            },
}}
