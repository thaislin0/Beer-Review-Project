# Generated by Django 3.1.7 on 2021-04-22 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210422_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cervejas',
            old_name='Familia',
            new_name='descricao_cerveja',
        ),
        migrations.RenameField(
            model_name='cervejas',
            old_name='Origem',
            new_name='familia_cerveja',
        ),
        migrations.RenameField(
            model_name='cervejas',
            old_name='image',
            new_name='foto_cerveja',
        ),
        migrations.RenameField(
            model_name='cervejas',
            old_name='description',
            new_name='nome_cerveja',
        ),
        migrations.RenameField(
            model_name='cervejas',
            old_name='nota',
            new_name='nota_cerveja',
        ),
        migrations.RenameField(
            model_name='cervejas',
            old_name='title',
            new_name='origem_cerveja',
        ),
        migrations.RenameField(
            model_name='cervejas',
            old_name='Alcool',
            new_name='quantidade_alcool',
        ),
        migrations.RenameField(
            model_name='cervejas',
            old_name='Tipo',
            new_name='tipo_cerveja',
        ),
    ]
