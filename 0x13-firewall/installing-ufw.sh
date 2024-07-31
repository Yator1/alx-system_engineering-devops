#!/usr/bin/env bash


sudo apt-get update
# Installing UFW if not installed
sudo apt install ufw

# Setting the default UFW incoming policy to deny(blocking all incoming traffic)
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allowing ssh, https and http connection respectively
sudo ufw allow 22
sudo ufw allow 443
sudo ufw allow 80

# 5. Checking the rules added so far
sudo ufw show added

# 6. Enabling the changes
sudo ufw enable
