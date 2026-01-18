#!/bin/bash

# Zezwól na dostęp do serwera X (grafiki) dla lokalnych użytkowników
xhost +local:root

# Uruchom kontener
docker run -it --rm \
    --name ros2_ur5_container \
    --net=host \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --privileged \
    my_ur5_project_image
