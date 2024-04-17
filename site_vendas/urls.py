from django.urls import path
from site_vendas.views import index

urlpatterns = [
    path('', index, name='index'),
]