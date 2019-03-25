config={'annotation': 'Muon channel. Comparison of MC templates with different systematic variations.',
 'command': 'MVC_template.py -b -c conf_cff.py',
 'latex_main': 'latex/report.tex',
 'mode': 'plots',
 'canvas':['canvas_btag','canvas_jec','canvas_shape_other', 'canvas_ps'],
 'canvas_btag':{
     "name":"canvas_btag",
     "type":"3x1_ratio_leg_bottom",
     "templates":["btagWeightCSVJESUp","btagWeightCSVJESDown","btagWeightCSVCFErr1Up","btagWeightCSVCFErr1Down",
                  "btagWeightCSVCFErr2Up","btagWeightCSVCFErr2Down","btagWeightCSVHFUp","btagWeightCSVHFDown","btagWeightCSVHFStats1Up","btagWeightCSVHFStats1Down",
                  "btagWeightCSVHFStats2Up","btagWeightCSVHFStats2Down","btagWeightCSVLFUp","btagWeightCSVLFDown","btagWeightCSVLFStats1Up","btagWeightCSVLFStats1Down",
                  "btagWeightCSVLFStats2Up","btagWeightCSVLFStats2Down"],
     "ratios":{
         "option":"normalized_difference",
         "templates":["up/central","down/central"],
         "yrange":[-0.2,0.2]
     },
     "legend":{
       "header":"b-tagging",
       "pos":[0.5,0.8,0.9,0.9],
       "entries":["btagWeightCSVJESUp","btagWeightCSVCFErr1Up","btagWeightCSVCFErr2Up","btagWeightCSVHFUp","btagWeightCSVHFStats1Up","btagWeightCSVHFStats2Up","btagWeightCSVLFUp","btagWeightCSVLFStats1Up","btagWeightCSVLFStats2Up",
                  "btagWeightCSVJESDown","btagWeightCSVCFErr1Down","btagWeightCSVCFErr2Down","btagWeightCSVHFDown","btagWeightCSVHFStats1Down","btagWeightCSVHFStats2Down","btagWeightCSVLFDown","btagWeightCSVLFStats1Down","btagWeightCSVLFStats2Down"]
     },
    "separators":{
         "labels":[["7/2",7.5],["7/3",14.5],["7/4",19.5],["8/2",24.7],["8/3",30.5],["8/4",34.5],["9/2",38.5],["9/3",42.5],["9/4",47.5],["10/2",51.5],["10/3",55.5],["10/4",59.6]],
         "ypos":0.5,
         "size":0.022,
     },
     "central":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M/bdt","7J3M/bdt","7J4M/bdt","8J2M/bdt","8J3M/bdt","8J4M/bdt","9J2M/bdt","9J3M/bdt","9J4M/bdt","10J2M/bdt","10J3M/bdt","10J4M/bdt"],
         },
         "style":{"SetLineWidth":2},
         "legend_entry":{"name":"central", "option":"l"}
     },
     "btagWeightCSVJESUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVJESUp/bdt","7J3M_btagWeightCSVJESUp/bdt","7J4M_btagWeightCSVJESUp/bdt","8J2M_btagWeightCSVJESUp/bdt","8J3M_btagWeightCSVJESUp/bdt","8J4M_btagWeightCSVJESUp/bdt","9J2M_btagWeightCSVJESUp/bdt","9J3M_btagWeightCSVJESUp/bdt","9J4M_btagWeightCSVJESUp/bdt","10J2M_btagWeightCSVJESUp/bdt","10J3M_btagWeightCSVJESUp/bdt","10J4M_btagWeightCSVJESUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":2,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{CSV,JES}","option":"l"}
     },
     "btagWeightCSVJESDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVJESDown/bdt","7J3M_btagWeightCSVJESDown/bdt","7J4M_btagWeightCSVJESDown/bdt","8J2M_btagWeightCSVJESDown/bdt","8J3M_btagWeightCSVJESDown/bdt","8J4M_btagWeightCSVJESDown/bdt","9J2M_btagWeightCSVJESDown/bdt","9J3M_btagWeightCSVJESDown/bdt","9J4M_btagWeightCSVJESDown/bdt","10J2M_btagWeightCSVJESDown/bdt","10J3M_btagWeightCSVJESDown/bdt","10J4M_btagWeightCSVJESDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":2,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{CSV,JES}","option":"l"}
     },
    
    "btagWeightCSVCFErr1Up":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVCFErr1Up/bdt","7J3M_btagWeightCSVCFErr1Up/bdt","7J4M_btagWeightCSVCFErr1Up/bdt","8J2M_btagWeightCSVCFErr1Up/bdt","8J3M_btagWeightCSVCFErr1Up/bdt","8J4M_btagWeightCSVCFErr1Up/bdt","9J2M_btagWeightCSVCFErr1Up/bdt","9J3M_btagWeightCSVCFErr1Up/bdt","9J4M_btagWeightCSVCFErr1Up/bdt","10J2M_btagWeightCSVCFErr1Up/bdt","10J3M_btagWeightCSVCFErr1Up/bdt","10J4M_btagWeightCSVCFErr1Up/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":3,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{CSV,CF Err1}","option":"l"}
     },
     "btagWeightCSVCFErr1Down":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVCFErr1Down/bdt","7J3M_btagWeightCSVCFErr1Down/bdt","7J4M_btagWeightCSVCFErr1Down/bdt","8J2M_btagWeightCSVCFErr1Down/bdt","8J3M_btagWeightCSVCFErr1Down/bdt","8J4M_btagWeightCSVCFErr1Down/bdt","9J2M_btagWeightCSVCFErr1Down/bdt","9J3M_btagWeightCSVCFErr1Down/bdt","9J4M_btagWeightCSVCFErr1Down/bdt","10J2M_btagWeightCSVCFErr1Down/bdt","10J3M_btagWeightCSVCFErr1Down/bdt","10J4M_btagWeightCSVCFErr1Down/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":3,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{CSV,CF Err1}","option":"l"}
     },
         
    "btagWeightCSVCFErr2Up":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVCFErr2Up/bdt","7J3M_btagWeightCSVCFErr2Up/bdt","7J4M_btagWeightCSVCFErr2Up/bdt","8J2M_btagWeightCSVCFErr2Up/bdt","8J3M_btagWeightCSVCFErr2Up/bdt","8J4M_btagWeightCSVCFErr2Up/bdt","9J2M_btagWeightCSVCFErr2Up/bdt","9J3M_btagWeightCSVCFErr2Up/bdt","9J4M_btagWeightCSVCFErr2Up/bdt","10J2M_btagWeightCSVCFErr2Up/bdt","10J3M_btagWeightCSVCFErr2Up/bdt","10J4M_btagWeightCSVCFErr2Up/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{CSV,CF Err2}","option":"l"}
     },
     "btagWeightCSVCFErr2Down":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVCFErr2Down/bdt","7J3M_btagWeightCSVCFErr2Down/bdt","7J4M_btagWeightCSVCFErr2Down/bdt","8J2M_btagWeightCSVCFErr2Down/bdt","8J3M_btagWeightCSVCFErr2Down/bdt","8J4M_btagWeightCSVCFErr2Down/bdt","9J2M_btagWeightCSVCFErr2Down/bdt","9J3M_btagWeightCSVCFErr2Down/bdt","9J4M_btagWeightCSVCFErr2Down/bdt","10J2M_btagWeightCSVCFErr2Down/bdt","10J3M_btagWeightCSVCFErr2Down/bdt","10J4M_btagWeightCSVCFErr2Down/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{CSV,CF Err2}","option":"l"}
     },
              
    "btagWeightCSVHFUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVHFUp/bdt","7J3M_btagWeightCSVHFUp/bdt","7J4M_btagWeightCSVHFUp/bdt","8J2M_btagWeightCSVHFUp/bdt","8J3M_btagWeightCSVHFUp/bdt","8J4M_btagWeightCSVHFUp/bdt","9J2M_btagWeightCSVHFUp/bdt","9J3M_btagWeightCSVHFUp/bdt","9J4M_btagWeightCSVHFUp/bdt","10J2M_btagWeightCSVHFUp/bdt","10J3M_btagWeightCSVHFUp/bdt","10J4M_btagWeightCSVHFUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":5,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{CSV,HF}","option":"l"}
     },
     "btagWeightCSVHFDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVHFDown/bdt","7J3M_btagWeightCSVHFDown/bdt","7J4M_btagWeightCSVHFDown/bdt","8J2M_btagWeightCSVHFDown/bdt","8J3M_btagWeightCSVHFDown/bdt","8J4M_btagWeightCSVHFDown/bdt","9J2M_btagWeightCSVHFDown/bdt","9J3M_btagWeightCSVHFDown/bdt","9J4M_btagWeightCSVHFDown/bdt","10J2M_btagWeightCSVHFDown/bdt","10J3M_btagWeightCSVHFDown/bdt","10J4M_btagWeightCSVHFDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":5,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{CSV,HF}","option":"l"}
     },
              
    "btagWeightCSVHFStats1Up":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVHFStats1Up/bdt","7J3M_btagWeightCSVHFStats1Up/bdt","7J4M_btagWeightCSVHFStats1Up/bdt","8J2M_btagWeightCSVHFStats1Up/bdt","8J3M_btagWeightCSVHFStats1Up/bdt","8J4M_btagWeightCSVHFStats1Up/bdt","9J2M_btagWeightCSVHFStats1Up/bdt","9J3M_btagWeightCSVHFStats1Up/bdt","9J4M_btagWeightCSVHFStats1Up/bdt","10J2M_btagWeightCSVHFStats1Up/bdt","10J3M_btagWeightCSVHFStats1Up/bdt","10J4M_btagWeightCSVHFStats1Up/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":6,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{CSV,HF Stat1}","option":"l"}
     },
     "btagWeightCSVHFStats1Down":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVHFStats1Down/bdt","7J3M_btagWeightCSVHFStats1Down/bdt","7J4M_btagWeightCSVHFStats1Down/bdt","8J2M_btagWeightCSVHFStats1Down/bdt","8J3M_btagWeightCSVHFStats1Down/bdt","8J4M_btagWeightCSVHFStats1Down/bdt","9J2M_btagWeightCSVHFStats1Down/bdt","9J3M_btagWeightCSVHFStats1Down/bdt","9J4M_btagWeightCSVHFStats1Down/bdt","10J2M_btagWeightCSVHFStats1Down/bdt","10J3M_btagWeightCSVHFStats1Down/bdt","10J4M_btagWeightCSVHFStats1Down/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":6,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{CSV,HF Stat1}","option":"l"}
     },
              
    "btagWeightCSVHFStats2Up":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVHFStats2Up/bdt","7J3M_btagWeightCSVHFStats2Up/bdt","7J4M_btagWeightCSVHFStats2Up/bdt","8J2M_btagWeightCSVHFStats2Up/bdt","8J3M_btagWeightCSVHFStats2Up/bdt","8J4M_btagWeightCSVHFStats2Up/bdt","9J2M_btagWeightCSVHFStats2Up/bdt","9J3M_btagWeightCSVHFStats2Up/bdt","9J4M_btagWeightCSVHFStats2Up/bdt","10J2M_btagWeightCSVHFStats2Up/bdt","10J3M_btagWeightCSVHFStats2Up/bdt","10J4M_btagWeightCSVHFStats2Up/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":7,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{CSV,HF Stat2}","option":"l"}
     },
     "btagWeightCSVHFStats2Down":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVHFStats2Down/bdt","7J3M_btagWeightCSVHFStats2Down/bdt","7J4M_btagWeightCSVHFStats2Down/bdt","8J2M_btagWeightCSVHFStats2Down/bdt","8J3M_btagWeightCSVHFStats2Down/bdt","8J4M_btagWeightCSVHFStats2Down/bdt","9J2M_btagWeightCSVHFStats2Down/bdt","9J3M_btagWeightCSVHFStats2Down/bdt","9J4M_btagWeightCSVHFStats2Down/bdt","10J2M_btagWeightCSVHFStats2Down/bdt","10J3M_btagWeightCSVHFStats2Down/bdt","10J4M_btagWeightCSVHFStats2Down/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":7,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{CSV,HF Stat2}","option":"l"}
     },
                   
    "btagWeightCSVLFUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVLFUp/bdt","7J3M_btagWeightCSVLFUp/bdt","7J4M_btagWeightCSVLFUp/bdt","8J2M_btagWeightCSVLFUp/bdt","8J3M_btagWeightCSVLFUp/bdt","8J4M_btagWeightCSVLFUp/bdt","9J2M_btagWeightCSVLFUp/bdt","9J3M_btagWeightCSVLFUp/bdt","9J4M_btagWeightCSVLFUp/bdt","10J2M_btagWeightCSVLFUp/bdt","10J3M_btagWeightCSVLFUp/bdt","10J4M_btagWeightCSVLFUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":8,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{CSV,LF}","option":"l"}
     },
     "btagWeightCSVLFDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVLFDown/bdt","7J3M_btagWeightCSVLFDown/bdt","7J4M_btagWeightCSVLFDown/bdt","8J2M_btagWeightCSVLFDown/bdt","8J3M_btagWeightCSVLFDown/bdt","8J4M_btagWeightCSVLFDown/bdt","9J2M_btagWeightCSVLFDown/bdt","9J3M_btagWeightCSVLFDown/bdt","9J4M_btagWeightCSVLFDown/bdt","10J2M_btagWeightCSVLFDown/bdt","10J3M_btagWeightCSVLFDown/bdt","10J4M_btagWeightCSVLFDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":8,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{CSV,LF}","option":"l"}
     },
              
    "btagWeightCSVLFStats1Up":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVLFStats1Up/bdt","7J3M_btagWeightCSVLFStats1Up/bdt","7J4M_btagWeightCSVLFStats1Up/bdt","8J2M_btagWeightCSVLFStats1Up/bdt","8J3M_btagWeightCSVLFStats1Up/bdt","8J4M_btagWeightCSVLFStats1Up/bdt","9J2M_btagWeightCSVLFStats1Up/bdt","9J3M_btagWeightCSVLFStats1Up/bdt","9J4M_btagWeightCSVLFStats1Up/bdt","10J2M_btagWeightCSVLFStats1Up/bdt","10J3M_btagWeightCSVLFStats1Up/bdt","10J4M_btagWeightCSVLFStats1Up/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":435,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{CSV,LF Stat1}","option":"l"}
     },
     "btagWeightCSVLFStats1Down":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVLFStats1Down/bdt","7J3M_btagWeightCSVLFStats1Down/bdt","7J4M_btagWeightCSVLFStats1Down/bdt","8J2M_btagWeightCSVLFStats1Down/bdt","8J3M_btagWeightCSVLFStats1Down/bdt","8J4M_btagWeightCSVLFStats1Down/bdt","9J2M_btagWeightCSVLFStats1Down/bdt","9J3M_btagWeightCSVLFStats1Down/bdt","9J4M_btagWeightCSVLFStats1Down/bdt","10J2M_btagWeightCSVLFStats1Down/bdt","10J3M_btagWeightCSVLFStats1Down/bdt","10J4M_btagWeightCSVLFStats1Down/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":435,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{CSV,LF Stat1}","option":"l"}
     },
              
    "btagWeightCSVLFStats2Up":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVLFStats2Up/bdt","7J3M_btagWeightCSVLFStats2Up/bdt","7J4M_btagWeightCSVLFStats2Up/bdt","8J2M_btagWeightCSVLFStats2Up/bdt","8J3M_btagWeightCSVLFStats2Up/bdt","8J4M_btagWeightCSVLFStats2Up/bdt","9J2M_btagWeightCSVLFStats2Up/bdt","9J3M_btagWeightCSVLFStats2Up/bdt","9J4M_btagWeightCSVLFStats2Up/bdt","10J2M_btagWeightCSVLFStats2Up/bdt","10J3M_btagWeightCSVLFStats2Up/bdt","10J4M_btagWeightCSVLFStats2Up/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":635,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{CSV,LF Stat2}","option":"l"}
     },
     "btagWeightCSVLFStats2Down":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_btagWeightCSVLFStats2Down/bdt","7J3M_btagWeightCSVLFStats2Down/bdt","7J4M_btagWeightCSVLFStats2Down/bdt","8J2M_btagWeightCSVLFStats2Down/bdt","8J3M_btagWeightCSVLFStats2Down/bdt","8J4M_btagWeightCSVLFStats2Down/bdt","9J2M_btagWeightCSVLFStats2Down/bdt","9J3M_btagWeightCSVLFStats2Down/bdt","9J4M_btagWeightCSVLFStats2Down/bdt","10J2M_btagWeightCSVLFStats2Down/bdt","10J3M_btagWeightCSVLFStats2Down/bdt","10J4M_btagWeightCSVLFStats2Down/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":635,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{CSV,LF Stat2}","option":"l"}
     },
 },
