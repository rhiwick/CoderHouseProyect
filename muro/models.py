from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class PosteosUsuarios(models.Model):
    autor = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='imagenes')
    titulo = models.CharField(max_length=15)
    sub_titulo = models.CharField(max_length=30)
    posteo = RichTextField()
    fecha_posteo = models.DateTimeField(null=True)
