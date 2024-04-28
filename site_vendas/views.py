from django.shortcuts import render, get_object_or_404
from site_vendas.models import DIM_Produto, FAT_item_nota
from .forms import camisetaForms , canecaforms , tiranteForms , blusaForms , shortForms

def index(request): # Define view para a página home
    produtos = DIM_Produto.objects.filter(Produto_ativo_PRODUTO = True) # Lista objetos da classse DIM_Produto no banco filtrando pelos objetos que tenham o parâmetro Produto_ativo = True
    # Os produtos trazidos acima serão os produtos a serem exibidos na página inicial, eles são puxados do banco e adicionados ao site dinâmicamente
    return render(request, 'site_vendas/index.html', {"cards":produtos})

def produto(request, nome): # Define view para a página de produto
    produto = get_object_or_404(DIM_Produto, Nome_PRODUTO=nome) # Ao selecionar um produto na página home o usuário será direcionado à página do produto selecionado filtando pela pk = produto_id definida no html
    form = 0
    match produto.Tipo_PRODUTO:
        case "camiseta":
            form = camisetaForms()
        case "caneca":
            form = canecaforms()
        case "blusa":
            form = blusaForms()
        case "tirante":
            form = tiranteForms()
        case "short":
            form = shortForms()

    if request.method == 'POST':
        match produto.Tipo_PRODUTO:
            case "camiseta":
                form = camisetaForms(request.POST)
            case "caneca":
                form = canecaforms(request.POST)
            case "blusa":
                form = blusaForms(request.POST)
            case "tirante":
                form = tiranteForms(request.POST)
            case "short":
                form = shortForms(request.POST)

        if form.is_valid():
            quantidade = form.cleaned_data.get('quantidade')
            tamanho = form.cleaned_data.get('tamanho')
            nome_estampa = form.cleaned_data.get('nome')
            rede_social = form.cleaned_data.get('rede_social')
        
        fat_item_nota = FAT_item_nota.objects.create(
            Nota_fiscal = None,
            Id_USUARIO = None,
            Id_PRODUTO = produto,
            Id_FORNECEDOR = None,
            Qtd_item = quantidade,
            Valor_total_item = produto.Preco_produto * quantidade,
            Personalizacao_1 = tamanho if tamanho else nome_estampa,
            Personalizacao_2 = nome_estampa if (tamanho and nome_estampa) else rede_social,
        )
    
    return render(request,'site_vendas/produto.html',{'produto': produto, "form": form })


def cart(request): # Define view para a página do carrinho de compras
    return render(request,'site_vendas/cart.html')




    