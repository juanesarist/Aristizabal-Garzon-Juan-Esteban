from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(null = True, max_length=50, verbose_name="pais")

    def __str__(self):
        return self.nombre
    
    class meta:
        verbose_name_plural = "Paises"

class Cliente(models.Model):
    nombre = models. CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.IntegerField(null=True)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL,blank=True, null=True, verbose_name="Pais de origen")

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    
