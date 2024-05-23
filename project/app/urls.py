
from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    #path('', views.mostrar_pacientes, name="home"),
    path('pacientes', views.pacientes_create.as_view(), name="registro_pacientes"),
    path("aboutus/", views.about_us, name="about_us"),
    #path("personaladm", views.personal_adm, name="registro_personaladm"),
    #path('mostarpacientes', views.mostrar_pacientes, name="mostrar_pacientes"),
    path('buscarpacientes', views.buscar_pacientes.as_view(), name="buscar_pacientes"),
    path('mostarpacientes/detail/<int:pk>', views.buscar_pacientes_info.as_view(), name="mostrar_pacientes_detail"),
    path('mostarpacientes/update/<int:pk>', views.buscar_pacientes_update.as_view(), name="mostrar_pacientes_update"),
    path('mostarpacientes/delete/<int:pk>', views.buscar_pacientes_delete.as_view(), name="mostrar_pacientes_delete"),
    #path("mostarmedicos", views.mostrar_personal_medico, name="mostrar_medicos"),
    #path("mostrarpersonaladm", views.mostrar_personal_adm, name="mostrar_personaladm"),
    

    
]