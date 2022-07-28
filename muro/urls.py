from . import views 
from django.urls import path


urlpatterns = [
    path('muro/', views.muro , name = 'muro'),


]