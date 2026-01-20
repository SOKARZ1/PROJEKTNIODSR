# Projekt sterowania manipulatorem UR5.

Niniejszy projekt przedstawia symulację sterowania przegubem robota typu UR5 z wykorzystaniem środowiska RViz2.

# Wymagania projektu
Projekt potrzebuje następujących dodatków do prawidłowego działania:
* System operacyjny Ubuntu 24.04
* Dystrybucja ROS 2  "Jazzy"
* Paczka docker

# Uruchamianie projektu
1. Wejść do folderu projektu poprzez terminal
2. Zbudować projekt poprzez komendy:
* sudo docker build -t my_ur5_project_image .
* sudo chmod +x run_docker.sh
* sudo xhost +
* sudo ./run_docker.sh
3. W aplikacji RViz2:
* Zmienić fixed frame na baselink
* Dodać model robota
* Podpiąć temat /robot_description pod robota

# Autorzy projektu:
* Kacper Gwizdoń
* Jakub Dudziak













