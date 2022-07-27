from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from distribucion.models import Transporte
# Create your views here.

class CearTransporte(LoginRequiredMixin, CreateView):
    model = Transporte
    template_name = 'Distribucion/crear_transporte.html'
    success_url = '/distribucion/crear_transporte'
    fields = ['codigo', 'tipo', 'marca', 'modelo', 'tara', 'ejes']
    
    
class EditarTransporte(LoginRequiredMixin, ListView):
    model = Transporte
    template_name = 'Distribucion/editar_transporte.html'
    success_url = '/distribucion/editar_transporte'
    fields = ['codigo', 'tipo', 'marca', 'modelo', 'tara', 'ejes']
    
    
class EliminarTransporte(LoginRequiredMixin, ListView):
    model = Transporte
    template_name = 'Distribucion/eliminar_transporte.html'
    success_url = '/distribucion/eliminar_transporte'
    
    
class EditeTransporte(LoginRequiredMixin, UpdateView):
    model = Transporte
    template_name = 'Distribucion/edite_transporte.html'
    success_url = '/distribucion/editar_transporte'
    fields = ['codigo', 'tipo', 'marca', 'modelo', 'tara', 'ejes']

    
    
class ElimineTransporte(LoginRequiredMixin, DeleteView):
    model = Transporte
    template_name = 'Distribucion/elimine_transporte.html'
    success_url = '/distribucion/eliminar_transporte'
    
    
class BusquedaTransporte(LoginRequiredMixin, ListView):
    model = Transporte
    template_name = 'Distribucion/busqueda_transporte.html'
    success_url = '/distribucion/busqueda_transporte'
    
    
def distribucion(request):
    return render(request, 'Distribucion/distribucion.html')