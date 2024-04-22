from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from usuarios.models import DIM_Usuario
from django.contrib import messages


def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            user = DIM_Usuario.objects.filter(Email_USUARIO=email).first()
            if user is not None:
                if user.Senha_USUARIO == senha:
                    request.session["email"] = user.Email_USUARIO
                    messages.success(request,f"Usuário  {user.Nome_USUARIO} logado com sucesso")
                    return redirect('/')
                else:
                    messages.error(request,"Senha incorreta!")
                    return redirect('login')
            else:
                messages.error(request,"Usuário não existe!")
                return redirect('login')
        else:
            messages.error(request,"Erro ao efetuar login")
            return redirect('login')
    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            if form.cleaned_data['senha_1'] != form.cleaned_data['senha_2']:
                messages.error(request, "Senhas divergentes")
                return redirect('cadastro') 
                    
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            if DIM_Usuario.objects.filter(Email_USUARIO=email).exists():
                messages.error(request,'Email já cadastrado')    
                return redirect('cadastro')
            senha = form['senha_1'].value()
            telefone = form['telefone'].value()
            cidade = form['cidade'].value()
            curso = form['curso'].value()
            unidade = form['unidade'].value()
            data_nascimento = form['data_nascimento'].value()

            if DIM_Usuario.objects.filter(Nome_USUARIO=nome).exists():
                return redirect('cadastro')
            
            user = DIM_Usuario.objects.create(
                Nome_USUARIO=nome,
                Email_USUARIO =email,
                Senha_USUARIO=senha,
                Telefone_USUARIO=telefone,
                Cidade_USUARIO=cidade,
                Curso_USUARIO=curso,
                Unidade_USUARIO=unidade,
                Data_nascimento_USUARIO=data_nascimento,
            )
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})