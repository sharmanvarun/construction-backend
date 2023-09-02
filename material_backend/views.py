# views.py in materials_backend app

# import json
# from channels.layers import get_channel_layer
# from django.http import HttpResponse
# from .models import Material

# def update_material_status(request, material_id):
#     # Update the material status as needed
#     material = Material.objects.get(pk=material_id)
#     new_status = # Calculate the new availability status

#     # Update the material's availability status
#     material.amount = new_status
#     material.save()

#     # Send a WebSocket update to the frontend
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         f"materials_{material_id}",
#         {
#             "type": "update_material_status",
#             "material_id": material_id,
#             "availability_status": new_status,
#         }
#     )

#     return HttpResponse("Material status updated")

