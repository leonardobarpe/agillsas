# Generated by Django 2.0.2 on 2019-02-15 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerolinea', '0032_auto_20190214_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='vUtilOpc_i',
            field=models.CharField(choices=[('h', 'Horas'), ('t', 'Tiempo'), ('a', 'Ambos')], default='h', max_length=20, null=True, verbose_name='TBO inspeccion inicial'),
        ),
    ]
