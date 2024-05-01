from django.shortcuts import render, redirect
from . import models, forms
# Create your views here.

def home(request):
    consulta_clientes = models.Cliente.objects.all()
    context = {"clientes": consulta_clientes}
    return render(request, "app/index.html", context)

def pacientes(request):
    if request.method == "POST":
        form = forms.pacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app:home")
    else:
        form = forms.pacienteForm()

    return render(request, "app/registropacientes.html", context = {"form":form})

