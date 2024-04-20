<h1 align="center"> Site para vendas da Atlética de Técnologia Barão de Mauá </h1>

Passo a passo para utilizar o repositório:

1. Fazer download do python caso ainda não o tenha
2. Clonar repositório para uma pasta vazia de seu sistema
3. Abrir repositório em uma IDE (vs code)
4. Linkar ele com este repositório online digitando no terminal: git remote add upstream https://github.com/Lu4head/Site_Tec_Barao.git 
5. Criar um ambiente virtual dentro do repositório digitando no terminal: python -m venv venv
6. Alterar seu terminal para dentro do ambiente virtual criado digitando no terminal: ./venv/Scripts/activate
7. Instalar as dependências digitando no terminal: pip install -r requirements.txt
8. No diretório base onde está o repositório criar um arquivo .env com a key que eu passar pra vocês
9. Subir banco de dados digitando no terminal: python manage.py migrate
10. Para dar RUN no projeto em sua máquina digitar no terminal: python manage.py runserver
