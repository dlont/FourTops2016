from cards_bin_list import binlist



na = '-'
lumiunc = 1.025
leptonsf = 1.03
syst_norm_size_list = {
'mu':{ 'NP_overlay_ttttNLO' : {
            'TTJets_norm'              :{"lnN:":[na         ]*len(binlist['mu'])},
            'tttt_norm'                :{"lnN:":['0.94/1.05']*len(binlist['mu'])},
            'ST_tW_norm'               :{"lnN:":[na         ]*len(binlist['mu'])},
            'EW_norm'                  :{"lnN:":[na         ]*len(binlist['mu'])},
            'TTRARE_norm'              :{"lnN:":[na         ]*len(binlist['mu'])},
            'lumi'                     :{"lnN:":[lumiunc    ]*len(binlist['mu'])},
            'leptonSFMu'               :{"lnN:":[leptonsf   ]*len(binlist['mu'])},
            'TTTTMEScale'              :{"shape":[1.         ]*len(binlist['mu'])},
            'ttMEScale'                :{"shape":[na         ]*len(binlist['mu'])},
            'TTJets_HDAMP'             :{"shape":[na         ]*len(binlist['mu'])},
            'TTJets_PDF'	       :{"shape":[na         ]*len(binlist['mu'])},
            'heavyFlav'                :{"shape":[na         ]*len(binlist['mu'])},
            'TTISR'                    :{"shape":[na         ]*len(binlist['mu'])},
            'TTFSR'                    :{"shape":[na         ]*len(binlist['mu'])},
            'TTUE'                     :{"shape":[na         ]*len(binlist['mu'])},
            'TTPT'                     :{"shape":[na         ]*len(binlist['mu'])},
            'TTTTISR'                  :{"shape":[1.         ]*len(binlist['mu'])},
            'TTTTFSR'                  :{"shape":[1.         ]*len(binlist['mu'])},
            'PU'                       :{"shape":[1.         ]*len(binlist['mu'])},
            'JES'                      :{"shape":[1.         ]*len(binlist['mu'])},
            'JER'                      :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVJES'         :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVHF'          :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVLF'          :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVHFStats1'    :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVHFStats2'    :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVLFStats1'    :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVLFStats2'    :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVCFErr1'      :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVCFErr2'      :{"shape":[1.         ]*len(binlist['mu'])}
},
       'ttbarTTX' : {
            'TTJets_norm'              :{"lnN:":['0.95/1.05']*len(binlist['mu'])},
            'tttt_norm'                :{"lnN:":[na         ]*len(binlist['mu'])},
            'ST_tW_norm'               :{"lnN:":[na         ]*len(binlist['mu'])},
            'EW_norm'                  :{"lnN:":[na         ]*len(binlist['mu'])},
            'TTRARE_norm'              :{"lnN:":[na         ]*len(binlist['mu'])},
            'lumi'                     :{"lnN:":[lumiunc    ]*len(binlist['mu'])},
            'leptonSFMu'               :{"lnN:":[leptonsf   ]*len(binlist['mu'])},
            'TTTTMEScale'              :{"shape":[na         ]*len(binlist['mu'])},
            'ttMEScale'                :{"shape":[1.         ]*len(binlist['mu'])},
            'TTJets_HDAMP'             :{"shape":[1.         ]*len(binlist['mu'])},
            'TTJets_PDF'	       :{"shape":[1.         ]*len(binlist['mu'])},
            'heavyFlav'                :{"shape":[1.         ]*len(binlist['mu'])},
            'TTISR'                    :{"shape":[1.         ]*len(binlist['mu'])},
            'TTFSR'                    :{"shape":[1.         ]*len(binlist['mu'])},
            'TTUE'                     :{"shape":[1.         ]*len(binlist['mu'])},
            'TTPT'                     :{"shape":[1.         ]*len(binlist['mu'])},
            'TTTTISR'                  :{"shape":[na         ]*len(binlist['mu'])},
            'TTTTFSR'                  :{"shape":[na         ]*len(binlist['mu'])},
            'PU'                       :{"shape":[1.         ]*len(binlist['mu'])},
            'JES'                      :{"shape":[1.         ]*len(binlist['mu'])},
            'JER'                      :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVJES'         :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVHF'          :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVLF'          :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVHFStats1'    :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVHFStats2'    :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVLFStats1'    :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVLFStats2'    :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVCFErr1'      :{"shape":[1.         ]*len(binlist['mu'])},
            'btagWeightCSVCFErr2'      :{"shape":[1.         ]*len(binlist['mu'])}
},
       'EW' : {
            'TTJets_norm'              :{"lnN:":[na         ]*len(binlist['mu'])},
            'tttt_norm'                :{"lnN:":[na         ]*len(binlist['mu'])},
            'ST_tW_norm'               :{"lnN:":[na         ]*len(binlist['mu'])},
            'EW_norm'                  :{"lnN:":[1.04       ]*len(binlist['mu'])},
            'TTRARE_norm'              :{"lnN:":[na         ]*len(binlist['mu'])},
            'lumi'                     :{"lnN:":[lumiunc    ]*len(binlist['mu'])},
            'leptonSFMu'               :{"lnN:":[leptonsf   ]*len(binlist['mu'])},
            'TTTTMEScale'              :{"shape":[na         ]*len(binlist['mu'])},
            'ttMEScale'                :{"shape":[na         ]*len(binlist['mu'])},
            'TTJets_HDAMP'             :{"shape":[na         ]*len(binlist['mu'])},
            'TTJets_PDF'	       :{"shape":[na         ]*len(binlist['mu'])},
            'heavyFlav'                :{"shape":[na         ]*len(binlist['mu'])},
            'TTISR'                    :{"shape":[na         ]*len(binlist['mu'])},
            'TTFSR'                    :{"shape":[na         ]*len(binlist['mu'])},
            'TTUE'                     :{"shape":[na         ]*len(binlist['mu'])},
            'TTPT'                     :{"shape":[na         ]*len(binlist['mu'])},
            'TTTTISR'                  :{"shape":[na         ]*len(binlist['mu'])},
            'TTTTFSR'                  :{"shape":[na         ]*len(binlist['mu'])},
            'PU'                       :{"shape":[na         ]*len(binlist['mu'])},
            'JES'                      :{"shape":[na         ]*len(binlist['mu'])},
            'JER'                      :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVJES'         :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVHF'          :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVLF'          :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVHFStats1'    :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVHFStats2'    :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVLFStats1'    :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVLFStats2'    :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVCFErr1'      :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVCFErr2'      :{"shape":[na         ]*len(binlist['mu'])}
},     
       'TTRARE' : {
            'TTJets_norm'           :{"lnN:":[na         ]*len(binlist['mu'])},
            'tttt_norm'             :{"lnN:":[na         ]*len(binlist['mu'])},
            'ST_tW_norm'            :{"lnN:":[na         ]*len(binlist['mu'])},
            'EW_norm'               :{"lnN:":[na         ]*len(binlist['mu'])},
            'TTRARE_norm'           :{"lnN:":[1.5        ]*len(binlist['mu'])},
            'lumi'                  :{"lnN:":[lumiunc    ]*len(binlist['mu'])},
            'leptonSFMu'            :{"lnN:":[leptonsf   ]*len(binlist['mu'])},
            'TTTTMEScale'           :{"shape":[na         ]*len(binlist['mu'])},
            'ttMEScale'             :{"shape":[na         ]*len(binlist['mu'])},
            'TTJets_HDAMP'          :{"shape":[na         ]*len(binlist['mu'])},
            'TTJets_PDF'	    :{"shape":[na         ]*len(binlist['mu'])},
            'heavyFlav'             :{"shape":[na         ]*len(binlist['mu'])},
            'TTISR'                 :{"shape":[na         ]*len(binlist['mu'])},
            'TTFSR'                 :{"shape":[na         ]*len(binlist['mu'])},
            'TTUE'                  :{"shape":[na         ]*len(binlist['mu'])},
            'TTPT'                  :{"shape":[na         ]*len(binlist['mu'])},
            'TTTTISR'               :{"shape":[na         ]*len(binlist['mu'])},
            'TTTTFSR'               :{"shape":[na         ]*len(binlist['mu'])},
            'PU'                    :{"shape":[na         ]*len(binlist['mu'])},
            'JES'                   :{"shape":[na         ]*len(binlist['mu'])},
            'JER'                   :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVJES'      :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVHF'       :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVLF'       :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVHFStats1' :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVHFStats2' :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVLFStats1' :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVLFStats2' :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVCFErr1'   :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVCFErr2'   :{"shape":[na         ]*len(binlist['mu'])}

},     
       'ST_tW' : {
            'TTJets_norm'            :{"lnN:":[na         ]*len(binlist['mu'])},
            'tttt_norm'              :{"lnN:":[na         ]*len(binlist['mu'])},
            'ST_tW_norm'             :{"lnN:":[1.04       ]*len(binlist['mu'])},
            'EW_norm'                :{"lnN:":[na         ]*len(binlist['mu'])},
            'TTRARE_norm'            :{"lnN:":[na         ]*len(binlist['mu'])},
            'lumi'                   :{"lnN:":[lumiunc    ]*len(binlist['mu'])},
            'leptonSFMu'             :{"lnN:":[leptonsf   ]*len(binlist['mu'])},
            'TTTTMEScale'            :{"shape":[na         ]*len(binlist['mu'])},
            'ttMEScale'              :{"shape":[na         ]*len(binlist['mu'])},
            'TTJets_HDAMP'           :{"shape":[na         ]*len(binlist['mu'])},
            'TTJets_PDF'	     :{"shape":[na         ]*len(binlist['mu'])},
            'heavyFlav'              :{"shape":[na         ]*len(binlist['mu'])},
            'TTISR'                  :{"shape":[na         ]*len(binlist['mu'])},
            'TTFSR'                  :{"shape":[na         ]*len(binlist['mu'])},
            'TTUE'                   :{"shape":[na         ]*len(binlist['mu'])},
            'TTPT'                   :{"shape":[na         ]*len(binlist['mu'])},
            'TTTTISR'                :{"shape":[na         ]*len(binlist['mu'])},
            'TTTTFSR'                :{"shape":[na         ]*len(binlist['mu'])},
            'PU'                     :{"shape":[na         ]*len(binlist['mu'])},
            'JES'                    :{"shape":[na         ]*len(binlist['mu'])},
            'JER'                    :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVJES'       :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVHF'        :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVLF'        :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVHFStats1'  :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVHFStats2'  :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVLFStats1'  :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVLFStats2'  :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVCFErr1'    :{"shape":[na         ]*len(binlist['mu'])},
            'btagWeightCSVCFErr2'    :{"shape":[na         ]*len(binlist['mu'])}
}, 
},
'el':{ 'NP_overlay_ttttNLO' : {
            'TTJets_norm'       :{"lnN:":[na         ]*len(binlist['el'])},
            'tttt_norm'         :{"lnN:":['0.94/1.05']*len(binlist['el'])},
            'ST_tW_norm'        :{"lnN:":[na         ]*len(binlist['el'])},
            'EW_norm'           :{"lnN:":[na         ]*len(binlist['el'])},
            'TTRARE_norm'       :{"lnN:":[na         ]*len(binlist['el'])},
            'lumi'              :{"lnN:":[lumiunc    ]*len(binlist['el'])},
            'leptonSFEl'        :{"lnN:":[leptonsf   ]*len(binlist['el'])}},
       'ttbarTTX' : {
            'TTJets_norm'       :{"lnN:":['0.95/1.05']*len(binlist['el'])},
            'tttt_norm'         :{"lnN:":[na         ]*len(binlist['el'])},
            'ST_tW_norm'        :{"lnN:":[na         ]*len(binlist['el'])},
            'EW_norm'           :{"lnN:":[na         ]*len(binlist['el'])},
            'TTRARE_norm'       :{"lnN:":[na         ]*len(binlist['el'])},
            'lumi'              :{"lnN:":[lumiunc    ]*len(binlist['el'])},
            'leptonSFEl'        :{"lnN:":[leptonsf   ]*len(binlist['el'])}},
       'EW' : {
            'TTJets_norm'       :{"lnN:":[na         ]*len(binlist['el'])},
            'tttt_norm'         :{"lnN:":[na         ]*len(binlist['el'])},
            'ST_tW_norm'        :{"lnN:":[na         ]*len(binlist['el'])},
            'EW_norm'           :{"lnN:":[1.04       ]*len(binlist['el'])},
            'TTRARE_norm'       :{"lnN:":[na         ]*len(binlist['el'])},
            'lumi'              :{"lnN:":[lumiunc    ]*len(binlist['el'])},
            'leptonSFEl'        :{"lnN:":[leptonsf   ]*len(binlist['el'])}},     
       'TTRARE' : {
            'TTJets_norm'       :{"lnN:":[na         ]*len(binlist['el'])},
            'tttt_norm'         :{"lnN:":[na         ]*len(binlist['el'])},
            'ST_tW_norm'        :{"lnN:":[na         ]*len(binlist['el'])},
            'EW_norm'           :{"lnN:":[na         ]*len(binlist['el'])},
            'TTRARE_norm'       :{"lnN:":[1.5        ]*len(binlist['el'])},
            'lumi'              :{"lnN:":[lumiunc    ]*len(binlist['el'])},
            'leptonSFEl'        :{"lnN:":[leptonsf   ]*len(binlist['el'])}},     
       'ST_tW' : {
            'TTJets_norm'       :{"lnN:":[na         ]*len(binlist['el'])},
            'tttt_norm'         :{"lnN:":[na         ]*len(binlist['el'])},
            'ST_tW_norm'        :{"lnN:":[1.04       ]*len(binlist['el'])},
            'EW_norm'           :{"lnN:":[na         ]*len(binlist['el'])},
            'TTRARE_norm'       :{"lnN:":[na         ]*len(binlist['el'])},
            'lumi'              :{"lnN:":[lumiunc    ]*len(binlist['el'])},
            'leptonSFEl'        :{"lnN:":[leptonsf   ]*len(binlist['el'])}}, 
}}
#syst_shape_size_list = {
#'el':{ 'NP_overlay_ttttNLO' : {
#            'TTTTMEScale'      :[1.         ]*len(binlist['el']),
#            'ttMEScale'    :[na         ]*len(binlist['el']),
#            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
#            'TTJets_PDF'	:[na         ]*len(binlist['el']),
#            'heavyFlav'        :[na         ]*len(binlist['el']),
#            'TTISR'             :[na         ]*len(binlist['el']),
#            'TTFSR'             :[na         ]*len(binlist['el']),
#            'TTUE'              :[na         ]*len(binlist['el']),
#            'TTPT'              :[na         ]*len(binlist['el']),
#            'TTTTISR'           :[1.         ]*len(binlist['el']),
#            'TTTTFSR'           :[1.         ]*len(binlist['el']),
#            'PU'                :[1.         ]*len(binlist['el']),
#            'JES'               :[1.         ]*len(binlist['el']),
#            'JER'               :[1.         ]*len(binlist['el']),
#            'btagWeightCSVJES'  :[1.         ]*len(binlist['el']),
#            'btagWeightCSVHF'   :[1.         ]*len(binlist['el']),
#            'btagWeightCSVLF'   :[1.         ]*len(binlist['el']),
#            'btagWeightCSVHFStats1':[1.         ]*len(binlist['el']),
#            'btagWeightCSVHFStats2':[1.         ]*len(binlist['el']),
#            'btagWeightCSVLFStats1':[1.         ]*len(binlist['el']),
#            'btagWeightCSVLFStats2':[1.         ]*len(binlist['el']),
#            'btagWeightCSVCFErr1':[1.        ]*len(binlist['el']),
#            'btagWeightCSVCFErr2':[1.         ]*len(binlist['el'])
#            },
#      'ttbarTTX' : {
#            'TTTTMEScale'      :[na         ]*len(binlist['el']),
#            'ttMEScale'    :[1.         ]*len(binlist['el']),
#            'TTJets_HDAMP'      :[1.         ]*len(binlist['el']),
#            'TTJets_PDF'	:[1.         ]*len(binlist['el']),
#            'heavyFlav'        :[1.         ]*len(binlist['el']),
#            'TTISR'             :[1.         ]*len(binlist['el']),
#            'TTFSR'             :[1.         ]*len(binlist['el']),
#            'TTUE'              :[1.         ]*len(binlist['el']),
#            'TTPT'              :[1.         ]*len(binlist['el']),
#            'TTTTISR'           :[na         ]*len(binlist['el']),
#            'TTTTFSR'           :[na         ]*len(binlist['el']),
#            'PU'                :[1.         ]*len(binlist['el']),
#            'JES'               :[1.         ]*len(binlist['el']),
#            'JER'               :[1.         ]*len(binlist['el']),
#            'btagWeightCSVJES'  :[1.         ]*len(binlist['el']),
#            'btagWeightCSVHF'   :[1.         ]*len(binlist['el']),
#            'btagWeightCSVLF'   :[1.         ]*len(binlist['el']),
#            'btagWeightCSVHFStats1':[1.         ]*len(binlist['el']),
#            'btagWeightCSVHFStats2':[1.         ]*len(binlist['el']),
#            'btagWeightCSVLFStats1':[1.         ]*len(binlist['el']),
#            'btagWeightCSVLFStats2':[1.         ]*len(binlist['el']),
#            'btagWeightCSVCFErr1':[1.        ]*len(binlist['el']),
#            'btagWeightCSVCFErr2':[1.         ]*len(binlist['el'])
#            },
#      'EW' : {
#            'TTTTMEScale'      :[na         ]*len(binlist['el']),
#            'ttMEScale'    :[na         ]*len(binlist['el']),
#            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
#            'TTJets_PDF'	:[na         ]*len(binlist['el']),
#            'heavyFlav'        :[na         ]*len(binlist['el']),
#            'TTISR'             :[na         ]*len(binlist['el']),
#            'TTFSR'             :[na         ]*len(binlist['el']),
#            'TTUE'              :[na         ]*len(binlist['el']),
#            'TTPT'              :[na         ]*len(binlist['el']),
#            'TTTTISR'           :[na         ]*len(binlist['el']),
#            'TTTTFSR'           :[na         ]*len(binlist['el']),
#            'PU'                :[na         ]*len(binlist['el']),
#            'JES'               :[na         ]*len(binlist['el']),
#            'JER'               :[na         ]*len(binlist['el']),
#            'btagWeightCSVJES'  :[na         ]*len(binlist['el']),
#            'btagWeightCSVHF'   :[na         ]*len(binlist['el']),
#            'btagWeightCSVLF'   :[na         ]*len(binlist['el']),
#            'btagWeightCSVHFStats1':[na         ]*len(binlist['el']),
#            'btagWeightCSVHFStats2':[na         ]*len(binlist['el']),
#            'btagWeightCSVLFStats1':[na         ]*len(binlist['el']),
#            'btagWeightCSVLFStats2':[na         ]*len(binlist['el']),
#            'btagWeightCSVCFErr1':[na        ]*len(binlist['el']),
#            'btagWeightCSVCFErr2':[na         ]*len(binlist['el'])
#            },
#      'ST_tW' : {
#            'TTTTMEScale'      :[na         ]*len(binlist['el']),
#            'ttMEScale'    :[na         ]*len(binlist['el']),
#            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
#            'TTJets_PDF'	:[na         ]*len(binlist['el']),
#            'heavyFlav'        :[na         ]*len(binlist['el']),
#            'TTISR'             :[na         ]*len(binlist['el']),
#            'TTFSR'             :[na         ]*len(binlist['el']),
#            'TTUE'              :[na         ]*len(binlist['el']),
#            'TTPT'              :[na         ]*len(binlist['el']),
#            'TTTTISR'           :[na         ]*len(binlist['el']),
#            'TTTTFSR'           :[na         ]*len(binlist['el']),
#            'PU'                :[na         ]*len(binlist['el']),
#            'JES'               :[na         ]*len(binlist['el']),
#            'JER'               :[na         ]*len(binlist['el']),
#            'btagWeightCSVJES'  :[na         ]*len(binlist['el']),
#            'btagWeightCSVHF'   :[na         ]*len(binlist['el']),
#            'btagWeightCSVLF'   :[na         ]*len(binlist['el']),
#            'btagWeightCSVHFStats1':[na         ]*len(binlist['el']),
#            'btagWeightCSVHFStats2':[na         ]*len(binlist['el']),
#            'btagWeightCSVLFStats1':[na         ]*len(binlist['el']),
#            'btagWeightCSVLFStats2':[na         ]*len(binlist['el']),
#            'btagWeightCSVCFErr1':[na        ]*len(binlist['el']),
#            'btagWeightCSVCFErr2':[na         ]*len(binlist['el'])
#            },
#      'TTRARE' : {
#            'TTTTMEScale'      :[na         ]*len(binlist['el']),
#            'ttMEScale'    :[na         ]*len(binlist['el']),
#            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
#            'TTJets_PDF'	:[na         ]*len(binlist['el']),
#            'heavyFlav'        :[na         ]*len(binlist['el']),
#            'TTISR'             :[na         ]*len(binlist['el']),
#            'TTFSR'             :[na         ]*len(binlist['el']),
#            'TTUE'              :[na         ]*len(binlist['el']),
#            'TTPT'              :[na         ]*len(binlist['el']),
#            'TTTTISR'           :[na         ]*len(binlist['el']),
#            'TTTTFSR'           :[na         ]*len(binlist['el']),
#            'PU'                :[na         ]*len(binlist['el']),
#            'JES'               :[na         ]*len(binlist['el']),
#            'JER'               :[na         ]*len(binlist['el']),
#            'btagWeightCSVJES'  :[na         ]*len(binlist['el']),
#            'btagWeightCSVHF'   :[na         ]*len(binlist['el']),
#            'btagWeightCSVLF'   :[na         ]*len(binlist['el']),
#            'btagWeightCSVHFStats1':[na         ]*len(binlist['el']),
#            'btagWeightCSVHFStats2':[na         ]*len(binlist['el']),
#            'btagWeightCSVLFStats1':[na         ]*len(binlist['el']),
#            'btagWeightCSVLFStats2':[na         ]*len(binlist['el']),
#            'btagWeightCSVCFErr1':[na        ]*len(binlist['el']),
#            'btagWeightCSVCFErr2':[na         ]*len(binlist['el'])            
#},
#}
#}
