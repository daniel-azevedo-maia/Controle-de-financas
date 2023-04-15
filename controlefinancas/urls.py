from .views import index, cadastrar, listar, editar, excluir
from django.urls import path

urlpatterns = [
    path('', index),
    path('cadastrar', cadastrar, name='cadastrar'),
    path('listar', listar, name='listar'),
    path('editar', editar, name='editar'),
    path('excluir', excluir, name='excluir')
]