#!/bin/bash

# RPi_syncGit_v02.sh

# Make Executable: 		sudo chmod +x RPi_syncGit_v02.sh
# Run:					sh RPi_syncGit_v02.sh

echo "-------------------"
echo "      Scripts      "
echo "-------------------"
echo
echo "This will discard all local changes!!!!"
echo
#read -p "Press enter to continue"
	
echo "-------------------------------"

echo "-->Chaning directory to destination"
cd /home/pi/Desktop/Github_Repo/RPI_Python_Projects
echo

echo "-->Changing branch to master"
git checkout master
echo

echo "-->Discarding local changes"
git reset --hard
echo

echo "-->Pulling from github"
git pull https://github.com/gundeepsaini/RPI_Python_Projects.git

echo
echo

#read -n 1 -s -r -p "DONE! Press any key to continue"

sleep 5