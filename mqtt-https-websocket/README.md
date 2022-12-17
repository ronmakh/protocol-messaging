## Description
This project aims to listen from a MQTT publisher and show the subscribed message in a frontend React app. 
Current progress uses flow as such: MQTT publisher > (MQTT listener+WebSocket publisher) > React app

MQTT publishers: 
- publish python.py
- publish_test.js

MQTT subscribers:
- subscribe_python.py
- subscribe_test.js

React App frontend: 
- taste_of_mqtt_in_react

MQTT over WebSockets subscriber:
- pub_sub_mqtt.py

Localhost server:
- server.py

WebSocket publisher:
- websocket_test.py



## Running MQTT publisher
Create and activate environment
```
python3 -m venv ./env
source ./env/bin/activate
pip3 install -r requirements.txt
```
Copy the contents from `.env` into your terminal and then run


## Running listener
[Python]
```
pipenv install
pipenv shell

python subscribe_python.py
```

[JavaScript]
```
npm install

node subscribe_test.js
```


## Running React App frontend
```
npm install

npm start
```


## References:

MQTT
http://www.steves-internet-guide.com/mqtt-websockets
https://www.emqx.com/en/blog/how-to-use-mqtt-in-python
https://www.emqx.com/en/blog/how-to-use-mqtt-in-nodejs
https://www.emqx.com/en/blog/connect-to-mqtt-broker-with-websocket
node-mqtt-pub-sub-demo/blob/master/subscriber.js

WebSocket
https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications
https://github.com/ParametricCamp/TutorialFiles/tree/master/Misc/WebSockets
https://blog.logrocket.com/websockets-tutorial-how-to-go-real-time-with-node-and-react-8e4693fbf843/

React
https://www.preciouschicken.com/blog/posts/a-taste-of-mqtt-in-react/
https://blog.logrocket.com/getting-started-with-node-js-mqtt/https://github.com/firebase007/
https://dev.to/muratcanyuksel/using-websockets-with-react-50pi