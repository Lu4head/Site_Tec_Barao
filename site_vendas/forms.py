from django import forms
from .models import DIM_Fornecedor,DIM_Produto, FAT_item_nota
from usuarios.models import DIM_Usuario

class produtoForms(forms.Form):
    quantidade = forms.IntegerField