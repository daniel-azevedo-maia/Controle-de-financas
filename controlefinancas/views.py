from django.shortcuts import render, redirect
from .models import Receita, Despesa
from django.core.files.storage import FileSystemStorage


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
                  {"receitas": receitas,
                   "despesas": despesas,
                   "receita_total": receita_total,
                   "despesa_total": despesa_total,
                   "saldo": saldo})


def excluir(request, id, tipo):

    if tipo == 'receita':
        receita = Receita.objects.get(pk=id)
        receita.delete()

    else:

        despesa = Despesa.objects.get(pk=id)
        despesa.delete()

    return redirect('listar')


def atualizar(request):


    if request.POST.get('tipo') == 'receita':
        receitaid = request.POST.get('id')
        receita = Receita.objects.get(pk=receitaid)
        receita.descricao = request.POST.get('descricao')
        receita.valor = request.POST.get('valor')
        receita.categoria = request.POST.get('categoria')
        receita.data = request.POST.get('data')
        receita.comprovante = request.POST.get('comprovante')

        comprovante_file = request.FILES.get('comprovante')
        if comprovante_file:
            fs = FileSystemStorage()
            filename = fs.save(comprovante_file.name, comprovante_file)
            receita.comprovante = filename

        receita.save()

    elif request.POST.get('tipo') == 'despesa':
        despesaid = request.POST.get('id')
        despesa = Despesa.objects.get(pk=despesaid)
        despesa.descricao = request.POST.get('descricao')
        despesa.valor = request.POST.get('valor')
        despesa.categoria = request.POST.get('categoria')
        despesa.data = request.POST.get('data')
        despesa.comprovante = request.POST.get('comprovante')

        comprovante_file = request.FILES.get('comprovante')
        if comprovante_file:
            fs = FileSystemStorage()
            filename = fs.save(comprovante_file.name, comprovante_file)
            despesa.comprovante = filename

        despesa.save()

    return redirect('listar')
