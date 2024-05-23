from django import forms
from . import models



class pacienteForm(forms.ModelForm):
    class Meta:
        model = models.Pacientes
        fields = "__all__"

