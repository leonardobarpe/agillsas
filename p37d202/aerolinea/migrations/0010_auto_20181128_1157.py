# Generated by Django 2.0.2 on 2018-11-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerolinea', '0009_vuelo_aeronave'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vuelo',
            options={'ordering': ['-creado'], 'verbose_name': 'Vuelo', 'verbose_name_plural': 'Vuelos'},
        ),
        migrations.AddField(
            model_name='componente',
            name='hDurg',
            field=models.IntegerField(blank=True, null=True, verbose_name='Horas durg'),
        ),
        migrations.AddField(
            model_name='componente',
            name='hRemanente',
            field=models.IntegerField(blank=True, null=True, verbose_name='Horas remanente'),
        ),
        migrations.AddField(
            model_name='componente',
            name='mDurg',
            field=models.IntegerField(blank=True, null=True, verbose_name='Minutos durg'),
        ),
        migrations.AddField(
            model_name='componente',
            name='mRemanente',
            field=models.IntegerField(blank=True, null=True, verbose_name='Minutos remanente'),
        ),
    ]
