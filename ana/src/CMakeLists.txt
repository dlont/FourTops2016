execute_process(COMMAND root-config --cflags OUTPUT_VARIABLE CMAKE_CXX_FLAGS_TEMP)
execute_process(COMMAND root-config --libs OUTPUT_VARIABLE CMAKE_LD_FLAGS_TEMP)
string(STRIP ${CMAKE_CXX_FLAGS_TEMP} CMAKE_CXX_FLAGS)
string(STRIP ${CMAKE_LD_FLAGS_TEMP} CMAKE_LD_FLAGS)

set(CMAKE_CXX_COMPILER "g++")
set(CMAKE_LD_FLAGS_TEMP "${CMAKE_LD_FLAGS_TEMP} -lTMVA")

# get git meta information
configure_file(
git_meta_info.cmake.in
git_meta_info.cmake
)


# include TopBrussels SingleLep header search path
include_directories(${TopBrussels_SOURCE_DIR})				# TopAnalysisBase/interface TopTreeProducer/interface
include_directories(${TopBrussels_SOURCE_DIR}/FourTops2016/SingleLepAnalysis/interface)		# SingleLep/interface/
include_directories(${TopBrussels_SOURCE_DIR}/FourTops2016/ana/inc)
include_directories(${TopBrussels_SOURCE_DIR}/FourTops2016/glog/include)
include_directories(${TopBrussels_SOURCE_DIR}/FourTops2016/gflags/include)

# include Python.h paths
include_directories(/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/python/2.7.11-ikhhed2/include/python2.7)
link_directories(/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/python/2.7.11-ikhhed2/lib)


# add FourTopSingleLep lib search path
link_directories(${TopBrussels_SOURCE_DIR}/FourTops2016/glog/lib)
link_directories(${TopBrussels_SOURCE_DIR}/FourTops2016/gflags/lib)

# add FourTopSingleLep lib search path
link_directories(${TopBrussels_SOURCE_DIR}/FourTops2016/SingleLepAnalysis/src)

# add TopTreeAna80 TopTreeAnaContent80 lib search path
link_directories(~/lib)

# define output target
set(EXECFILE "FourTops")
#add_executable(${EXECFILE} FourTops.cc)
add_executable(${EXECFILE} FourTop_EventSelection_SingleLepton_Run2_Local.cc BTagSF.cc VecTLorentzVector.cpp)
#add_executable(${EXECFILE} FourTop_EventSelection_SingleLepton_Run2_Local_sync.cc BTagSF.cc)

# link against root and FourTopSingleLep TopTreeAna80 TopTreeAnaContent80
target_link_libraries(${EXECFILE} PUBLIC glog gflags FourTopSingleLep TopTreeAna80 TopTreeAnaContent80 TMVA python2.7 PRIVATE ${CMAKE_LD_FLAGS})
install(TARGETS ${EXECFILE} DESTINATION ${CMAKE_INSTALL_PREFIX})
add_custom_command(TARGET ${EXECFILE} PRE_BUILD COMMAND cmake -P git_meta_info.cmake)
set(ROOT_VECTLORENTZVEC_LINKDEF "${TopBrussels_SOURCE_DIR}/FourTops2016/ana/inc/VecTLorentzVector_LinkDef.h")
add_custom_command(OUTPUT ${TopBrussels_SOURCE_DIR}/FourTops2016/ana/src/VecTLorentzVector.cpp DEPENDS ${ROOT_VECTLORENTZVEC_LINKDEF} 
 COMMAND rootcint -f ${TopBrussels_SOURCE_DIR}/FourTops2016/ana/src/VecTLorentzVector.cpp -c -p TLorentzVector.h ${ROOT_VECTLORENTZVEC_LINKDEF}
 COMMENT "Generating dictionary")
