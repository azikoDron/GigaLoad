import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_groupName = "group_chat"
        # self.channel_name = "GigaLoad"
        await self.channel_layer.group_add(
            self.room_groupName,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_groupName,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # print(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        time = text_data_json["time"]
        print(text_data)

        await self.channel_layer.group_send(
            self.room_groupName, {
                "type": "send_message",
                "message": message,
                "username": username,
                "time": time,
                # "GigaLoad": "Hello"
            })
        await self.channel_layer.group_send(self.room_groupName, {"type": "send_message",
                                                                  "message": message,
                                                                  "username": "GigaLoad",
                                                                  "time": time})

    async def send_message(self, event):
        message = event["message"]
        username = event["username"]
        time = event["time"]
        await self.send(text_data=json.dumps({"message": message, "username": username, "time": time}))