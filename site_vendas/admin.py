from django.contrib import admin
from site_vendas.models import DIM_Fornecedor, DIM_Produto , FAT_pedido_compra , FAT_item_nota

class ListaFornecedor(admin.ModelAdmin):
    list_display = ("id","Nome_FORNECEDOR","Cnpj_FORNECEDOR","Cidade_FORNECEDOR","Estado_FORNECEDOR",)
    list_display_links = ("id","Nome_FORNECEDOR",)
    search_fields = ("Nome_FORNECEDOR",)
    list_filter = ("Cidade_FORNECEDOR","Estado_FORNECEDOR",)
    list_per_page = 10

admin.site.register(DIM_Fornecedor, ListaFornecedor)

# Exibição e controle dos produtos na pág de admin
class ListaProdutos(admin.ModelAdmin):
    list_display = ("id","Nome_PRODUTO","Tipo_PRODUTO","Preco_produto","Produto_ativo_PRODUTO") # Quais campos serão exibidos
    list_display_links = ("id","Nome_PRODUTO") # Quais campos serão links clicáveis para acessar aquele objeto
    search_fields = ("nome",) # Quais campos podem ser pesquisados na barra de pesquisas
    list_filter = ("Tipo_PRODUTO","Produto_ativo_PRODUTO",) # Por quais campos podemos filtar os objetos daquela classe
    list_editable = ("Produto_ativo_PRODUTO",) # Quais campos podem ser editados direto pela pág de Produtos sem acessar diretamente o objeto
    list_per_page = 10 # Quantos objetos serão listados por página da página de produtos

admin.site.register(DIM_Produto, ListaProdutos)

# class ListaItemNota(admin.ModelAdmin): # Tirar depois ( INÚTIL ! )
#     list_display = ("id","Id_USUARIO","Id_PRODUTO","Nota_fiscal")
#     list_display_links = ("id",)
#     search_fields = ("Id_USUARIO","Id_PRODUTO","Nota_fiscal")
#     list_filter = ("Id_USUARIO","Id_PRODUTO","Nota_fiscal")
#     list_per_page = 50

# admin.site.register(FAT_item_nota, ListaItemNota)

