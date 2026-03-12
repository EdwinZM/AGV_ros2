import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node

import xacro

def generate_launch_description():

    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('AGV_ros2'), 'launch', 'robot.launch.py'
        )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

                       
    
    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "diff_cont",
            '--controller-ros-args',
            '-r /diff_cont/cmd_vel:=/cmd_vel'
        ],
    )

    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_broad"],
    )

    
    controller_params_file = os.path.join(get_package_share_directory('AGV_ros2'),'config','my_controllers.yaml')

    controller_manager = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[controller_params_file],
    )

    twist_mux_config = os.path.join(get_package_share_directory('AGV_ros2'),
        'config', 'twist_mux.yaml')
    twist_mux = Node(
        package='twist_mux',
        executable='twist_mux',
        output='screen',
        remappings={('/cmd_vel_out', '/cmd_vel')},
        parameters=[
            {'use_sim_time': False},
            twist_mux_config])


    # Launch them all!
    return LaunchDescription([
        rsp,
        controller_manager,
        diff_drive_spawner,
        joint_broad_spawner,
        twist_mux,
    ])