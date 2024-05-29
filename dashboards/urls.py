from django.urls import path
from dashboards.views import dash

urlpatterns = [
    path('dashboards',dash,name='dashboards'),
    # Tem um redirecionamento no /admin q ao clicar no botão dashboards vai pra essa pagina, está na linha 157 no settings.py
    #path('pagina',view,name='nome'),
]