from . import views 
from django.urls import path


urlpatterns = [
    path('muro/' , views.Muro.as_view() , name = 'muro'),
    path('postear/', views.postear , name = 'postear'),


]