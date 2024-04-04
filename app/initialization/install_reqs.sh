#!/bin/bash

sudo apt update -y

# Install pip
sudo apt install python3-pip -y

# Install python libraries
pip3 install -r requirements.txt
sudo pip3 install streamlit