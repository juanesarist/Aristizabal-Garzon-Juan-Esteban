from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Pacientes(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    cedula = models.IntegerField(null=True)
    telefono = models.IntegerField(null=True)
    nacimiento = models.DateField(null=True)
    pais_origen = models.CharField(max_length=50, null=True, verbose_name="Pais de origen")
    names = (("Hombre","Hombre"),("Mujer","Mujer"))
    sexo = models.CharField(max_length= 50, choices=names, null=True)
    tipo_consulta = (("Consulta general","Consulta general"), ("Revision examenes","Revision examenes"), ("Psicologia","Psicologia"))
    consulta = models.CharField(max_length= 200, choices=tipo_consulta, null=True)
    descripcion = models.CharField(max_length=250, null=True)
    avatar = models.ImageField(upload_to="avatares",null=True, blank=True)
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    

    

