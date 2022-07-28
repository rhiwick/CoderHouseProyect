from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def muro(request):
    return render(request, "muro/base.html")
    