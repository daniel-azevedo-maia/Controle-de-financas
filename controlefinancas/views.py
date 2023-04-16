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
            despesa.save()

        # Redirecionar para a página de listar
        return redirect('listar')

    return render(request, 'cadastrar.html')

def listar(request):
    receitas = Receita.objects.all()
    despesas = Despesa.objects.all()

    receita_total = despesa_total = 0
    for r in range(0, receitas.count()):
        receita_total += receitas[r].valor

    for d in range(0, despesas.count()):
        despesa_total += despesas[d].valor
    
    saldo = receita_total - despesa_total

    return render(request, 'listar.html', 
                  {"receitas" : receitas, 
                   "despesas" : despesas, 
                   "receita_total" : receita_total,
                   "despesa_total" : despesa_total,
                   "saldo" : saldo})

def editar(request):
    return render(request, 'editar.html')

def excluir(request):
    return render(request, 'excluir.html')
