cmake_minimum_required(VERSION 2.8.3)
project(ari_2dnav_gazebo)

find_package(catkin REQUIRED)

catkin_package()
include_directories(SYSTEM ${catkin_INCLUDE_DIRS})
foreach(dir launch)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
