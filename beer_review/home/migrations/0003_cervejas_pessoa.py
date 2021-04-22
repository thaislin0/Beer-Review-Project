# Generated by Django 3.1.7 on 2021-04-21 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('home', '0002_remove_cervejas_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='cervejas',
            name='pessoa',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa'),
            preserve_default=False,
        ),
    ]