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
		'btagWeightCSVHFStats1':{
			'up':[bin+'_btagWeightCSVHFStats1Up/bdt' for bin in binlist],
			'down':[bin+'_btagWeightCSVHFStats1Down/bdt' for bin in binlist],
			'linestyle':2}
		,
		'btagWeightCSVHFStats2':{
			'up':[bin+'_btagWeightCSVHFStats2Up/bdt' for bin in binlist],
			'down':[bin+'_btagWeightCSVHFStats2Down/bdt' for bin in binlist],
			'linestyle':3}
		,
		'btagWeightCSVHF':{
			'up':[bin+'_btagWeightCSVHFUp/bdt' for bin in binlist],
			'down':[bin+'_btagWeightCSVHFDown/bdt' for bin in binlist],
			'linestyle':4}
		}
	}
}
