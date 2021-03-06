# Generated by Django 3.0.4 on 2020-05-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thessia', '0008_auto_20200511_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='PruebaUno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept', models.CharField(max_length=50, verbose_name='concepto')),
                ('definition', models.CharField(max_length=200, verbose_name='definicion')),
            ],
            options={
                'verbose_name': 'PruebaUno',
                'verbose_name_plural': 'PruebasUno',
                'ordering': ['-concept'],
            },
        ),
    ]
