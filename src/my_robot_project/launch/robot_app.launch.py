import os
from launch import LaunchDescription
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Znajdujemy pakiet z opisem UR (ten który sklonowałeś)
    ur_description_pkg = FindPackageShare("ur_description")
    
    # Ścieżka do pliku Xacro UR5
    urdf_file = PathJoinSubstitution([ur_description_pkg, "urdf", "ur.urdf.xacro"])

    # Generowanie opisu robota komendą xacro
    # Parametry: name=ur5, ur_type=ur5
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
        # 1. Robot State Publisher (z prawdziwym modelem UR5)
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            output="screen",
            parameters=[robot_description],
        ),
        
        # 2. RViz2
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            output="screen",
        ),

        # 3. Twój symulator kamery
        Node(
            package='my_robot_project',
            executable='camera_sim',
            name='camera_simulator',
        ),

        # 4. Twój kontroler UR5
        Node(
            package='my_robot_project',
            executable='controller',
            name='ur5_controller',
            output="screen",
        )
    ])
