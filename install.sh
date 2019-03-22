#!/usr/bin/bash

echo "Mohon tunggu yah"
echo "sedang menginstall.."
apt upgrade -y && apt update
apt install python 
pip install --upgrade pip
pip3 install mps_youtube
pip3 install youtube_dl
pip3 install mpv
