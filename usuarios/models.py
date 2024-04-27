from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User





class DIM_Usuario(models.Model):
# Modelo/Classe que define a tabela de Usuários da aplicação no banco de dados
    cursos = [ # Dicionário para utilização dos campos choices com todos os cursos do CBM
        ("administracao", "Administração"),
        ("arquitetura_e_urbanismo", "Arquitetura e Urbanismo"),
        ("biomedicina", "Biomedicina"),
        ("ciencia_computacao", "Ciência da Computação"),
        ("ciencias_biologicas", "Ciências Biológicas"),
        ("design_grafico", "Design Gráfico"),
        ("direito", "Direito"),
        ("enfermagem", "Enfermagem"),
        ("estetica_e_cosmetica", "Estética e Cosmética"),
        ("farmacia", "Farmácia"),
        ("fisioterapia", "Fisioterapia"),
        ("gestao_de_recursos_humanos", "Gestão de Recursos Humanos"),
        ("gestao_financeira", "Gestão Financeira"),
        ("historia", "História"),
        ("jornalismo", "Jornalismo"),
        ("letras", "Letras"),
        ("marketing", "Marketing"),
        ("medicina", "Medicina"),
        ("medcina_veterinaria", "Medicina Veterinária"),
        ("nutricao", "Nutrição"),
        ("pedagogia", "Pedagogia"),
        ("producao_audiovisual", "Produção Audiovisual"),
        ("psicologia", "Psicologia"),
        ("publicidade_e_propaganda", "Publicidade e Propaganda")
        ]

    unidades = [ # Dicionário para utilização dos campos choices com todos as unidades do CBM
        ("unidade_arquitetura_e_urbanismo", "Unidade Arquitetura e Urbanismo"),
        ("unidade_central", "Unidade Central"),
        ("unidade_direito", "Unidade Direito"),
        ("unidade_gastronomia", "Unidade Gastronomia"),
        ("unidade_independencia", "Unidade Independência")
        ]
    
    

    Nome_USUARIO = models.CharField(max_length=150, null=False, blank=False, default="", verbose_name="Nome do usuario")
    Data_nascimento_USUARIO = models.DateField(verbose_name="Data de nascimento do usuario", null=True)
    Idade_USUARIO = models.PositiveIntegerField(null=True, blank=True, verbose_name="Idade do usuario") # Idade é calculada através da data de nascimento e o dia atual pela função save()
    Curso_USUARIO = models.CharField(max_length=50, choices=cursos, default="", verbose_name="Curso do usuario") # Campo de escolha de cursos que usa o dicionário cursos
    Unidade_USUARIO = models.CharField(max_length=50, choices=unidades, default="", verbose_name="Unidade de ensino") # Campo de escolha de unidades que usa o dicionário unidades
    Cidade_USUARIO = models.CharField(max_length=100, null=False, blank=False, default="", verbose_name="Cidade do usuario")
    Email_USUARIO  = models.EmailField(max_length=254, null=True, blank=True, default="", verbose_name="E-mail do usuario")
    Telefone_USUARIO = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefone do usuario", default="")
    Senha_USUARIO  = models.CharField(max_length=50, verbose_name="Senha do usuario", default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dim_usuario') # Relaciona um usuário da tabela padrão do Django User com cada usuário criado na aplicação

    class Meta:
        verbose_name = "Usuario_aplicação" # Nome de exibição da classe no singular
        verbose_name_plural = "Usuarios_aplicação" # Nome de exibição da classe no plural

    def __str__(self):
        return self.Nome_USUARIO # Exibição ao printar o objeto

    def save(self, *args, **kwargs): # Função para calcular a idade do usuário através da data de nascimento
        if self.Data_nascimento_USUARIO:
            if isinstance(self.Data_nascimento_USUARIO, str): # Garante que a data de nascimento vai ter a formatação correta e o tipo correto
                data_nascimento = datetime.strptime(self.Data_nascimento_USUARIO, '%Y-%m-%d').date() 
            else:
                data_nascimento = self.Data_nascimento_USUARIO

            hoje = timezone.now().date() # Função que armazena o dia atual
            idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)) # idade = dia atual - data de nascimento - 0 ou 1 (se a pessoa já fez aniversário esse ano ou não)
            self.Idade_USUARIO = idade

        super(DIM_Usuario, self).save(*args, **kwargs)
        