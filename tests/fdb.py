import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from datetime import datetime
import time
import paho.mqtt.client as mqtt


def button_callback(channel):
    print(str(datetime.now()) + "Button was pushed!")
    trigger()
    time.sleep(2)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def trigger():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("mqtt.iglor.es", 8080, 60)
    payload = {
        "data": "bomb"
    }
    print("lalas")
    client.publish("3522109c644e08605c46308a880dcb7d/smartphone", payload=bytes(payload), qos=0, retain=False)
    time.sleep(0.5)

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
