import os
from launch import LaunchDescription
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
   
    ur_description_pkg = FindPackageShare("ur_description")
    
    
    urdf_file = PathJoinSubstitution([ur_description_pkg, "urdf", "ur.urdf.xacro"])

   
    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            urdf_file,
            " ",
            "name:=", "ur5",
            " ",
            "ur_type:=", "ur5",
        ]
    )
    
    robot_description = {"robot_description": robot_description_content}

    return LaunchDescription([
        
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            output="screen",
            parameters=[robot_description],
        ),
        
        #  RViz2
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            output="screen",
        ),

        #  symulator kamery
        Node(
            package='my_robot_project',
            executable='camera_sim',
            name='camera_simulator',
        ),

        # kontroler UR5
        Node(
            package='my_robot_project',
            executable='controller',
            name='ur5_controller',
            output="screen",
        )
    ])
