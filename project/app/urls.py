
from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('pacientes', views.pacientes_create.as_view(), name="registro_pacientes"),
    path("aboutus/", views.about_us, name="about_us"),
    path('buscarpacientes', views.buscar_pacientes.as_view(), name="buscar_pacientes"),
    path('mostarpacientes/detail/<int:pk>', views.buscar_pacientes_info.as_view(), name="mostrar_pacientes_detail"),
    path('mostarpacientes/update/<int:pk>', views.buscar_pacientes_update.as_view(), name="mostrar_pacientes_update"),
    path('mostarpacientes/delete/<int:pk>', views.buscar_pacientes_delete.as_view(), name="mostrar_pacientes_delete"),

    

    
]