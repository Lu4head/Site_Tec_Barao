from django import forms
from usuarios.models import DIM_Usuario

# Validação dos campos sendo feitas nas respectivas views em usuarios/views.py
class LoginForms(forms.Form): # Formulário da Pág de Login de Usuário
    email = forms.EmailField(
        label= "Email", # Nome do campo
        required= True, # Se o campo é obrigatório
        max_length= 150, # Tamanho máximo (sempre <= que o campo do banco)
        widget= forms.EmailInput( # Input do tipo e-mail já faz algumas validações automáticamente
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: joaosilva@xpto.com", # Placeholder de exibição para ajudar o usuário
            }
        ),
    )
    senha = forms.CharField(
        label= "Senha:", # Nome do campo
        required= True, # Se o campo é obrigatório
        max_length= 50, # Tamanho máximo (sempre <= que o campo do banco)
        widget=forms.PasswordInput( # Input do tipo senha já faz algumas validações automáticamente
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha"
            }
        ),
    )

class CadastroForms(forms.Form): # Formulário da Pág de Cadastro de Usuário
    nome_cadastro = forms.CharField( # Nome completo do usuário
        label = "Nome Completo:",
        required = True,
        max_length = 150,
        widget = forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: João Silva",
            }
        ),
    )
    email = forms.EmailField( # Email do usuário
        label = "Email:",
        required = True,
        max_length = 150,
        widget = forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: joaosilva@xpto.com",
            }
        ),
    )
    senha_1 = forms.CharField( # Senha do usuário
        label = "Senha:",
        required = True,
        max_length = 50,
        widget = forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha"
            }
        ),
    )
    senha_2 = forms.CharField( # Confirmação da senha
        label = "Confirme sua senha:",
        required = True,
        max_length = 50,
        widget = forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite novamente sua senha"
            }
        ),
    )
    telefone = forms.CharField( # Telefone do usuário
        label = "Telefone:",
        required= True,
        max_length= 20,
        widget = forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"55 16 91234-5678"
            }
        ),
        )
    cidade = forms.CharField( # Cidade onde o usuário mora
        label = "Cidade:",
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua cidade"
            }
        )
    )
    curso = forms.ChoiceField( # Curso da faculdade que o usuário faz parte
        label = "Curso:",
        required = True,
        choices = DIM_Usuario.cursos, # Possíveis escolhas importada do dicionário de cursos da Classe/Model DIM_Usuario definida em usuarios/models.py
        widget = forms.Select(attrs={"class":"form-control"}) # Define campo de seleção de escolha
    )
    unidade =forms.ChoiceField( # Unidade da faculdade que o usuário estuda
        label = "Unidade:",
        required = True,
        choices = DIM_Usuario.unidades, # Possíveis escolhas importada do dicionário de unidades da Classe/Model DIM_Usuario definida em usuarios/models.py
        widget = forms.Select(attrs={"class":"form-control"}) # Define campo de seleção de escolha
    )
    data_nascimento = forms.DateField(
        label = "Data de Nascimento:",
        required = True,
        widget = forms.DateInput(
            attrs={'type': 'date', "class":"form-control"}
        )
    )