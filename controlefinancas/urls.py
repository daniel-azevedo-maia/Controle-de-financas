from .views import index, cadastrar, listar, editar
from django.urls import path

urlpatterns = [
    path('', index),
    path('cadastrar', cadastrar, name='cadastrar'),
    path('listar', listar, name='listar'),
    path('editar', editar, name='editar')
]