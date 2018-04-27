# path = '/storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/result/final_unblinding/50bins/plots_mu_optbin/'
path = '/storage_mnt/storage/user/dlontkov/TTP_CMSSW_8_0_26_patch1/src/TopBrussels/FourTops2016/result/final_unblinding/filtered_samples/plots_mu_filt/'
binlist = ['7J2M','7J3M','7J4M','8J2M','8J3M','8J4M','9J2M','9J3M','10J2M','10J3M']

config = {
'plot':{
    'yaxis':{'min':0.0,'max':2.0}
},
'data':{
        'inputfile':path+'Hists_data.root',
        'central':[bin+'/bdt' for bin in binlist]
},
'shape_sys':{
	'inputfile':path+'Hists_TT_CARDS.root',
	'central':[bin+'/bdt' for bin in binlist],
	'sources':
		{
		'SubTotalFlavourJES':{
			'up':[bin+'_SubTotalFlavorJESUp/bdt' for bin in binlist],
			'down':[bin+'_SubTotalFlavorJESDown/bdt' for bin in binlist],
			'linestyle':1}
		,
		'SubTotalScaleJES':{
			'up':[bin+'_SubTotalScaleJESUp/bdt' for bin in binlist],
			'down':[bin+'_SubTotalScaleJESDown/bdt' for bin in binlist],
			'linestyle':2}
		,
		'SubTotalRelativeJES':{
			'up':[bin+'_SubTotalRelativeJESUp/bdt' for bin in binlist],
			'down':[bin+'_SubTotalRelativeJESDown/bdt' for bin in binlist],
			'linestyle':3}
		,
		'SubTotalPileUpJES':{
			'up':[bin+'_SubTotalPileUpJESUp/bdt' for bin in binlist],
			'down':[bin+'_SubTotalPileUpJESDown/bdt' for bin in binlist],
			'linestyle':4}
		,
		'SubTotalPtJES':{
			'up':[bin+'_SubTotalPtJESUp/bdt' for bin in binlist],
			'down':[bin+'_SubTotalPtJESDown/bdt' for bin in binlist],
			'linestyle':5}
		}
	}
}
