import json
from paho.mqtt import client as mqtt_client
import os
from dotenv import load_dotenv

load_dotenv()

PORT_MQTT=os.getenv('TOPIC_MQTT')
PORT_MQTT_WS=os.getenv('PORT_MQTT_WS')
BROKER_MQTT=os.getenv('BROKER_MQTT')
CLIENT_ID_MQTT=os.getenv('CLIENT_ID_MQTT')
CLIENT_ID_MQTT2=os.getenv('CLIENT_ID_MQTT2')
USERNAME_MQTT=os.getenv('USERNAME_MQTT')
PASSWORD_MQTT=os.getenv('PASSWORD_MQTT')
TOPIC_MQTT=os.getenv('TOPIC_MQTT')


# # To check your env vars are correct
# print(PORT_MQTT)
# print(BROKER_MQTT)
# print(CLIENT_ID_MQTT)
# print(USERNAME_MQTT)
# print(PASSWORD_MQTT)
# print(TOPIC_MQTT)


#<<<<<<< HEAD
def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker here
    print("Connected with resulting code {0}".format(str(rc)))  # Print result of connection attempt!
    client.subscribe(TOPIC_MQTT, qos=2)  


def on_message(client, userdata, msg):  # The callback for when a 'publish' message is received from the server.
    v = msg.payload.decode('utf-8').replace("'", "\"")
    v = json.loads(v)
    print("==============data is subscribed===============")
    print(v)

def on_disconnect(client, userdata, rc):
    print("Client disconnected!")

def main():
	# Some instance of the client
	client = mqtt_client.Client(CLIENT_ID_MQTT)  
	
	# client.tls_set("ca.crt", "client.crt", "client.key")
	# client.tls_insecure_set(True)
	
	client.on_connect = on_connect  # Define a callback function for successful connection
	client.on_disconnect = on_disconnect
	#client.tls_set()
	client.on_message = on_message  # Define a callback function for receipt of a message
	client.username_pw_set(
	    username=USERNAME_MQTT,
	    password=PASSWORD_MQTT
	)
	client.connect(BROKER_MQTT, PORT_MQTT)
	client.loop_forever()  # Start networking daemon


if __name__ == '__main__':
    main()
