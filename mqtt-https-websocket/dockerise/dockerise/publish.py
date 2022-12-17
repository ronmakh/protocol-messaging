import paho.mqtt.client as paho
import os
from dotenv import load_dotenv
import http.client as httplib

load_dotenv()

conn_flag=False
client = ""

LOAD_ENV_MQTT_CLIENT_ID = os.getenv("DEFINE_MQTT_CLIENT_ID")
LOAD_ENV_MQTT_USERNAME = os.getenv("DEFINE_MQTT_USERNAME")
LOAD_ENV_MQTT_PASSWORD = os.getenv("DEFINE_MQTT_PASSWORD")
LOAD_ENV_MQTT_BROKER = os.getenv("DEFINE_MQTT_BROKER")
LOAD_ENV_MQTT_PORT = os.getenv("DEFINE_MQTT_PORT")

def on_connect(client, userdata, flags, rc):
    global conn_flag
    conn_flag = True
    print("Connected ", conn_flag)
    conn_flag = True

def on_log(client, userdata, level, buf):
    print("Buffer ", buf)

def on_disconnect(client, userdata, rc):
    print("Client disconnected ok")
    conn_flag = False

def checkInternetAvailability( url="1.1.1.1", timeout=10 ):
    conn = httplib.HTTPConnection(
        url,
        timeout=timeout
    )
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except KeyboardInterrupt:
        print("Stopping .checkInternetAvailability() service...")
        return False
    except Exception as e:
        print("Error [.checkInternetAvailability()]: "+str(e))
        return False

try:
    client = paho.Client(LOAD_ENV_MQTT_CLIENT_ID)
    client.on_log = on_log
    client.username_pw_set(
        LOAD_ENV_MQTT_USERNAME,
        password=LOAD_ENV_MQTT_PASSWORD
    )
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(
        LOAD_ENV_MQTT_BROKER,
        int(LOAD_ENV_MQTT_PORT)
    )
except socket.gaierror as ae:
    print("socket.gaierror: ", str(ae))
    # conn_flag=False
    client1.loop_stop()
except Exception as e:
    print("Failing: ", str(e))
    client.loop_stop()

def call_publish(topic, message):
    global client
    if checkInternetAvailability():
        client.publish(
            topic,
            payload=message,
            qos=2
        )
        client.loop_start()