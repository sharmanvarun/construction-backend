
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import json
from channels.layers import get_channel_layer
from materials.models import Material
from asgiref.sync import async_to_sync

@receiver([post_save, post_delete], sender=Material)
def material_updated(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    # Send a WebSocket update when a material is updated
    async_to_sync(channel_layer.group_send)(
        f"materials_{instance.id}",
        {
            "type": "send_material_update",
            "message": {
                "material_id": instance.id,
                "name": instance.name,
                "description": instance.description,
                "amount": instance.amount,
            },
        }
    )
    print("VARUN SIGNAL updated")

