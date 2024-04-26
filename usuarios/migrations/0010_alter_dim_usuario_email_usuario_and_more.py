# Generated by Django 5.0.4 on 2024-04-25 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_dim_usuario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dim_usuario',
            name='Email_USUARIO',
            field=models.EmailField(blank=True, default='', max_length=254, null=True, verbose_name='E-mail do usuario'),
        ),
        migrations.AlterField(
            model_name='dim_usuario',
            name='Telefone_USUARIO',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Telefone do usuario'),
        ),
    ]