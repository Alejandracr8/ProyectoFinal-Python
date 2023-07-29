from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cilindro
from .forms import CilindroForm
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.http import HttpRequest, HttpResponse

def listar_cilindros(request: HttpRequest) ->  HttpResponse:
    cilindros = Cilindro.objects.all()
    return render(request, 'listar_cilindros.html', {'cilindros': cilindros})

def crear_cilindro(request:HttpRequest) ->  HttpResponse:
    if request.method == 'POST':
        form = CilindroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cilindros')
    else:
        form = CilindroForm()
    return render(request, 'crear_cilindro.html', {'form': form})

def editar_cilindro(request: HttpRequest, cilindro_id) ->  HttpResponse:
    cilindro = get_object_or_404(Cilindro, pk=cilindro_id)
    if request.method == 'POST':
        form = CilindroForm(request.POST, instance=cilindro)
        if form.is_valid():
            form.save()
            return redirect('listar_cilindros')
    else:
        form = CilindroForm(instance=cilindro)
    return render(request, 'editar_cilindro.html', {'form': form})

def borrar_cilindro(request: HttpRequest, cilindro_id) ->  HttpResponse:
    cilindro = get_object_or_404(Cilindro, pk=cilindro_id)
    if request.method == 'POST':
        cilindro.borrar()
        return redirect('listar_cilindros')
    return render(request, 'borrar_cilindro.html', {'cilindro': cilindro})
