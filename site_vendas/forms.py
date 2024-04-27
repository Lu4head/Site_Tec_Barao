from django import forms
from .models import DIM_Fornecedor,DIM_Produto, FAT_item_nota
from usuarios.models import DIM_Usuario

class vestuarioForms(forms.Form):
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

    
