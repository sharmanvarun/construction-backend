# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class MaterialConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         print("varun connected")
#         await self.accept()

#     async def disconnect(self, close_code):
#         print("varun disconnect",close_code)
#         pass

#     async def send_material_update(self, event):
#         print('WHY IS THIS NOT WORKUNGGGGG')
#         # Send the updated material data to the client
#         await self.send(text_data=json.dumps(event['message']))

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MaterialConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # WebSocket connection logic
        print("CONNECTEDD VARUNS")
        await self.accept()

    async def disconnect(self, close_code):
        # WebSocket disconnection logic
        pass

    async def send_material_update(self, event):
        # Send the updated material data to the client
        await self.send(text_data=json.dumps(event['message']))

        # Print a message to confirm WebSocket message sent
        print("WebSocket message sent to consumer client:", event['message'])
