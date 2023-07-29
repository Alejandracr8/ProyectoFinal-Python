
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cilindro
from .forms import CilindroForm
from django.http import HttpResponse
from django.http.request import HttpRequest

def list_cilindros(request):
    cilindros = Cilindro.objects.all()
    return render(request, 'list_cilindros.html', {'cilindros': cilindros})

def create_cilindro(request):
    if request.method == 'POST':
        form = CilindroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_cilindros')
    else:
        form = CilindroForm()
    return render(request, 'create_cilindro.html', {'form': form})

def edit_cilindro(request, cilindro_id):
    cilindro = get_object_or_404(Cilindro, pk=cilindro_id)
    if request.method == 'POST':
        form = CilindroForm(request.POST, instance=cilindro)
        if form.is_valid():
            form.save()
            return redirect('list_cilindros')
    else:
        form = CilindroForm(instance=cilindro)
    return render(request, 'edit_cilindro.html', {'form': form})

def delete_cilindro(request, cilindro_id):
    cilindro = get_object_or_404(Cilindro, pk=cilindro_id)
    if request.method == 'POST':
        cilindro.delete()
        return redirect('list_cilindros')
    return render(request, 'delete_cilindro.html', {'cilindro': cilindro})
