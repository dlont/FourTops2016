cmake_minimum_required (VERSION 2.6)
project(MVATrainer)

IF(IS_DIRECTORY ${TopBrussels_SOURCE_DIR})
	MESSAGE(STATUS "TopBrussels was set to: ${TopBrussels_SOURCE_DIR}")
ELSE()
	MESSAGE(FATAL_ERROR "TopBrussels was not found in: ${TopBrussels_SOURCE_DIR}")
ENDIF()

execute_process(COMMAND root-config --cflags OUTPUT_VARIABLE CMAKE_CXX_FLAGS_TEMP)
execute_process(COMMAND root-config --libs OUTPUT_VARIABLE CMAKE_LD_FLAGS_TEMP)
string(STRIP ${CMAKE_CXX_FLAGS_TEMP} CMAKE_CXX_FLAGS)
string(STRIP ${CMAKE_LD_FLAGS_TEMP} CMAKE_LD_FLAGS)

SET(CMAKE_CXX_FLAGS_DEBUG   "-ggdb3 -gdwarf-3 -O0 -fno-inline" CACHE STRING "Debug options." FORCE   )

# Find c++ boost lib
FIND_PACKAGE(Boost COMPONENTS program_options REQUIRED)
include_directories(${Boost_INCLUDE_DIRS})

# Add ROOT TMVA lib
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -lTMVA")

set(CMAKE_CXX_COMPILER "g++")

# include TopBrussels SingleLep header search path
# include_directories(${TopBrussels_SOURCE_DIR})                  #TopAnalysisBase/interface TopTreeProducer/interface

# add TopTreeAna80 TopTreeAnaContent80 lib search path
link_directories(~/lib)

# define output target
add_executable(MVATrainer MVATrainer.cpp BookMethods.cpp)

# link against root and TopTreeAna80 TopTreeAnaContent80
target_link_libraries(MVATrainer PRIVATE ${CMAKE_LD_FLAGS})
# link against boost
target_link_libraries(MVATrainer ${Boost_LIBRARIES})

install(TARGETS MVATrainer DESTINATION /user/dlontkov/t2016/MVA/tttt_ttz_tth_tt_split_training)
