#!/bin/bash
set -e

# Załaduj środowisko ROS 2 Jazzy
source /opt/ros/jazzy/setup.bash

# Załaduj Twój zbudowany workspace
if [ -f /root/ros2_ws/install/setup.bash ]; then
  source /root/ros2_ws/install/setup.bash
fi

# Wykonaj komendę przekazaną do dockera
exec "$@"
