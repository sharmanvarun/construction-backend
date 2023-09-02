

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from materials import consumers

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": URLRouter(consumers.websocket_urlpatterns),
# })

websocket_urlpatterns = [
    path("ws/materials/", consumers.MaterialConsumer.as_asgi()),
]
application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/materials/", consumers.MaterialConsumer.as_asgi()),
    ]),
})

# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path
# from materials import consumers

# websocket_urlpatterns = [
#     path("ws/materials/", consumers.MaterialConsumer.as_asgi()),
# ]

# application = ProtocolTypeRouter({
#     "websocket": URLRouter(websocket_urlpatterns),
# })