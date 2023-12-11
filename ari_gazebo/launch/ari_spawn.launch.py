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

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():

    model_name = DeclareLaunchArgument(
        "model_name", default_value="ari", description="Gazebo model name"
    )

    ari_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-topic",
            "robot_description",
            "-entity",
            LaunchConfiguration("model_name"),
            # LaunchConfiguration('gzpose'),
        ],
        output="screen",
    )

    # Create the launch description and populate
    ld = LaunchDescription()

    # ld.add_action(gz_pose)
    ld.add_action(model_name)
    ld.add_action(ari_entity)

    return ld
