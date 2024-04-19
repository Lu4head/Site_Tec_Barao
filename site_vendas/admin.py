from django.contrib import admin
from site_vendas.models import DIM_Fornecedor, DIM_Produto , FAT_pedido_compra , FAT_venda


class ListaProdutos(admin.ModelAdmin):
    list_display = ("id","Nome_PRODUTO","Tipo_PRODUTO","Preco_produto","Produto_ativo_PRODUTO")
    list_display_links = ("id","Nome_PRODUTO")
    search_fields = ("nome",)
    list_filter = ("Tipo_PRODUTO","Produto_ativo_PRODUTO",)
    list_editable = ("Produto_ativo_PRODUTO",)
    list_per_page = 10

admin.site.register(DIM_Produto, ListaProdutos)
