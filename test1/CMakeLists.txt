cmake_minimum_required(VERSION 3.13)
project(test1 CXX)

set(EIGEN3_DIR /usr/include/eigen3)
include_directories(${EIGEN3_DIR})

find_package(GTSAMCMakeTools)
find_package(GTSAM REQUIRED)
find_package(Eigen3 REQUIRED)

add_executable(test1 test1.cpp)
target_link_libraries(test1
    gtsam
)