from django.shortcuts import render, get_object_or_404, redirect
from site_vendas.models import DIM_Produto, FAT_item_nota, FAT_Nota, DIM_Fornecedor
from .forms import camisetaForms , canecaforms , tiranteForms , blusaForms , shortForms
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from .utils import update_nota_total
from django.core.mail import EmailMessage
import os
from .pixcodegen import Payload
from django.db.models import Sum


email_atletica = "luan.emanuelriar@gmail.com"
chave_pix = "+5516993561500"
nome_dono_chave = "LuanEmanuel"
cidade_dono_chave = "Brodowski"

def index(request): # Define view para a página home
    produtos = DIM_Produto.objects.filter(Produto_ativo_PRODUTO = True) # Lista objetos da classse DIM_Produto no banco filtrando pelos objetos que tenham o parâmetro Produto_ativo = True
    # Os produtos trazidos acima serão os produtos a serem exibidos na página inicial, eles são puxados do banco e adicionados ao site dinâmicamente
    return render(request, 'site_vendas/index.html', {"cards":produtos})

def produto(request, nome_produto): # Define view para a página de produto
    produto = get_object_or_404(DIM_Produto, Nome_PRODUTO=nome_produto) # Ao selecionar um produto na página home o usuário será direcionado à página do produto selecionado filtando pela pk = produto_id definida no html
    form = 0 # inicializa o formulario como 0 ao acessar a pagina para garantir que não sera usado o formulario errado
    match produto.Tipo_PRODUTO: # Verifica o tipo do produto e preenche o formulário para salvar no banco de acordo com as personalizações de cada tipo
        case "camiseta":
            form = camisetaForms
            form = camisetaForms(request.POST)
            if form.is_valid():
                if request.user.is_authenticated:
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
                else:
                    messages.error(request,"Precisa estar logado para adicionar produtos ao carrinho!")
                    return redirect(f'./{produto.Nome_PRODUTO}') 
                    
        case "caneca":
            form = canecaforms()
            form = canecaforms(request.POST)
            if form.is_valid():
                if request.user.is_authenticated:
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
                else:
                    messages.error(request,"Precisa estar logado para adicionar produtos ao carrinho!")
                    return redirect(f'./{produto.Nome_PRODUTO}') 
                
        case "blusa":
            form = blusaForms()
            form = blusaForms(request.POST)
            if form.is_valid():
                if request.user.is_authenticated:
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
                else:
                    messages.error(request,"Precisa estar logado para adicionar produtos ao carrinho!")
                    return redirect(f'./{produto.Nome_PRODUTO}') 
                
        case "tirante":
            form = tiranteForms()
            form = tiranteForms(request.POST)
            if form.is_valid():
                if request.user.is_authenticated:
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
                else:
                    messages.error(request,"Precisa estar logado para adicionar produtos ao carrinho!")
                    return redirect(f'./{produto.Nome_PRODUTO}') 
                
        case "short":
            form = shortForms()
            form = shortForms(request.POST)
            if form.is_valid():
                if request.user.is_authenticated:
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
                else:
                    messages.error(request,"Precisa estar logado para adicionar produtos ao carrinho!")
                    return redirect(f'./{produto.Nome_PRODUTO}') 
                
    return render(request,'site_vendas/produto.html',{'produto': produto, "form": form })


