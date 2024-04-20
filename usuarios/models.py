from django.db import models
from datetime import datetime
from django.utils import timezone



class DIM_Usuario(models.Model):

    cursos = [("design_grafico", "Design Gráfico"),
          ("ciencia_computacao", "Ciência da Computação")]

    unidades = [("unidade_independencia", "Unidade Independência"),
            ("unidade_central", "Unidade Central"),
            ("unidade_direito", "Unidade Direito")]

    Nome_USUARIO = models.CharField(max_length=150, null=False, blank=False, default="", verbose_name="Nome do usuario")
    Data_nascimento_USUARIO = models.DateField(verbose_name="Data de nascimento do usuario", null=True)
    Idade_USUARIO = models.PositiveIntegerField(null=True, blank=True, verbose_name="Idade do usuario")
    Curso_USUARIO = models.CharField(max_length=50, choices=cursos, default="", verbose_name="Curso do usuario")
    Unidade_USUARIO = models.CharField(max_length=30, choices=unidades, default="", verbose_name="Unidade de ensino")
    Cidade_USUARIO = models.CharField(max_length=100, null=False, blank=False, default="", verbose_name="Cidade do usuario")
    Email_USUARIO  = models.EmailField(max_length=254, null=False, blank=False, default="", unique=True, verbose_name="E-mail do usuario")
    Telefone_USUARIO = models.CharField(max_length=20, null=False, blank=False, unique=True, verbose_name="Telefone do usuario", default="")
    Senha_USUARIO  = models.CharField(max_length=50, verbose_name="Senha do usuario", default="")

    class Meta:
        verbose_name = "Usuario_aplicação"
        verbose_name_plural = "Usuarios_aplicação"

    def __str__(self):
        return self.Nome_USUARIO

    def save(self, *args, **kwargs):
        if self.Data_nascimento_USUARIO:
            if isinstance(self.Data_nascimento_USUARIO, str):
                data_nascimento = datetime.strptime(self.Data_nascimento_USUARIO, '%Y-%m-%d').date()
            else:
                data_nascimento = self.Data_nascimento_USUARIO

            hoje = timezone.now().date()
            idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
            self.Idade_USUARIO = idade

        super(DIM_Usuario, self).save(*args, **kwargs)
