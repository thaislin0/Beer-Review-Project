# Generated by Django 3.1.7 on 2021-04-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_cervejas_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cervejas',
            name='nota',
            field=models.IntegerField(default='5', max_length=5),
        ),
    ]