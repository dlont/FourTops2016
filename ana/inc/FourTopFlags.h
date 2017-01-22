#ifndef FOURTOPFLAGS_H
#define FOURTOPFLAGS_H

#include <string>
#include <boost/algorithm/string.hpp>  
#include <gflags/gflags.h>

DEFINE_string(dataset_name, "", "Dataset name");
DEFINE_string(dataset_title, "", "Dataset title");
DEFINE_int32(dataset_color,1,"Dataset color code");                             // Default: black
DEFINE_int32(dataset_linestyle,1,"Dataset line style");                         // Default: solid line
DEFINE_int32(dataset_linewidth,2,"Dataset line width");                         // Default: 2
DEFINE_double(dataset_norm_factor,1.,"Dataset normalisation factor");           //Default 1.
DEFINE_double(dataset_eq_lumi,1.,"Dataset equivalent luminosity");              //Default 1.
DEFINE_double(dataset_cross_section,1.,"Dataset cross section");                //Default 1.
DEFINE_double(dataset_preselection_eff,1.,"Dataset preselection efficiency");   //Default 1.
DEFINE_string(fourtops_channel, "NONE", "Decay channel identifier");
DEFINE_string(ls, "central", "Jet energy scale variation");           //Default central
DEFINE_string(fourtops_jer, "central", "Jet energy resolution variation");      //Default central
DEFINE_string(input_files, "", "List of input ROOT files to run over");
DEFINE_string(jobid, "XYZ", "Job id signature");                                //Default "XYZ"
DEFINE_int32(nevents, -1, "Number of events to run over");                      // Default: all

bool isJESDown() {
    auto flag = false;
    boost::algorithm::to_lower(FLAGS_fourtops_jes);
    if (FLAGS_fourtops_jes.find("down") != string::npos) flag = true;
    DLOG(INFO)<<"isJESDown flag "<<flag;
    return flag;
}

bool isJESUp() {
    auto flag = false;
    boost::algorithm::to_lower(FLAGS_fourtops_jes);
    if (FLAGS_fourtops_jes.find("up") != string::npos) flag = true;
    DLOG(INFO)<<"JESUp flag "<<flag;
    return flag;
}

bool isJERDown() {
    auto flag = false;
    boost::algorithm::to_lower(FLAGS_fourtops_jer);
    if (FLAGS_fourtops_jer.find("down") != string::npos) flag = true;
    DLOG(INFO)<<"isJERDown flag "<<flag;
    return flag;
}

bool isJERUp() {
    auto flag = false;
    boost::algorithm::to_lower(FLAGS_fourtops_jer);
    if (FLAGS_fourtops_jer.find("up") != string::npos) flag = true;
    DLOG(INFO)<<"isJERUp flag "<<flag;
    return flag;
}
#endif //FOURTOPFLAGS_H
