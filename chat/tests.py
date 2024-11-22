import asyncio

from django.test import TestCase
import json
# Create your tests here.

from chat.consumer import ChatConsumer

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic import websocket
#a = ChatConsumer().channel_receive

async def connect_to_server():
    async with  connect("ws://localhost:8000") as websocket:
        await websocket.send("Hello, Server!")
        response = await websocket.recv()
        print(f"Received: {response}")


asyncio.get_event_loop().run_until_complete(connect_to_server())