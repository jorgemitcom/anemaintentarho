# Generated by Django 3.0.4 on 2020-05-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thessia', '0010_pruebatres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pruebatres',
            name='def1',
            field=models.CharField(max_length=200, verbose_name='def1'),
        ),
        migrations.AlterField(
            model_name='pruebatres',
            name='def2',
            field=models.CharField(max_length=200, verbose_name='def2'),
        ),
        migrations.AlterField(
            model_name='pruebatres',
            name='def3',
            field=models.CharField(max_length=200, verbose_name='def3'),
        ),
    ]