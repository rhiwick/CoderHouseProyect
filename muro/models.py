from django.db import models
from ckeditor.fields import RichTextField
from django.forms import IntegerField


class PosteosUsuarios(models.Model):
    autor = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='imagenes')
    titulo = models.CharField(max_length=15)
    sub_titulo = models.CharField(max_length=30)
    posteo = RichTextField()
    fecha_posteo = models.DateTimeField(null=True)


class Autor(models.Model):
    id = IntegerField()
    usuario = models.CharField(max_length=50) 
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    correo = models.EmailField(null=True)
    descripcion = RichTextField(null=True)
    
