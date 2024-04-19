from usuarios.models import DIM_Usuario

def create_DIM_USUARIO(form):
    # Extrair os dados do formulário
    nome = form.cleaned_data['nome_cadastro']
    email = form.cleaned_data['email']
    senha = form.cleaned_data['senha_1']
    telefone = form.cleaned_data['telefone']
    cidade = form.cleaned_data['cidade']
    curso = form.cleaned_data['curso']
    unidade = form.cleaned_data['unidade']
    data_nascimento = form.cleaned_data['data_nascimento']

    # Criar um novo usuário usando o seu modelo de usuário personalizado
    user = DIM_USUARIO.objects.create_user(
        email=email,
        password=senha,
        nome=nome,
        telefone=telefone,
        cidade=cidade,
        curso=curso,
        unidade=unidade,
        data_nascimento=data_nascimento
    )

    return user
