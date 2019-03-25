config={'annotation': 'Combined Electon+Muon channel. Comparison of MC templates with different systematic variations.',
 'command': 'MVC_template.py -b -c conf_cff.py',
 'latex_main': 'latex/report.tex',
 'mode': 'plots',
 'canvas':['canvas_ps'],

 'canvas_ps':{
    "name":"canvas_ps",
     "type":"3x1_ratio_leg_bottom",
     "templates":["TTTTISRUp",        "TTTTISRDown",
                  "TTTTFSRUp",        "TTTTFSRDown", 
                  ],
     "ratios":{
         "option":"normalized_difference",
         "templates":["up/central","down/central"],
         "yrange":[-0.3,0.3]
     },
     "legend":{
       "header":"PS variations",
       "pos":[0.5,0.8,0.9,0.9],
       "entries":["TTTTISRUp","TTTTFSRUp",
                  "TTTTISRDown","TTTTFSRDown"]
     },
    "separators":{
         "labels":[["7",12.5],["8",30.5],["9",43.5],["10+",55.6],["FAKE",0.0]],
         "ypos":0.6,
         "size":0.042,
     },
     "central":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TTTT_CARDS.root",
            "subhistograms":["7J2M/bdt","7J3M/bdt","7J4M/bdt","8J2M/bdt","8J3M/bdt","8J4M/bdt","9J2M/bdt","9J3M/bdt","9J4M/bdt","10J2M/bdt","10J3M/bdt","10J4M/bdt"],
         },
	 "axes":{"x":{"SetTitle":"Jet multiplicity","SetLabelSize":0.0},"y":{"SetTitle":"Events/bin"}},
         "style":{"SetLineWidth":2},
         "legend_entry":{"name":"central", "option":"l"}
     },
     "TTTTISRUp":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TTTT_CARDS.root",
            "subhistograms":["7J2M_TTTTISRUp/bdt","7J3M_TTTTISRUp/bdt","7J4M_TTTTISRUp/bdt","8J2M_TTTTISRUp/bdt","8J3M_TTTTISRUp/bdt","8J4M_TTTTISRUp/bdt","9J2M_TTTTISRUp/bdt","9J3M_TTTTISRUp/bdt","9J4M_TTTTISRUp/bdt","10J2M_TTTTISRUp/bdt","10J3M_TTTTISRUp/bdt","10J4M_TTTTISRUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":2,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{ISR}","option":"l"}
     },
     "TTTTISRDown":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TTTT_CARDS.root",
            "subhistograms":["7J2M_TTTTISRDown/bdt","7J3M_TTTTISRDown/bdt","7J4M_TTTTISRDown/bdt","8J2M_TTTTISRDown/bdt","8J3M_TTTTISRDown/bdt","8J4M_TTTTISRDown/bdt","9J2M_TTTTISRDown/bdt","9J3M_TTTTISRDown/bdt","9J4M_TTTTISRDown/bdt","10J2M_TTTTISRDown/bdt","10J3M_TTTTISRDown/bdt","10J4M_TTTTISRDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":2,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{ISR}","option":"l"}
     },
    
    "TTTTFSRUp":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TTTT_CARDS.root",
            "subhistograms":["7J2M_TTTTFSRUp/bdt","7J3M_TTTTFSRUp/bdt","7J4M_TTTTFSRUp/bdt","8J2M_TTTTFSRUp/bdt","8J3M_TTTTFSRUp/bdt","8J4M_TTTTFSRUp/bdt","9J2M_TTTTFSRUp/bdt","9J3M_TTTTFSRUp/bdt","9J4M_TTTTFSRUp/bdt","10J2M_TTTTFSRUp/bdt","10J3M_TTTTFSRUp/bdt","10J4M_TTTTFSRUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":3,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{FSR}","option":"l"}
     },
     "TTTTFSRDown":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TTTT_CARDS.root",
            "subhistograms":["7J2M_TTTTFSRDown/bdt","7J3M_TTTTFSRDown/bdt","7J4M_TTTTFSRDown/bdt","8J2M_TTTTFSRDown/bdt","8J3M_TTTTFSRDown/bdt","8J4M_TTTTFSRDown/bdt","9J2M_TTTTFSRDown/bdt","9J3M_TTTTFSRDown/bdt","9J4M_TTTTFSRDown/bdt","10J2M_TTTTFSRDown/bdt","10J3M_TTTTFSRDown/bdt","10J4M_TTTTFSRDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":3,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{FSR}","option":"l"}
     },
         
    "TTUEUp":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TTTT_CARDS.root",
            "subhistograms":["7J2M_TTUEUp/bdt","7J3M_TTUEUp/bdt","7J4M_TTUEUp/bdt","8J2M_TTUEUp/bdt","8J3M_TTUEUp/bdt","8J4M_TTUEUp/bdt","9J2M_TTUEUp/bdt","9J3M_TTUEUp/bdt","9J4M_TTUEUp/bdt","10J2M_TTUEUp/bdt","10J3M_TTUEUp/bdt","10J4M_TTUEUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{UE}","option":"l"}
     },
     "TTUEDown":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TTTT_CARDS.root",
            "subhistograms":["7J2M_TTUEDown/bdt","7J3M_TTUEDown/bdt","7J4M_TTUEDown/bdt","8J2M_TTUEDown/bdt","8J3M_TTUEDown/bdt","8J4M_TTUEDown/bdt","9J2M_TTUEDown/bdt","9J3M_TTUEDown/bdt","9J4M_TTUEDown/bdt","10J2M_TTUEDown/bdt","10J3M_TTUEDown/bdt","10J4M_TTUEDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{UE}","option":"l"}
     },
              
    "TTJets_HDAMPUp":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TTTT_CARDS.root",
            "subhistograms":["7J2M_TTJets_HDAMPUp/bdt","7J3M_TTJets_HDAMPUp/bdt","7J4M_TTJets_HDAMPUp/bdt","8J2M_TTJets_HDAMPUp/bdt","8J3M_TTJets_HDAMPUp/bdt","8J4M_TTJets_HDAMPUp/bdt","9J2M_TTJets_HDAMPUp/bdt","9J3M_TTJets_HDAMPUp/bdt","9J4M_TTJets_HDAMPUp/bdt","10J2M_TTJets_HDAMPUp/bdt","10J3M_TTJets_HDAMPUp/bdt","10J4M_TTJets_HDAMPUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":5,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{hDAMP}","option":"l"}
     },
     "TTJets_HDAMPDown":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TTTT_CARDS.root",
            "subhistograms":["7J2M_TTJets_HDAMPDown/bdt","7J3M_TTJets_HDAMPDown/bdt","7J4M_TTJets_HDAMPDown/bdt","8J2M_TTJets_HDAMPDown/bdt","8J3M_TTJets_HDAMPDown/bdt","8J4M_TTJets_HDAMPDown/bdt","9J2M_TTJets_HDAMPDown/bdt","9J3M_TTJets_HDAMPDown/bdt","9J4M_TTJets_HDAMPDown/bdt","10J2M_TTJets_HDAMPDown/bdt","10J3M_TTJets_HDAMPDown/bdt","10J4M_TTJets_HDAMPDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":5,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{hDAMP}","option":"l"}
     },

 },
}
