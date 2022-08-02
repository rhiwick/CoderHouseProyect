from . import views
from django.urls import path


urlpatterns = [
    path('crear_transporte/', views.CearTransporte.as_view() , name = 'crear_transporte'),
    path('distribucion/', views.distribucion, name = 'distribucion'),
    path('editar_transporte/', views.EditarTransporte.as_view(), name = 'editar_transporte'),
    path('eliminar_transporte/', views.EliminarTransporte.as_view() , name = 'eliminar_transporte'),
    path('edite_transporte/<int:pk>/', views.EditeTransporte.as_view() , name = 'edite_transporte'),
    path('elimine_transporte/<int:pk>/', views.ElimineTransporte.as_view() , name = 'elimine_transporte'),
    path('busqueda_transporte/' , views.BusquedaTransporte.as_view() , name = 'busqueda_transporte'),

]