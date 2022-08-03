from django import forms
from ckeditor.fields import RichTextFormField
from .models import *


class FormCrearMensaje(forms.Form):
    a_user = forms.CharField(max_length=30)
    mensaje = RichTextFormField()
    
    
