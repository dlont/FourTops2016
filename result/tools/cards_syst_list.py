from cards_bin_list import binlist

systtypelist = {
'mu':{
'TTJets_norm':'lnN',
'TTJets_MEScale':'shape',
'TTTT_norm':'lnN',
'TTTT_MEScale':'shape',
'ST_tW_norm':'lnN',
'EW_norm':'lnN',
'LUMI':'lnN',
'PU':'shape',
'JES':'shape',
'JER':'shape',
'leptonSFMu':'lnN'
#{'ScaleH',
#{'heavyFlav',
#{'btagWeightCSVHF',
#{'btagWeightCSVLF',
#{'btagWeightCSVHFStats1',
#{'btagWeightCSVHFStats2',
#{'btagWeightCSVLFStats1',
#{'btagWeightCSVLFStats2',
#{'btagWeightCSVCFErr1',
#{'btagWeightCSVCFErr2'
}}
na = '-'
lumiunc = 1.062
leptonsf = 1.02
syst_norm_size_list = {
'mu':{ 'TTTT' : {
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            'TTTT_norm'         :['0.94/1.05']*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'LUMI'              :[lumiunc    ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},
       'TT' : {
            'TTJets_norm'       :['0.95/1.05']*len(binlist['mu']),
            'TTTT_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'LUMI'              :[lumiunc    ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},
       'EW' : {
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            'TTTT_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[1.04       ]*len(binlist['mu']),
            'LUMI'              :[lumiunc    ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},     
       'ST' : {
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            'TTTT_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[1.04       ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'LUMI'              :[lumiunc    ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])}, 
},
'el':{ 'TTTT' : {
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            'TTTT_norm'         :['0.94/1.05']*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'LUMI'              :[lumiunc    ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},
       'TT' : {
            'TTJets_norm'       :['0.95/1.05']*len(binlist['mu']),
            'TTTT_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'LUMI'              :[lumiunc    ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},
       'EW' : {
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            'TTTT_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[1.04       ]*len(binlist['mu']),
            'LUMI'              :[lumiunc    ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},     
       'ST' : {
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            'TTTT_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[1.04       ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'LUMI'              :[lumiunc    ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])}, 
}}
syst_shape_size_list = {
'el':{ 'TTTT' : {
            'TTTT_MEScale'      :[1.         ]*len(binlist['el']),
            'TTJets_MEScale'    :[na         ]*len(binlist['el']),
            'PU'                :[1.         ]*len(binlist['el']),
            'JES'               :[1.         ]*len(binlist['el']),
            'JER'               :[1.         ]*len(binlist['el'])
            },
      'TT' : {
            'TTTT_MEScale'      :[na         ]*len(binlist['el']),
            'TTJets_MEScale'    :[1.         ]*len(binlist['el']),
            'PU'                :[1.         ]*len(binlist['el']),
            'JES'               :[1.         ]*len(binlist['el']),
            'JER'               :[1.         ]*len(binlist['el'])
            },
      'EW' : {
            'TTTT_MEScale'      :[na         ]*len(binlist['el']),
            'TTJets_MEScale'    :[na         ]*len(binlist['el']),
            'PU'                :[na         ]*len(binlist['el']),
            'JES'               :[na         ]*len(binlist['el']),
            'JER'               :[na         ]*len(binlist['el'])
            },
      'ST' : {
            'TTTT_MEScale'      :[na         ]*len(binlist['el']),
            'TTJets_MEScale'    :[na         ]*len(binlist['el']),
            'PU'                :[na         ]*len(binlist['el']),
            'JES'               :[na         ]*len(binlist['el']),
            'JER'               :[na         ]*len(binlist['el'])
            },
},
'el':{ 'TTTT' : {
            'TTTT_MEScale'      :[1.         ]*len(binlist['el']),
            'TTJets_MEScale'    :[na         ]*len(binlist['el']),
            'PU'                :[1.         ]*len(binlist['el']),
            'JES'               :[1.         ]*len(binlist['el']),
            'JER'               :[1.         ]*len(binlist['el'])
            },
      'TT' : {
            'TTTT_MEScale'      :[na         ]*len(binlist['el']),
            'TTJets_MEScale'    :[1.         ]*len(binlist['el']),
            'PU'                :[1.         ]*len(binlist['el']),
            'JES'               :[1.         ]*len(binlist['el']),
            'JER'               :[1.         ]*len(binlist['el'])
            },
      'EW' : {
            'TTTT_MEScale'      :[na         ]*len(binlist['el']),
            'TTJets_MEScale'    :[na         ]*len(binlist['el']),
            'PU'                :[na         ]*len(binlist['el']),
            'JES'               :[na         ]*len(binlist['el']),
            'JER'               :[na         ]*len(binlist['el'])
            },
      'ST' : {
            'TTTT_MEScale'      :[na         ]*len(binlist['el']),
            'TTJets_MEScale'    :[na         ]*len(binlist['el']),
            'PU'                :[na         ]*len(binlist['el']),
            'JES'               :[na         ]*len(binlist['el']),
            'JER'               :[na         ]*len(binlist['el'])
            },
}}