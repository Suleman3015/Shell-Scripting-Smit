#/bin/bash

sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-pip python3-env -y

python3 --version
pip3 --version

sudo update-alternative --install /usr/bin/python python /usr/bin/python3 1
