from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class DIM_Fornecedor (models.Model):
    Nome_FORNECEDOR = models.CharField(max_length=100, null= False, blank= False, default="", verbose_name= "Nome do fornecedor")
    Endereco_FORNECEDOR = models.CharField(max_length= 200, default="", verbose_name="Endereço do fornecedor")
    Cnpj_FORNECEDOR = models.CharField(max_length=14, null= False, blank= False, unique= True,verbose_name= "CNPJ do fornecedor",default= "")
    Cidade_FORNECEDOR = models.CharField(max_length= 50, verbose_name="Cidade do fornecedor", default= "")
    Cep_FORNECEDOR = models.CharField(max_length=8, verbose_name="CEP do fornecedor",blank= False, null= False, default= "")
    Estado_FORNECEDOR = models.CharField(max_length=2, verbose_name="Estado do fornecedor",default= "")
    
    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.Nome_FORNECEDOR
    
    
class DIM_Produto (models.Model):
# Modelo/Classe que define a tabela de Produtos no banco de dados
# tipo_do_produto = Dicionário que define todos os tipos de produtos existentes que será utilizada para preenchimento do campo  Tipo_PRODUTO do tipo choices.
    tipo_do_produto = [("camiseta", "Camiseta"),
                     ("caneca", "Caneca"),
                     ("blusa","Blusa"),
                     ("tirante","Tirante"),
                     ("short","Short"),
                     ]
    
    ID_FORNECEDOR = models.ForeignKey(DIM_Fornecedor,on_delete=models.CASCADE, default= "")
    Nome_PRODUTO = models.CharField(max_length= 100, null = False, blank= False, default= "",unique=True ,verbose_name= "Nome do produto")
    Descricao_PRODUTO = models.CharField(max_length= 300, verbose_name="Descrição do produto", default= "")
    Tipo_PRODUTO = models.CharField(max_length= 50, choices= tipo_do_produto, verbose_name="Tipo de produto", default="")
    Preco_produto = models.DecimalField(max_digits= 6, decimal_places= 2, null= True, blank= False, verbose_name="Preço unitario do produto")
    Lote_minimo_PRODUTO = models.DecimalField(max_digits= 2, decimal_places= 0, verbose_name= "Quantidade minima de compra",null= True,blank= True)
    Preco_venda_PRODUTO = models.DecimalField(max_digits= 6, decimal_places= 0, null= True, blank= False, verbose_name="Preço de venda do produto",default=0)
    Produto_ativo_PRODUTO = models.BooleanField(default= False)
    Leedtime_PRODUTO = models.DecimalField(max_digits= 2, decimal_places= 0, verbose_name="Tempo medio de espera do produto", null= True,blank=False)
    Imagem_PRODUTO = models.ImageField(upload_to="fotos/", default= "")
    

    class Meta:
    # Define características extras da classe não relacionadas diretamente aos objetos no banco, como nome de exibição da classe, nome da tabela no banco e etc...
        verbose_name = "Produto" # Nome de exibição da classe caso seja singular
        verbose_name_plural = "Produtos" # Nome de exibição da classe caso seja plural

    def __str__(self):
        return self.Nome_PRODUTO # O que deve ser exibido ao printar um objeto dessa classe
    



class FAT_Nota(models.Model):
    Valor_total_nota = models.DecimalField(max_digits= 6, decimal_places=2, null=True,blank=True, verbose_name="Total da venda")
    Data_VENDA = models.DateField(verbose_name= "Data da venda",default=timezone.now)
    Encerrada = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Nota Fiscal"
        verbose_name_plural = "Notas Fiscais" 

class FAT_item_nota (models.Model):
    Nota_fiscal = models.ForeignKey(FAT_Nota, blank=True, null = True, on_delete= models.CASCADE, default='')
    Id_USUARIO = models.ForeignKey(User, blank=True, null = True, on_delete= models.CASCADE, default='')
    Id_PRODUTO = models.ForeignKey(DIM_Produto, blank=True, null = True, on_delete=models.CASCADE, default="")
    Qtd_item = models.IntegerField(null= False, verbose_name="Quantidade de venda",default=1)
    Valor_total_item = models.DecimalField(max_digits= 6, decimal_places=2, null= True,blank=False, verbose_name="Valor total por produto")
    Personalizacao_1 = models.CharField(max_length=30, null=True,blank= True)
    Personalizacao_2 = models.CharField(max_length=30, null=True,blank= True)
    Personalizacao_3 = models.CharField(max_length=30, null=True,blank= True)

    class Meta:
        verbose_name = "ItemPedido"
        verbose_name_plural = "ItemPedidos" 
        
#Sinal para salvar valores na fat_nota    
@receiver(post_save, sender=FAT_item_nota)
def update_nota_total(sender, instance, **kwargs):
    # Verifica se a instância é uma nova entrada ou uma atualização
    if kwargs.get('created', False) or kwargs.get('update_fields', False):
        # Obtém a nota fiscal associada ao item
        nota_fiscal = instance.Nota_fiscal
        # Obtém todos os itens associados à nota fiscal
        items_nota = FAT_item_nota.objects.filter(Nota_fiscal=nota_fiscal)
        # Calcula o novo valor total da nota somando os valores totais de todos os itens
        novo_valor_total = sum(item.Valor_total_item for item in items_nota) 

        # Atualiza o valor_total_nota na instância da FAT_Nota
        nota_fiscal.Valor_total_nota = novo_valor_total
        nota_fiscal.save()
    

  
class FAT_pedido_compra (models.Model):
    Id_ADM = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # ID da conta administrativa que liberou o pedido da compra
    Id_PRODUTO = models.ForeignKey(DIM_Produto, on_delete=models.CASCADE, default="")
    Id_FORNECEDOR = models.ForeignKey(DIM_Fornecedor, on_delete= models.CASCADE)
    Qtd_PEDIDO = models.DecimalField(max_digits= 2, decimal_places=0, null= True,blank=False, verbose_name="Quantidade de itens")
    Data_PEDIDO = models.DateField(default= timezone.now,verbose_name="Data do pedido")
    Data_chegada_PEDIDO = models.DateField(verbose_name="Data da chegada do pedido", null= True)
    Custo_PEDIDO = models.DecimalField(max_digits=6, decimal_places=2, null= True,blank= False, verbose_name="Custo total do pedido")
    
    class Meta:
        verbose_name = "Pedido de Compra"
        verbose_name_plural = "Pedidos de Compra"
