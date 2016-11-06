cmake_minimum_required (VERSION 2.6)
project(FourTops2016)
subdirs(SingleLepAnalysis ana)

IF(IS_DIRECTORY ${TopBrussels_SOURCE_DIR})
	MESSAGE(STATUS "TopBrussels was set to: ${TopBrussels_SOURCE_DIR}")
ELSE()
	MESSAGE(FATAL_ERROR "TopBrussels was not found in: ${TopBrussels_SOURCE_DIR}")
ENDIF()

SET(CMAKE_CXX_FLAGS_DEBUG   "-g3 -ggdb -O0" CACHE STRING "Debug options." FORCE   )
