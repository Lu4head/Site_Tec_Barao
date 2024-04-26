from django.urls import path
from usuarios import views


urlpatterns = [
    path('login/', views.login, name='login'), # Tela de login
    path('cadastro/', views.cadastro, name='cadastro'), # Tela de cadastro
    path('logout/',  views.logout, name="logout") # Botão de logout que redireciona para tela de login
]