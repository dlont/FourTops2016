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
		{'ISR':{
			'up':[bin+'_TTISRUp/bdt' for bin in binlist],
			'down':[bin+'_TTISRDown/bdt' for bin in binlist],
			'linestyle':2}
		,
		'FSR':{
			'up':[bin+'_TTFSRUp/bdt' for bin in binlist],
			'down':[bin+'_TTFSRDown/bdt' for bin in binlist],
			'linestyle':3}
		,
		'UE':{
			'up':[bin+'_TTUEUp/bdt' for bin in binlist],
			'down':[bin+'_TTUEDown/bdt' for bin in binlist],
			'linestyle':4}
        ,
		'HDAMP':{
			'up':[bin+'_TTJets_HDAMPUp/bdt' for bin in binlist],
			'down':[bin+'_TTJets_HDAMPDown/bdt' for bin in binlist],
			'linestyle':5}
		}
	}
}
