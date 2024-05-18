
from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.buscar_pacientes, name="home"),
    path('pacientes', views.pacientes, name="registro_pacientes"),
    path("medicos", views.personal_medico, name="registro_medicos"),
    path("personaladm", views.personal_adm, name="registro_personaladm"),
    path('mostarpacientes', views.mostrar_pacientes, name="mostrar_pacientes"),
    path('mostarpacientes/detail/<int:pk>', views.buscar_pacientes_info, name="mostrar_pacientes_detail"),
    path('mostarpacientes/update/<int:pk>', views.buscar_pacientes_update, name="mostrar_pacientes_update"),
    path('mostarpacientes/delete/<int:pk>', views.buscar_pacientes_delete, name="mostrar_pacientes_delete"),
    path("mostarmedicos", views.mostrar_personal_medico, name="mostrar_medicos"),
    path("mostrarpersonaladm", views.mostrar_personal_adm, name="mostrar_personaladm"),
    

    
]