//publisher.js 
const { connect } = require('mqtt');
const mqtt = require('mqtt') 


//the client id is used by the MQTT broker to keep track of clients and and their // state
const clientId = 'mqttjs_' + Math.random().toString(8).substr(2, 4) 

//set MQTT broker connection address (WebSocket in this case)
const brokerUrl = "mqtt://broker.emqx.io:1883"

const client  = mqtt.connect(brokerUrl, {clientId: clientId, clean: false}); 

console.log(brokerUrl, 'client', clientId) 

const topicName = 'test/connection/ben'

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function sleep_5sec() {
    await sleep(5000);
    console.log('Done');
}


function cons(){
client.on("connect",function(connack){	
    console.log("client connected", connack);
 
 // on client conection publish messages to the topic on the server/broker 
 
   const payload = {1: "Hello world", 2: "Allez Allez~"}
 
   client.publish(topicName, JSON.stringify(payload), {qos: 1, retain: true}, (PacketCallback, err) => {
     
       if(err) {
           console.log(err, 'MQTT publish packet')
       }
   })
 
 
   //assumming messages comes in every 3 seconds to our server and we need to publish or proecess these messages
   setInterval(() => console.log("Message published"), 3000);
 
 })
}

cons()

client.on("error", function(err) {
    console.log("Error: " + err)
    if(err.code == "ENOTFOUND") {
        console.log("Network error, make sure you have an active internet connection")
    }
})

client.on("close", function() {
    console.log("Connection closed by client")
})


client.on("reconnect", function() {
    console.log("Client trying a reconnection")
})

client.on("offline", function() {
    console.log("Client is currently offline")
})