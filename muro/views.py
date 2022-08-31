from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
from datetime import datetime
from accounts.models import MasDatosUsuario as descripcion
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



class Posteos(ListView):
    template_name = 'Muro/base.html'
    queryset = models.PosteosUsuarios.objects.all().order_by('-id')
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de post'
        
        return context


class Misposteos(ListView):
        
        template_name = 'Muro/base_misposteos.html'
        #queryset = models.PosteosUsuarios.objects.filter(autor=current_user)
        paginate_by = 5
        def get_queryset(self, *args, **kwargs):
            return models.PosteosUsuarios.objects.filter(autor=self.request.user)
    
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['message'] = 'Listado de post'
        
            return context

class EliminePosteo(LoginRequiredMixin, DeleteView):
        model = Posteos
        template_name = 'Muro/base_misposteos.html'
        #success_url = '/blog/misposteos/'
        def get_queryset(self, *args, **kwargs):
            return models.PosteosUsuarios.objects.filter(autor=self.request.user)
    
        # def get_context_data(self, **kwargs):
        #     context = super().get_context_data(**kwargs)
        #     context['message'] = 'Listado de post'
        
        #     return context
    
@login_required
def postear(request):
    
    user = request.user
    datos_post = models.PosteosUsuarios()
    datos_autor = models.Autor()

    
    if request.method == 'POST':
        form = forms.FormCrearPosteo(request.POST, request.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            datos_post.titulo = data.get('titulo')
            datos_post.sub_titulo = data.get('sub_titulo')
            datos_post.posteo = data.get('posteo')
            datos_post.imagen = data.get('imagen')
            datos_post.fecha_posteo = datetime.now()
            datos_post.autor = user.username
            datos_post.save()
            
            
            mas_datos_usuario, _ = descripcion.objects.get_or_create(user=user)
            datos_autor.descripcion = mas_datos_usuario.descripcion
            datos_autor.nombre = user.first_name
            datos_autor.apellido = user.last_name
            datos_autor.correo = user.email
            datos_autor.usuario = user.username
            datos_autor.id = user.id
            
            datos_autor.save()
            
            return redirect('posteos')
        else:
            return render(request,'Muro/crear_post.html',{'form':form})
    form = forms.FormCrearPosteo(
        initial = {
            'titulo': '',
            'sub_titulo': '',
            'posteo' : '',
            'imagen' : '',
            
                    } )
    return render(request, 'Muro/crear_post.html',{'form':form})



def ver_autor(request, user):
    
    object_list = models.Autor.objects.filter(usuario=user)
    
    return render(request, 'Muro/autor.html', {'object_list':object_list})


