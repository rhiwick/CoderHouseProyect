from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.contrib.auth.models import User
 

class Mensajeria(models.Model):
    de_user = models.CharField(max_length=30)
    a_user = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = RichTextField()
    fecha_mensaje = models.DateTimeField(null=True)
    
    def __str__(self):
        return f'{self.de_user}'
