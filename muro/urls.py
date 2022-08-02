from . import views 
from django.urls import path


urlpatterns = [
    path('muro/' , views.muro , name = 'muro'),
    path('postear/', views.postear , name = 'postear'),
    #path('ver_autor/<user>', views.ver_autor , name = 'ver_autor'),
    path('posteos/', views.Posteos.as_view() , name = 'posteos'),
    
]