from django.db import models
from datetime import datetime
from django import forms
from django.utils import timezone

cursos = [("Design gráfico"), ("Ciência da computação")]
unidades = [("Unidade independência"), ("Unidade central"), ("Unidade direito")]
tipo_do_produto = [("Vesturario"), ("Caneca")]

class DIM_Usuario(models.Model):
    Nome_USUARIO = models.CharField(max_length=150, null= False, blank= False, default= "", verbose_name= "Nome do usuario")
    #Endereco_USUARIO = models.CharField(max_length= 200)
    Data_nascimento_USUARIO = models.DateField(verbose_name= "Data de nascimento do usuario")
    Idade_USUARIO = models.PositiveIntegerField(null= True, blank= True, verbose_name= "Idade do usuario")
    Curso_USUARIO = models.CharField(max_length= 50, choices= cursos, default= "", verbose_name= "Curso do usuario") 
    Unidade_USUARIO =  models.CharField(max_length= 30, choices= unidades, default= "", verbose_name= "Unidade de ensino") 
    #Cep_USUARIO = models.CharField(max_length=8)
    Cidade_usuario = models.CharField(max_length= 100, null= False, blank= False, default= "", verbose_name="Cidade do usuario")
    Email_usuario = models.EmailField(max_length=254, null= False, blank = False, default= "", unique= True, verbose_name= "E-mail do usuario")
    Telefone_usuario = models.CharField(max_length = 20, null= False, blank= False, unique= True, verbose_name= "Telefone do usuario") 
    Senha_usuario = models.CharField(max_length= 50, verbose_name= "Senha do usuario") # tratar senha melhor

    def save(self, *args, **kwargs): #para calcular e salvar idade
        if self.Data_nascimento_USUARIO:
            Today = datetime.today().date()
            idade = Today.year - self.Data_nascimento_USUARIO.year - ((Today.month,Today.day)< (self.Data_nascimento_USUARIO.month, self.Data_nascimento_USUARIO.day))
            self.Idade_USUARIO = idade
            super().save(*args, **kwargs)

class DIM_Produto (models.Model):
    Nome_PRODUTO = models.CharField(max_length= 100, null = False, blank= False, default= "", verbose_name= "Nome do produto")
    Descricao_PRODUTO = models.CharField(max_length= 300, verbose_name="Descrição do produto")
    Tipo_PRODUTO = models.CharField(max_length= 20, choices= tipo_do_produto, verbose_name="Tipo de produto")
    Preco_produto = models.DecimalField(max_digits= 6, decimal_places= 2, null= False, blank= False, verbose_name="Preço unitario do produto")
    Lote_minimo_PRODUTO = models.DecimalField(max_digits= 2, decimal_places= 0, verbose_name= "Quantidade minima de compra")
    Preco_venda_PRODUTO = models.DecimalField(max_digits= 2, decimal_places= 0, null= False, blank= False, verbose_name="Preço de venda do produto")
    Produto_ativo_PRODUTO = models.BooleanField(default= False)
    Leedtime_PRODUTO = models.DecimalField(max_digits= 2, decimal_places= 0, verbose_name="Tempo medio de espera do produto")
    Imagem_PRODUTO = models.ImageField(upload_to="fotos/") 

class DIM_Fornecedor (models.Model):
    Nome_FORNECEDOR = models.CharField(max_length=100, null= False, blank= False, default="", verbose_name= "Nome do fornecedor")
    Endereco_FORNECEDOR = models.CharField(max_length= 200, default="", verbose_name="Endereço do fornecedor")
    Cnpj_FORNECEDOR = models.CharField(max_length=14, null= False, blank= False, unique= True,verbose_name= "CNPJ do fornecedor")
    Cidade_FORNECEDOR = models.CharField(max_length= 50, verbose_name="Cidade do fornecedor")
    Cep_FORNECEDOR = models.CharField(max_length=8, verbose_name="CEP do fornecedor")
    Estado_FORNECEDOR = models.CharField(max_length=2, verbose_name="Estado do fornecedor")

class FAT_venda (models.Model):
    Id_USUARIO = models.ForeignKey(DIM_Usuario, on_delete= models.CASCADE)
    Id_PRODUTO = models.ForeignKey(DIM_Produto, on_delete=models.CASCADE)
    Id_FORNECEDOR = models.ForeignKey(DIM_Fornecedor, on_delete=models.CASCADE)
    Qtd_VENDA = models.IntegerField(null= False, verbose_name="Quantidade de venda")
    Total_VENDA = models.DecimalField(max_digits= 6, decimal_places=2, null= False, verbose_name="Total da venda")
    Data_VENDA = models.DateField(timezone.now(), verbose_name= "Data da venda")

class FAT_pedido_compra (models.Model):
    #Id_ADM = models.ForeignKey()
    Id_PRODUTO = models.ForeignKey(DIM_Produto, on_delete=models.CASCADE)
    Id_FORNECEDOR = models.ForeignKey(DIM_Fornecedor, on_delete= models.CASCADE)
    Qtd_PEDIDO = models.DecimalField(max_digits= 2, decimal_places=0, null= False, verbose_name="Quantidade de itens")
    Data_PEDIDO = models.DateField(default= timezone.now(),verbose_name="Data do pedido")
    Data_chegada_PEDIDO = models.DateField(verbose_name="Data da chegada do pedido")
    Custo_PEDIDO = models.DecimalField(max_digits=6, decimal_places=2, null= False, verbose_name="Custo total do pedido")


    def __str__(self):
        return self
    
class DIM_Produto(models.Model):

    def __str__(self):
        return self


class DIM_Fornecedor(models.Model):

    def __str__(self):
        return self

class FAT_venda(models.Model):

    def __str__(self):
        return self
    
class FAT_pedido_compra(models.Model):

    def __str__(self):
        return self
    