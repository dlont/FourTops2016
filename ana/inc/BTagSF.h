#ifndef BTagSF_H
#define BTagSF_H

#include <vector>
#include <map>
#include <string>

#include "TopTreeProducer/interface/TRootPFJet.h"

#include "TopTreeAnalysisBase/Tools/interface/BTagCalibrationStandalone.h"

class BTagCalibration;
class BTagCalibrationReader;

class BTagSF {
public:
    BTagSF(const BTagCalibration* calib);
    ~BTagSF();
    std::map<std::string,double> getSFs(const std::vector<TopTree::TRootPFJet*>&);
    
private:
    void initSysReaders();
    
private:
    const BTagCalibration* _calibration = nullptr;
    BTagCalibrationReader* _reader = nullptr;
    BTagCalibrationReader* _reader_JESUp = nullptr;
    BTagCalibrationReader* _reader_JESDown = nullptr;
    BTagCalibrationReader* _reader_LFUp = nullptr;
    BTagCalibrationReader* _reader_LFDown = nullptr;
    BTagCalibrationReader* _reader_HFUp = nullptr;
    BTagCalibrationReader* _reader_HFDown = nullptr;
    BTagCalibrationReader* _reader_HFStats1Up = nullptr;
    BTagCalibrationReader* _reader_HFStats1Down = nullptr;
    BTagCalibrationReader* _reader_HFStats2Up = nullptr;
    BTagCalibrationReader* _reader_HFStats2Down = nullptr;
    BTagCalibrationReader* _reader_LFStats1Up = nullptr;
    BTagCalibrationReader* _reader_LFStats1Down = nullptr;
    BTagCalibrationReader* _reader_LFStats2Up = nullptr;
    BTagCalibrationReader* _reader_LFStats2Down = nullptr;
    BTagCalibrationReader* _reader_CFErr1Up = nullptr;
    BTagCalibrationReader* _reader_CFErr1Down = nullptr;
    BTagCalibrationReader* _reader_CFErr2Up = nullptr;
    BTagCalibrationReader* _reader_CFErr2Down = nullptr;
    bool _isCSVRS = true;
};
#endif //BTagSF_H
