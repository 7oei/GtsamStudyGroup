cmake_minimum_required(VERSION 3.13)
project(tutorial3 CXX)

set(EIGEN3_DIR /usr/include/eigen3)
include_directories(${EIGEN3_DIR})

find_package(GTSAMCMakeTools)
find_package(GTSAM REQUIRED)
find_package(Eigen3 REQUIRED)

add_executable(tutorial3 tutorial3.cpp)
target_link_libraries(tutorial3
    gtsam
)