Docker img of ubuntu with ros2 ->

sudo apt update
sudo apt install docker.io

docker --version

docker pull ekm9/ros2_ubuntu

docker run -it ekm9/ros2_ubuntu /bin/bash ros-
