from cards_bin_list import binlist

systtypelist = {
'mu':{
'TTJets_norm':'lnN',
#'TTJets_MEScale':'shape',
'TTTT_norm':'lnN',
#'TTTT_MEScale':'shape',
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
}}
syst_shape_size_list = {
'mu':{ 'TTTT' : {
#            'TTTT_MEScale'      :[1.         ]*len(binlist['mu']),
#            'TTJets_MEScale'    :[na         ]*len(binlist['mu']),
            'PU'                :[1.         ]*len(binlist['mu']),
#            'JES'               :[1.         ]*len(binlist['mu']),
#            'JER'               :[1.         ]*len(binlist['mu'])
            },
      'TT' : {
#            'TTTT_MEScale'      :[na         ]*len(binlist['mu']),
#            'TTJets_MEScale'    :[1.         ]*len(binlist['mu']),
            'PU'                :[1.         ]*len(binlist['mu']),
#            'JES'               :[1.         ]*len(binlist['mu']),
#            'JER'               :[1.         ]*len(binlist['mu'])
            },
      'EW' : {
#            'TTTT_MEScale'      :[na         ]*len(binlist['mu']),
#            'TTJets_MEScale'    :[na         ]*len(binlist['mu']),
            'PU'                :[1.         ]*len(binlist['mu']),
#            'JES'               :[1.         ]*len(binlist['mu']),
#            'JER'               :[1.         ]*len(binlist['mu'])
            },
      'ST' : {
#            'TTTT_MEScale'      :[na         ]*len(binlist['mu']),
#            'TTJets_MEScale'    :[na         ]*len(binlist['mu']),
            'PU'                :[1.         ]*len(binlist['mu']),
#            'JES'               :[1.         ]*len(binlist['mu']),
#            'JER'               :[1.         ]*len(binlist['mu'])
            },
}}