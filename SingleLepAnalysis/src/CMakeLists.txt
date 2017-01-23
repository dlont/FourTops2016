execute_process(COMMAND root-config --cflags OUTPUT_VARIABLE CMAKE_CXX_FLAGS_TEMP)
execute_process(COMMAND root-config --libs OUTPUT_VARIABLE CMAKE_LD_FLAGS_TEMP)
string(STRIP ${CMAKE_CXX_FLAGS_TEMP} CMAKE_CXX_FLAGS)
string(STRIP ${CMAKE_LD_FLAGS_TEMP} CMAKE_LD_FLAGS)

set(CMAKE_CXX_COMPILER "g++")

message( "CMAKE_C_FLAGS: ${CMAKE_CXX_FLAGS}" )
message( "CMAKE_LD_FLAGS: ${CMAKE_LD_FLAGS}" )

#add_definitions(-DNOTRIGMC)

# include TopBrussels header search path
include_directories(${TopBrussels_SOURCE_DIR})
include_directories(${TopBrussels_SOURCE_DIR}/FourTops2016)

# add TopTreeAna80 TopTreeAnaContent80 lib search path
link_directories(~/lib)

# include TopBrussels header search path
include_directories(${FourTops2016_SOURCE_DIR}/SingleLepAnalysis/interface)
#message(STATUS "lib SingleLepton dir: ${FourTops_SOURCE_DIR}")

# define output target
add_library(FourTopSingleLep SHARED CutsTable.cc EventBDT.cc HadronicTopReco.cc Trigger.cc Zpeak.cc MultiTopEvent.cpp)

# link against root and TopTreeAna80 TopTreeAnaContent80
target_link_libraries(FourTopSingleLep PUBLIC TopTreeAna80 TopTreeAnaContent80 PRIVATE ${CMAKE_LD_FLAGS})
install(TARGETS FourTopSingleLep DESTINATION ~/lib)

