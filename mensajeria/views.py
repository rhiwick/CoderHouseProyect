from django.shortcuts import render, redirect

from datetime import datetime
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


@login_required
def ver_mensajes(request):
    
    user = request.user
    
    object_list = reversed(models.Mensajeria.objects.filter(a_user=user))
    
    return render(request, 'mensajeria/mensajes.html', {'object_list':object_list})



@login_required
def enviar_mensaje(request):
    
    user = request.user
    form = forms.FormCrearMensaje()
    mensajes = models.Mensajeria()

    
    if request.method == 'POST':
        form = forms.FormCrearMensaje(request.POST)
        
        
        
        if form.is_valid():
            data = form.cleaned_data
            mensajes.mensaje = data.get('mensaje')
            mensajes.a_user = data.get('a_user')
            mensajes.de_user = user.username
            mensajes.fecha_mensaje = datetime.now()
          
        
            mensajes.save()
            
            return redirect('mensajes')
        else:
            return render(request,'mensajeria/enviar_mensajes.html',{'form':form})
    form = forms.FormCrearMensaje(
        initial = {
            'a_user': '',
            'mensaje': '',
                    } )
    return render(request, 'mensajeria/enviar_mensajes.html',{'form':form})