from cards_bin_list import binlist
from cards_constants import na, lumiunc, leptonsf

mu_Rare1TTH_norm = (
       'Rare1TTH' , {
	    'TTH_norm':[1.5         ]*len(binlist['mu']),
	    'TTZ_norm':[na         ]*len(binlist['mu']),
	    'TTW_norm':[na         ]*len(binlist['mu']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['mu']),
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            #'TTJets_norm8'      :[na         ]*len(binlist['mu']),
            #'TTJets_norm9'      :[na         ]*len(binlist['mu']),
            'TTJets_norm10'     :[na         ]*len(binlist['mu']),
            'tttt_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'TTRARE_plus_norm'       :[na         ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'TTISR'             :[na         ]*len(binlist['mu']),
            'TTFSR'             :[na         ]*len(binlist['mu']),
            'TTUE'              :[na         ]*len(binlist['mu']),
            'TTTTISR'           :[na         ]*len(binlist['mu']),
            'TTTTFSR'           :[na         ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},
)
mu_Rare1TTH_shape = (
      'Rare1TTH' , {
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
            'SubTotalFlavorJES'               :[na         ]*len(binlist['mu']),
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
            }
)
el_Rare1TTH_norm = (
       'Rare1TTH' , {
	    'TTH_norm':[1.5         ]*len(binlist['el']),
	    'TTZ_norm':[na         ]*len(binlist['el']),
	    'TTW_norm':[na         ]*len(binlist['el']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
            'TTJets_norm'       :[na         ]*len(binlist['el']),
            #'TTJets_norm8'      :[na         ]*len(binlist['el']),
            #'TTJets_norm9'      :[na         ]*len(binlist['el']),
            'TTJets_norm10'     :[na         ]*len(binlist['el']),
            'tttt_norm'         :[na         ]*len(binlist['el']),
            'ST_tW_norm'        :[na         ]*len(binlist['el']),
            'EW_norm'           :[na         ]*len(binlist['el']),
            'TTRARE_plus_norm'       :[na         ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'TTISR'             :[na         ]*len(binlist['el']),
            'TTFSR'             :[na         ]*len(binlist['el']),
            'TTUE'              :[na         ]*len(binlist['el']),
            'TTTTISR'           :[na         ]*len(binlist['el']),
            'TTTTFSR'           :[na         ]*len(binlist['el']),
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])},
)
el_Rare1TTH_shape = (
      'Rare1TTH' , {
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
            'SubTotalFlavorJES'               :[na         ]*len(binlist['el']),
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
            }
)
