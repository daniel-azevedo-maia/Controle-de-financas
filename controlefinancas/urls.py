from .views import index, cadastrar, listar, excluir, atualizar, exportarExcel
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', index, name="index"),
    path('cadastrar', cadastrar, name='cadastrar'),
    path('atualizar', atualizar, name='atualizar'),
    path('listar', listar, name='listar'),
    path('<str:tipo>/excluir/<int:id>', excluir, name='excluir'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('exportarExcel', exportarExcel, name="exportarExcel")


]