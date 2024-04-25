from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from usuarios.models import DIM_Usuario
from django.contrib import messages
from datetime import datetime
from usuarios.utils import validar_campo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            user = authenticate(request, username=email, password=senha)
            if user is not None and user.is_active:
                    auth_login(request,user)
                    messages.success(request,f"Usuário  {user.first_name} logado com sucesso")
                    return redirect('/')
            else:
                messages.error(request,"Senha incorreta!")
                return redirect('login')
        else:
            messages.error(request,"Erro ao efetuar login")
                
    return render(request, 'usuarios/login.html', {"form": form})

def logout(request):
    auth_logout(request)
    messages.success(request, "logout realizado com sucesso")
    return redirect ('login')

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            if form.cleaned_data['senha_1'] != form.cleaned_data['senha_2']:
                messages.error(request, "Senhas divergentes")
                return redirect('cadastro') 


            nome = form.cleaned_data['nome_cadastro']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha_1']
            telefone = form.cleaned_data['telefone']
            cidade = form.cleaned_data['cidade']
            curso = form.cleaned_data['curso']
            unidade = form.cleaned_data['unidade']
            data_nascimento = form.cleaned_data['data_nascimento']

            if DIM_Usuario.objects.filter(Nome_USUARIO=nome).exists():
                messages.error(request,"Já há um usuário cadastrado com este nome.")
                return redirect('cadastro')

                    
            nome = form['nome_cadastro'].value()
            
            if not validar_campo(nome):
                messages.error(request,"Nome contém caracteres inválidos")
                return redirect('cadastro')

            if DIM_Usuario.objects.filter(Email_USUARIO=email).exists():
                messages.error(request,'Email já cadastrado')    
                return redirect('cadastro')

            if not validar_campo(cidade):
                messages.error(request,"Cidade contém caracteres inválidos")
                return redirect('cadastro')

            # Convertendo a data de nascimento em uma string antes de usar strptime()
            data_nascimento_str = data_nascimento.strftime('%Y-%m-%d')

            ano_nascimento = data_nascimento.year

            if ano_nascimento < (datetime.now().year - 110) or ano_nascimento > datetime.now().year:
                messages.error(request,"Data de nascimento inválida!")
                return redirect('cadastro')

            # Criando usuário na tabela User do Django
            user = User.objects.create_user(
                username=email,  # Usando o e-mail como nome de usuário
                email=email,
                password=senha,
                first_name=nome
            )

            # Criando usuário no modelo DIM_Usuario associado ao usuário criado acima
            dim_usuario = DIM_Usuario.objects.create(
                Nome_USUARIO=nome,
                Telefone_USUARIO=telefone,
                Cidade_USUARIO=cidade,
                Curso_USUARIO=curso,
                Unidade_USUARIO=unidade,
                Data_nascimento_USUARIO=data_nascimento_str,
                user=user  # associando o usuário ao DIM_Usuario
            )

            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')
    return render(request, 'usuarios/cadastro.html', {"form": form})
