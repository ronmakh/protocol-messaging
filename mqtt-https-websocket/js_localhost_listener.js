const socket = io("http://localhost:8080"); // connects to server address


socket.on('connection', () => {
  console.log('connected to server');
});

socket.emit("Pong: ", "hello") // this is to send

/* this is to listen */
socket.on("connection", (params) => {
    console.log(params)
})