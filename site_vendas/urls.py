from django.urls import path
from site_vendas.views import index, produto, cart

urlpatterns = [
    path('', index, name='index'), # Home do site
    path('produto/<str:nome_produto>', produto, name='produto'), # Tela individual de cada produto
    path('cart', cart, name='cart'), # Tela do carrinho de compras
]