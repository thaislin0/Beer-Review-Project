# Generated by Django 3.1.7 on 2021-04-14 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210414_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='tipo_cerveja',
            field=models.CharField(default='', editable=False, max_length=150),
        ),
    ]
