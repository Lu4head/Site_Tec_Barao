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
from site_vendas.models import FAT_Nota

def login(request):
# Caso formulário não seja preenchido corretamente usuário é direcionado de volta para tela de login
# Em caso de sucesso ao realizar login o usuário é direcionado para pág home

    form = LoginForms() # define o Forms a ser utilizado na pag de login como LoginForms()
    if request.method == 'POST': # Verifica se o html está executando a função POST com o conteúdo do formulário
        form = LoginForms(request.POST) # Formulário = conteúdo preenchido no formulário na função POST
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            user = authenticate(request, username=email, password=senha) # Verifica se o email do usuário coincide com a senha salva para este no banco
            if user is not None and user.is_active:
                    auth_login(request,user) # Função para fazer login armezenando alguns dados do usuário
                    messages.success(request,f"Usuário  {user.first_name} logado com sucesso")
                    return redirect('/')
            else:
                messages.error(request,"Senha incorreta!")
                return redirect('login') 
        else:
            messages.error(request,"Erro ao efetuar login")
                
    return render(request, 'usuarios/login.html', {"form": form})

def logout(request):
    if 'nota_fiscal_id' in request.session:
        nota_fiscal_id = request.session['nota_fiscal_id']
        nota_fiscal = FAT_Nota.objects.get(id=nota_fiscal_id)
        if not nota_fiscal.Encerrada:
            nota_fiscal.delete()
    auth_logout(request) # realiza logout do usuário
    messages.success(request, "logout realizado com sucesso")
    return redirect ('login') # redireciona para tela de login

def cadastro(request):
    form = CadastroForms() # define o Forms a ser utilizado na pag de login como CadastroForms()
    if request.method == 'POST': # Verifica se o html está executando a função POST com o conteúdo do formulário
        form = CadastroForms(request.POST) # Formulário = conteúdo preenchido no formulário na função POST
        if form.is_valid():
            if form.cleaned_data['senha_1'] != form.cleaned_data['senha_2']: # Verifica se a senha inserida e a confirmação de senha são diferentes
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
                    
            nome = form['nome_cadastro'].value()
            
            if not validar_campo(nome): # Valida se no campo nome não há caracteres inválidos como números, caractéres especiais e etc
                messages.error(request,"Nome contém caracteres inválidos")
                return redirect('cadastro')

            if DIM_Usuario.objects.filter(Email_USUARIO=email).exists(): # Verifica se o email já não está cadastrado em outro usuário
                messages.error(request,'Email já cadastrado')    
                return redirect('cadastro')

            if not validar_campo(cidade): # Valida se no campo cidade não há caracteres inválidos como números, caractéres especiais e etc
                messages.error(request,"Cidade contém caracteres inválidos")
                return redirect('cadastro')

            # Convertendo a data de nascimento em uma string antes de usar strptime()
            data_nascimento_str = data_nascimento.strftime('%Y-%m-%d')

            ano_nascimento = data_nascimento.year

            if ano_nascimento < (datetime.now().year - 110) or ano_nascimento > datetime.now().year:
            # Valida se a data de nascimento definida pelo usuário é válida
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
