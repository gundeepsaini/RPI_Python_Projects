#!/bin/bash

# RPi_syncGit_Arduino_v01.sh

# Make Executable: 		sudo chmod +x RPi_syncGit_Arduino_v01.sh
# Run:					sh RPi_syncGit_Arduino_v01.sh

echo "-------------------"
echo "      Arduino      "
echo "-------------------"
echo
echo "This will discard all local changes!!!!"
echo
read -p "Press enter to continue"
	
echo "-------------------------------"

echo "-->Chaning directory to destination"
cd /home/pi/Desktop/GitHub_Rpi/Arduino_Sketchbook_GitHub
echo

echo "-->Changing branch to master"
git checkout master
echo

echo "-->Discarding local changes"
git reset --hard
echo

echo "-->Pulling from github"
git pull https://github.com/gundeepsaini/Arduino_Sketchbook_GitHub.git

echo
echo
read -n 1 -s -r -p "DONE! Press any key to continue"