# Generated by Django 5.0.4 on 2024-05-19 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_vendas', '0021_fat_nota_encerrada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fat_item_nota',
            name='Lote_pendente',
            field=models.BooleanField(default=True),
        ),
    ]