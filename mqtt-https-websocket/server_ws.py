# Acts as localhost server
import websockets
import asyncio
import requests
import json

PORT = 3001

print("Server listening on Port " + str(PORT))

async def echo(websocket, path):
    print("A client just connected")
    try:
        async for message in websocket:
            print("Received message from client: " + message)
            payload = {'value':message}
            r = requests.post('http://localhost:8080', params=payload)
            print(r)
            await websocket.send("Pong: " + message)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")

start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()