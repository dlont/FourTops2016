
#include "BTagSF.h"

#include "TopTreeAnalysisBase/Tools/interface/BTagCalibrationStandalone.h"
#include "TopTreeProducer/interface/TRootPFJet.h"

#include "TString.h"

#include <vector>
#include <cassert>

BTagSF::BTagSF(const BTagCalibration* calib):
    _calibration(calib) {
        initSysReaders();
}
    
BTagSF::~BTagSF(){
    delete _reader;
    delete _reader_JESUp;
    delete _reader_JESDown;
    delete _reader_LFUp;
    delete _reader_LFDown;
    delete _reader_HFUp;
    delete _reader_HFDown;
    delete _reader_HFStats1Up;
    delete _reader_HFStats1Down;
    delete _reader_HFStats2Up;
    delete _reader_HFStats2Down;
    delete _reader_LFStats1Up;
    delete _reader_LFStats1Down;
    delete _reader_LFStats2Up;
    delete _reader_LFStats2Down;
    delete _reader_CFErr1Up;
    delete _reader_CFErr1Down;
    delete _reader_CFErr2Up;
    delete _reader_CFErr2Down;
}
    
std::map<std::string,double> BTagSF::getSFs(const std::vector<TopTree::TRootPFJet*>& jets){
    std::map<string,double> w;
    
    // Reshaping weights
    std::vector<TString> systematics =  {
        "nominal",
        "JESUp", "JESDown",
        "LFUp", "LFDown",
        "HFUp", "HFDown",
        "CSVHFStats1Up", "CSVHFStats1Down",
        "CSVHFStats2Up", "CSVHFStats2Down",
        "CSVLFStats1Up", "CSVLFStats1Down",
        "CSVLFStats2Up", "CSVLFStats2Down",
        "CSVCFErr1Up", "CSVCFErr1Down",
        "CSVCFErr2Up", "CSVCFErr2Down"
    };
    
    for ( auto sys_name: systematics ) {
        double event_wgt_csv = 1.0;
        for (int iJet = 0; iJet<int(jets.size()); iJet++) {
            double pt = jets[iJet]->Pt();
            double eta = jets[iJet]->Eta();

            if (!(pt > 20. && fabs(eta) < 2.4)) continue;

            double csv = jets[iJet]->btag_combinedInclusiveSecondaryVertexV2BJetTags();
            if (csv < 0.0) csv = -0.05;
            if (csv > 1.0) csv = 1.0;

            int flavor = std::abs(jets[iJet]->hadronFlavour());

            if (pt > 1000) pt = 999.;

            bool isBFlav = false;
            bool isCFlav = false;
            bool isLFlav = false;
            if (abs(flavor) == 5) isBFlav = true;
            else if (abs(flavor) == 4) isCFlav = true;
            else isLFlav = true;

            double my_jet_sf = 1.;

            BTagEntry::JetFlavor jf = BTagEntry::FLAV_UDSG;
            if (isBFlav) jf = BTagEntry::FLAV_B;
            else if (isCFlav) jf = BTagEntry::FLAV_C;
            else jf = BTagEntry::FLAV_UDSG;

            if (sys_name.Contains("JESUp") && !isCFlav) my_jet_sf = _reader_JESUp->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("JESDown") && !isCFlav) my_jet_sf = _reader_JESDown->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("LFUp") && isBFlav) my_jet_sf = _reader_LFUp->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("LFDown") && isBFlav) my_jet_sf = _reader_LFDown->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("HFUp") && isLFlav) my_jet_sf = _reader_HFUp->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("HFDown") && isLFlav) my_jet_sf = _reader_HFDown->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("CSVHFStats1Up") && isBFlav) my_jet_sf = _reader_HFStats1Up->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("CSVHFStats1Down") && isBFlav) my_jet_sf = _reader_HFStats1Down->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("CSVHFStats2Up") && isBFlav) my_jet_sf = _reader_HFStats2Up->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("CSVHFStats2Down") && isBFlav) my_jet_sf = _reader_HFStats2Down->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("CSVLFStats1Up") && isLFlav) my_jet_sf = _reader_LFStats1Up->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("CSVLFStats1Down") && isLFlav) my_jet_sf = _reader_LFStats1Down->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("CSVLFStats2Up") && isLFlav) my_jet_sf = _reader_LFStats2Up->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("CSVLFStats2Down") && isLFlav) my_jet_sf = _reader_LFStats2Down->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("CSVCFErr1Up") && isCFlav) my_jet_sf = _reader_CFErr1Up->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("CSVCFErr1Down") && isCFlav) my_jet_sf = _reader_CFErr1Down->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("CSVCFErr2Up") && isCFlav) my_jet_sf = _reader_CFErr2Up->eval(jf, eta, pt, csv);
            else if (sys_name.Contains("CSVCFErr2Down") && isCFlav) my_jet_sf = _reader_CFErr2Down->eval(jf, eta, pt, csv);
            else my_jet_sf = _reader->eval(jf, eta, pt, csv);

            assert(my_jet_sf > 0.);
            event_wgt_csv *= my_jet_sf;
        }
        w[sys_name.Data()] = event_wgt_csv;
    }
    
    return w;
}

void BTagSF::initSysReaders() {
    _reader= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "central"); // systematics type

    // JESUp
    _reader_JESUp= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "up_jes"); // systematics type
    // JESDown
    _reader_JESDown= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "down_jes"); // systematics type

    // LFUp
    _reader_LFUp= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "up_lf"); // systematics type
    // LFDown
    _reader_LFDown= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "down_lf"); // systematics type

    // HFUp
    _reader_HFUp= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "up_hf"); // systematics type
    // HFDown
    _reader_HFDown= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "down_hf"); // systematics type

    // HFStats1Up
    _reader_HFStats1Up= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "up_hfstats1"); // systematics type
    // HFStats1Down
    _reader_HFStats1Down= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "down_hfstats1"); // systematics type

    // HFStats2Up
    _reader_HFStats2Up= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "up_hfstats2"); // systematics type
    // HFStats2Down
    _reader_HFStats2Down= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "down_hfstats2"); // systematics type

    // LFStats1Up
    _reader_LFStats1Up= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "up_lfstats1"); // systematics type
    // LFStats1Down
    _reader_LFStats1Down= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "down_lfstats1"); // systematics type

    // LFStats2Up
    _reader_LFStats2Up= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "up_lfstats2"); // systematics type
    // LFStats2Down
    _reader_LFStats2Down= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "down_lfstats2"); // systematics type

    // CFErr1Up
    _reader_CFErr1Up= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "up_cferr1"); // systematics type
    // CFErr1Down
    _reader_CFErr1Down= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "down_cferr1"); // systematics type

    // CFErr2Up
    _reader_CFErr2Up= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "up_cferr2"); // systematics type
    // CFErr2Down
    _reader_CFErr2Down= new BTagCalibrationReader(_calibration, // calibration instance
            BTagEntry::OP_RESHAPING, // operating point
            "iterativefit", // measurement type
            "down_cferr2"); // systematics type
}
