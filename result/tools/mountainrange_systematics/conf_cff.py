config={'annotation': 'Example annotation',
 'command': 'MVC_template.py -b -c conf_cff.py',
 'latex_main': 'latex/report.tex',
 'mode': 'plots',
 
 'canvas':['canvas_btag','canvas_jec'],
 'canvas_btag':{
     "name":"canvas_btag",
     "type":"3x1_ratio_leg_bottom",
     "templates":["central","up","down"],
     "ratios":{
         "option":"normalized_difference",
         "templates":["up/central","down/central"]
     },
     "legend":{
       "header":"b-tagging",
       "pos":[0.5,0.8,0.9,0.9],
       "entries":["central","up","down"]
     },
     "central":{
         "type":{         
            "algorithm":"from_file",
            "infile":"",
            "subhistograms":["10J2M/bdt","10J3M/bdt","10J4M/bdt"],
         },
         "style":{},
         "legend_entry":{"option":"l"}
     },
     "up":{
         "type":{         
            "algorithm":"from_file",
            "infile":"",
            "subhistograms":["10J2M/bdt","10J3M/bdt","10J4M/bdt"],
         },
         "style":{},
         "legend_entry":{"option":"l"}
     },
     "down":{
         "type":{         
            "algorithm":"from_file",
            "infile":"",
            "subhistograms":["10J2M/bdt","10J3M/bdt","10J4M/bdt"],
         },
         "style":{},
         "legend_entry":{"option":"l"}
     },
 },
 'canvas_jec':{}
}