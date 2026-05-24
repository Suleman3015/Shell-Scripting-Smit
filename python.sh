#/bin/bash

sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-pip python3-env -y

python3 --version
pip3 --version

#alternative for python3 is python
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
