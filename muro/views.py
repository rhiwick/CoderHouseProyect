from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
from datetime import datetime
from accounts.models import MasDatosUsuario as descripcion
from django.views.generic.list import ListView



# class Muro(ListView):
#     model = models.PosteosUsuarios
#     template_name = 'Muro/base.html'
    
#     def get_queryset(self):
        
#         object_list = self.model.objects.all()
        
#         return object_list

class Posteos(ListView):
    template_name = 'Muro/base.html'
    queryset = models.PosteosUsuarios.objects.all().order_by('-id')
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de post'
        
        return context


def muro(request):
    posteos = reversed(models.PosteosUsuarios.objects.all())
    return render(request, 'Muro/base.html', {'object_list':posteos} ) 
    
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
            
            return redirect('muro')
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


def backup(request):
    return render(request, 'base_backup.html')


def ver_autor(request, user):
    print(user)
    object_list = models.Autor.objects.filter(usuario=user)
    print(object_list)
        
    return render(request, 'Muro/autor.html', {'object_list':object_list})