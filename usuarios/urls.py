from django.urls import path
from usuarios.views import login, cadastro,logout_view
 

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout/', logout_view, name='logout'),
]