def cart(request): # Define view para a página do carrinho de compras
    if request.user.is_authenticated:
        if 'nota_fiscal_id' in request.session: #Verifica se existe uma nota vinculada ao usuario da sessão
            nota_fiscal_id = request.session['nota_fiscal_id'] #Recupera o id da nota
            nota_fiscal = FAT_Nota.objects.get(id=nota_fiscal_id) #Recupera a nota
            items = FAT_item_nota.objects.filter(Nota_fiscal=nota_fiscal) # Obtem todo os itens da nota
            total = sum(item.Valor_total_item for item in items) #Soma o valor total da nota
            

            if request.method == 'POST' and 'action' in request.POST: 
                action = request.POST.get('action')
                if action == "add" or action == "rm":
                    item_nota = request.POST.get("product_id")
                    if FAT_item_nota.objects.filter(Nota_fiscal = nota_fiscal , Id_USUARIO = request.user.id , id = item_nota).exists():
                        produto_atual = FAT_item_nota.objects.filter(Nota_fiscal = nota_fiscal , Id_USUARIO = request.user.id , id = item_nota).get()
                        if (action == "add") and (produto_atual.Qtd_item < 99): produto_atual.Qtd_item += 1 # Adiciona quantidade do produto
                        if (action == "rm") and (produto_atual.Qtd_item > 1): produto_atual.Qtd_item -= 1 # Diminui quantidade do produto
                        produto_atual.Valor_total_item = float(produto_atual.Id_PRODUTO.Preco_produto) * float(produto_atual.Qtd_item) # Recalcula valor total
                        produto_atual.save() # Salva dados atualizados no banco
                        update_nota_total(nota_fiscal)
                        return redirect('cart')

                if action == "remover": # Remover Produto do Carrinho
                    item_nota = request.POST.get("product_id")
                    if FAT_item_nota.objects.filter(Nota_fiscal = nota_fiscal , Id_USUARIO = request.user.id , id = item_nota).exists():
                        item_remover = FAT_item_nota.objects.get(Nota_fiscal=nota_fiscal, Id_USUARIO=request.user.id, id=item_nota)
                        item_remover.delete()
                        update_nota_total(nota_fiscal)
                        return redirect('cart')
                    
            
            if request.method == 'POST' and 'encerrar_nota_fiscal' in request.POST: # Concluir compra do carrinho
                pix = Payload(nome_dono_chave, chave_pix, total, cidade_dono_chave, nota_fiscal.id)
                pix.gerarPayload()
                pix_code = pix.payload_completa
                qr_code_file_name = f"{nota_fiscal.id}.png"

                corpo_email_usuario = "Confirmação de Compra - Atlética Barão de Mauá\n"

                for item in FAT_item_nota.objects.filter(Nota_fiscal=nota_fiscal, Id_USUARIO=request.user.id):
                    corpo_email_usuario += f"Produto: {item.Id_PRODUTO.Nome_PRODUTO}, Quantidade: {item.Qtd_item}, Preço: {(item.Id_PRODUTO.Preco_produto) * (item.Qtd_item)}\n"

                # Adicionar o valor total e o código Pix ao corpo do e-mail
                
                corpo_email_usuario += f"\nValor Total: {total}\nCódigo Pix para pagamento: {pix_code}"

                email_usuario = EmailMessage(
                    "Confirmação de Compra - Atlética Barão de Mauá",
                    corpo_email_usuario,
                    "capygramadora@outlook.com",
                    [f"{request.user.email}"],
                    )
                
                #Anexar o QR Code ao e-mail
                email_usuario.attach_file(qr_code_file_name)

                # Enviar o e-mail
                # email_usuario.send(fail_silently=False)

                nota_fiscal.Encerrada = True
                nota_fiscal.save()

                # Deletar o QR Code após o envio do e-mail
                os.remove(qr_code_file_name)
                
                # Quando o usuário concluir a compra deve ser incrementado no banco q tantos de certo produto foram vendidos
                # quando chegar a tantos produtos vendidos o admin deve receber um email avisando para comprar um novo lote daquele produto
                check_pending_lots()

                # Remove a nota fiscal da sessão
                del request.session['nota_fiscal_id']
                # Redireciona para alguma página após encerrar a nota fiscal
                messages.success(request,f"Compra realizada com sucesso!")
                return redirect('/')
            
            return render(request, 'site_vendas/cart.html', {'items': items, 'total': total})
        
        elif request.method == 'POST' and 'encerrar_nota_fiscal' in request.POST: # Usuário logado mas sem produtos tenta realizar compra
            messages.error(request,"Não há nenhum produto no carrinho")
            redirect ('.') # Volta pra mesma página

    else:   
        if request.method == 'POST' and 'encerrar_nota_fiscal' in request.POST: # Se usuario tentar finalizar compra sem estar logado
            messages.error(request,"Precisa estar logado realizar uma compra!")
            redirect ('.') # Volta pra mesma página

    return render(request, 'site_vendas/cart.html')

def check_pending_lots():
    for item in FAT_item_nota.objects.filter(Lote_pendente=True):
        produto = item.Id_PRODUTO
        pendentes = FAT_item_nota.objects.filter(Id_PRODUTO=produto, Lote_pendente=True)
        qtd_total = sum(pendente.Qtd_item for pendente in pendentes)  # Soma total das quantidades de itens pendentes
        if qtd_total >= produto.Lote_minimo_PRODUTO:
            for pendente in pendentes:
                pendente.Lote_pendente = False
                pendente.save()
            # enviar_email_para_admin(pendentes)

# def enviar_email_para_admin(produto):
#     email_admin = "gustavotduzzi@outlook.com"
#     assunto = f"Solicitação de novo lote para o produto {produto.Nome_PRODUTO}"
#     mensagem = f"O produto {produto.Nome_PRODUTO} atingiu o limite mínimo de vendas. Por favor, faça um novo pedido de lote."
#     send_mail(assunto, mensagem, "capygramadora@outlook.com", [email_admin])
    