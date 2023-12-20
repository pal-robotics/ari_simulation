# Copyright (c) 2023 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from os import environ, pathsep

from ament_index_python.packages import get_package_prefix, get_package_share_directory

from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    SetEnvironmentVariable,
)
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_pal.include_utils import include_launch_py_description


def get_model_paths(packages_names):
    model_paths = ""
    for package_name in packages_names:
        if model_paths != "":
            model_paths += pathsep

        package_path = get_package_prefix(package_name)
        model_path = os.path.join(package_path, "share")

        model_paths += model_path

    return model_paths


def get_resource_paths(packages_names):
    resource_paths = ""
    for package_name in packages_names:
        if resource_paths != "":
            resource_paths += pathsep

        package_path = get_package_prefix(package_name)
        resource_paths += package_path

    return resource_paths


def generate_launch_description():

    # TODO: ari_2dnav
    # navigation_arg = DeclareLaunchArgument(
    #    "navigation",
    #    default_value="false",
    #    description="Specify if launching Navigation2",
    # )

    moveit_arg = DeclareLaunchArgument(
        "moveit", default_value="false", description="Specify if launching MoveIt2"
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(
                    get_package_share_directory("pal_gazebo_worlds"), "launch"
                ),
                "/pal_gazebo.launch.py",
            ]
        ),
    )

    ari_spawn = include_launch_py_description(
        "ari_gazebo", ["launch", "ari_spawn.launch.py"],
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    ari_bringup = include_launch_py_description(
        "ari_bringup", ["launch", "ari_bringup.launch.py"],
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # TODO
    # navigation = include_launch_py_description(
    #    "ari_2dnav",
    #    ["launch", "ari_sim_nav_bringup.launch.py"],
    #    condition=IfCondition(LaunchConfiguration("navigation")),
    # )

    move_group = include_launch_py_description(
        "ari_moveit_config",
        ["launch", "move_group.launch.py"],
        launch_arguments={'use_sim_time': 'true'}.items(),
        condition=IfCondition(LaunchConfiguration("moveit")),
    )

    # @TODO: review pal_gazebo
    # @TODO: simulation_ari_bringup?
    # @TODO: pal_pcl_points_throttle_and_filter

    packages = [
        "ari_description",
    ]
    model_path = get_model_paths(packages)
    resource_path = get_resource_paths(packages)

    if "GAZEBO_MODEL_PATH" in environ:
        model_path += pathsep + environ["GAZEBO_MODEL_PATH"]

    if "GAZEBO_RESOURCE_PATH" in environ:
        resource_path += pathsep + environ["GAZEBO_RESOURCE_PATH"]

    # Create the launch description and populate
    ld = LaunchDescription()

    ld.add_action(SetEnvironmentVariable("GAZEBO_MODEL_PATH", model_path))
    # Using this prevents shared library from being found
    # ld.add_action(SetEnvironmentVariable('GAZEBO_RESOURCE_PATH', ari_resource_path))

    ld.add_action(gazebo)
    ld.add_action(ari_spawn)
    ld.add_action(ari_bringup)

    # ld.add_action(navigation_arg)
    # ld.add_action(navigation)

    ld.add_action(moveit_arg)
    ld.add_action(move_group)

    return ld
