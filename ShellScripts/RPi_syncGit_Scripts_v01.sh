#!/bin/bash

# RPi_syncGit_Scripts_v01.sh

# Make Executable: 		sudo chmod +x RPi_syncGit_Scripts_v01.sh
# Run:					sh RPi_syncGit_Scripts_v01.sh

echo "Sync Scripts"
echo "This will discard all local changes!!!!"
read -p "Press enter to continue"
	
cd /home/pi/Desktop/GitHub_Rpi/RPI_Python_Projects
git checkout master
git reset --hard
git pull https://github.com/gundeepsaini/RPI_Python_Projects.git
# ls

read -n 1 -s -r -p "Press any key to continue"