# Generated by Django 5.0.4 on 2024-04-19 04:45

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_vendas', '0002_dim_fornecedor_dim_produto_dim_usuario_fat_venda_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dim_usuario',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='dim_usuario',
            name='nome',
        ),
        migrations.AddField(
            model_name='dim_fornecedor',
            name='Cep_FORNECEDOR',
            field=models.CharField(default='', max_length=8, verbose_name='CEP do fornecedor'),
        ),
        migrations.AddField(
            model_name='dim_fornecedor',
            name='Cidade_FORNECEDOR',
            field=models.CharField(default='', max_length=50, verbose_name='Cidade do fornecedor'),
        ),
        migrations.AddField(
            model_name='dim_fornecedor',
            name='Cnpj_FORNECEDOR',
            field=models.CharField(default='', max_length=14, unique=True, verbose_name='CNPJ do fornecedor'),
        ),
        migrations.AddField(
            model_name='dim_fornecedor',
            name='Endereco_FORNECEDOR',
            field=models.CharField(default='', max_length=200, verbose_name='Endereço do fornecedor'),
        ),
        migrations.AddField(
            model_name='dim_fornecedor',
            name='Estado_FORNECEDOR',
            field=models.CharField(default='', max_length=2, verbose_name='Estado do fornecedor'),
        ),
        migrations.AddField(
            model_name='dim_fornecedor',
            name='Nome_FORNECEDOR',
            field=models.CharField(default='', max_length=100, verbose_name='Nome do fornecedor'),
        ),
        migrations.AddField(
            model_name='dim_produto',
            name='Descricao_PRODUTO',
            field=models.CharField(default='', max_length=300, verbose_name='Descrição do produto'),
        ),
        migrations.AddField(
            model_name='dim_produto',
            name='Imagem_PRODUTO',
            field=models.ImageField(default='', upload_to='fotos/'),
        ),
        migrations.AddField(
            model_name='dim_produto',
            name='Leedtime_PRODUTO',
            field=models.DecimalField(decimal_places=0, max_digits=2, null=True, verbose_name='Tempo medio de espera do produto'),
        ),
        migrations.AddField(
            model_name='dim_produto',
            name='Lote_minimo_PRODUTO',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True, verbose_name='Quantidade minima de compra'),
        ),
        migrations.AddField(
            model_name='dim_produto',
            name='Nome_PRODUTO',
            field=models.CharField(default='', max_length=100, verbose_name='Nome do produto'),
        ),
        migrations.AddField(
            model_name='dim_produto',
            name='Preco_produto',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Preço unitario do produto'),
        ),
        migrations.AddField(
            model_name='dim_produto',
            name='Preco_venda_PRODUTO',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2, null=True, verbose_name='Preço de venda do produto'),
        ),
        migrations.AddField(
            model_name='dim_produto',
            name='Produto_ativo_PRODUTO',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dim_produto',
            name='Tipo_PRODUTO',
            field=models.CharField(choices=[('vestuario', 'Vestuário'), ('caneca', 'Caneca')], default='', max_length=50, verbose_name='Tipo de produto'),
        ),
        migrations.AddField(
            model_name='dim_usuario',
            name='Cidade_usuario',
            field=models.CharField(default='', max_length=100, verbose_name='Cidade do usuario'),
        ),
        migrations.AddField(
            model_name='dim_usuario',
            name='Curso_USUARIO',
            field=models.CharField(choices=[('design_grafico', 'Design Gráfico'), ('ciencia_computacao', 'Ciência da Computação')], default='', max_length=50, verbose_name='Curso do usuario'),
        ),
        migrations.AddField(
            model_name='dim_usuario',
            name='Data_nascimento_USUARIO',
            field=models.DateField(null=True, verbose_name='Data de nascimento do usuario'),
        ),
        migrations.AddField(
            model_name='dim_usuario',
            name='Email_usuario',
            field=models.EmailField(default='', max_length=254, unique=True, verbose_name='E-mail do usuario'),
        ),
        migrations.AddField(
            model_name='dim_usuario',
            name='Idade_USUARIO',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Idade do usuario'),
        ),
        migrations.AddField(
            model_name='dim_usuario',
            name='Nome_USUARIO',
            field=models.CharField(default='', max_length=150, verbose_name='Nome do usuario'),
        ),
        migrations.AddField(
            model_name='dim_usuario',
            name='Senha_usuario',
            field=models.CharField(default='', max_length=50, verbose_name='Senha do usuario'),
        ),
        migrations.AddField(
            model_name='dim_usuario',
            name='Telefone_usuario',
            field=models.CharField(default='', max_length=20, unique=True, verbose_name='Telefone do usuario'),
        ),
        migrations.AddField(
            model_name='dim_usuario',
            name='Unidade_USUARIO',
            field=models.CharField(choices=[('unidade_independencia', 'Unidade Independência'), ('unidade_central', 'Unidade Central'), ('unidade_direito', 'Unidade Direito')], default='', max_length=30, verbose_name='Unidade de ensino'),
        ),
        migrations.AddField(
            model_name='fat_venda',
            name='Data_VENDA',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data da venda'),
        ),
        migrations.AddField(
            model_name='fat_venda',
            name='Id_FORNECEDOR',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='site_vendas.dim_fornecedor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fat_venda',
            name='Id_PRODUTO',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='site_vendas.dim_produto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fat_venda',
            name='Id_USUARIO',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='site_vendas.dim_usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fat_venda',
            name='Qtd_VENDA',
            field=models.IntegerField(default=0, verbose_name='Quantidade de venda'),
        ),
        migrations.AddField(
            model_name='fat_venda',
            name='Total_VENDA',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Total da venda'),
        ),
        migrations.CreateModel(
            name='FAT_pedido_compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qtd_PEDIDO', models.DecimalField(decimal_places=0, max_digits=2, null=True, verbose_name='Quantidade de itens')),
                ('Data_PEDIDO', models.DateField(default=django.utils.timezone.now, verbose_name='Data do pedido')),
                ('Data_chegada_PEDIDO', models.DateField(null=True, verbose_name='Data da chegada do pedido')),
                ('Custo_PEDIDO', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Custo total do pedido')),
                ('Id_FORNECEDOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_vendas.dim_fornecedor')),
                ('Id_PRODUTO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_vendas.dim_produto')),
            ],
        ),
    ]
