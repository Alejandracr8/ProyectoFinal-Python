from django import forms
from .models import Cilindro

class CilindroForm(forms.ModelForm):
    class Meta:
        model = Cilindro
        fields = ['numero_serie', 'tipo_gas', 'capacidad', 'ubicacion']


