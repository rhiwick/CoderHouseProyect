from . import views 
from django.urls import path


urlpatterns = [
    path('muro/' , views.muro , name = 'muro'),
    path('postear/', views.postear , name = 'postear'),
    path('ver_autor/', views.ver_autor , name = 'ver_autor'),



]