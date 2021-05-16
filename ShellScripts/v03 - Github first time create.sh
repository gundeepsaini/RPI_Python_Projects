#!/bin/bash

# Make Executable: 		sudo chmod +x RPi_syncGit_v02.sh


echo "-------------------"
echo "      Scripts      "
echo "-------------------"
echo
echo "This will sync github repos to the folder!!!!"
echo
#read -p "Press enter to continue"
	
echo "-------------------------------"

echo "--> Create DIR and change to destination"
mkdir /home/pi/Desktop/Github_Repo/RPI_Python_Projects
cd /home/pi/Desktop/Github_Repo/RPI_Python_Projects

echo "-->Pulling from github"
git clone https://github.com/gundeepsaini/RPI_Python_Projects.git
echo
echo

echo "-------------------------------"

echo "--> Create DIR and change to destination"
mkdir /home/pi/Desktop/Github_Repo/CustomROM_SonOff
cd /home/pi/Desktop/Github_Repo/CustomROM_SonOff

echo "-->Pulling from github"
git clone https://github.com/gundeepsaini/CustomROM_SonOff.git
echo
echo

echo "-------------------------------"


#read -n 1 -s -r -p "DONE! Press any key to continue"

sleep 5