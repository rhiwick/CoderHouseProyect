



from .views import about_rodri, about_santi, inicio, index, crear_producto, busqueda_producto, maestro_producto, editar_producto, eliminar_producto, edite_producto, elimine_producto
from django.urls import path

urlpatterns = [
    path('', inicio),
    path('index/', index, name= 'index'),
    path('crear-stock/', crear_producto, name = 'crear_producto'),
    path('maestro/', maestro_producto, name = 'maestro'),
    path('editar_producto/', editar_producto, name = 'editar_producto'),
    path('eliminar_producto/', eliminar_producto, name = 'eliminar_producto'),
    path('edite_producto/<int:id>/', edite_producto, name = 'edite_producto'),
    path('elimine_producto/<int:id>/', elimine_producto, name = 'elimine_producto'),
    path('busqueda/' ,busqueda_producto, name = 'busqueda_producto'),
    path('about_santi/' ,about_santi, name = 'about_santi'),
    path('about_rodri/' ,about_rodri, name = 'about_rodri'),

    
]