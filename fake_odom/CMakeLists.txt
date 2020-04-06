cmake_minimum_required(VERSION 2.8.3)
project(fake_odom)## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS 

roscpp 
std_msgs
tf
nav_msgs

)## Declare ROS messages and services
catkin_package(
#  INCLUDE_DIRS include      #only include if we have headers, etc
#  LIBRARIES test_package
#  CATKIN_DEPENDS roscpp
#  DEPENDS system_lib
)

# Add the dependencies from catkin i.e ( ${catkin_EXPORTED_TARGETS}), and from your package i.e (${${PROJECT_NAME}_EXPORTED_TARGETS})
#add_dependencies(listener ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})


include_directories(include)
include_directories(SYSTEM ${catkin_INCLUDE_DIRS})

add_executable(ground_truth_pub src/ground_truth_pub.cpp)
target_link_libraries(ground_truth_pub ${catkin_LIBRARIES})

install(TARGETS ground_truth_pub
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)



