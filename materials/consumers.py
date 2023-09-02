import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Material

class MaterialConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def update_amount(self, event):
        material_id = event['material_id']
        new_amount = event['new_amount']

        await self.send(json.dumps({
            'material_id': material_id,
            'new_amount': new_amount,
        }))

    @staticmethod
    @async_to_sync
    def update_material_amount(material_id, new_amount):
        material = Material.objects.get(pk=material_id)
        material.amount = new_amount
        material.save()

    async def receive(self, text_data):
        data = json.loads(text_data)
        material_id = data['material_id']
        new_amount = data['new_amount']

        # Update the amount in the database
        self.update_material_amount(material_id, new_amount)

        # Send the updated data to all connected clients
        await self.channel_layer.group_add(
            str(material_id),
            self.channel_name
        )

        await self.send(json.dumps({
            'material_id': material_id,
            'new_amount': new_amount,
        }))

        await self.channel_layer.group_discard(
            str(material_id),
            self.channel_name
        )
