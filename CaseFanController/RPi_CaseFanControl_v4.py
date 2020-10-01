# TODO: Add Intro and code overview 

# v3: Added error handling
# v4: Check log file size and delete if size > 1MB

import RPi.GPIO as GPIO
import time
import subprocess

# CPU Temperature Zones
CPU_Temp_Warm       = 40    # Fan runs at Speed 1
CPU_Temp_Hot        = 50    # Fan runs at Speed 2
CPU_Temp_SuperHot   = 55    # Fan runs at Speed 3

# FAN Dutycycle setpoints
FAN_Speed0 = 0              # if CPU Temp < Warm
FAN_Speed1 = 50             # if CPU Temp > Warm
FAN_Speed2 = 75             # if CPU Temp > Hot
FAN_Speed3 = 100            # if CPU Temp > SuperHot

# Cycle Time
SLEEP_INTERVAL = 30  # secs - Temperature check interval

# GPIO 
FAN_Pin = 18

# Others
log_filename = "/home/pi/Desktop/log_fan_controller.csv"



def Fan_CMD(Speed_State):
    try:
        if Speed_State == 0:
            DutyCycle = FAN_Speed0
        if Speed_State == 1:
            DutyCycle = FAN_Speed1
        if Speed_State == 2:
            DutyCycle = FAN_Speed2
        if Speed_State == 3:
            DutyCycle = FAN_Speed3

        if DutyCycle < 100 and not DutyCycle == 0:
            # Start fan 100% and then slow down - else fan fails to start because of high starting torque
            PWM.ChangeDutyCycle(100)
            time.sleep(1)
        PWM.ChangeDutyCycle(DutyCycle)
        # print("FAN at", Speed_State, " - ", DutyCycle, "%")
        return DutyCycle
    except:
        print("Error in: Fan_CMD")
        return 0    


def get_CPU_Temp():
    try:
        output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True)
        temp_str = output.stdout.decode()
        # print(temp_str)
        CPU_Temp = float(temp_str.split('=')[1].split('\'')[0])
        # print(CPU_Temp)
        return CPU_Temp
    except (IndexError, ValueError):
        print("Error in: get_CPU_Temp")        
        raise RuntimeError('Could not parse temperature output.')
        return 0  


if __name__ == '__main__':
        
    try:
        # Logging - startup
        log = open(log_filename, 'a')
        log.write("\n\n{0};Script Startup;\n".format(time.ctime()))
        log.close()


        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(FAN_Pin, GPIO.OUT)    
        PWM = GPIO.PWM(FAN_Pin, 50)  # pin, frequency
        
        # Always start script with fan @ 100%
        PWM.start(100)      
        CMD = 3
        FAN_DutyCycle = Fan_CMD(CMD)

        while True:
            
            CPU_Temp = int(get_CPU_Temp())
            Last_CMD = CMD
            
            if CPU_Temp >= CPU_Temp_SuperHot:
                CMD = 3
            elif CPU_Temp >= CPU_Temp_Hot:
                CMD = 2
            elif CPU_Temp >= CPU_Temp_Warm:
                CMD = 1
            elif CPU_Temp < CPU_Temp_Warm:
                CMD = 0
            else:
                # Failed to read temp or other error - turn on fan to 100%
                CMD = 3
            if not CMD == Last_CMD: 
                FAN_DutyCycle = Fan_CMD(CMD)
            print(time.ctime(),": CPU Temp:", CPU_Temp, "°C", "FAN state:", CMD, "DutyCycle:", FAN_DutyCycle)
            
            log = open(log_filename, 'a')
            log.write("{0};CPU temp;{1};DutyCycle;{2};\n".format(time.ctime(),CPU_Temp,FAN_DutyCycle))            
            log.close()
            
            time.sleep(SLEEP_INTERVAL)
    
    except:
        print("Error in: Main")
            
    

