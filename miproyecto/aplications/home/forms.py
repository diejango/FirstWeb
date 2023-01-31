from django import forms 
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = ('__all__')
        widgets={
            'titulo' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese texto aqui'
                }
            )
        }
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if titulo == 'pinga':
            raise forms.ValidationError('oe ctmr no seas malcriado')
    
    
        return titulo