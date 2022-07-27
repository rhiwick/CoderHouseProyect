from django.db import models

# Create your models here.

class Producto(models.Model):
    producto_cia = models.CharField(max_length=15)
    producto_codigo = models.CharField(max_length=10)
    producto_descripcion = models.CharField(max_length=30)
    producto_cantidad = models.IntegerField(null=0) #siempre empiezo en 0
    producto_costo = models.IntegerField(null=0)
    producto_fecha = models.DateTimeField(null=True)
    
    def __str__(self):
        return f'{self.producto_codigo}'
    

