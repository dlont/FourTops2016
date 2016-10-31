execute_process(COMMAND root-config --cflags OUTPUT_VARIABLE CMAKE_CXX_FLAGS_TEMP)
execute_process(COMMAND root-config --libs OUTPUT_VARIABLE CMAKE_LD_FLAGS_TEMP)
string(STRIP ${CMAKE_CXX_FLAGS_TEMP} CMAKE_CXX_FLAGS)
string(STRIP ${CMAKE_LD_FLAGS_TEMP} CMAKE_LD_FLAGS)

set(CMAKE_CXX_COMPILER "g++")

# include TopBrussels SingleLep header search path
include_directories(${TopBrussels_SOURCE_DIR})				# TopAnalysisBase/interface TopTreeProducer/interface
include_directories(${TopBrussels_SOURCE_DIR}/FourTops2016/SingleLepAnalysis/interface)		# SingleLep/interface/
include_directories(${TopBrussels_SOURCE_DIR}/FourTops2016/ana/inc)

# add FourTopSingleLep lib search path
link_directories(${TopBrussels_SOURCE_DIR}/FourTops2016/SingleLepAnalysis/src)

# add TopTreeAna80 TopTreeAnaContent80 lib search path
link_directories(~/lib)

# define output target
#add_executable(FourTops FourTops.cc)
add_executable(FourTops FourTop_EventSelection_SingleLepton_Run2_Local.cc)

# link against root and FourTopSingleLep TopTreeAna80 TopTreeAnaContent80
target_link_libraries(FourTops PUBLIC FourTopSingleLep TopTreeAna80 TopTreeAnaContent80 PRIVATE ${CMAKE_LD_FLAGS})
install(TARGETS FourTops DESTINATION ~/CMSSW_8_0_21/src/TopBrussels/FourTops2016/)
