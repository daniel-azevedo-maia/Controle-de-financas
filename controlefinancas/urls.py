from .views import index, cadastrar, listar, excluir, atualizar
from django.urls import path

urlpatterns = [
    path('', index),
    path('cadastrar', cadastrar, name='cadastrar'),
    path('atualizar', atualizar, name='atualizar'),
    path('listar', listar, name='listar'),
    path('<str:tipo>/excluir/<int:id>', excluir, name='excluir')
]