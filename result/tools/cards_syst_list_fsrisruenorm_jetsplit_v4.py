from cards_bin_list import binlist
from cards_constants import na, lumiunc, leptonsf
# from Rare1TTH_sys import mu_Rare1TTH_norm, mu_Rare1TTH_shape, el_Rare1TTH_norm, el_Rare1TTH_shape
# from Rare1TTZ_sys import mu_Rare1TTZ_norm, mu_Rare1TTZ_shape, el_Rare1TTZ_norm, el_Rare1TTZ_shape
# from Rare1TTW_sys import mu_Rare1TTW_norm, mu_Rare1TTW_shape, el_Rare1TTW_norm, el_Rare1TTW_shape
from Rare1TTHZ_sys import mu_Rare1TTHZ_norm, mu_Rare1TTHZ_shape, el_Rare1TTHZ_norm, el_Rare1TTHZ_shape

import math

systtypelist = {
'mu':{
'TTHZ_norm':'lnN',
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
'TTRARE_plus_norm':'lnN',
'lumi':'lnN',
'PU':'shape',
'SubTotalPileUpJES':'shape',
'SubTotalScaleJES':'shape',
'SubTotalTimePtEtaJES':'shape',
'SubTotalPtJES':'shape',
'SubTotalRelativeJES':'shape',
'SubTotalFlavorJES':'shape',
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
'TTHZ_norm':'lnN',
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
'TTRARE_plus_norm':'lnN',
'EW_norm':'lnN',
'lumi':'lnN',
'PU':'shape',
'SubTotalPileUpJES':'shape',
'SubTotalScaleJES':'shape',
'SubTotalTimePtEtaJES':'shape',
'SubTotalPtJES':'shape',
'SubTotalRelativeJES':'shape',
'SubTotalFlavorJES':'shape',
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
      '''
      Retrive normalization systematic uncertainties for each process

      Relative uncertainty of some sources that have large statistical component due to limited size
      of MC samples, such as HDAMP, I/FSR, UE, is calculated separately using MC templates provided 
      in corresponding rootfiles.

      Args: 
            rootfiles: A dict() with MC process to filename map, e.g. {'ST_tW':'./file_ST_tW.root', 'TTRARE_plus':'./file_TTRARE.root'}
            ch: A str() with analysis channel name, e.g. "mu" or "el"
      Returns:
            Double nested dictionary with MC process, systematics name and list systematic variation effect in each search category
            Example:
            'mu':{
	            'NP_overlay_ttttNLO' : {
	                  'TTHZ_norm'         :[na         ]*len(binlist['mu']),
                        'TTJets_HDAMP'      :[na         ]*len(binlist['mu']),
                        'tttt_norm'         :['0.94/1.05']*len(binlist['mu']),
                        'ST_tW_norm'        :[na         ]*len(binlist['mu']),
                  },
                  'ttbarTTX' : {
                        'EW_norm'           :[na         ]*len(binlist['mu']),
                        'TTRARE_plus_norm'  :[na         ]*len(binlist['mu']),
                        'lumi'              :[lumiunc    ]*len(binlist['mu']),
                        'TTISR'             :sysdic['TTISR'],
                  }
            'el':{...}
            }
      '''


      sysdic = {}
      sysdic_njnb = {}
      # Calculate normalization effect from systematic shapes templates
      for sys in ["TTISR","TTFSR","TTUE","TTJets_HDAMP"]:
		#precompute uncertainties by merging btag categories together
		njets_integral_central = {'7':0.,'8':0.,'9':0.,'10':0.}	# WARNING: hardcoded categories. Code will crash if category name changes
		njets_integrals_up = {'7':0.,'8':0.,'9':0.,'10':0.}
		njets_integrals_down = {'7':0.,'8':0.,'9':0.,'10':0.}
		njets_mcstat_up = {'7':0.,'8':0.,'9':0.,'10':0.}
		njets_mcstat_down = {'7':0.,'8':0.,'9':0.,'10':0.}
		for icat,cat in enumerate(binlist[ch]):
			cat = cat.replace("mu",""); cat = cat.replace("el","");	#strip prefix
			#identify jet multiplicity from label. It should be in 2-3 characters of the category name
			njets = cat[0:2];njets=njets.replace("J","")
			central = rootfiles['ttbarTTX'].Get(cat+'/bdt').Integral()
			sysup   = rootfiles['ttbarTTX'].Get(cat+'_'+sys+'Up/bdt').Integral()
			sysdown = rootfiles['ttbarTTX'].Get(cat+'_'+sys+'Down/bdt').Integral()
			mcstat_sysup = rootfiles['ttbarTTX'].Get(cat+'_'+sys+'Up/bdt').GetEntries()
			mcstat_sysdown = rootfiles['ttbarTTX'].Get(cat+'_'+sys+'Down/bdt').GetEntries()
			njets_integral_central[njets]+=central
			njets_integrals_up[njets]+=sysup
			njets_integrals_down[njets]+=sysdown
			njets_mcstat_up[njets]+=mcstat_sysup
			njets_mcstat_down[njets]+=mcstat_sysdown
		for njets in ['7','8','9','10']:
			njets_mcstat_up[njets] = math.sqrt(njets_mcstat_up[njets])/njets_mcstat_up[njets] if njets_mcstat_up[njets]>0 else 0.
			njets_mcstat_down[njets] = math.sqrt(njets_mcstat_down[njets])/njets_mcstat_down[njets] if njets_mcstat_down[njets]>0 else 0.
			

		syslist = []
		for icat,cat in enumerate(binlist[ch]):
			cat = cat.replace("mu",""); cat = cat.replace("el","");	#strip prefix
			njets = cat[0:2];njets=njets.replace("J","")
			central = njets_integral_central[njets]
			sysup   = njets_integrals_up[njets]
			sysdown = njets_integrals_down[njets]
			mcstat_sysup = njets_mcstat_up[njets]
			mcstat_sysdown = njets_mcstat_down[njets]
			#print cat, sys, central, sysup, sysdown
			up = 1.
			down = 1.
			if (sysdown/central > 1 and sysup/central < 1):
				up = 1.+max([abs(sysdown/central-1.), mcstat_sysdown, mcstat_sysup])
				down = 1.-max([abs(sysup/central-1.), mcstat_sysdown, mcstat_sysup])
			if (sysdown/central < 1 and sysup/central > 1):
				up = 1.+max([abs(sysup/central-1.), mcstat_sysdown, mcstat_sysup])
				down = 1.-max([abs(sysdown/central-1.), mcstat_sysdown, mcstat_sysup])
			if (sysdown/central > 1 and sysup/central > 1):
				up = 1.+max([abs(sysup/central-1.), abs(sysdown/central-1.), mcstat_sysdown, mcstat_sysup])
				down = 1.-max([abs(sysup/central-1.), abs(sysdown/central-1.), mcstat_sysdown, mcstat_sysup])
			if (sysdown/central < 1 and sysup/central < 1):
				up = 1.+max([abs(sysup/central-1.), abs(sysdown/central-1.), mcstat_sysdown, mcstat_sysup])
				down = 1.-max([abs(sysup/central-1.), abs(sysdown/central-1.), mcstat_sysdown, mcstat_sysup])
			unc = ''+str(down)+'/'+str(up)
			syslist.append( unc )
			
			# split systematics
			list_of_uncertainties = binlist[ch]
			list_of_uncertainties = ['-' if cat not in x else unc for x in list_of_uncertainties]
			#sysdic_njnb[sys+binlist[ch][icat]] = list_of_uncertainties
			#systtypelist[ch][sys+'_'+binlist[ch][icat]] = 'lnN'
			
		sysdic[sys] = syslist

	#for key in sysdic.keys(): print key, sysdic[key]
      for key in sysdic_njnb.keys(): print key, sysdic_njnb[key]

      # Calculate normalization effect from systematic shapes templates
      for sys in ["TTTTISR","TTTTFSR"]:
		#precompute uncertainties by merging btag categories together
		njets_integral_central = {'7':0.,'8':0.,'9':0.,'10':0.}	# WARNING: hardcoded categories. Code will crash if category name changes
		njets_integrals_up = {'7':0.,'8':0.,'9':0.,'10':0.}
		njets_integrals_down = {'7':0.,'8':0.,'9':0.,'10':0.}
		njets_mcstat_up = {'7':0.,'8':0.,'9':0.,'10':0.}
		njets_mcstat_down = {'7':0.,'8':0.,'9':0.,'10':0.}
		for icat,cat in enumerate(binlist[ch]):
			cat = cat.replace("mu",""); cat = cat.replace("el","");	#strip prefix
			#identify jet multiplicity from label. It should be in 2-3 characters of the category name
			njets = cat[0:2];njets=njets.replace("J","")
			central = rootfiles['NP_overlay_ttttNLO'].Get(cat+'/bdt').Integral()
			sysup   = rootfiles['NP_overlay_ttttNLO'].Get(cat+'_'+sys+'Up/bdt').Integral()
			sysdown = rootfiles['NP_overlay_ttttNLO'].Get(cat+'_'+sys+'Down/bdt').Integral()
			mcstat_sysup = rootfiles['NP_overlay_ttttNLO'].Get(cat+'_'+sys+'Up/bdt').GetEntries()
			mcstat_sysdown = rootfiles['NP_overlay_ttttNLO'].Get(cat+'_'+sys+'Down/bdt').GetEntries()
			njets_integral_central[njets]+=central
			njets_integrals_up[njets]+=sysup
			njets_integrals_down[njets]+=sysdown
			njets_mcstat_up[njets]+=mcstat_sysup
			njets_mcstat_down[njets]+=mcstat_sysdown
		for njets in ['7','8','9','10']:
			njets_mcstat_up[njets] = math.sqrt(njets_mcstat_up[njets])/njets_mcstat_up[njets] if njets_mcstat_up[njets]>0. else 0.
			njets_mcstat_down[njets] = math.sqrt(njets_mcstat_down[njets])/njets_mcstat_down[njets] if njets_mcstat_down[njets]>0. else 0.
			

		syslist = []
		for icat,cat in enumerate(binlist[ch]):
			cat = cat.replace("mu",""); cat = cat.replace("el","");	#strip prefix
			njets = cat[0:2];njets=njets.replace("J","")
			central = njets_integral_central[njets]
			sysup   = njets_integrals_up[njets]
			sysdown = njets_integrals_down[njets]
			mcstat_sysup = njets_mcstat_up[njets]
			mcstat_sysdown = njets_mcstat_down[njets]
			#print cat, njets, central, sysup, sysdown, mcstat_sysup, mcstat_sysdown
			#print cat, sys, central, sysup, sysdown
			up = 1.
			down = 1.
			if (sysdown/central > 1 and sysup/central < 1):
				up = 1.+max([abs(sysdown/central-1.), mcstat_sysdown, mcstat_sysup])
				down = 1.-max([abs(sysup/central-1.), mcstat_sysdown, mcstat_sysup])
			if (sysdown/central < 1 and sysup/central > 1):
				up = 1.+max([abs(sysup/central-1.), mcstat_sysdown, mcstat_sysup])
				down = 1.-max([abs(sysdown/central-1.), mcstat_sysdown, mcstat_sysup])
			if (sysdown/central > 1 and sysup/central > 1):
				up = 1.+max([abs(sysup/central-1.), abs(sysdown/central-1.), mcstat_sysdown, mcstat_sysup])
				down = 1.-max([abs(sysup/central-1.), abs(sysdown/central-1.), mcstat_sysdown, mcstat_sysup])
			if (sysdown/central < 1 and sysup/central < 1):
				up = 1.+max([abs(sysup/central-1.), abs(sysdown/central-1.), mcstat_sysdown, mcstat_sysup])
				down = 1.-max([abs(sysup/central-1.), abs(sysdown/central-1.), mcstat_sysdown, mcstat_sysup])
			unc = ''+str(down)+'/'+str(up)
			syslist.append( unc )
			
			# split systematics
			list_of_uncertainties = binlist[ch]
			list_of_uncertainties = ['-' if cat not in x else unc for x in list_of_uncertainties]
			#sysdic_njnb[sys+binlist[ch][icat]] = list_of_uncertainties
			#systtypelist[ch][sys+'_'+binlist[ch][icat]] = 'lnN'
			
		sysdic[sys] = syslist

      syst_norm_size_list_dict = {
'mu':{
	    mu_Rare1TTHZ_norm[0]:mu_Rare1TTHZ_norm[1],
	    'NP_overlay_ttttNLO' : {
	    'TTHZ_norm':[na         ]*len(binlist['mu']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['mu']),
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            #'TTJets_norm8'      :[na         ]*len(binlist['mu']),
            #'TTJets_norm9'      :[na         ]*len(binlist['mu']),
            'TTJets_norm10'     :[na         ]*len(binlist['mu']),
            'tttt_norm'         :['0.94/1.05']*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'TTRARE_plus_norm'          :[na         ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'TTISR'             :[na         ]*len(binlist['mu']),
            'TTFSR'             :[na         ]*len(binlist['mu']),
            'TTUE'              :[na         ]*len(binlist['mu']),
            'TTTTISR'           :sysdic['TTTTISR'],
            'TTTTFSR'           :sysdic['TTTTFSR'],
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},
       'ttbarTTX' : {
	    'TTHZ_norm':[na         ]*len(binlist['mu']),
            'TTJets_HDAMP'      :sysdic['TTJets_HDAMP'],
            'TTJets_norm'       :TTJets_norm7_mu_unc,
            #'TTJets_norm8'      :TTJets_norm8_mu_unc,
            #'TTJets_norm9'      :TTJets_norm9_mu_unc,
            'TTJets_norm10'     :TTJets_norm10_mu_unc,
            'tttt_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'TTRARE_plus_norm'       :[na         ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'TTISR'             :sysdic['TTISR'],
            'TTFSR'             :sysdic['TTFSR'],
            'TTUE'              :sysdic['TTUE'],
            'TTTTISR'           :[na         ]*len(binlist['mu']),
            'TTTTFSR'           :[na         ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},
       'EW' : {
	    'TTHZ_norm':[na         ]*len(binlist['mu']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['mu']),
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            #'TTJets_norm8'      :[na         ]*len(binlist['mu']),
            #'TTJets_norm9'      :[na         ]*len(binlist['mu']),
            'TTJets_norm10'     :[na         ]*len(binlist['mu']),
            'tttt_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[1.04       ]*len(binlist['mu']),
            'TTRARE_plus_norm'          :[na         ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'TTISR'             :[na         ]*len(binlist['mu']),
            'TTFSR'             :[na         ]*len(binlist['mu']),
            'TTUE'              :[na         ]*len(binlist['mu']),
            'TTTTISR'           :[na         ]*len(binlist['mu']),
            'TTTTFSR'           :[na         ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},
       'TTRARE_plus' : {
	    'TTHZ_norm':[na         ]*len(binlist['mu']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['mu']),
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            #'TTJets_norm8'      :[na         ]*len(binlist['mu']),
            #'TTJets_norm9'      :[na         ]*len(binlist['mu']),
            'TTJets_norm10'     :[na         ]*len(binlist['mu']),
            'tttt_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[na         ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'TTRARE_plus_norm'          :[1.5        ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'TTISR'             :[na         ]*len(binlist['mu']),
            'TTFSR'             :[na         ]*len(binlist['mu']),
            'TTUE'              :[na         ]*len(binlist['mu']),
            'TTTTISR'           :[na         ]*len(binlist['mu']),
            'TTTTFSR'           :[na         ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},
       'ST_tW' : {
	    'TTHZ_norm':[na         ]*len(binlist['mu']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['mu']),
            'TTJets_norm'       :[na         ]*len(binlist['mu']),
            #'TTJets_norm8'      :[na         ]*len(binlist['mu']),
            #'TTJets_norm9'      :[na         ]*len(binlist['mu']),
            'TTJets_norm10'     :[na         ]*len(binlist['mu']),
            'tttt_norm'         :[na         ]*len(binlist['mu']),
            'ST_tW_norm'        :[1.04       ]*len(binlist['mu']),
            'EW_norm'           :[na         ]*len(binlist['mu']),
            'TTRARE_plus_norm'          :[na         ]*len(binlist['mu']),
            'lumi'              :[lumiunc    ]*len(binlist['mu']),
            'TTISR'             :[na         ]*len(binlist['mu']),
            'TTFSR'             :[na         ]*len(binlist['mu']),
            'TTUE'              :[na         ]*len(binlist['mu']),
            'TTTTISR'           :[na         ]*len(binlist['mu']),
            'TTTTFSR'           :[na         ]*len(binlist['mu']),
            'leptonSFMu'        :[leptonsf   ]*len(binlist['mu'])},
},
'el':{
	    el_Rare1TTHZ_norm[0]:el_Rare1TTHZ_norm[1],
       'NP_overlay_ttttNLO' : {
	    'TTHZ_norm':[na         ]*len(binlist['el']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
            'TTJets_norm'       :[na         ]*len(binlist['el']),
            #'TTJets_norm8'      :[na         ]*len(binlist['el']),
            #'TTJets_norm9'      :[na         ]*len(binlist['el']),
            'TTJets_norm10'     :[na         ]*len(binlist['el']),
            'tttt_norm'         :['0.94/1.05']*len(binlist['el']),
            'ST_tW_norm'        :[na         ]*len(binlist['el']),
            'EW_norm'           :[na         ]*len(binlist['el']),
            'TTRARE_plus_norm'          :[na         ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'TTISR'             :[na         ]*len(binlist['el']),
            'TTFSR'             :[na         ]*len(binlist['el']),
            'TTUE'              :[na         ]*len(binlist['el']),
            'TTTTISR'           :sysdic['TTTTISR'],
            'TTTTFSR'           :sysdic['TTTTFSR'],
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])},
       'ttbarTTX' : {
	    'TTHZ_norm':[na         ]*len(binlist['el']),
            'TTJets_HDAMP'      :sysdic['TTJets_HDAMP'],
            'TTJets_norm'       :TTJets_norm7_el_unc,
            #'TTJets_norm8'      :TTJets_norm8_el_unc,
            #'TTJets_norm9'      :TTJets_norm9_el_unc,
            'TTJets_norm10'     :TTJets_norm10_el_unc,
            'tttt_norm'         :[na         ]*len(binlist['el']),
            'ST_tW_norm'        :[na         ]*len(binlist['el']),
            'EW_norm'           :[na         ]*len(binlist['el']),
            'TTRARE_plus_norm'          :[na         ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'TTISR'             :sysdic['TTISR'],
            'TTFSR'             :sysdic['TTFSR'],
            'TTUE'              :sysdic['TTUE'],
            'TTTTISR'           :[na         ]*len(binlist['el']),
            'TTTTFSR'           :[na         ]*len(binlist['el']),
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])},
       'EW' : {
	    'TTHZ_norm':[na         ]*len(binlist['el']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
            'TTJets_norm'       :[na         ]*len(binlist['el']),
            #'TTJets_norm8'      :[na         ]*len(binlist['el']),
            #'TTJets_norm9'      :[na         ]*len(binlist['el']),
            'TTJets_norm10'     :[na         ]*len(binlist['el']),
            'tttt_norm'         :[na         ]*len(binlist['el']),
            'ST_tW_norm'        :[na         ]*len(binlist['el']),
            'EW_norm'           :[1.04       ]*len(binlist['el']),
            'TTRARE_plus_norm'          :[na         ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'TTISR'             :[na         ]*len(binlist['el']),
            'TTFSR'             :[na         ]*len(binlist['el']),
            'TTUE'              :[na         ]*len(binlist['el']),
            'TTTTISR'           :[na         ]*len(binlist['el']),
            'TTTTFSR'           :[na         ]*len(binlist['el']),
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])},
       'TTRARE_plus' : {
	    'TTHZ_norm':[na         ]*len(binlist['el']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
            'TTJets_norm'       :[na         ]*len(binlist['el']),
            #'TTJets_norm8'      :[na         ]*len(binlist['el']),
            #'TTJets_norm9'      :[na         ]*len(binlist['el']),
            'TTJets_norm10'     :[na         ]*len(binlist['el']),
            'tttt_norm'         :[na         ]*len(binlist['el']),
            'ST_tW_norm'        :[na         ]*len(binlist['el']),
            'EW_norm'           :[na         ]*len(binlist['el']),
            'TTRARE_plus_norm'          :[1.5        ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'TTISR'             :[na         ]*len(binlist['el']),
            'TTFSR'             :[na         ]*len(binlist['el']),
            'TTUE'              :[na         ]*len(binlist['el']),
            'TTTTISR'           :[na         ]*len(binlist['el']),
            'TTTTFSR'           :[na         ]*len(binlist['el']),
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])},
       'ST_tW' : {
	    'TTHZ_norm':[na         ]*len(binlist['el']),
            'TTJets_HDAMP'      :[na         ]*len(binlist['el']),
            'TTJets_norm'       :[na         ]*len(binlist['el']),
            #'TTJets_norm8'      :[na         ]*len(binlist['el']),
            #'TTJets_norm9'      :[na         ]*len(binlist['el']),
            'TTJets_norm10'     :[na         ]*len(binlist['el']),
            'tttt_norm'         :[na         ]*len(binlist['el']),
            'ST_tW_norm'        :[1.04       ]*len(binlist['el']),
            'EW_norm'           :[na         ]*len(binlist['el']),
            'TTRARE_plus_norm'          :[na         ]*len(binlist['el']),
            'lumi'              :[lumiunc    ]*len(binlist['el']),
            'TTISR'             :[na         ]*len(binlist['el']),
            'TTFSR'             :[na         ]*len(binlist['el']),
            'TTUE'              :[na         ]*len(binlist['el']),
            'TTTTISR'           :[na         ]*len(binlist['el']),
            'TTTTFSR'           :[na         ]*len(binlist['el']),
            'leptonSFEl'        :[leptonsf   ]*len(binlist['el'])}, }
	}

	#for key in sysdic_njnb.keys():
	#	syst_norm_size_list_dict[ch]['ttbarTTX'][key] = sysdic_njnb[key]
	#	syst_norm_size_list_dict[ch]['NP_overlay_ttttNLO'][key] = [na]*len(binlist[ch])
	#	syst_norm_size_list_dict[ch]['ST_tW'][key] = [na]*len(binlist[ch])
	#	syst_norm_size_list_dict[ch]['TTRARE_plus'][key] = [na]*len(binlist[ch])
	#	syst_norm_size_list_dict[ch]['EW'][key] = [na]*len(binlist[ch])
	#	syst_norm_size_list_dict[ch]['Rare1TTHZ'][key] = [na]*len(binlist[ch])

      return syst_norm_size_list_dict


#
# Double nested dictionary with MC process, systematics name and list systematic variation effect in each search category
# Example:
# 'mu':{
#  'NP_overlay_ttttNLO' : {
#             'TTTTMEScale'       :[1.         ]*len(binlist['mu']),
#             'ttMEScale'         :[na         ]*len(binlist['mu']),
#       },
#       'ttbarTTX' : {
#             'TTTTMEScale'       :[na         ]*len(binlist['mu']),
#             'SubTotalPtJES'     :[1          ]*len(binlist['mu']),
#       }
# 'el':{...}
# }
      
syst_shape_size_list = {
'mu':{
	    mu_Rare1TTHZ_shape[0]:mu_Rare1TTHZ_shape[1],
	    'NP_overlay_ttttNLO' : {
            'TTTTMEScale'      :[1.         ]*len(binlist['mu']),
            'ttMEScale'    :[na         ]*len(binlist['mu']),
            'TTJets_PDF'	:[na         ]*len(binlist['mu']),
            'heavyFlav'        :[na         ]*len(binlist['mu']),
            'TTPT'              :[na         ]*len(binlist['mu']),
            'PU'                :[1.         ]*len(binlist['mu']),
            'SubTotalRelativeJES'               :[1.         ]*len(binlist['mu']),
            'SubTotalPtJES'               :[1.         ]*len(binlist['mu']),
            'SubTotalScaleJES'               :[1.         ]*len(binlist['mu']),
            'SubTotalTimePtEtaJES'               :[1.         ]*len(binlist['mu']),
            'SubTotalPileUpJES'               :[1.         ]*len(binlist['mu']),
            'SubTotalFlavorJES'               :[1.         ]*len(binlist['mu']),
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
            'SubTotalTimePtEtaJES'               :[1.         ]*len(binlist['mu']),
            'SubTotalPileUpJES'               :[1.         ]*len(binlist['mu']),
            'SubTotalFlavorJES'               :[1.         ]*len(binlist['mu']),
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
            'SubTotalTimePtEtaJES'               :[na         ]*len(binlist['mu']),
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
            'SubTotalTimePtEtaJES'               :[na         ]*len(binlist['mu']),
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
            },
      'TTRARE_plus' : {
            'TTTTMEScale'      :[na         ]*len(binlist['mu']),
            'ttMEScale'    :[na         ]*len(binlist['mu']),
            'TTJets_PDF'	:[na         ]*len(binlist['mu']),
            'heavyFlav'        :[na         ]*len(binlist['mu']),
            'TTPT'              :[na         ]*len(binlist['mu']),
            'PU'                :[na         ]*len(binlist['mu']),
            'SubTotalRelativeJES'               :[na         ]*len(binlist['mu']),
            'SubTotalPtJES'               :[na         ]*len(binlist['mu']),
            'SubTotalScaleJES'               :[na         ]*len(binlist['mu']),
            'SubTotalTimePtEtaJES'               :[na         ]*len(binlist['mu']),
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
            },
},
'el':{
	    el_Rare1TTHZ_shape[0]:el_Rare1TTHZ_shape[1],
            'NP_overlay_ttttNLO' : {
            'TTTTMEScale'      :[1.         ]*len(binlist['el']),
            'ttMEScale'    :[na         ]*len(binlist['el']),
            'TTJets_PDF'	:[na         ]*len(binlist['el']),
            'heavyFlav'        :[na         ]*len(binlist['el']),
            'TTPT'              :[na         ]*len(binlist['el']),
            'PU'                :[1.         ]*len(binlist['el']),
            'SubTotalRelativeJES'               :[1.         ]*len(binlist['el']),
            'SubTotalPtJES'               :[1.         ]*len(binlist['el']),
            'SubTotalScaleJES'               :[1.         ]*len(binlist['el']),
            'SubTotalTimePtEtaJES'               :[1.         ]*len(binlist['el']),
            'SubTotalPileUpJES'               :[1.         ]*len(binlist['el']),
            'SubTotalFlavorJES'               :[1.         ]*len(binlist['el']),
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
            'SubTotalTimePtEtaJES'               :[1.         ]*len(binlist['el']),
            'SubTotalPileUpJES'               :[1.         ]*len(binlist['el']),
            'SubTotalFlavorJES'               :[1.         ]*len(binlist['el']),
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
            'SubTotalTimePtEtaJES'               :[na         ]*len(binlist['el']),
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
            'SubTotalTimePtEtaJES'               :[na         ]*len(binlist['el']),
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
            },
      'TTRARE_plus' : {
            'TTTTMEScale'      :[na         ]*len(binlist['el']),
            'ttMEScale'    :[na         ]*len(binlist['el']),
            'TTJets_PDF'	:[na         ]*len(binlist['el']),
            'heavyFlav'        :[na         ]*len(binlist['el']),
            'TTPT'              :[na         ]*len(binlist['el']),
            'PU'                :[na         ]*len(binlist['el']),
            'SubTotalRelativeJES'               :[na         ]*len(binlist['el']),
            'SubTotalPtJES'               :[na         ]*len(binlist['el']),
            'SubTotalScaleJES'               :[na         ]*len(binlist['el']),
            'SubTotalTimePtEtaJES'               :[na         ]*len(binlist['el']),
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
            },
}}
