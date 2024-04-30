from .models import FAT_item_nota

def update_nota_total(nota_fiscal):
    # Obtém todos os itens associados à nota fiscal
    items_nota = FAT_item_nota.objects.filter(Nota_fiscal=nota_fiscal)
    # Calcula o novo valor total da nota somando os valores totais de todos os itens
    novo_valor_total = sum(item.Valor_total_item for item in items_nota) 
    # Atualiza o valor_total_nota na instância da FAT_Nota
    nota_fiscal.Valor_total_nota = novo_valor_total
    nota_fiscal.save()