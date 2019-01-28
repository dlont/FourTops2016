config={'annotation': 'Combined Electon+Muon channel. Comparison of MC templates with different systematic variations.',
 'command': 'MVC_template.py -b -c conf_cff.py',
 'latex_main': 'latex/report.tex',
 'mode': 'plots',
 'canvas':['canvas_ps'],

 'canvas_ps':{
    "name":"canvas_ps",
     "type":"3x1_ratio_leg_bottom",
     "templates":["TTISRUp",        "TTISRDown",
                  "TTFSRUp",        "TTFSRDown",
                  "TTUEUp",         "TTUEDown",
                  "TTJets_HDAMPUp", "TTJets_HDAMPDown",    
                  ],
     "ratios":{
         "option":"normalized_difference",
         "templates":["up/central","down/central"],
         "yrange":[-0.3,0.3]
     },
     "legend":{
       "header":"PS variations",
       "pos":[0.5,0.8,0.9,0.9],
       "entries":["TTISRUp","TTFSRUp","TTUEUp","TTJets_HDAMPUp",
                  "TTISRDown","TTFSRDown","TTUEDown","TTJets_HDAMPDown",]
     },
    "separators":{
         "labels":[["7/2",7.5],["7/3",14.5],["7/4",19.5],["8/2",24.7],["8/3",30.5],["8/4",34.5],["9/2",38.5],["9/3",42.5],["9/4",47.5],["10/2",51.5],["10/3",55.5],["10/4",59.6]],
         "ypos":0.5,
         "size":0.022,
     },
     "central":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TT_CARDS.root",
            "subhistograms":["7J2M/bdt","7J3M/bdt","7J4M/bdt","8J2M/bdt","8J3M/bdt","8J4M/bdt","9J2M/bdt","9J3M/bdt","9J4M/bdt","10J2M/bdt","10J3M/bdt","10J4M/bdt"],
         },
         "style":{"SetLineWidth":2},
         "legend_entry":{"name":"central", "option":"l"}
     },
     "TTISRUp":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTISRUp/bdt","7J3M_TTISRUp/bdt","7J4M_TTISRUp/bdt","8J2M_TTISRUp/bdt","8J3M_TTISRUp/bdt","8J4M_TTISRUp/bdt","9J2M_TTISRUp/bdt","9J3M_TTISRUp/bdt","9J4M_TTISRUp/bdt","10J2M_TTISRUp/bdt","10J3M_TTISRUp/bdt","10J4M_TTISRUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":2,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{ISR}","option":"l"}
     },
     "TTISRDown":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTISRDown/bdt","7J3M_TTISRDown/bdt","7J4M_TTISRDown/bdt","8J2M_TTISRDown/bdt","8J3M_TTISRDown/bdt","8J4M_TTISRDown/bdt","9J2M_TTISRDown/bdt","9J3M_TTISRDown/bdt","9J4M_TTISRDown/bdt","10J2M_TTISRDown/bdt","10J3M_TTISRDown/bdt","10J4M_TTISRDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":2,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{ISR}","option":"l"}
     },
    
    "TTFSRUp":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTFSRUp/bdt","7J3M_TTFSRUp/bdt","7J4M_TTFSRUp/bdt","8J2M_TTFSRUp/bdt","8J3M_TTFSRUp/bdt","8J4M_TTFSRUp/bdt","9J2M_TTFSRUp/bdt","9J3M_TTFSRUp/bdt","9J4M_TTFSRUp/bdt","10J2M_TTFSRUp/bdt","10J3M_TTFSRUp/bdt","10J4M_TTFSRUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":3,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{FSR}","option":"l"}
     },
     "TTFSRDown":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTFSRDown/bdt","7J3M_TTFSRDown/bdt","7J4M_TTFSRDown/bdt","8J2M_TTFSRDown/bdt","8J3M_TTFSRDown/bdt","8J4M_TTFSRDown/bdt","9J2M_TTFSRDown/bdt","9J3M_TTFSRDown/bdt","9J4M_TTFSRDown/bdt","10J2M_TTFSRDown/bdt","10J3M_TTFSRDown/bdt","10J4M_TTFSRDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":3,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{FSR}","option":"l"}
     },
         
    "TTUEUp":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTUEUp/bdt","7J3M_TTUEUp/bdt","7J4M_TTUEUp/bdt","8J2M_TTUEUp/bdt","8J3M_TTUEUp/bdt","8J4M_TTUEUp/bdt","9J2M_TTUEUp/bdt","9J3M_TTUEUp/bdt","9J4M_TTUEUp/bdt","10J2M_TTUEUp/bdt","10J3M_TTUEUp/bdt","10J4M_TTUEUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{UE}","option":"l"}
     },
     "TTUEDown":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTUEDown/bdt","7J3M_TTUEDown/bdt","7J4M_TTUEDown/bdt","8J2M_TTUEDown/bdt","8J3M_TTUEDown/bdt","8J4M_TTUEDown/bdt","9J2M_TTUEDown/bdt","9J3M_TTUEDown/bdt","9J4M_TTUEDown/bdt","10J2M_TTUEDown/bdt","10J3M_TTUEDown/bdt","10J4M_TTUEDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{UE}","option":"l"}
     },
              
    "TTJets_HDAMPUp":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTJets_HDAMPUp/bdt","7J3M_TTJets_HDAMPUp/bdt","7J4M_TTJets_HDAMPUp/bdt","8J2M_TTJets_HDAMPUp/bdt","8J3M_TTJets_HDAMPUp/bdt","8J4M_TTJets_HDAMPUp/bdt","9J2M_TTJets_HDAMPUp/bdt","9J3M_TTJets_HDAMPUp/bdt","9J4M_TTJets_HDAMPUp/bdt","10J2M_TTJets_HDAMPUp/bdt","10J3M_TTJets_HDAMPUp/bdt","10J4M_TTJets_HDAMPUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":5,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{hDAMP}","option":"l"}
     },
     "TTJets_HDAMPDown":{
         "type":{         
            "algorithm":"from_file_norm_nj",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_elmu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_4ps//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTJets_HDAMPDown/bdt","7J3M_TTJets_HDAMPDown/bdt","7J4M_TTJets_HDAMPDown/bdt","8J2M_TTJets_HDAMPDown/bdt","8J3M_TTJets_HDAMPDown/bdt","8J4M_TTJets_HDAMPDown/bdt","9J2M_TTJets_HDAMPDown/bdt","9J3M_TTJets_HDAMPDown/bdt","9J4M_TTJets_HDAMPDown/bdt","10J2M_TTJets_HDAMPDown/bdt","10J3M_TTJets_HDAMPDown/bdt","10J4M_TTJets_HDAMPDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":5,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{hDAMP}","option":"l"}
     },

 },
}
