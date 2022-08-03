from django import forms

class FormCrearProducto(forms.Form):
    producto_cia =  forms.CharField(max_length=30)
    producto_codigo = forms.CharField()
    producto_descripcion = forms.CharField()
    producto_costo = forms.IntegerField(required=False)
    producto_fecha = forms.DateField(required=False)
    
class FormBusquedaProducto(forms.Form):
    producto_codigo = forms.CharField(max_length=30)
    
class FormEliminarProducto(forms.Form):
    producto_codigo = forms.CharField(max_length=30)
    
class FormEditarProducto(forms.Form):
    producto_cia =  forms.CharField(max_length=30)
    producto_codigo = forms.CharField()
    producto_descripcion = forms.CharField(max_length=30)
    producto_costo = forms.IntegerField(required=False)
    
    
class FormCrearTransporte(forms.Form):
    codigo =  forms.CharField(max_length=15)
    tipo = forms.CharField(max_length=15)
    marca = forms.CharField(max_length=10)
    modelo = forms.CharField(max_length=30)
    tara = forms.IntegerField()
    ejes = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)