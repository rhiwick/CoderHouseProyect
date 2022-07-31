from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
from datetime import datetime
from django.views.generic.list import ListView

# Create your views here.
class Muro(ListView):
    model = models.PosteosUsuarios
    template_name = 'Muro/base.html'
    
    def get_queryset(self):
        posteos = self.request.GET.get('id', '')
        if posteos:
            object_list = self.model.objects.filter(id__icontains=posteos)
        else:
            object_list = self.model.objects.all()
        print(object_list)
        return object_list

    
@login_required
def postear(request):
    user = request.user
    datos_post, _ = models.PosteosUsuarios.objects.get_or_create(autor=user)
    
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
            user.save()
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