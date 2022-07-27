from datetime import datetime
import imp
from vistas.forms import FormCrearProducto, FormBusquedaProducto, FormEliminarProducto, FormEditarProducto


from django.shortcuts import redirect, render
from vistas.models import Producto

from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form_crear_producto = FormCrearProducto(request.POST)
        if form_crear_producto.is_valid():
            informacion = form_crear_producto.cleaned_data
            
            producto = Producto(producto_cia = informacion['producto_cia'],
                             producto_codigo = informacion['producto_codigo'], 
                             producto_descripcion = informacion['producto_descripcion'],
                             producto_costo = informacion['producto_costo'],
                             producto_fecha = datetime.now(),
                             producto_cantidad = 0
                             )
                             
            producto.save()
            
            return render(request, 'Maestros/crear_stock.html')
    else:
        form_crear_producto = FormCrearProducto()
    
    return render(request,'Maestros/crear_stock.html',{'miProducto':form_crear_producto, } )


def busqueda_producto(request):
    id_producto = request.GET.get('producto_codigo')
    #productos_listado = Producto.objects.all()
    
    if id_producto:
        productos_listado = Producto.objects.filter(producto_codigo=id_producto)
        
    else:
        productos_listado = Producto.objects.all()
        form = FormBusquedaProducto()
    
    form = FormBusquedaProducto()
    return render(request, 'Maestros/busqueda_producto.html', {'form':form,'productos_listado':productos_listado} )

def maestro_producto(request):
    return render(request, 'Maestros/maestro.html')




@login_required
def eliminar_producto(request):
    id_producto = request.GET.get('producto_codigo')
    productos_listado = Producto.objects.all()
    if id_producto:
        productos_listado = Producto.objects.filter(producto_codigo=id_producto)
    else:
        productos_listado = Producto.objects.all()
        form = FormEliminarProducto()
    form = FormEliminarProducto()
    return render(request, 'Maestros/eliminar_producto.html', {'form':form,'productos_listado':productos_listado})

@login_required
def elimine_producto(request, id):
    producto_a_eliminar = Producto.objects.get(id=id)
    producto_a_eliminar.delete()
    return redirect('eliminar_producto')


@login_required
def editar_producto(request):
    id_producto = request.GET.get('producto_codigo')
    productos_listado = Producto.objects.all()
    if id_producto:
        productos_listado = Producto.objects.filter(producto_codigo=id_producto)
    else:
        productos_listado = Producto.objects.all()
        form = FormBusquedaProducto()
    form = FormBusquedaProducto()
    return render(request, 'Maestros/editar_producto.html' ,{'form':form,'productos_listado':productos_listado})

@login_required
def edite_producto(request, id):
    prod = Producto.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormEditarProducto(request.POST)
        if form.is_valid():
            prod.producto_cia = form.cleaned_data.get('producto_cia')
            prod.producto_codigo = form.cleaned_data.get('producto_codigo')
            prod.producto_descripcion = form.cleaned_data.get('producto_descripcion')
            prod.producto_costo = form.cleaned_data.get('producto_costo')
            prod.save()
            return redirect('editar_producto')
        
        else:
            return render(request, 'Maestros/edite_producto.html', {'form': form, 'producto':prod})

    form_producto = FormEditarProducto(initial={'producto_cia': prod.producto_cia,'producto_codigo': prod.producto_codigo, 'producto_descripcion': prod.producto_descripcion, 'producto_costo': prod.producto_costo})
    return render(request, 'Maestros/edite_producto.html', {'form':form_producto, 'producto':prod})