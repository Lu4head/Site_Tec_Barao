from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from usuarios.models import DIM_Usuario

def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            user = DIM_Usuario.objects.filter(Email_USUARIO=email).first()

            if user is not None and user.Senha_USUARIO == senha:
                request.session["email"] = user.Email_USUARIO
                return redirect('/')
            else:
                return redirect('login')          
    return render(request,'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form['senha_1'].value() != form['senha_2'].value():
                return redirect('cadastro')
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
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
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})