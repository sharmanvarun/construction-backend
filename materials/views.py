from rest_framework import generics, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Material
from .serializers import MaterialSerializer
from .consumers import MaterialConsumer
from asgiref.sync import async_to_sync
from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from channels.layers import get_channel_layer

class MaterialList(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['amount']
    search_fields = ['name', 'description']

class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MaterialUpdateAmount(generics.UpdateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_amount = int(request.data.get('amount', 0))  # Get the new amount from the request data

        # Update the material amount in the database
        instance.amount = new_amount
        instance.save()
            # Broadcast the update to WebSocket clients
        self.broadcast_update(instance.id, new_amount)

        return Response({'message': 'Material amount updated successfully','id':instance.id,'amount':instance.amount})

    def broadcast_update(self, material_id, new_amount):
        # Get the channel layer
        channel_layer = get_channel_layer()
        # Construct the message to send to clients
        message = {
            'type': 'update_material_amount',
            'material_id': material_id,
            'new_amount': new_amount,
        }

        # Send the message to a custom channel group for broadcasting
        async_to_sync(channel_layer.group_send)("update_material_amount", message)
