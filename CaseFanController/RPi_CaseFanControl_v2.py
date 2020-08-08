# TODO: Add Intro and code overview 

import RPi.GPIO as GPIO
import time
import subprocess

# CPU Temperature Zones
CPU_Temp_Warm = 40
CPU_Temp_Hot = 50
CPU_Temp_SuperHot = 55

# FAN Dutycycle setpoints
FAN_Speed0 = 0
FAN_Speed1 = 50
FAN_Speed2 = 75
FAN_Speed3 = 100

# Other parameters
SLEEP_INTERVAL = 30  # in secs - Temperature check interval
FAN_Pin = 18
FAN_State = True
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(FAN_Pin, GPIO.OUT)
PWM = GPIO.PWM(FAN_Pin, 50)  # pin, frequency
PWM.start(100)  # Always start script with fan @ 100%


def Fan_CMD(Speed_State):
    if Speed_State == 0:
        DutyCycle = FAN_Speed0
    if Speed_State == 1:
        DutyCycle = FAN_Speed1
    if Speed_State == 2:
        DutyCycle = FAN_Speed2
    if Speed_State == 3:
        DutyCycle = FAN_Speed3

    if DutyCycle < 100 and not DutyCycle == 0:
        PWM.ChangeDutyCycle(100)
        time.sleep(1)
    PWM.ChangeDutyCycle(DutyCycle)
    # print("FAN at", Speed_State, " - ", DutyCycle, "%")
    return DutyCycle

def get_CPU_Temp():
    output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True)
    temp_str = output.stdout.decode()
    # print(temp_str)
    try:
        CPU_Temp = float(temp_str.split('=')[1].split('\'')[0])
        # print(CPU_Temp)
        return CPU_Temp
    except (IndexError, ValueError):
        raise RuntimeError('Could not parse temperature output.')


if __name__ == '__main__':
    
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
        print("CPU temp:", CPU_Temp, "°C", "FAN state:", CMD, "DutyCycle:", FAN_DutyCycle)
        time.sleep(SLEEP_INTERVAL)

