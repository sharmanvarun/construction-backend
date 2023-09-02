# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# import materials.routing  # Import your routing configuration

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'material_backend.settings')
# # application = get_asgi_application()

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             materials.routing.websocket_urlpatterns
#         )
#     ),
# })

# import os
# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'material_backend.settings')

# application = get_asgi_application()

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import materials.routing  # Import your routing configuration

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'material_backend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            materials.routing.websocket_urlpatterns
        )
    ),
})