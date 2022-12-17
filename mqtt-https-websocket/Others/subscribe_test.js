// controller.js

const mqtt = require('mqtt')

require('dotenv').config()
const broker = process.env.BROKER_MQTT
const port = process.env.PORT_MQTT
const clientId = process.env.PORT_MQTT
const topicName = process.env.PORT_MQTT
const username = process.env.USERNAME_MQTT
const password = process.env.PORT_MQTT

const options = {
  clientId: clientId,
  clean: true,
  connectTimeout: 4000,
  username: username,
  password: password,
  reconnectPeriod: 1000,
}

const client = mqtt.connect(broker, options)

// connect to same client and subscribe to same topic name 
client.on('connect', () => {
  // can also accept objects in the form {'topic': qos}
  client.subscribe(topicName, (err, granted) => {
    if (err) {
      console.log(err, 'err');
    }
    console.log(granted, 'granted')
  })
})


// on receive message event, log the message to the console
client.on('message', (topic, message, packet) => {
  console.log(packet, packet.payload.toString());
  if (topic === topicName) {
    console.log(JSON.parse(message));
  }
})

client.on("packetsend", (packet) => {
  console.log(packet, 'packet2');
})