config={'annotation': 'Muon channel. Comparison of MC templates with HF and PDF systematic variations.',
 'command': 'MVC_template.py -b -c conf_cff.py',
 'latex_main': 'latex/report.tex',
 'mode': 'plots',
 'canvas':['canvas_shape_other'],
#  --------------------------------------------
# ----------------------------------------
 'canvas_shape_other':{
    "name":"canvas_shape_other",
     "type":"3x1_ratio_leg_bottom",
     "templates":["heavyFlavUp",     "heavyFlavDown",
                  "TTJets_PDFUp",    "TTJets_PDFDown"],
     "ratios":{
         "option":"normalized_difference",
         "templates":["up/central","down/central"],
         "yrange":[-0.3,0.3]
     },
     "legend":{
       "header":"SHAPE other components",
       "pos":[0.5,0.8,0.9,0.9],
       "entries":["heavyFlavUp","TTJets_PDFUp",
                  "heavyFlavDown","TTJets_PDFDown"]
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
         
    "TTJets_PDFUp":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.42_weightbugfix_v3//Hists_TT_PDF.root",
            "subhistograms":["7J2M_TTJets_PDFUp/bdt","7J3M_TTJets_PDFUp/bdt","7J4M_TTJets_PDFUp/bdt","8J2M_TTJets_PDFUp/bdt","8J3M_TTJets_PDFUp/bdt","8J4M_TTJets_PDFUp/bdt","9J2M_TTJets_PDFUp/bdt","9J3M_TTJets_PDFUp/bdt","9J4M_TTJets_PDFUp/bdt","10J2M_TTJets_PDFUp/bdt","10J3M_TTJets_PDFUp/bdt","10J4M_TTJets_PDFUp/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":3},
         "style_ratio":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":3,"Scale":1.},
         "legend_entry":{"name":"+#delta_{PDF} (shape+norm)","option":"l"}
     },
     "TTJets_PDFDown":{
         "type":{         
            "algorithm":"from_file",
            "infile":"/user/dlontkov/t2016/result/final_unblinding/filtered_samples/plots_mu_filt_custombinning_10J4M_JERSummer16_v0.0.42_weightbugfix_v3//Hists_TT_PDF.root",
            "subhistograms":["7J2M_TTJets_PDFDown/bdt","7J3M_TTJets_PDFDown/bdt","7J4M_TTJets_PDFDown/bdt","8J2M_TTJets_PDFDown/bdt","8J3M_TTJets_PDFDown/bdt","8J4M_TTJets_PDFDown/bdt","9J2M_TTJets_PDFDown/bdt","9J3M_TTJets_PDFDown/bdt","9J4M_TTJets_PDFDown/bdt","10J2M_TTJets_PDFDown/bdt","10J3M_TTJets_PDFDown/bdt","10J4M_TTJets_PDFDown/bdt"],
         },
         "style":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":2},
         "style_ratio":{"SetLineWidth":2,"SetLineColor":4,"SetLineStyle":2,"Scale":1.},
         "legend_entry":{"name":"-#delta_{PDF} (shape+norm)","option":"l"}
     },
 },
 # ----------------------------------------
}
