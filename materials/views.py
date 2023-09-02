from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Material
from .serializers import MaterialSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class MaterialList(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['amount']
    search_fields = ['name', 'description']

    def perform_create(self, serializer):
        # Save the new material
        material = serializer.save()

        # Send WebSocket update to clients
        event = {
            'type': 'material.update',  # Custom event type for WebSocket consumer
            'message': {
                'id': material.id,
                'name': material.name,
                'description': material.description,
                'amount': material.amount,
                'image_url': material.image.url if material.image else None,
            }
        }

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("material_updates", event)

        # Print a message to confirm WebSocket update
        print("WebSocket update sent after creating material:", material)

class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    def perform_update(self, serializer):
        # Update the material
        material = serializer.save()

        # Send WebSocket update to clients
        event = {
            'type': 'material.update',  # Custom event type for WebSocket consumer
            'message': {
                'id': material.id,
                'name': material.name,
                'description': material.description,
                'amount': material.amount,
                'image_url': material.image.url if material.image else None,
            }
        }

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("material_updates", event)

        # Print a message to confirm WebSocket update
        print("WebSocket update sent after updating material from views:", material)


# from rest_framework import generics, filters
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import Material
# from .serializers import MaterialSerializer

# class MaterialList(generics.ListCreateAPIView):
#     queryset = Material.objects.all()
#     serializer_class = MaterialSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['amount']
#     search_fields = ['name', 'description']

# class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Material.objects.all()
#     serializer_class = MaterialSerializer

# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync

# @async_to_sync
# async def update_material_availability(material_id, new_status):
#     # Update the material availability status in your database
#     material = Material.objects.get(pk=material_id)
#     material.availability_status = new_status
#     material.save()

#     # Send the update to connected WebSocket clients
#     channel_layer = get_channel_layer()
#     await channel_layer.group_send(
#         "materials_updates",  # Group name for WebSocket consumers
#         {
#             "type": "send.material.update",
#             "message": {
#                 "id": material_id,
#                 "availability_status": new_status,
#             },
#         },
#     )

class MaterialUpdateAmount(generics.UpdateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
