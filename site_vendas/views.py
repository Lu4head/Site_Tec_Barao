from django.shortcuts import render, get_object_or_404
from site_vendas.models import DIM_Produto



def index(request):
    produtos = DIM_Produto.objects.filter(Produto_ativo_PRODUTO = True)

    return render(request, 'site_vendas/index.html', {"cards":produtos})

def produto(request, produto_id):
    produto = get_object_or_404(DIM_Produto, pk= produto_id)
    return render(request,'site_vendas/produto.html',{'produto': produto})


def cart(request):
    return render(request,'site_vendas/cart.html')