from django.db import models
from django.utils import timezone
from usuarios.models import DIM_Usuario
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models






class DIM_Produto (models.Model):

    tipo_do_produto = [("vestuario", "Vestuário"),
                     ("caneca", "Caneca")]
    
    Nome_PRODUTO = models.CharField(max_length= 100, null = False, blank= False, default= "", verbose_name= "Nome do produto")
    Descricao_PRODUTO = models.CharField(max_length= 300, verbose_name="Descrição do produto", default= "")
    Tipo_PRODUTO = models.CharField(max_length= 50, choices= tipo_do_produto, verbose_name="Tipo de produto", default="")
    Preco_produto = models.DecimalField(max_digits= 6, decimal_places= 2, null= True, blank= False, verbose_name="Preço unitario do produto")
    Lote_minimo_PRODUTO = models.DecimalField(max_digits= 2, decimal_places= 0, verbose_name= "Quantidade minima de compra",null= True,blank= True)
    Preco_venda_PRODUTO = models.DecimalField(max_digits= 2, decimal_places= 0, null= True, blank= False, verbose_name="Preço de venda do produto",default=0)
    Produto_ativo_PRODUTO = models.BooleanField(default= False)
    Leedtime_PRODUTO = models.DecimalField(max_digits= 2, decimal_places= 0, verbose_name="Tempo medio de espera do produto", null= True,blank=False)
    Imagem_PRODUTO = models.ImageField(upload_to="fotos/", default= "") 

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.Nome_PRODUTO
    

class DIM_Fornecedor (models.Model):
    Nome_FORNECEDOR = models.CharField(max_length=100, null= False, blank= False, default="", verbose_name= "Nome do fornecedor")
    Endereco_FORNECEDOR = models.CharField(max_length= 200, default="", verbose_name="Endereço do fornecedor")
    Cnpj_FORNECEDOR = models.CharField(max_length=14, null= False, blank= False, unique= True,verbose_name= "CNPJ do fornecedor",default= "")
    Cidade_FORNECEDOR = models.CharField(max_length= 50, verbose_name="Cidade do fornecedor", default= "")
    Cep_FORNECEDOR = models.CharField(max_length=8, verbose_name="CEP do fornecedor",blank= False, null= False, default= "")
    Estado_FORNECEDOR = models.CharField(max_length=2, verbose_name="Estado do fornecedor",default= "")

    def __str__(self):
        return self.Nome_FORNECEDOR

class FAT_venda (models.Model):
    Id_USUARIO = models.ForeignKey(DIM_Usuario, on_delete= models.CASCADE, default='')
    Id_PRODUTO = models.ForeignKey(DIM_Produto, on_delete=models.CASCADE)
    Id_FORNECEDOR = models.ForeignKey(DIM_Fornecedor, on_delete=models.CASCADE)
    Qtd_VENDA = models.IntegerField(null= False, verbose_name="Quantidade de venda",default=0)
    Total_VENDA = models.DecimalField(max_digits= 6, decimal_places=2, null= True,blank=False, verbose_name="Total da venda")
    Data_VENDA = models.DateField(verbose_name= "Data da venda",default=timezone.now)


class FAT_pedido_compra (models.Model):
    Id_ADM = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Id_PRODUTO = models.ForeignKey(DIM_Produto, on_delete=models.CASCADE, default="")
    Id_FORNECEDOR = models.ForeignKey(DIM_Fornecedor, on_delete= models.CASCADE)
    Qtd_PEDIDO = models.DecimalField(max_digits= 2, decimal_places=0, null= True,blank=False, verbose_name="Quantidade de itens")
    Data_PEDIDO = models.DateField(default= timezone.now,verbose_name="Data do pedido")
    Data_chegada_PEDIDO = models.DateField(verbose_name="Data da chegada do pedido", null= True)
    Custo_PEDIDO = models.DecimalField(max_digits=6, decimal_places=2, null= True,blank= False, verbose_name="Custo total do pedido")
    
    class Meta:
        verbose_name = "Pedido de Compra"
        verbose_name_plural = "Pedidos de Compra"