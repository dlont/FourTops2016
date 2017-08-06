from cards_bin_list import binlist

systtypelist = {
'mu':{
'TTJets_norm':'lnN',
'ttMEScale':'shape',
'TTJets_HDAMP':'shape',
'TTJets_PDF':'shape',
'heavyFlav':'shape',
'tttt_norm':'lnN',
'TTTT_MEScale':'shape',
'ST_tW_norm':'lnN',
'EW_norm':'lnN',
'TTRARE_norm':'lnN',
'lumi':'lnN',
'PU':'shape',
'JES':'shape',
'JER':'shape',
'leptonSFMu':'lnN',
#{'ScaleH',
#{'heavyFlav',
'TTISR':'shape',
'TTFSR':'shape',
'TTUE':'shape',
'TTPT':'shape',
'TTTTISR':'shape',
'TTTTFSR':'shape',
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
'ttMEScale':'shape',
'TTJets_HDAMP':'shape',
'TTJets_PDF':'shape',
'heavyFlav':'shape',
'tttt_norm':'lnN',
'TTTT_MEScale':'shape',
'ST_tW_norm':'lnN',
'TTRARE_norm':'lnN',
'EW_norm':'lnN',
'lumi':'lnN',
'PU':'shape',
'JES':'shape',
'JER':'shape',
'leptonSFEl':'lnN',
#{'ScaleH',
#{'heavyFlav',
'TTISR':'shape',
'TTFSR':'shape',
'TTUE':'shape',
'TTPT':'shape',
'TTTTISR':'shape',
'TTTTFSR':'shape',
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
syst_norm_size_list = {
'mu':{ 'NP_overlay_ttttNLO' : {
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            'tttt_norm'         :['0.94/1.05']*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'TTRARE_norm'          :[na         ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},
       'ttbarTTX' : {
            'TTJets_norm'       :['0.95/1.05']*len(binlist['mu']),
            'tttt_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'TTRARE_norm'          :[na         ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},
       'EW' : {
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            'tttt_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[1.04       ]*len(binlist['mu']),
            'TTRARE_norm'          :[na         ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},     
       'TTRARE' : {
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            'tttt_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'TTRARE_norm'          :[1.5        ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},     
       'ST_tW' : {
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            'tttt_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[1.04       ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'TTRARE_norm'          :[na         ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])}, 
},
'el':{ 'NP_overlay_ttttNLO' : {
            'TTJets_norm'       :[na         ]*len(binlist['el']),
            'tttt_norm'         :['0.94/1.05']*len(binlist['el']),
            'ST_tW_norm'        :[na         ]*len(binlist['el']),
            'EW_norm'           :[na         ]*len(binlist['el']),
            'TTRARE_norm'          :[na         ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])},
       'ttbarTTX' : {
            'TTJets_norm'       :['0.95/1.05']*len(binlist['el']),
            'tttt_norm'         :[na         ]*len(binlist['el']),
            'ST_tW_norm'        :[na         ]*len(binlist['el']),
            'EW_norm'           :[na         ]*len(binlist['el']),
            'TTRARE_norm'          :[na         ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])},
       'EW' : {
            'TTJets_norm'       :[na         ]*len(binlist['el']),
            'tttt_norm'         :[na         ]*len(binlist['el']),
            'ST_tW_norm'        :[na         ]*len(binlist['el']),
            'EW_norm'           :[1.04       ]*len(binlist['el']),
            'TTRARE_norm'          :[na         ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])},     
       'TTRARE' : {
            'TTJets_norm'       :[na         ]*len(binlist['el']),
            'tttt_norm'         :[na         ]*len(binlist['el']),
            'ST_tW_norm'        :[na         ]*len(binlist['el']),
            'EW_norm'           :[na         ]*len(binlist['el']),
            'TTRARE_norm'          :[1.5        ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])},     
       'ST_tW' : {
            'TTJets_norm'       :[na         ]*len(binlist['el']),
            'tttt_norm'         :[na         ]*len(binlist['el']),
            'ST_tW_norm'        :[1.04       ]*len(binlist['el']),
            'EW_norm'           :[na         ]*len(binlist['el']),
            'TTRARE_norm'          :[na         ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])}, 
}}
syst_shape_size_list = {
'mu':{ 'NP_overlay_ttttNLO' : {
            'TTTT_MEScale'      :[1.         ]*len(binlist['mu']),
            'ttMEScale'    :[na         ]*len(binlist['mu']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['mu']),
            'TTJets_PDF'	:[na         ]*len(binlist['mu']),
            'heavyFlav'        :[na         ]*len(binlist['mu']),
            'TTISR'             :[na         ]*len(binlist['mu']),
            'TTFSR'             :[na         ]*len(binlist['mu']),
            'TTUE'              :[na         ]*len(binlist['mu']),
            'TTPT'              :[na         ]*len(binlist['mu']),
            'TTTTISR'           :[1.         ]*len(binlist['mu']),
            'TTTTFSR'           :[1.         ]*len(binlist['mu']),
            'PU'                :[1.         ]*len(binlist['mu']),
            'JES'               :[1.         ]*len(binlist['mu']),
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
            'TTTT_MEScale'      :[na         ]*len(binlist['mu']),
            'ttMEScale'    :[1.         ]*len(binlist['mu']),
            'TTJets_HDAMP'      :[1.         ]*len(binlist['mu']),
            'TTJets_PDF'	:[1.         ]*len(binlist['mu']),
            'heavyFlav'        :[1.         ]*len(binlist['mu']),
            'TTISR'             :[1.         ]*len(binlist['mu']),
            'TTFSR'             :[1.         ]*len(binlist['mu']),
            'TTUE'              :[1.         ]*len(binlist['mu']),
            'TTPT'              :[1.         ]*len(binlist['mu']),
            'TTTTISR'           :[na         ]*len(binlist['mu']),
            'TTTTFSR'           :[na         ]*len(binlist['mu']),
            'PU'                :[1.         ]*len(binlist['mu']),
            'JES'               :[1.         ]*len(binlist['mu']),
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
            'TTTT_MEScale'      :[na         ]*len(binlist['mu']),
            'ttMEScale'    :[na         ]*len(binlist['mu']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['mu']),
            'TTJets_PDF'	:[na         ]*len(binlist['mu']),
            'heavyFlav'        :[na         ]*len(binlist['mu']),
            'TTISR'             :[na         ]*len(binlist['mu']),
            'TTFSR'             :[na         ]*len(binlist['mu']),
            'TTUE'              :[na         ]*len(binlist['mu']),
            'TTPT'              :[na         ]*len(binlist['mu']),
            'TTTTISR'           :[na         ]*len(binlist['mu']),
            'TTTTFSR'           :[na         ]*len(binlist['mu']),
            'PU'                :[na         ]*len(binlist['mu']),
            'JES'               :[na         ]*len(binlist['mu']),
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
            'TTTT_MEScale'      :[na         ]*len(binlist['mu']),
            'ttMEScale'    :[na         ]*len(binlist['mu']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['mu']),
            'TTJets_PDF'	:[na         ]*len(binlist['mu']),
            'heavyFlav'        :[na         ]*len(binlist['mu']),
            'TTISR'             :[na         ]*len(binlist['mu']),
            'TTFSR'             :[na         ]*len(binlist['mu']),
            'TTUE'              :[na         ]*len(binlist['mu']),
            'TTPT'              :[na         ]*len(binlist['mu']),
            'TTTTISR'           :[na         ]*len(binlist['mu']),
            'TTTTFSR'           :[na         ]*len(binlist['mu']),
            'PU'                :[na         ]*len(binlist['mu']),
            'JES'               :[na         ]*len(binlist['mu']),
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
            'TTTT_MEScale'      :[na         ]*len(binlist['mu']),
            'ttMEScale'    :[na         ]*len(binlist['mu']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['mu']),
            'TTJets_PDF'	:[na         ]*len(binlist['mu']),
            'heavyFlav'        :[na         ]*len(binlist['mu']),
            'TTISR'             :[na         ]*len(binlist['mu']),
            'TTFSR'             :[na         ]*len(binlist['mu']),
            'TTUE'              :[na         ]*len(binlist['mu']),
            'TTPT'              :[na         ]*len(binlist['mu']),
            'TTTTISR'           :[na         ]*len(binlist['mu']),
            'TTTTFSR'           :[na         ]*len(binlist['mu']),
            'PU'                :[na         ]*len(binlist['mu']),
            'JES'               :[na         ]*len(binlist['mu']),
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
            'TTTT_MEScale'      :[1.         ]*len(binlist['el']),
            'ttMEScale'    :[na         ]*len(binlist['el']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
            'TTJets_PDF'	:[na         ]*len(binlist['el']),
            'heavyFlav'        :[na         ]*len(binlist['el']),
            'TTISR'             :[na         ]*len(binlist['el']),
            'TTFSR'             :[na         ]*len(binlist['el']),
            'TTUE'              :[na         ]*len(binlist['el']),
            'TTPT'              :[na         ]*len(binlist['el']),
            'TTTTISR'           :[1.         ]*len(binlist['el']),
            'TTTTFSR'           :[1.         ]*len(binlist['el']),
            'PU'                :[1.         ]*len(binlist['el']),
            'JES'               :[1.         ]*len(binlist['el']),
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
            'TTTT_MEScale'      :[na         ]*len(binlist['el']),
            'ttMEScale'    :[1.         ]*len(binlist['el']),
            'TTJets_HDAMP'      :[1.         ]*len(binlist['el']),
            'TTJets_PDF'	:[1.         ]*len(binlist['el']),
            'heavyFlav'        :[1.         ]*len(binlist['el']),
            'TTISR'             :[1.         ]*len(binlist['el']),
            'TTFSR'             :[1.         ]*len(binlist['el']),
            'TTUE'              :[1.         ]*len(binlist['el']),
            'TTPT'              :[1.         ]*len(binlist['el']),
            'TTTTISR'           :[na         ]*len(binlist['el']),
            'TTTTFSR'           :[na         ]*len(binlist['el']),
            'PU'                :[1.         ]*len(binlist['el']),
            'JES'               :[1.         ]*len(binlist['el']),
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
            'TTTT_MEScale'      :[na         ]*len(binlist['el']),
            'ttMEScale'    :[na         ]*len(binlist['el']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
            'TTJets_PDF'	:[na         ]*len(binlist['el']),
            'heavyFlav'        :[na         ]*len(binlist['el']),
            'TTISR'             :[na         ]*len(binlist['el']),
            'TTFSR'             :[na         ]*len(binlist['el']),
            'TTUE'              :[na         ]*len(binlist['el']),
            'TTPT'              :[na         ]*len(binlist['el']),
            'TTTTISR'           :[na         ]*len(binlist['el']),
            'TTTTFSR'           :[na         ]*len(binlist['el']),
            'PU'                :[na         ]*len(binlist['el']),
            'JES'               :[na         ]*len(binlist['el']),
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
            'TTTT_MEScale'      :[na         ]*len(binlist['el']),
            'ttMEScale'    :[na         ]*len(binlist['el']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
            'TTJets_PDF'	:[na         ]*len(binlist['el']),
            'heavyFlav'        :[na         ]*len(binlist['el']),
            'TTISR'             :[na         ]*len(binlist['el']),
            'TTFSR'             :[na         ]*len(binlist['el']),
            'TTUE'              :[na         ]*len(binlist['el']),
            'TTPT'              :[na         ]*len(binlist['el']),
            'TTTTISR'           :[na         ]*len(binlist['el']),
            'TTTTFSR'           :[na         ]*len(binlist['el']),
            'PU'                :[na         ]*len(binlist['el']),
            'JES'               :[na         ]*len(binlist['el']),
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
            'TTTT_MEScale'      :[na         ]*len(binlist['el']),
            'ttMEScale'    :[na         ]*len(binlist['el']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
            'TTJets_PDF'	:[na         ]*len(binlist['el']),
            'heavyFlav'        :[na         ]*len(binlist['el']),
            'TTISR'             :[na         ]*len(binlist['el']),
            'TTFSR'             :[na         ]*len(binlist['el']),
            'TTUE'              :[na         ]*len(binlist['el']),
            'TTPT'              :[na         ]*len(binlist['el']),
            'TTTTISR'           :[na         ]*len(binlist['el']),
            'TTTTFSR'           :[na         ]*len(binlist['el']),
            'PU'                :[na         ]*len(binlist['el']),
            'JES'               :[na         ]*len(binlist['el']),
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
