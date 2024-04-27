from django.contrib import admin
from site_vendas.models import DIM_Fornecedor, DIM_Produto , FAT_pedido_compra , FAT_item_nota
# Exibição e controle dos produtos na pág de admin
class ListaProdutos(admin.ModelAdmin):
    list_display = ("id","Nome_PRODUTO","Tipo_PRODUTO","Preco_produto","Produto_ativo_PRODUTO") # Quais campos serão exibidos
    list_display_links = ("id","Nome_PRODUTO") # Quais campos serão links clicáveis para acessar aquele objeto
    search_fields = ("nome",) # Quais campos podem ser pesquisados na barra de pesquisas
    list_filter = ("Tipo_PRODUTO","Produto_ativo_PRODUTO",) # Por quais campos podemos filtar os objetos daquela classe
    list_editable = ("Produto_ativo_PRODUTO",) # Quais campos podem ser editados direto pela pág de Produtos sem acessar diretamente o objeto
    list_per_page = 10 # Quantos objetos serão listados por página da página de produtos

admin.site.register(DIM_Produto, ListaProdutos)

# class ListaPedidos(admin.ModelAdmin):
#     list_display = ("id","Data_PEDIDO","Data_chegada_PEDIDO")
#     list_display_links = ("id",)
#     search_fields = ("Data_Pedido",)
#     list_filter = ("Data_PEDIDO","Data_chegada_PEDIDO","Id_FORNECEDOR","Id_PRODUTO","Id_ADM")
#     list_per_page = 10

# admin.site.register(FAT_pedido_compra, ListaPedidos)
