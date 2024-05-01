from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Medicos)
admin.site.register(models.Pacientes)
admin.site.register(models.PersonalAdm)