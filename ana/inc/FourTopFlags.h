#ifndef FOURTOPFLAGS_H
#define FOURTOPFLAGS_H
#include <gflags/gflags.h>

//DEFINE_int32(, true, "Include 'advanced' options in the menu listing");
DEFINE_string(dataset_name, "", "Dataset name");
DEFINE_string(dataset_title, "", "Dataset title");
DEFINE_int32(dataset_color,1,"Dataset color code");                             // Default: black
DEFINE_int32(dataset_linestyle,1,"Dataset line style");                         // Default: solid line
DEFINE_int32(dataset_linewidth,2,"Dataset line width");                         // Default: 2
DEFINE_double(dataset_norm_factor,1.,"Dataset normalisation factor");           //Default 1.
DEFINE_double(dataset_eq_lumi,1.,"Dataset equivalent luminosity");              //Default 1.
DEFINE_double(dataset_cross_section,1.,"Dataset cross section");              //Default 1.
DEFINE_double(dataset_preselection_eff,1.,"Dataset preselection efficiency");   //Default 1.
DEFINE_string(fourtops_channel, "NONE", "Decay channel identifier");            
DEFINE_string(input_files, "", "List of input ROOT files to run over");            
DEFINE_string(jobid,"XYZ","Job id signature");                                  //Default "XYZ"
#endif //FOURTOPFLAGS_H
