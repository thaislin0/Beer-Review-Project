# Generated by Django 3.1.7 on 2021-04-23 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210422_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cervejas',
            name='foto_cerveja',
            field=models.ImageField(upload_to='home/images'),
        ),
    ]
