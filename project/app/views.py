from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
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



def personal_medico(request):
    if request.method == "POST":
            form = forms.medicosForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("app:registro_medicos")
    else:
            form = forms.medicosForm()

    return render(request, "app/registromedico.html", context = {"form":form})

def personal_adm(request):
    if request.method == "POST":
            form = forms.personaladmForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("app:registro_personaladm")
    else:
            form = forms.personaladmForm()

    return render(request, "app/registropersonaladm.html", context = {"form":form})

# def buscar_pacientes(request):
#      consulta = request.GET.get("consulta", None)
#      if consulta:
#          print(consulta)
#          query = models.Pacientes.objects.filter(cedula__icontains=consulta)
#      else:
#          query = models.Pacientes.objects.all()
#      context = {"pacientes": query}
#      return render(request, "app/mostrarpacientes.html", context)

class buscar_pacientes(ListView):
     model = models.Pacientes
     context_object_name = "pacientes"
     template_name = "app/mostrarpacientes.html"


# def buscar_pacientes_info(request, pk):
#      query = models.Pacientes.objects.get(id=pk)
#      return render(request, "app/mostrarpacientes_detail.html", {"paciente":query})

class buscar_pacientes_info(DetailView):
     model = models.Pacientes
     context_object_name = "paciente"
     template_name = "app/mostrarpacientes_detail.html"

class pacientes_create(CreateView):
     model = models.Pacientes
     form_class = forms.pacienteForm
     template_name = "app/registropacientes.html"
     success_url = reverse_lazy("app:registro_pacientes")
     

# def pacientes(request):
#     if request.method == "POST":
#         form = forms.pacienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("app:registro_pacientes")
#     else:
#         form = forms.pacienteForm()

#     return render(request, "app/registropacientes.html", context = {"form":form})

class buscar_pacientes_update(UpdateView):
     model = models.Pacientes
     form_class = forms.pacienteForm
     template_name = "app/registropacientes.html"
     success_url = reverse_lazy("app:buscar_pacientes")

# def buscar_pacientes_update(request, pk = int):
#     query = models.Pacientes.objects.get(id=pk) 
#     if request.method == "POST":
#         form = forms.pacienteForm(request.POST, instance=query)
#         if form.is_valid():
#             form.save()
#             return redirect("app:home")
#     else:
#         form = forms.pacienteForm(instance=query)

#     return render(request, "app/mostrarpacientes_update.html", context = {"form":form})

# def buscar_pacientes_delete(request, pk = int):
#     query = models.Pacientes.objects.get(id=pk) 
#     if request.method == "POST":
#         query.delete()
#         return redirect("app:home")
#     return render(request, "app/mostrarpacientes_delete.html", context = {"paciente":query})

class buscar_pacientes_delete(DeleteView):
    model = models.Pacientes
    template_name = "app/mostrarpacientes_delete.html"
    success_url = reverse_lazy("app:buscar_pacientes")