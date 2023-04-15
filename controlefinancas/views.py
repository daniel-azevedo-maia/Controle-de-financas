from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')

def listar(request):
    return render(request, 'listar.html')

def editar(request):
    return render(request, 'editar.html')