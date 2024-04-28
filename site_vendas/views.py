from django.shortcuts import render, get_object_or_404, redirect
from site_vendas.models import DIM_Produto, FAT_item_nota, FAT_Nota, DIM_Fornecedor
from .forms import camisetaForms , canecaforms , tiranteForms , blusaForms , shortForms
from django.utils import timezone
from django.contrib.auth.models import User

def index(request): # Define view para a página home
    produtos = DIM_Produto.objects.filter(Produto_ativo_PRODUTO = True) # Lista objetos da classse DIM_Produto no banco filtrando pelos objetos que tenham o parâmetro Produto_ativo = True
    # Os produtos trazidos acima serão os produtos a serem exibidos na página inicial, eles são puxados do banco e adicionados ao site dinâmicamente
    return render(request, 'site_vendas/index.html', {"cards":produtos})

def produto(request, nome): # Define view para a página de produto
    produto = get_object_or_404(DIM_Produto, Nome_PRODUTO=nome) # Ao selecionar um produto na página home o usuário será direcionado à página do produto selecionado filtando pela pk = produto_id definida no html
    form = 0
    match produto.Tipo_PRODUTO:
        case "camiseta":
            form = camisetaForms
            form = camisetaForms(request.POST)
            if form.is_valid():
                if 'nota_fiscal_id' not in request.session: # Verifica se já tem uma nota fiscal vinculada ao usuario na sessão
                    nota_fiscal = FAT_Nota.objects.create( # Cria a nota
                        Valor_total_nota=0,
                        Data_VENDA=timezone.now()
                    )
                    request.session['nota_fiscal_id'] = nota_fiscal.id
                else:
                    nota_fiscal_id = request.session['nota_fiscal_id'] #recupera o a nota para usar mais tarde
                    nota_fiscal = FAT_Nota.objects.get(id=nota_fiscal_id)

                qtd_item = form.cleaned_data['quantidade']
                tamanho = form.cleaned_data['tamanho'] 
                nome_personalizacao = form.cleaned_data['nome']

                item_nota = FAT_item_nota.objects.create(
                    Nota_fiscal=nota_fiscal,
                    Id_USUARIO=request.user,
                    Id_PRODUTO=produto,
                    Qtd_item=qtd_item,
                    Valor_total_item=produto.Preco_produto * qtd_item,
                    Personalizacao_1=tamanho,
                    Personalizacao_2=nome_personalizacao
                )
                return redirect('/')
                    

        case "caneca":
            form = canecaforms()
            form = canecaforms(request.POST)
            if form.is_valid():
                if 'nota_fiscal_id' not in request.session:
                    nota_fiscal = FAT_Nota.objects.create(
                        Valor_total_nota=0,
                        Data_VENDA=timezone.now()
                    )
                    request.session['nota_fiscal_id'] = nota_fiscal.id
                else:
                    nota_fiscal_id = request.session['nota_fiscal_id']
                    nota_fiscal = FAT_Nota.objects.get(id=nota_fiscal_id)

                qtd_item = form.cleaned_data['quantidade']
                nome_personalizacao = form.cleaned_data['nome_personalizacao']

                item_nota = FAT_item_nota.objects.create(
                    Nota_fiscal=nota_fiscal,
                    Id_USUARIO=request.user,
                    Id_PRODUTO=produto,
                    Qtd_item=qtd_item,
                    Valor_total_item=produto.Preco_produto * qtd_item,
                    Personalizacao_1=nome_personalizacao
                    
                )
                return redirect('/')
        case "blusa":
            form = blusaForms()
            form = blusaForms(request.POST)
            if form.is_valid():
                if 'nota_fiscal_id' not in request.session:
                    nota_fiscal = FAT_Nota.objects.create(
                        Valor_total_nota=0,
                        Data_VENDA=timezone.now()
                    )
                    request.session['nota_fiscal_id'] = nota_fiscal.id
                else:
                    nota_fiscal_id = request.session['nota_fiscal_id']
                    nota_fiscal = FAT_Nota.objects.get(id=nota_fiscal_id)

                qtd_item = form.cleaned_data['quantidade']
                tamanho = form.cleaned_data['tamanho'] 

                item_nota = FAT_item_nota.objects.create(
                    Nota_fiscal=nota_fiscal,
                    Id_USUARIO=request.user,
                    Id_PRODUTO=produto,
                    Qtd_item=qtd_item,
                    Valor_total_item=produto.Preco_produto * qtd_item,
                    Personalizacao_1=tamanho
                    
                )
                return redirect('/')
        case "tirante":
            form = tiranteForms()
            form = tiranteForms(request.POST)
            if form.is_valid():
                if 'nota_fiscal_id' not in request.session:
                    nota_fiscal = FAT_Nota.objects.create(
                        Valor_total_nota=0,
                        Data_VENDA=timezone.now()
                    )
                    request.session['nota_fiscal_id'] = nota_fiscal.id
                else:
                    nota_fiscal_id = request.session['nota_fiscal_id']
                    nota_fiscal = FAT_Nota.objects.get(id=nota_fiscal_id)

                qtd_item = form.cleaned_data['quantidade']
                nome_personalizacao = form.cleaned_data['nome_personalizacao'] 
                rede_social = form.cleaned_data['rede_social']

                item_nota = FAT_item_nota.objects.create(
                    Nota_fiscal=nota_fiscal,
                    Id_USUARIO=request.user,
                    Id_PRODUTO=produto,
                    Qtd_item=qtd_item,
                    Valor_total_item=produto.Preco_produto * qtd_item,
                    Personalizacao_1=nome_personalizacao,
                    Personalizacao_2=rede_social
                )
                return redirect('/')
        case "short":
            form = shortForms()
            form = shortForms(request.POST)
            if form.is_valid():
                if 'nota_fiscal_id' not in request.session:
                    nota_fiscal = FAT_Nota.objects.create(
                        Valor_total_nota=0,
                        Data_VENDA=timezone.now()
                    )
                    request.session['nota_fiscal_id'] = nota_fiscal.id
                else:
                    nota_fiscal_id = request.session['nota_fiscal_id']
                    nota_fiscal = FAT_Nota.objects.get(id=nota_fiscal_id)

                qtd_item = form.cleaned_data['quantidade']
                tamanho = form.cleaned_data['tamanho'] 
             

                item_nota = FAT_item_nota.objects.create(
                    Nota_fiscal=nota_fiscal,
                    Id_USUARIO=request.user,
                    Id_PRODUTO=produto,
                    Qtd_item=qtd_item,
                    Valor_total_item=produto.Preco_produto * qtd_item,
                    Personalizacao_1=tamanho,
                )
                return redirect('/')
    return render(request,'site_vendas/produto.html',{'produto': produto, "form": form })


def cart(request): # Define view para a página do carrinho de compras
    if 'nota_fiscal_id' in request.session: #Verifica se existe uma nota vinculada ao usuario da sessão
        nota_fiscal_id = request.session['nota_fiscal_id'] #Recupera o id da nota
        nota_fiscal = FAT_Nota.objects.get(id=nota_fiscal_id) #Recupera a nota
        items = FAT_item_nota.objects.filter(Nota_fiscal=nota_fiscal) # Obtem todo os itens da nota
        total = sum(item.Valor_total_item for item in items) #Soma o valor total da nota
        
        #para encerrar a nota fiscal
        if request.method == 'POST' and 'encerrar_nota_fiscal' in request.POST:
            # Remove a nota fiscal da sessão
            del request.session['nota_fiscal_id']
            # Redireciona para alguma página após encerrar a nota fiscal
            return redirect('/')
        return render(request, 'site_vendas/cart.html', {'items': items, 'total': total})
    else:
        return render(request, 'site_vendas/cart.html')



    