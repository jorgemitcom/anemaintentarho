# Generated by Django 3.0.4 on 2020-04-28 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thessia', '0002_auto_20200428_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuento',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='cuento',
            name='last_modified_by',
        ),
    ]