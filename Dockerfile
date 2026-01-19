
FROM ros:jazzy


ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-opencv \
    ros-jazzy-rviz2 \
    ros-jazzy-xacro \
    ros-jazzy-robot-state-publisher \
    ros-jazzy-joint-state-publisher \
    ros-jazzy-cv-bridge \
    git \
    libgl1 \
    libgl1-mesa-dri \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /root/ros2_ws/src


RUN git clone -b ros2 https://github.com/UniversalRobots/Universal_Robots_ROS2_Description.git


COPY src/my_robot_project ./my_robot_project


WORKDIR /root/ros2_ws
RUN . /opt/ros/jazzy/setup.sh && colcon build

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["ros2", "launch", "my_robot_project", "robot_app.launch.py"]
