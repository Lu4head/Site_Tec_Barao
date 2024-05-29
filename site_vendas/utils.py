from .models import FAT_item_nota
from django.core.mail import send_mail

def update_nota_total(nota_fiscal):
    # Obtém todos os itens associados à nota fiscal
    items_nota = FAT_item_nota.objects.filter(Nota_fiscal=nota_fiscal)
    # Calcula o novo valor total da nota somando os valores totais de todos os itens
    novo_valor_total = sum(item.Valor_total_item for item in items_nota) 
    # Atualiza o valor_total_nota na instância da FAT_Nota
    nota_fiscal.Valor_total_nota = novo_valor_total
    nota_fiscal.save()

def check_pending_lots():
    for item in FAT_item_nota.objects.filter(Lote_pendente=True):
        produto = item.Id_PRODUTO
        pendentes = FAT_item_nota.objects.filter(Id_PRODUTO=produto, Lote_pendente=True)
        qtd_total = sum(pendente.Qtd_item for pendente in pendentes)  # Soma total das quantidades de itens pendentes
        if qtd_total >= produto.Lote_minimo_PRODUTO:
            enviar_email_para_admin(pendentes, produto)
            for pendente in pendentes:
                pendente.Lote_pendente = False
                pendente.save()
            

def enviar_email_para_admin(pendentes, produto):
    email_admin = "capygramadora@outlook.com"
    assunto = f"Solicitação de novo lote para o produto {produto.Nome_PRODUTO}"
    mensagem = f"O produto {produto.Nome_PRODUTO} atingiu o limite mínimo de vendas. Por favor, faça um novo pedido de lote."
    for pendente in pendentes:
        mensagem += f"\n. Para usuário {pendente.Id_USUARIO.first_name} - {pendente.Qtd_item} unidades."
    send_mail(assunto, mensagem, "capygramadora@outlook.com", [email_admin])