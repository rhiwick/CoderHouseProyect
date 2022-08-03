
from django.urls import path
from .views import ver_mensajes, enviar_mensaje



urlpatterns = [
    path('mensajes/', ver_mensajes , name = 'mensajes'),
    path('enviar_mensajes', enviar_mensaje , name = 'enviar_mensajes'),
    
]