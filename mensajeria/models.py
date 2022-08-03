from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Mensajeria(models.Model):
    de_user = models.CharField(max_length=30)
    a_user = models.CharField(max_length=30)
    mensaje = RichTextField()
    fecha_mensaje = models.DateTimeField(null=True)