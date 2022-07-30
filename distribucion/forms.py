from django import forms


class FormBusquedaTransporte(forms.Form):
    codigo = forms.CharField(max_length=15)