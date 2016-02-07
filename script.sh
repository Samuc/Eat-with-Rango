#!/bin/bash

sudo apt-get update
sudo apt-get install python-setuptools
sudo apt-get install python-dev
sudo apt-get install build-essential
sudo apt-get install git
sudo apt-get install pkg-config
sudo apt-get install libtiff4-dev
sudo apt-get install libjpeg8-dev
sudo apt-get install zlib1g-dev
sudo easy_install pip
sudo -H pip install Pillow --upgrade
sudo pip install django --upgrade
sudo pip install -r requirements.txt
