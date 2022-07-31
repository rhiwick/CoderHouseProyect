from django import forms
from ckeditor.fields import RichTextFormField


class FormCrearPosteo(forms.Form):
    imagen = forms.ImageField()
    titulo = forms.CharField()
    sub_titulo = forms.CharField()
    posteo = RichTextFormField()