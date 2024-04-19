from django import forms

cursos =    [("design_grafico", "Design Gráfico"),
                 ("ciencia_computacao", "Ciência da Computação")]

unidades =  [("unidade_independencia", "Unidade Independência"),
                 ("unidade_central", "Unidade Central"),
                 ("unidade_direito", "Unidade Direito")]

class LoginForms(forms.Form):
    nome_login = forms.CharField(
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
    senha = forms.CharField(
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

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
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
    email = forms.EmailField(
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
    senha_1 = forms.CharField(
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
    senha_2 = forms.CharField(
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
    telefone = forms.CharField(
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
    cidade = forms.CharField(
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
    curso = forms.ChoiceField(
        label = "Curso:",
        required = True,
        choices = cursos,
        widget = forms.Select(attrs={"class":"form-control"})
    )
    unidade =forms.ChoiceField(
        label = "Unidade:",
        required = True,
        choices = unidades,
        widget = forms.Select(attrs={"class":"form-control"})
    )
    data_nascimento = forms.DateField(
        label = "Data de Nascimento:",
        required = True,
        widget = forms.DateInput(
            attrs={'type': 'date', "class":"form-control"}
        )
    )