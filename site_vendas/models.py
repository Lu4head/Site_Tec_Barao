from django.db import models

class DIM_Usuario(models.Model):
    nome = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome
    
class DIM_Produto(models.Model):

    def __str__(self):
        return self


class DIM_Fornecedor(models.Model):

    def __str__(self):
        return self

class FAT_venda(models.Model):

    def __str__(self):
        return self