#  --------------------------------------------
 'canvas_jec':{
    "name":"canvas_jec",
     "type":"3x1_ratio_leg_bottom",
     "templates":[
                  "SubTotalPileUpJESUp","SubTotalPileUpJESDown",
                  "SubTotalFlavorJESUp","SubTotalFlavorJESDown",
                  "SubTotalPtJESUp",    "SubTotalPtJESDown",    
                  "SubTotalRelativeJESUp",  "SubTotalRelativeJESDown",
                  "SubTotalScaleJESUp","SubTotalScaleJESDown",
                  "SubTotalTimePtEtaJESUp","SubTotalTimePtEtaJESDown",
                  "JERUp","JERDown"],
     "ratios":{
         "option":"normalized_difference",
         "templates":["up/central","down/central"],
         "yrange":[-0.2,0.2]
     },
     "legend":{
       "header":"JEC Components",
       "pos":[0.5,0.8,0.9,0.9],
       "entries":["SubTotalPileUpJESUp","SubTotalFlavorJESUp","SubTotalPtJESUp","SubTotalRelativeJESUp","SubTotalScaleJESUp","SubTotalTimePtEtaJESUp","JERUp",
                  "SubTotalPileUpJESDown","SubTotalFlavorJESDown","SubTotalPtJESDown","SubTotalRelativeJESDown","SubTotalScaleJESDown","SubTotalTimePtEtaJESDown","JERDown"]
     },
    "separators":{
         "labels":[["7/2",7.5],["7/3",14.5],["7/4",19.5],["8/2",24.7],["8/3",30.5],["8/4",34.5],["9/2",38.5],["9/3",42.5],["9/4",47.5],["10/2",51.5],["10/3",55.5],["10/4",59.6]],
         "ypos":0.5,
         "size":0.022,
     },
     "central":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M/bdt","7J3M/bdt","7J4M/bdt","8J2M/bdt","8J3M/bdt","8J4M/bdt","9J2M/bdt","9J3M/bdt","9J4M/bdt","10J2M/bdt","10J3M/bdt","10J4M/bdt"],
         },
         "style":{"SetLineWidth":2},
         "legend_entry":{"name":"central", "option":"l"}
     },
     "SubTotalPileUpJESUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_SubTotalPileUpJESUp/bdt","7J3M_SubTotalPileUpJESUp/bdt","7J4M_SubTotalPileUpJESUp/bdt","8J2M_SubTotalPileUpJESUp/bdt","8J3M_SubTotalPileUpJESUp/bdt","8J4M_SubTotalPileUpJESUp/bdt","9J2M_SubTotalPileUpJESUp/bdt","9J3M_SubTotalPileUpJESUp/bdt","9J4M_SubTotalPileUpJESUp/bdt","10J2M_SubTotalPileUpJESUp/bdt","10J3M_SubTotalPileUpJESUp/bdt","10J4M_SubTotalPileUpJESUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":2,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{JES,PU}","option":"l"}
     },
     "SubTotalPileUpJESDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_SubTotalPileUpJESDown/bdt","7J3M_SubTotalPileUpJESDown/bdt","7J4M_SubTotalPileUpJESDown/bdt","8J2M_SubTotalPileUpJESDown/bdt","8J3M_SubTotalPileUpJESDown/bdt","8J4M_SubTotalPileUpJESDown/bdt","9J2M_SubTotalPileUpJESDown/bdt","9J3M_SubTotalPileUpJESDown/bdt","9J4M_SubTotalPileUpJESDown/bdt","10J2M_SubTotalPileUpJESDown/bdt","10J3M_SubTotalPileUpJESDown/bdt","10J4M_SubTotalPileUpJESDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":2,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{JES,PU}","option":"l"}
     },
    
    "SubTotalFlavorJESUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_SubTotalFlavorJESUp/bdt","7J3M_SubTotalFlavorJESUp/bdt","7J4M_SubTotalFlavorJESUp/bdt","8J2M_SubTotalFlavorJESUp/bdt","8J3M_SubTotalFlavorJESUp/bdt","8J4M_SubTotalFlavorJESUp/bdt","9J2M_SubTotalFlavorJESUp/bdt","9J3M_SubTotalFlavorJESUp/bdt","9J4M_SubTotalFlavorJESUp/bdt","10J2M_SubTotalFlavorJESUp/bdt","10J3M_SubTotalFlavorJESUp/bdt","10J4M_SubTotalFlavorJESUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":3,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{JES,Flav}","option":"l"}
     },
     "SubTotalFlavorJESDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_SubTotalFlavorJESDown/bdt","7J3M_SubTotalFlavorJESDown/bdt","7J4M_SubTotalFlavorJESDown/bdt","8J2M_SubTotalFlavorJESDown/bdt","8J3M_SubTotalFlavorJESDown/bdt","8J4M_SubTotalFlavorJESDown/bdt","9J2M_SubTotalFlavorJESDown/bdt","9J3M_SubTotalFlavorJESDown/bdt","9J4M_SubTotalFlavorJESDown/bdt","10J2M_SubTotalFlavorJESDown/bdt","10J3M_SubTotalFlavorJESDown/bdt","10J4M_SubTotalFlavorJESDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":3,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{JES,Flav}","option":"l"}
     },
         
    "SubTotalPtJESUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_SubTotalPtJESUp/bdt","7J3M_SubTotalPtJESUp/bdt","7J4M_SubTotalPtJESUp/bdt","8J2M_SubTotalPtJESUp/bdt","8J3M_SubTotalPtJESUp/bdt","8J4M_SubTotalPtJESUp/bdt","9J2M_SubTotalPtJESUp/bdt","9J3M_SubTotalPtJESUp/bdt","9J4M_SubTotalPtJESUp/bdt","10J2M_SubTotalPtJESUp/bdt","10J3M_SubTotalPtJESUp/bdt","10J4M_SubTotalPtJESUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{JES,pT}","option":"l"}
     },
     "SubTotalPtJESDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_SubTotalPtJESDown/bdt","7J3M_SubTotalPtJESDown/bdt","7J4M_SubTotalPtJESDown/bdt","8J2M_SubTotalPtJESDown/bdt","8J3M_SubTotalPtJESDown/bdt","8J4M_SubTotalPtJESDown/bdt","9J2M_SubTotalPtJESDown/bdt","9J3M_SubTotalPtJESDown/bdt","9J4M_SubTotalPtJESDown/bdt","10J2M_SubTotalPtJESDown/bdt","10J3M_SubTotalPtJESDown/bdt","10J4M_SubTotalPtJESDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{JES,pT}","option":"l"}
     },
              
    "SubTotalRelativeJESUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_SubTotalRelativeJESUp/bdt","7J3M_SubTotalRelativeJESUp/bdt","7J4M_SubTotalRelativeJESUp/bdt","8J2M_SubTotalRelativeJESUp/bdt","8J3M_SubTotalRelativeJESUp/bdt","8J4M_SubTotalRelativeJESUp/bdt","9J2M_SubTotalRelativeJESUp/bdt","9J3M_SubTotalRelativeJESUp/bdt","9J4M_SubTotalRelativeJESUp/bdt","10J2M_SubTotalRelativeJESUp/bdt","10J3M_SubTotalRelativeJESUp/bdt","10J4M_SubTotalRelativeJESUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":5,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{JES,rel}","option":"l"}
     },
     "SubTotalRelativeJESDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_SubTotalRelativeJESDown/bdt","7J3M_SubTotalRelativeJESDown/bdt","7J4M_SubTotalRelativeJESDown/bdt","8J2M_SubTotalRelativeJESDown/bdt","8J3M_SubTotalRelativeJESDown/bdt","8J4M_SubTotalRelativeJESDown/bdt","9J2M_SubTotalRelativeJESDown/bdt","9J3M_SubTotalRelativeJESDown/bdt","9J4M_SubTotalRelativeJESDown/bdt","10J2M_SubTotalRelativeJESDown/bdt","10J3M_SubTotalRelativeJESDown/bdt","10J4M_SubTotalRelativeJESDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":5,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{JES,rel}","option":"l"}
     },
              
    "SubTotalScaleJESUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_SubTotalScaleJESUp/bdt","7J3M_SubTotalScaleJESUp/bdt","7J4M_SubTotalScaleJESUp/bdt","8J2M_SubTotalScaleJESUp/bdt","8J3M_SubTotalScaleJESUp/bdt","8J4M_SubTotalScaleJESUp/bdt","9J2M_SubTotalScaleJESUp/bdt","9J3M_SubTotalScaleJESUp/bdt","9J4M_SubTotalScaleJESUp/bdt","10J2M_SubTotalScaleJESUp/bdt","10J3M_SubTotalScaleJESUp/bdt","10J4M_SubTotalScaleJESUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":6,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{JES,scale}","option":"l"}
     },
     "SubTotalScaleJESDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_SubTotalScaleJESDown/bdt","7J3M_SubTotalScaleJESDown/bdt","7J4M_SubTotalScaleJESDown/bdt","8J2M_SubTotalScaleJESDown/bdt","8J3M_SubTotalScaleJESDown/bdt","8J4M_SubTotalScaleJESDown/bdt","9J2M_SubTotalScaleJESDown/bdt","9J3M_SubTotalScaleJESDown/bdt","9J4M_SubTotalScaleJESDown/bdt","10J2M_SubTotalScaleJESDown/bdt","10J3M_SubTotalScaleJESDown/bdt","10J4M_SubTotalScaleJESDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":6,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{JES,scale}","option":"l"}
     },
              
    "SubTotalTimePtEtaJESUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_SubTotalTimePtEtaJESUp/bdt","7J3M_SubTotalTimePtEtaJESUp/bdt","7J4M_SubTotalTimePtEtaJESUp/bdt","8J2M_SubTotalTimePtEtaJESUp/bdt","8J3M_SubTotalTimePtEtaJESUp/bdt","8J4M_SubTotalTimePtEtaJESUp/bdt","9J2M_SubTotalTimePtEtaJESUp/bdt","9J3M_SubTotalTimePtEtaJESUp/bdt","9J4M_SubTotalTimePtEtaJESUp/bdt","10J2M_SubTotalTimePtEtaJESUp/bdt","10J3M_SubTotalTimePtEtaJESUp/bdt","10J4M_SubTotalTimePtEtaJESUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":7,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{JES,time}","option":"l"}
     },
     "SubTotalTimePtEtaJESDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_SubTotalTimePtEtaJESDown/bdt","7J3M_SubTotalTimePtEtaJESDown/bdt","7J4M_SubTotalTimePtEtaJESDown/bdt","8J2M_SubTotalTimePtEtaJESDown/bdt","8J3M_SubTotalTimePtEtaJESDown/bdt","8J4M_SubTotalTimePtEtaJESDown/bdt","9J2M_SubTotalTimePtEtaJESDown/bdt","9J3M_SubTotalTimePtEtaJESDown/bdt","9J4M_SubTotalTimePtEtaJESDown/bdt","10J2M_SubTotalTimePtEtaJESDown/bdt","10J3M_SubTotalTimePtEtaJESDown/bdt","10J4M_SubTotalTimePtEtaJESDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":7,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{JES,time}","option":"l"}
     },
                   
    "JERUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_JERUp/bdt","7J3M_JERUp/bdt","7J4M_JERUp/bdt","8J2M_JERUp/bdt","8J3M_JERUp/bdt","8J4M_JERUp/bdt","9J2M_JERUp/bdt","9J3M_JERUp/bdt","9J4M_JERUp/bdt","10J2M_JERUp/bdt","10J3M_JERUp/bdt","10J4M_JERUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":435,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{JER}","option":"l"}
     },
     "JERDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_JERDown/bdt","7J3M_JERDown/bdt","7J4M_JERDown/bdt","8J2M_JERDown/bdt","8J3M_JERDown/bdt","8J4M_JERDown/bdt","9J2M_JERDown/bdt","9J3M_JERDown/bdt","9J4M_JERDown/bdt","10J2M_JERDown/bdt","10J3M_JERDown/bdt","10J4M_JERDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":435,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{JER}","option":"l"}
     },
 },
