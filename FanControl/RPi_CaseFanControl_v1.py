import RPi.GPIO as GPIO
import time
import subprocess

ON_THRESHOLD = 50  # (degrees Celsius) Fan kicks on at this temperature.
OFF_THRESHOLD = 45  # (degrees Celsius) Fan shuts off at this temperature.
SLEEP_INTERVAL = 30  # (seconds) How often we check the core temperature.
FAN_Pin = 18
FAN_State = True


def Config_GPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(FAN_Pin, GPIO.OUT)


def Fan_CMD(cmd):
    Config_GPIO()
    if cmd == 1:
        GPIO.output(FAN_Pin, GPIO.HIGH)
        # print("FAN on")
    if cmd == 0:
        GPIO.output(FAN_Pin, GPIO.LOW)
        # print("FAN off")


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
    # Turn on fan with script start
    FAN_State = True
    FAN_State_Str = "Fan ON"
    Fan_CMD(FAN_State)

    while True:
        CPU_Temp = int(get_CPU_Temp())

        # Start the fan if the temperature has reached the limit and the fan isn't already running.
        if CPU_Temp > ON_THRESHOLD and not FAN_State:
            FAN_State = True
            FAN_State_Str = "Fan ON"
            Fan_CMD(FAN_State)

        # Stop the fan if the fan is running and the temperature has dropped below the limit.
        elif FAN_State and CPU_Temp < OFF_THRESHOLD:
            FAN_State = False
            FAN_State_Str = "Fan OFF"
            Fan_CMD(FAN_State)

        print("Checking CPU temp!", CPU_Temp, "°C", FAN_State_Str)
        time.sleep(SLEEP_INTERVAL)
