# Generated by Django 3.0.4 on 2020-05-06 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thessia', '0005_auto_20200429_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuento',
            name='pages',
            field=models.IntegerField(default=0, verbose_name='paginas'),
        ),
        migrations.AddField(
            model_name='cuento',
            name='texto',
            field=models.CharField(default='nada', max_length=10000, verbose_name='texto'),
        ),
    ]
