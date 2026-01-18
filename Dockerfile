# Używamy oficjalnego obrazu ROS 2 Jazzy
FROM ros:jazzy

# Ustawiamy zmienną, aby instalacje nie pytały o strefę czasową
ENV DEBIAN_FRONTEND=noninteractive

# 1. Instalacja zależności systemowych i graficznych
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

# 2. Przygotowanie workspace w kontenerze
WORKDIR /root/ros2_ws/src

# 3. Klonowanie repozytorium UR5
RUN git clone -b ros2 https://github.com/UniversalRobots/Universal_Robots_ROS2_Description.git

# 4. Kopiowanie Twojego pakietu z komputera do kontenera
COPY src/my_robot_project ./my_robot_project

# 5. Budowanie projektu
WORKDIR /root/ros2_ws
RUN . /opt/ros/jazzy/setup.sh && colcon build

# 6. Konfiguracja Entrypointa
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# 7. Domyślna komenda po uruchomieniu
CMD ["ros2", "launch", "my_robot_project", "robot_app.launch.py"]
