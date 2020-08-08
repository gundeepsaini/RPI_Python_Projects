
# References: 
# https://shop.sb-components.co.uk/blogs/posts/auto-run-python-program-on-raspberry-pi-startup
# https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/all



#To get the edit file for crontab
sudo crontab -e

#Auto start on reboot
@reboot python /home/pi/Desktop/GitHub_Rpi/RPI_Python_Projects/CaseFanController/RPi_CaseFanControl_v3.py &





#Open rc.local file as super user-

sudo nano /etc/rc.local

#After this, you will enter the nano file editor and here we have to add a command to execute our python program. Add the complete file execution line before ‘exit 0’ line at the end. After the editing saves the file and exit. For exit in nano type Ctrl x and for saving the file type Y.
#Use ‘&’ at the end of the line if your program contains an infinite loop.

python3 /home/pi/Desktop/GitHub_Rpi/RPI_Python_Projects/CaseFanController/RPi_CaseFanControl_v3.py &




