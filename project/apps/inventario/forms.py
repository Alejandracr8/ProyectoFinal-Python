from django import forms
from .models import Cilindro, Ubicacion

class CilindroForm(forms.ModelForm):
    class Meta:
        model = Cilindro
        fields = ['numero_serie', 'tipo_gas', 'capacidad', 'ubicacion', 'fecha_ingreso']


class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['nombre', 'direccion']

