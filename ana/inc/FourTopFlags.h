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
DEFINE_string(fourtops_jes, "central", "Jet energy scale variation");           //Default central
DEFINE_string(fourtops_jer, "central", "Jet energy resolution variation");      //Default central
DEFINE_string(fourtops_eleid, "VID", "Electron ID type (VID,CUT)");     	//Default VID
DEFINE_bool(fourtops_btagregular,true,"Regular btagging SF");
DEFINE_bool(fourtops_btagcsvrs,true,"CSV reshaping btagging SF");
DEFINE_bool(fourtops_toprew,true,"Apply top reweighting");                      //Default apply
DEFINE_bool(is_local_output,false,"Store outout in /user space or at /scratch/$PBS_JOBID");      //Default /scratch/$PBS_JOBID
DEFINE_string(input_files, "", "List of input ROOT files to run over");
DEFINE_string(jobid, "XYZ", "Job id signature");                                //Default "XYZ"
DEFINE_int32(nevents, -1, "Number of events to run over");                      // Default: all

bool isJESDown() {
    auto flag = false;
    auto temp_flag = FLAGS_fourtops_jes;
    boost::algorithm::to_lower(temp_flag);
    if (FLAGS_fourtops_jes.find("down") != string::npos) flag = true;
    DLOG(INFO)<<"isJESDown flag "<<flag;
    return flag;
}

bool isJESUp() {
    auto flag = false;
    auto temp_flag = FLAGS_fourtops_jes;
    boost::algorithm::to_lower(temp_flag);
    if (FLAGS_fourtops_jes.find("up") != string::npos) flag = true;
    DLOG(INFO)<<"JESUp flag "<<flag;
    return flag;
}

std::string JESSource() {
    std::string source = "Total";
    const std::array<const std::string,19> possible_options = 
	{
	"central",
	"Total_up",		"Total_down",
	"SubTotalPileUp_up", 	"SubTotalPileUp_down",
	"SubTotalRelative_up", 	"SubTotalRelative_down", 
	"SubTotalPt_up", 	"SubTotalPt_down",
	"SubTotalScale_up", 	"SubTotalScale_down",
    "SubTotalTimePtEta_up", "SubTotalTimePtEta_down",
	"SubTotalFlavor_up",	"SubTotalFlavor_down",
	};

    if ( std::find( std::begin(possible_options), std::end(possible_options), FLAGS_fourtops_jes ) != std::end(possible_options) ) {
   	return FLAGS_fourtops_jes;
    } else {
	throw std::runtime_error("JES option NOT found: "+FLAGS_fourtops_jes);
    }

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


enum struct ElectronID {VIDbased=100, CUTbased=200};
std::ostream& operator<<(std::ostream& os, ElectronID id)
{
        return os << static_cast<int>(id);
}

ElectronID electronID() {
    auto flag = ElectronID::VIDbased;
    if (FLAGS_fourtops_eleid.find("VID") != string::npos) flag = ElectronID::VIDbased;
    if (FLAGS_fourtops_eleid.find("CUT") != string::npos) flag = ElectronID::CUTbased;
    if (flag==ElectronID::CUTbased) DLOG(INFO)<<"ElecronID: "<< "CUT based" << std::endl;
    else DLOG(INFO)<<"ElecronID: "<< "VID based" << std::endl;
    return flag;
}

#endif //FOURTOPFLAGS_H
