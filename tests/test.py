import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.iglor.es", 8080, 60)

a = True
while True:
    payload = {
        "action": {
            "module": "multimedia",
            "value": "text",
            "data": {
                "file": "Hola Claudia",
                "default-sound": "notif.mp3",
                "vibration": 0,
                "background-color": "#0041F1"
            },
            "aref": "string",
            "filters": []
        }
    }

    torch = {
        "action": {
            "module": "hardware",
            "value": "torch",
            "data": {
                "torch": [{
                    "active": "true",
                    "seconds": 1
                }],
                "default-sound": "sound.mp3",
                "vibration": 1
            },
        },
        "aref": "string",
        "filters": []
    }

    question = {
        "action": {
            "module": "quiz",
            "value": "question",
            "data": {
                "file": "Quien es la mas putaaaa?",
                "options": [
                    {
                        "text": "Claudia",
                        "value": False
                    },
                    {
                        "text": "Gisela",
                        "value": False
                    },
                    {
                        "text": "Reme",
                        "value": False
                    },
                ],
                "default-sound": "sound.mp3",
                "vibration": 0.1
            },
        },
        "aref": "string",
        "filters": []
    }

    print("lalas")
    client.publish("3522109c644e08605c46308a880dcb7d/smartphone", payload=bytes(payload), qos=0, retain=False)
    a = not a
    time.sleep(0.5)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()