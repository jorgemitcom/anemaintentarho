# Generated by Django 3.0.4 on 2020-05-11 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thessia', '0007_auto_20200507_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuento',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thessia_cuento_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
    ]
