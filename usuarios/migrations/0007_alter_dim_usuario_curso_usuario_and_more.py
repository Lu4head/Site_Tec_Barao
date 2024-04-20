# Generated by Django 5.0.4 on 2024-04-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_alter_dim_usuario_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dim_usuario',
            name='Curso_USUARIO',
            field=models.CharField(choices=[('design_grafico', 'Design Gráfico'), ('ciencia_computacao', 'Ciência da Computação'), ('administracao', 'Administração'), ('arquitetura_e_urbanismo', 'Arquitetura e Urbanismo'), ('biomedicina', 'Biomedicina'), ('ciencias_biologicas', 'Ciências Biológicas'), ('direito', 'Direito'), ('enfermagem', 'Enfermagem'), ('estetica_e_cosmetica', 'Estética e Cosmética'), ('farmacia', 'Farmácia'), ('fisioterapia', 'Fisioterapia'), ('gestao_de_recursos_humanos', 'Gestão de Recursos Humanos'), ('gestao_financeira', 'Gestão Financeira'), ('historia', 'História'), ('jornalismo', 'Jornalismo'), ('letras', 'Letras'), ('marketing', 'Marketing'), ('medicina', 'Medicina'), ('medcina_veterinaria', 'Medicina Veterinária'), ('nutricao', 'Nutrição'), ('pedagogia', 'Pedagogia'), ('producao_audiovisual', 'Produção Audiovisual'), ('psicologia', 'Psicologia'), ('publicidade_e_propaganda', 'Publicidade e Propaganda')], default='', max_length=50, verbose_name='Curso do usuario'),
        ),
        migrations.AlterField(
            model_name='dim_usuario',
            name='Unidade_USUARIO',
            field=models.CharField(choices=[('unidade_independencia', 'Unidade Independência'), ('unidade_central', 'Unidade Central'), ('unidade_direito', 'Unidade Direito'), ('unidade_gastronomia', 'Unidade Gastronomia'), ('unidade_arquitetura_e_urbanismo', 'Unidade Arquitetura e Urbanismo')], default='', max_length=50, verbose_name='Unidade de ensino'),
        ),
    ]
