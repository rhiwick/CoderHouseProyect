from secrets import choice
from django import forms
from ckeditor.fields import RichTextFormField
from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import User
from .models import *


class FormCrearMensaje(forms.Form):
    
    a_user = forms.ModelChoiceField(queryset= User.objects.all())
    mensaje = RichTextFormField()



