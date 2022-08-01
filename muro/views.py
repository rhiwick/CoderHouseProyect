from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
from datetime import datetime
from django.views.generic.list import ListView



# class Muro(ListView):
#     model = models.PosteosUsuarios
#     template_name = 'Muro/base.html'
    
#     def get_queryset(self):
        
#         object_list = self.model.objects.all()
        
#         return object_list


def muro(request):
    posteos = models.PosteosUsuarios.objects.all()
    return render(request, 'Muro/base.html', {'object_list':posteos} ) 
    
@login_required
def postear(request):
    user = request.user
    datos_post = models.PosteosUsuarios()
    
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