# ----------------------------------------
 'canvas_shape_other':{
    "name":"canvas_shape_other",
     "type":"3x1_ratio_leg_bottom",
     "templates":["heavyFlavUp",     "heavyFlavDown",
                  "PUUp",            "PUDown",
                  "TTJets_PDFUp",    "TTJets_PDFDown",    
                  "ttMEScaleUp",     "ttMEScaleDown",
                  "TTPTUp",          "TTPTDown"],
     "ratios":{
         "option":"normalized_difference",
         "templates":["up/central","down/central"],
         "yrange":[-0.3,0.3]
     },
     "legend":{
       "header":"SHAPE other components",
       "pos":[0.5,0.8,0.9,0.9],
       "entries":["heavyFlavUp","PUUp","TTJets_PDFUp","ttMEScaleUp","TTPTUp",
                  "heavyFlavDown","PUDown","TTJets_PDFDown","ttMEScaleDown","TTPTDown"]
     },
    "separators":{
         "labels":[["7/2",7.5],["7/3",14.5],["7/4",19.5],["8/2",24.7],["8/3",30.5],["8/4",34.5],["9/2",38.5],["9/3",42.5],["9/4",47.5],["10/2",51.5],["10/3",55.5],["10/4",59.6]],
         "ypos":0.5,
         "size":0.022,
     },
     "central":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M/bdt","7J3M/bdt","7J4M/bdt","8J2M/bdt","8J3M/bdt","8J4M/bdt","9J2M/bdt","9J3M/bdt","9J4M/bdt","10J2M/bdt","10J3M/bdt","10J4M/bdt"],
         },
         "style":{"SetLineWidth":2},
         "legend_entry":{"name":"central", "option":"l"}
     },
     "heavyFlavUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_heavyFlavUp/bdt","7J3M_heavyFlavUp/bdt","7J4M_heavyFlavUp/bdt","8J2M_heavyFlavUp/bdt","8J3M_heavyFlavUp/bdt","8J4M_heavyFlavUp/bdt","9J2M_heavyFlavUp/bdt","9J3M_heavyFlavUp/bdt","9J4M_heavyFlavUp/bdt","10J2M_heavyFlavUp/bdt","10J3M_heavyFlavUp/bdt","10J4M_heavyFlavUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":2,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{HF frac}","option":"l"}
     },
     "heavyFlavDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_heavyFlavDown/bdt","7J3M_heavyFlavDown/bdt","7J4M_heavyFlavDown/bdt","8J2M_heavyFlavDown/bdt","8J3M_heavyFlavDown/bdt","8J4M_heavyFlavDown/bdt","9J2M_heavyFlavDown/bdt","9J3M_heavyFlavDown/bdt","9J4M_heavyFlavDown/bdt","10J2M_heavyFlavDown/bdt","10J3M_heavyFlavDown/bdt","10J4M_heavyFlavDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":2,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{HF frac}","option":"l"}
     },
    
    "PUUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_PUUp/bdt","7J3M_PUUp/bdt","7J4M_PUUp/bdt","8J2M_PUUp/bdt","8J3M_PUUp/bdt","8J4M_PUUp/bdt","9J2M_PUUp/bdt","9J3M_PUUp/bdt","9J4M_PUUp/bdt","10J2M_PUUp/bdt","10J3M_PUUp/bdt","10J4M_PUUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":3,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{PU}","option":"l"}
     },
     "PUDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_PUDown/bdt","7J3M_PUDown/bdt","7J4M_PUDown/bdt","8J2M_PUDown/bdt","8J3M_PUDown/bdt","8J4M_PUDown/bdt","9J2M_PUDown/bdt","9J3M_PUDown/bdt","9J4M_PUDown/bdt","10J2M_PUDown/bdt","10J3M_PUDown/bdt","10J4M_PUDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":3,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{PU}","option":"l"}
     },
         
    "TTJets_PDFUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTJets_PDFUp/bdt","7J3M_TTJets_PDFUp/bdt","7J4M_TTJets_PDFUp/bdt","8J2M_TTJets_PDFUp/bdt","8J3M_TTJets_PDFUp/bdt","8J4M_TTJets_PDFUp/bdt","9J2M_TTJets_PDFUp/bdt","9J3M_TTJets_PDFUp/bdt","9J4M_TTJets_PDFUp/bdt","10J2M_TTJets_PDFUp/bdt","10J3M_TTJets_PDFUp/bdt","10J4M_TTJets_PDFUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{PDF}","option":"l"}
     },
     "TTJets_PDFDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTJets_PDFDown/bdt","7J3M_TTJets_PDFDown/bdt","7J4M_TTJets_PDFDown/bdt","8J2M_TTJets_PDFDown/bdt","8J3M_TTJets_PDFDown/bdt","8J4M_TTJets_PDFDown/bdt","9J2M_TTJets_PDFDown/bdt","9J3M_TTJets_PDFDown/bdt","9J4M_TTJets_PDFDown/bdt","10J2M_TTJets_PDFDown/bdt","10J3M_TTJets_PDFDown/bdt","10J4M_TTJets_PDFDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{PDF}","option":"l"}
     },
              
    "ttMEScaleUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_ttMEScaleUp/bdt","7J3M_ttMEScaleUp/bdt","7J4M_ttMEScaleUp/bdt","8J2M_ttMEScaleUp/bdt","8J3M_ttMEScaleUp/bdt","8J4M_ttMEScaleUp/bdt","9J2M_ttMEScaleUp/bdt","9J3M_ttMEScaleUp/bdt","9J4M_ttMEScaleUp/bdt","10J2M_ttMEScaleUp/bdt","10J3M_ttMEScaleUp/bdt","10J4M_ttMEScaleUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":5,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{ME scale}","option":"l"}
     },
     "ttMEScaleDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_ttMEScaleDown/bdt","7J3M_ttMEScaleDown/bdt","7J4M_ttMEScaleDown/bdt","8J2M_ttMEScaleDown/bdt","8J3M_ttMEScaleDown/bdt","8J4M_ttMEScaleDown/bdt","9J2M_ttMEScaleDown/bdt","9J3M_ttMEScaleDown/bdt","9J4M_ttMEScaleDown/bdt","10J2M_ttMEScaleDown/bdt","10J3M_ttMEScaleDown/bdt","10J4M_ttMEScaleDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":5,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{ME scale}","option":"l"}
     },
              
    "TTPTUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTPTUp/bdt","7J3M_TTPTUp/bdt","7J4M_TTPTUp/bdt","8J2M_TTPTUp/bdt","8J3M_TTPTUp/bdt","8J4M_TTPTUp/bdt","9J2M_TTPTUp/bdt","9J3M_TTPTUp/bdt","9J4M_TTPTUp/bdt","10J2M_TTPTUp/bdt","10J3M_TTPTUp/bdt","10J4M_TTPTUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":6,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{pT top}","option":"l"}
     },
     "TTPTDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTPTDown/bdt","7J3M_TTPTDown/bdt","7J4M_TTPTDown/bdt","8J2M_TTPTDown/bdt","8J3M_TTPTDown/bdt","8J4M_TTPTDown/bdt","9J2M_TTPTDown/bdt","9J3M_TTPTDown/bdt","9J4M_TTPTDown/bdt","10J2M_TTPTDown/bdt","10J3M_TTPTDown/bdt","10J4M_TTPTDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":6,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{pT top}","option":"l"}
     },
 },
 # ----------------------------------------
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
            "algorithm":"from_file_norm",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M/bdt","7J3M/bdt","7J4M/bdt","8J2M/bdt","8J3M/bdt","8J4M/bdt","9J2M/bdt","9J3M/bdt","9J4M/bdt","10J2M/bdt","10J3M/bdt","10J4M/bdt"],
         },
         "style":{"SetLineWidth":2},
         "legend_entry":{"name":"central", "option":"l"}
     },
     "TTISRUp":{
         "type":{         
            "algorithm":"from_file_norm",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTISRUp/bdt","7J3M_TTISRUp/bdt","7J4M_TTISRUp/bdt","8J2M_TTISRUp/bdt","8J3M_TTISRUp/bdt","8J4M_TTISRUp/bdt","9J2M_TTISRUp/bdt","9J3M_TTISRUp/bdt","9J4M_TTISRUp/bdt","10J2M_TTISRUp/bdt","10J3M_TTISRUp/bdt","10J4M_TTISRUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":2,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{ISR}","option":"l"}
     },
     "TTISRDown":{
         "type":{         
            "algorithm":"from_file_norm",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTISRDown/bdt","7J3M_TTISRDown/bdt","7J4M_TTISRDown/bdt","8J2M_TTISRDown/bdt","8J3M_TTISRDown/bdt","8J4M_TTISRDown/bdt","9J2M_TTISRDown/bdt","9J3M_TTISRDown/bdt","9J4M_TTISRDown/bdt","10J2M_TTISRDown/bdt","10J3M_TTISRDown/bdt","10J4M_TTISRDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":2,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{ISR}","option":"l"}
     },
    
    "TTFSRUp":{
         "type":{         
            "algorithm":"from_file_norm",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTFSRUp/bdt","7J3M_TTFSRUp/bdt","7J4M_TTFSRUp/bdt","8J2M_TTFSRUp/bdt","8J3M_TTFSRUp/bdt","8J4M_TTFSRUp/bdt","9J2M_TTFSRUp/bdt","9J3M_TTFSRUp/bdt","9J4M_TTFSRUp/bdt","10J2M_TTFSRUp/bdt","10J3M_TTFSRUp/bdt","10J4M_TTFSRUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":3,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{FSR}","option":"l"}
     },
     "TTFSRDown":{
         "type":{         
            "algorithm":"from_file_norm",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTFSRDown/bdt","7J3M_TTFSRDown/bdt","7J4M_TTFSRDown/bdt","8J2M_TTFSRDown/bdt","8J3M_TTFSRDown/bdt","8J4M_TTFSRDown/bdt","9J2M_TTFSRDown/bdt","9J3M_TTFSRDown/bdt","9J4M_TTFSRDown/bdt","10J2M_TTFSRDown/bdt","10J3M_TTFSRDown/bdt","10J4M_TTFSRDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":3,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{FSR}","option":"l"}
     },
         
    "TTUEUp":{
         "type":{         
            "algorithm":"from_file_norm",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTUEUp/bdt","7J3M_TTUEUp/bdt","7J4M_TTUEUp/bdt","8J2M_TTUEUp/bdt","8J3M_TTUEUp/bdt","8J4M_TTUEUp/bdt","9J2M_TTUEUp/bdt","9J3M_TTUEUp/bdt","9J4M_TTUEUp/bdt","10J2M_TTUEUp/bdt","10J3M_TTUEUp/bdt","10J4M_TTUEUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{UE}","option":"l"}
     },
     "TTUEDown":{
         "type":{         
            "algorithm":"from_file_norm",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTUEDown/bdt","7J3M_TTUEDown/bdt","7J4M_TTUEDown/bdt","8J2M_TTUEDown/bdt","8J3M_TTUEDown/bdt","8J4M_TTUEDown/bdt","9J2M_TTUEDown/bdt","9J3M_TTUEDown/bdt","9J4M_TTUEDown/bdt","10J2M_TTUEDown/bdt","10J3M_TTUEDown/bdt","10J4M_TTUEDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{UE}","option":"l"}
     },
              
    "TTJets_HDAMPUp":{
         "type":{         
            "algorithm":"from_file_norm",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTJets_HDAMPUp/bdt","7J3M_TTJets_HDAMPUp/bdt","7J4M_TTJets_HDAMPUp/bdt","8J2M_TTJets_HDAMPUp/bdt","8J3M_TTJets_HDAMPUp/bdt","8J4M_TTJets_HDAMPUp/bdt","9J2M_TTJets_HDAMPUp/bdt","9J3M_TTJets_HDAMPUp/bdt","9J4M_TTJets_HDAMPUp/bdt","10J2M_TTJets_HDAMPUp/bdt","10J3M_TTJets_HDAMPUp/bdt","10J4M_TTJets_HDAMPUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":5,"SetLineStyle":3},
         "legend_entry":{"name":"+#delta_{hDAMP}","option":"l"}
     },
     "TTJets_HDAMPDown":{
         "type":{         
            "algorithm":"from_file_norm",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.41_weightbugfix_v2//Hists_TT_CARDS.root",
            "subhistograms":["7J2M_TTJets_HDAMPDown/bdt","7J3M_TTJets_HDAMPDown/bdt","7J4M_TTJets_HDAMPDown/bdt","8J2M_TTJets_HDAMPDown/bdt","8J3M_TTJets_HDAMPDown/bdt","8J4M_TTJets_HDAMPDown/bdt","9J2M_TTJets_HDAMPDown/bdt","9J3M_TTJets_HDAMPDown/bdt","9J4M_TTJets_HDAMPDown/bdt","10J2M_TTJets_HDAMPDown/bdt","10J3M_TTJets_HDAMPDown/bdt","10J4M_TTJets_HDAMPDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":5,"SetLineStyle":2},
         "legend_entry":{"name":"-#delta_{hDAMP}","option":"l"}
     },

 },
}
