#Script subscribes to MQTT broker and publish to WebSocket via async feature

import time
import paho.mqtt.client as mqtt
import asyncio
import websockets

#Environment variable setup
import os
from dotenv import load_dotenv
load_dotenv()
PORT_MQTT=int(os.getenv('PORT_MQTT'))
BROKER_MQTT=os.getenv('BROKER_MQTT')
CLIENT_ID_MQTT=os.getenv('CLIENT_ID_MQTT')
USERNAME_MQTT=os.getenv('USERNAME_MQTT')
PASSWORD_MQTT=os.getenv('PASSWORD_MQTT')
TOPIC_MQTT=os.getenv('TOPIC_MQTT')
WS_LINK = 'ws://localhost:3001'           #localhost
WS_LINK2='wss://ws.postman-echo.com/raw'  #free ws server


# Callback Function on Connection with MQTT Server
def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    client.subscribe(TOPIC_MQTT)

# Callback Function on Receiving the Subscribed Topic/Message
def on_message( client, userdata, msg):
    message = msg.payload.decode('utf-8').replace("'", "\"")
    #pass message to async function
    asyncio.run(hello(message))

# async function to publish function input to websocket server
async def hello(text):
    async with websockets.connect(WS_LINK) as websocket:  #this line asyncs with server
        await websocket.send(text)  #send ws packet to server

def main():
    client = mqtt.Client(CLIENT_ID_MQTT)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER_MQTT, PORT_MQTT)
    client.username_pw_set(USERNAME_MQTT, PASSWORD_MQTT)

    client.loop_forever()
    time.sleep(1)

main()
