# Generated by Django 2.0.2 on 2019-02-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerolinea', '0023_aeronave_ordencom'),
    ]

    operations = [
        migrations.AddField(
            model_name='aeronave',
            name='alerta',
            field=models.CharField(default='No', max_length=20, verbose_name='Alerta'),
        ),
        migrations.AddField(
            model_name='componente',
            name='alerta',
            field=models.CharField(default='No', max_length=20, verbose_name='Alerta'),
        ),
    ]
