from django.contrib import admin
from .models import Receita, Despesa

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data', 'categoria')
    list_display_links = ('descricao',)
    search_fields = ('descricao', 'valor', 'data',)
    list_per_page: 2

admin.site.register(Receita, ListandoReceitas)

class ListandoDespesas(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data', 'categoria')
    list_display_links = ('descricao',)
    search_fields = ('descricao', 'valor', 'data',)
    list_per_page: 2

admin.site.register(Despesa, ListandoDespesas)