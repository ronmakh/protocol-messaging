from asyncio import transports
#import os
#from dotenv import load_dotenv
import random
import time
import json
from paho.mqtt import client as mqtt_client


import os
from dotenv import load_dotenv
load_dotenv()
PORT_MQTT=int(os.getenv('PORT_MQTT'))
BROKER_MQTT=os.getenv('BROKER_MQTT')
CLIENT_ID_MQTT=os.getenv('CLIENT_ID_MQTT')
USERNAME_MQTT=os.getenv('USERNAME_MQTT')
PASSWORD_MQTT=os.getenv('PASSWORD_MQTT')
TOPIC_MQTT=os.getenv('TOPIC_MQTT')


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(CLIENT_ID_MQTT)
    client.username_pw_set(USERNAME_MQTT, PASSWORD_MQTT)
    client.on_connect = on_connect
    client.connect(BROKER_MQTT, PORT_MQTT)
    print(client)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        msg = json.dumps(msg)
        result = client.publish(TOPIC_MQTT, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{TOPIC_MQTT}`")
        else:
            print(f"Failed to send message to topic {TOPIC_MQTT}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()