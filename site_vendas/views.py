from django.shortcuts import render, get_object_or_404
from site_vendas.models import DIM_Produto



def index(request): # Define view para a página home
    produtos = DIM_Produto.objects.filter(Produto_ativo_PRODUTO = True) # Lista objetos da classse DIM_Produto no banco filtrando pelos objetos que tenham o parâmetro Produto_ativo = True
    # Os produtos trazidos acima serão os produtos a serem exibidos na página inicial, eles são puxados do banco e adicionados ao site dinâmicamente
    return render(request, 'site_vendas/index.html', {"cards":produtos})

def produto(request, produto_id): # Define view para a página de produto
    produto = get_object_or_404(DIM_Produto, pk= produto_id) # Ao selecionar um produto na página home o usuário será direcionado à página do produto selecionado filtando pela pk = produto_id definida no html
    return render(request,'site_vendas/produto.html',{'produto': produto})


def cart(request): # Define view para a página do carrinho de compras
    return render(request,'site_vendas/cart.html')