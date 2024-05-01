from django import forms
from . import models



class pacienteForm(forms.ModelForm):
    class Meta:
        model = models.Pacientes
        fields = "__all__"

class medicosForm(forms.ModelForm):
    class Meta:
        model = models.Medicos
        fields = "__all__"

class personaladmForm(forms.ModelForm):
    class Meta:
        model = models.PersonalAdm
        fields = "__all__"