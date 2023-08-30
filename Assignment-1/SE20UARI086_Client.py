import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = input("Enter a message to send to the server: ")
        await websocket.send(message)
        print(f"Sent to server: {message}")
        
        response = await websocket.recv()
        print(f"Received from server: {response}")

asyncio.run(hello())
