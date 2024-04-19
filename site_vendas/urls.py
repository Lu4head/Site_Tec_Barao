from django.urls import path
from site_vendas.views import index, produto, cart

urlpatterns = [
    path('', index, name='index'),
    path('produto/<int:produto_id>', produto, name='produto'),
    path('cart', cart, name='cart'),
]