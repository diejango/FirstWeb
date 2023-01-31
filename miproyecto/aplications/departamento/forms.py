from django import forms 
from .models import Departamento

class newDepartamentoForm(forms.Form):
    """Form definition for Departamento."""
    nombre= forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    departamento=forms.CharField(max_length=50)
    shortname=forms.CharField (max_length=20)

    #class Meta:
     #   """Meta definition for Departamentoform."""

      #  model = Departamento
       # fields = ('',)
