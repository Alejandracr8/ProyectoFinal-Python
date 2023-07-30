from datetime import date
from django.shortcuts import render, redirect
from .models import Cilindro
from .forms import CilindroForm
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.http import HttpRequest, HttpResponse
from typing import Any

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from . import forms, models


@login_required
def index(request):
    return render(request, "inventario/index.html")


class listar_cilindros(ListView):
    model = models.Cilindro

class crear_cilindro(CreateView):
    model = models.Cilindro
    form_class = forms.CilindroForm
    success_url = reverse_lazy("cilindro:listar_cilindro")

class borrar_cilindro(DeleteView):
    model = models.Cilindro
    success_url = reverse_lazy("cilindro:listar_cilindro")

class editar_cilindro(UpdateView):
    model = models.Cilindro
    form_class = forms.CilindroForm
    success_url = reverse_lazy("cilindro:listar_cilindro")



class listar_ubicacion(ListView):
    model = models.Ubicacion

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Ubicacion.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Ubicacion.objects.all()
        return object_list


class crear_ubicacion(CreateView):
    model = models.Ubicacion
    form_class = forms.UbicacionForm
    success_url = reverse_lazy("cilindro:listar_ubicacion")

class editar_ubicacion(UpdateView):
    model = models.Ubicacion
    form_class = forms.UbicacionForm
    success_url = reverse_lazy("producto:producto_list")


class borrar_ubicacion(DeleteView):
    model = models.Ubicacion
    success_url = reverse_lazy("cilindro:listar_uboicacion")