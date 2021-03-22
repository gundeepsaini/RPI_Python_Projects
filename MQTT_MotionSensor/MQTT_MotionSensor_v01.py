
# https://www.emqx.io/blog/how-to-use-mqtt-in-python

from Secrets_Python import *
MQTT_TOPIC_STATE_PIR = "HA/KitchenPi/PIR/state"
PIR_INPUT_PIN = 17


# Will Topic - Availability
#define MQTT_TOPIC_WILL        "HA/Kitchen/status"
#define MQTT_OFFLINE           "Offline"
#define MQTT_ONLINE            "Active"


from paho.mqtt import client as mqtt_client
import time
import RPi.GPIO as GPIO           
import datetime

Last_PIR_State = False


def RPi_GPIO_Config():	
	GPIO.setmode(GPIO.BCM)           		 	 # Set's GPIO pins to BCM GPIO numbering
	GPIO.setup(PIR_INPUT_PIN, GPIO.IN)           # Set our input pin to be an input
	#GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	#GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	


def RPi_GPIO_Read():
	ReadState = GPIO.input(PIR_INPUT_PIN)
	return ReadState


def RPi_GPIO_StateChange():
	global Last_PIR_State
	ReadState = GPIO.input(PIR_INPUT_PIN)
	
	if(ReadState == Last_PIR_State):
		return False, ReadState
	else:
		Last_PIR_State = ReadState
		return True, ReadState


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    
    # Set Connecting Client ID
    client = mqtt_client.Client(SECRET_DeviceName_RPi1)
    client.username_pw_set(SECRET_MQTT_User, SECRET_MQTT_Pass)
    client.on_connect = on_connect
    client.connect(SECRET_MQTT_Server, SECRET_MQTT_Port)
    return client


def publish(client):
     msg_count = 0
     while True:
         
         ChangeState, CurrentState = RPi_GPIO_StateChange()

         if(CurrentState):
         	mqtt_message = "ON"
         else:
         	mqtt_message = "OFF"

         if(ChangeState):
         	client.publish(MQTT_TOPIC_STATE_PIR, mqtt_message)
         	print(mqtt_message)

         time.sleep(1/1000.0)

         


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    RPi_GPIO_Config()
    run()         




