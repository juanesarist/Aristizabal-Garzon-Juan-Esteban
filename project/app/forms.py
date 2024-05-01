from django import forms
from . import models

# class pacienteForm(forms.Form):
#     nombre = forms.CharField()

class pacienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"