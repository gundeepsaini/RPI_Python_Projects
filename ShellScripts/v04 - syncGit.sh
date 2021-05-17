#!/bin/bash

# Make Executable: 		sudo chmod +x v04 - syncGit.sh
# Run:					sh v04 - syncGit.sh

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
echo "-->Changing branch to master"
git checkout master
echo "-->Discarding local changes"
git reset --hard
echo "-->Pulling from github"
git pull https://github.com/gundeepsaini/RPI_Python_Projects.git

echo "-------------------------------"

echo "-->Chaning directory to destination"
cd /home/pi/Desktop/Github_Repo/CustomROM_SonOff
echo "-->Changing branch to master"
git checkout master
echo "-->Discarding local changes"
git reset --hard
echo "-->Pulling from github"
git pull https://github.com/gundeepsaini/CustomROM_SonOff.git

echo "-------------------------------"

echo

#read -n 1 -s -r -p "DONE! Press any key to continue"

sleep 5