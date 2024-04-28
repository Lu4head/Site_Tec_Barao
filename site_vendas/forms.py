from django import forms
from .models import DIM_Fornecedor,DIM_Produto, FAT_item_nota
from usuarios.models import DIM_Usuario

lista_tamanhos = [("P","P"),
                ("M","M"),
                ("G","G"),
                ]
class camisetaForms(forms.Form):

    quantidade = forms.IntegerField(
        label="Quantidade a comprar",
        required=True,
        max_value=99,
        min_value=1,
        widget=forms.NumberInput(
            attrs={
                "class": "",
                "id": "",
                "placeholder": "1",
            }
        )
    )
    
    tamanho = forms.ChoiceField(
        label = "Tamanho:",
        required = True,
        choices = lista_tamanhos, # Possíveis escolhas importada do dicionário de cursos da Classe/Model DIM_Usuario definida em usuarios/models.py
        widget = forms.Select(attrs={"class":"form-control"}) # Define campo de seleção de escolha
    )

    nome = forms.CharField(
        label="Nome escrito na estampa",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Insira o nome aqui",
            }
        )
    )



class canecaforms(forms.Form):
    quantidade = forms.IntegerField(
        label= "Quantidade a comprar",
        required= True,
        max_value= 99,
        min_value=1,
        widget= forms.NumberInput(
            attrs={
                    "class": "",
                    "id":"",
                    "placeholder":"1",
            }
        )
    )
    nome = forms.CharField(
        label="Nome escrito na caneca",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Insira o nome aqui",
            }
        )
    )

class blusaForms(forms.Form):
    quantidade = forms.IntegerField(
        label="Quantidade a comprar",
        required=True,
        max_value=99,
        min_value=1,
        widget=forms.NumberInput(
            attrs={
       
         "class": "",
                "id": "",
                "placeholder": "1",
            }
        )
    )

    tamanho = forms.ChoiceField(
        label = "Tamanho:",
        required = True,
        choices = lista_tamanhos, # Possíveis escolhas importada do dicionário de cursos da Classe/Model DIM_Usuario definida em usuarios/models.py
        widget = forms.Select(attrs={"class":"form-control"}) # Define campo de seleção de escolha
    )


class tiranteForms(forms.Form):
    quantidade = forms.IntegerField(
        label="Quantidade a comprar",
        required=True,
        max_value=99,
        min_value=1,
        widget=forms.NumberInput(
            attrs={
       
         "class": "",
                "id": "",
                "placeholder": "1",
            }
        )
    )

    nome = forms.CharField(
        label="Nome escrito no tirante",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Insira o nome aqui",
            }
        )
    )

    rede_social = forms.CharField(
    label="@ de alguma rede social para o tirante\n*não obrigatório",
    required= False,
    max_length=30,
    widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Insira o @ aqui",
            }
        )
    )

class shortForms(forms.Form):
    quantidade = forms.IntegerField(
        label="Quantidade a comprar",
        required=True,
        max_value=99,
        min_value=1,
        widget=forms.NumberInput(
            attrs={
       
         "class": "",
                "id": "",
                "placeholder": "1",
            }
        )
    )

    tamanho = forms.ChoiceField(
        label = "Tamanho:",
        required = True,
        choices = lista_tamanhos, # Possíveis escolhas importada do dicionário de cursos da Classe/Model DIM_Usuario definida em usuarios/models.py
        widget = forms.Select(attrs={"class":"form-control"}) # Define campo de seleção de escolha
    )