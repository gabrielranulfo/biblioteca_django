# Generated by Django 4.1.1 on 2022-09-15 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0009_remove_livros_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='usuario',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
    ]
