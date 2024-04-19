from django.contrib import admin
from usuarios.models import DIM_Usuario

class ListaUsuarios(admin.ModelAdmin):
    list_display = ("id","Nome_USUARIO","Curso_USUARIO","Email_USUARIO","Telefone_USUARIO")
    list_display_links = ("id","Nome_USUARIO")
    search_fields = ("Nome_USUARIO",)
    list_filter = ("Cidade_USUARIO","Curso_USUARIO",)
    list_per_page = 50

admin.site.register(DIM_Usuario, ListaUsuarios)