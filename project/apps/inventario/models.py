from django.db import models

# Create your models here.
from django.db import models

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
   

class Cilindro(models.Model):
    numero_serie = models.CharField(max_length=100, unique=True)
    tipo_gas = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)  