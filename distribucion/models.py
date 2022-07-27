from django.db import models

# Create your models here.
class Transporte(models.Model):
    codigo = models.CharField(max_length=15)
    tipo = models.CharField(max_length=15)
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=30)
    tara = models.IntegerField() #siempre empiezo en 0
    ejes = models.IntegerField()
    
    def __str__(self):
        return f'{self.codigo}'