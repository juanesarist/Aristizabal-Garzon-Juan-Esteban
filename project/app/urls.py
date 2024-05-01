
from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.mostrar_pacientes, name="home"),
    path('pacientes', views.personal_medico, name="registro_pacientes"),
    path("medicos", views.pacientes, name="registro_medicos"),
    path("personaladm", views.personal_adm, name="registro_personaladm"),
    path('mostarpacientes', views.mostrar_personal_medico, name="mostrar_pacientes"),
    path("mostarmedicos", views.mostrar_pacientes, name="mostrar_medicos"),
    path("mostrarpersonaladm", views.mostrar_personal_adm, name="mostrar_personaladm"),
    

    
]