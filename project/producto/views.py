from django.shortcuts import render

from . import models
# Create your views here.

def home(request):
    consulta_productos = models.producto_categoria.objects.all()
    context = {"productos": consulta_productos}
    return render(request, "producto/index.html", context)