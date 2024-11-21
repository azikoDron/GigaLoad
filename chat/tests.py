from django.test import TestCase
import json
# Create your tests here.

from chat.consumer import ChatConsumer

from channels.generic.websocket import AsyncWebsocketConsumer

a = AsyncWebsocketConsumer().connect()



# async def receive(text_data):
#     text_data_json = json.loads(text_data)
#     # print(text_data)
#     message = text_data_json["message"]
#     username = text_data_json["username"]
#     time = text_data_json["time"]
#     await print(g.accept())
#
# receive("as")