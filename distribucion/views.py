from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from distribucion.forms import FormBusquedaTransporte

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
    
    def get_queryset(self):
        transporte = self.request.GET.get('codigo', '')
        if transporte:
            object_list = self.model.objects.filter(codigo__icontains=transporte)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FormBusquedaTransporte()
        return context
    
    
class EliminarTransporte(LoginRequiredMixin, ListView):
    model = Transporte
    template_name = 'Distribucion/eliminar_transporte.html'
    success_url = '/distribucion/eliminar_transporte'
    
    def get_queryset(self):
        transporte = self.request.GET.get('codigo', '')
        if transporte:
            object_list = self.model.objects.filter(codigo__icontains=transporte)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FormBusquedaTransporte()
        return context
    
    
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
    
    def get_queryset(self):
        transporte = self.request.GET.get('codigo', '')
        if transporte:
            object_list = self.model.objects.filter(codigo__icontains=transporte)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FormBusquedaTransporte()
        return context

    
    
def distribucion(request):
    return render(request, 'Distribucion/distribucion.html')