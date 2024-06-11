# Generated by Django 5.0.4 on 2024-06-11 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_vendas', '0022_fat_item_nota_lote_pendente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dim_produto',
            name='Preco_venda_PRODUTO',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, null=True, verbose_name='Preço de venda do produto'),
        ),
    ]
