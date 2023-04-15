from django.shortcuts import render, redirect
from .models import Receita, Despesa

def index(request):
    return render(request, 'index.html')

def cadastrar(request):
    if request.method == 'POST':

        tipo = request.POST.get('tipo')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        data = request.POST.get('data')
        comprovante = request.FILES.get('comprovante')

        # Verifica se é receita ou despesa. A depender, persiste no BD.

        if tipo == 'receita':
            receita = Receita(
                descricao=descricao,
                valor=valor,
                categoria=categoria,
                data=data,
                comprovante=comprovante
            )
            receita.save()
        else:
            despesa = Despesa(
            descricao=descricao,
            valor=valor,
            categoria=categoria,
            data=data,
            comprovante=comprovante
        )
            receita.save()

        # Redirecionar para a página de listar
        return redirect('listar')

    return render(request, 'cadastrar.html')

def listar(request):
    receitas = Receita.objects.all()

    return render(request, 'listar.html', {"receitas" : receitas})

def editar(request):
    return render(request, 'editar.html')

def excluir(request):
    return render(request, 'excluir.html')
