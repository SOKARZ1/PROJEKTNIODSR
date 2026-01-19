# Projekt sterowania manipulatorem UR5.

Niniejszy projekt przedstawia symulację sterowania przegubem robota typu UR5 z wykorzystaniem środowiska RWiz2.

# Wymagania projektu
Projekt potrzebuje następujących dodatków do prawidłowego działania:
* System operacyjny Ubuntu 24.04
* Dystrybucja ROS 2  "Jazzy"
* Paczka docker

# Uruchamianie projektu
1. Wejść do folderu projektu poprzez terminal
2. Zbudować projekt poprzez komendy:
* docker build -t my_ur5_project_image-
* sudo chmod +x start_docker.sh
* sudo xhost +
* sudo ./start_docker.sh
3. W aplikacji Rwiz2:
* Zmienić współrzędne na baselink
* Dodać model robota
* Podpiąć temat pod robota

# Autorzy projektu:
Kacper Gwizdoń
Jakub Dudziak






