from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def about_us(request):
    return render(request, "app/aboutus.html")

class buscar_pacientes(LoginRequiredMixin, ListView):
     model = models.Pacientes
     context_object_name = "pacientes"
     template_name = "app/mostrarpacientes.html"

     def get_queryset(self):
        if self.request.GET.get("consulta"):
               consulta = self.request.GET.get("consulta")
               pacientes = models.Pacientes.objects.filter(cedula__icontains=consulta)
        else:
          pacientes = models.Pacientes.objects.all()
        return pacientes




class buscar_pacientes_info(LoginRequiredMixin, DetailView):
     model = models.Pacientes
     context_object_name = "paciente"
     template_name = "app/mostrarpacientes_detail.html"

class pacientes_create(LoginRequiredMixin, CreateView):
     model = models.Pacientes
     form_class = forms.pacienteForm
     template_name = "app/registropacientes.html"
     success_url = reverse_lazy("app:registro_pacientes")
     



class buscar_pacientes_update(LoginRequiredMixin, UpdateView):
     model = models.Pacientes
     form_class = forms.pacienteForm
     template_name = "app/registropacientes.html"
     success_url = reverse_lazy("app:buscar_pacientes")



class buscar_pacientes_delete(LoginRequiredMixin, DeleteView):
    model = models.Pacientes
    template_name = "app/mostrarpacientes_delete.html"
    success_url = reverse_lazy("app:buscar_pacientes")