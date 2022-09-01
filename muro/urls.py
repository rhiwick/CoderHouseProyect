from . import views 
from django.urls import path



urlpatterns = [
    path('postear/', views.postear , name = 'postear'),
    path('ver_autor/<user>', views.ver_autor , name = 'ver_autor'),
    path('posteos/', views.Posteos.as_view() , name = 'posteos'),
    path('misposteos/', views.Misposteos.as_view() , name = 'misposteos'),
    path('misposteos/eliminar/<int:posteo_id>/', views.EliminePosteo , name = 'eliminar_posteo'),
]