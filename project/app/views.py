from django.shortcuts import render, redirect
from . import models, forms
# Create your views here.

def mostrar_pacientes(request):
    consulta_pacientes = models.Pacientes.objects.all()
    context = {"pacientes": consulta_pacientes}
    return render(request, "app/mostrarpacientes.html", context)

def mostrar_personal_medico(request):
    consulta_medicos = models.Medicos.objects.all()
    context = {"medicos": consulta_medicos}
    return render(request, "app/mostrarmedicos.html", context)

def mostrar_personal_adm(request):
    consulta_personal_adm = models.Pacientes.objects.all()
    context = {"personaladm": consulta_personal_adm}
    return render(request, "app/mostrarpersonaladm.html", context)

def pacientes(request):
    if request.method == "POST":
        form = forms.pacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app:home")
    else:
        form = forms.pacienteForm()

    return render(request, "app/registropacientes.html", context = {"form":form})

def personal_medico(request):
    if request.method == "POST":
            form = forms.medicosForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("app:home")
    else:
            form = forms.medicosForm()

    return render(request, "app/registromedico.html", context = {"form":form})

def personal_adm(request):
    if request.method == "POST":
            form = forms.personaladmForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("app:home")
    else:
            form = forms.personaladmForm()

    return render(request, "app/registropersonaladm.html", context = {"form":form})