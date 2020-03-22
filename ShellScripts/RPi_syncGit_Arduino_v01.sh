#!/bin/bash

# RPi_syncGit_Arduino_v01.sh

# Make Executable: 		sudo chmod +x RPi_syncGit_Arduino_v01.sh
# Run:					sh RPi_syncGit_Arduino_v01.sh

echo "-------------------"
echo "      Arduino      "
echo "-------------------"
echo "This will discard all local changes!!!!"
echo " "
read -p "Press enter to continue"
	
cd /home/pi/Desktop/GitHub_Rpi/Arduino_Sketchbook_GitHub
#git checkout master
#git reset --hard
#git pull https://github.com/gundeepsaini/Arduino_Sketchbook_GitHub.git

# ls

read -n 1 -s -r -p "Press any key to continue"