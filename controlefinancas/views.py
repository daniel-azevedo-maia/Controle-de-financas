from django.shortcuts import render, redirect
from .models import Receita, Despesa
from django.core.files.storage import FileSystemStorage
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

import pandas as pd
import numpy as np

def index(request):
    return render(request, 'index.html')

@login_required
def cadastrar(request):
    if request.method == 'POST':

        tipo = request.POST.get('tipo')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        valor = Decimal(valor) if valor else None
        categoria = request.POST.get('categoria')
        data = request.POST.get('data')
        comprovante = request.FILES.get('comprovante')

        # Verifica se é receita ou despesa. A depender, persiste no BD.

        if tipo == 'receita':
            receita = Receita(
                user=request.user,
                descricao=descricao,
                valor=valor,
                categoria=categoria,
                data=data,
                comprovante=comprovante
            )
            receita.save()
        else:
            despesa = Despesa(
                user=request.user,
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


@login_required
def listar(request):
    receitas = Receita.objects.filter(user=request.user)  # Filtra as receitas do usuário atual
    despesas = Despesa.objects.filter(user=request.user)  # Filtra as despesas do usuário atual

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

@login_required
def excluir(request, id, tipo):

    if tipo == 'receita':
        receita = Receita.objects.get(pk=id)
        receita.delete()

    else:

        despesa = Despesa.objects.get(pk=id)
        despesa.delete()

    return redirect('listar')

@login_required
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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def exportarExcel(request):
    receitas = Receita.objects.all()

    dadosReceita = {
        'ID': [receita.id for receita in receitas],
        'DESCRIÇÃO': [receita.descricao for receita in receitas],
        'VALOR': [receita.valor for receita in receitas]
    }


    despesas = Despesa.objects.all()

    dadosDespesa = {
        'ID': [despesa.id for despesa in despesas],
        'DESCRIÇÃO': [despesa.descricao for despesa in despesas],
        'VALOR': [despesa.valor for despesa in despesas]
    }

    df_receitas = pd.DataFrame(dadosReceita)
    df_despesas = pd.DataFrame(dadosDespesa)

     # Criar um novo arquivo Excel usando 'openpyxl'
    file_name = 'registros_receitas_despesas.xlsx'
    wb = Workbook()

    # Escrever os dados do DataFrame de receitas na primeira planilha
    ws_receitas = wb.active
    ws_receitas.title = "Receitas"
    for r in dataframe_to_rows(df_receitas, index=False, header=True):
        ws_receitas.append(r)

    ws_despesas = wb.create_sheet("Despesas")
    for r in dataframe_to_rows(df_despesas, index=False, header=True):
        ws_despesas.append(r)

    wb.save(file_name)

    with open(file_name, 'rb') as excel_file:
        response = HttpResponse(excel_file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={file_name}'
        return response