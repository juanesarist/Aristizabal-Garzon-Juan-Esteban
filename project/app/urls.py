
from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.home, name="home"),
    path("pacientes/registro", views.pacientes, name="pacientes_registro"),
    

    
]