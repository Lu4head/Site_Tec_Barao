# Generated by Django 5.0.4 on 2024-04-28 02:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_vendas', '0012_remove_dim_produto_customizacao_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dim_produto',
            name='Tipo_PRODUTO',
            field=models.CharField(choices=[('camiseta', 'Camiseta'), ('caneca', 'Caneca'), ('blusa', 'Blusa'), ('tirante', 'Tirante'), ('short', 'Short')], default='', max_length=50, verbose_name='Tipo de produto'),
        ),
        migrations.AlterField(
            model_name='fat_item_nota',
            name='Id_FORNECEDOR',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='site_vendas.dim_fornecedor'),
        ),
        migrations.AlterField(
            model_name='fat_item_nota',
            name='Id_PRODUTO',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='site_vendas.dim_produto'),
        ),
        migrations.AlterField(
            model_name='fat_item_nota',
            name='Nota_fiscal',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='site_vendas.fat_nota'),
        ),
    ]
