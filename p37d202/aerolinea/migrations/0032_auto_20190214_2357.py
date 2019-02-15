# Generated by Django 2.0.2 on 2019-02-15 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerolinea', '0031_auto_20190214_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='componente',
            name='hvUtil_i',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Horas inspec inicial TBO'),
        ),
        migrations.AddField(
            model_name='componente',
            name='vUtilOpc_i',
            field=models.CharField(choices=[('h', 'Horas'), ('t', 'Tiempo'), ('a', 'Ambos')], default='h', max_length=20, verbose_name='TBO inspeccion inicial'),
        ),
        migrations.AddField(
            model_name='componente',
            name='vUtil_i',
            field=models.DateField(blank=True, null=True, verbose_name='TBO Calendario inspec inicial'),
        ),
        migrations.AlterField(
            model_name='componente',
            name='ordenTrabajo',
            field=models.CharField(default='OT7', max_length=20, verbose_name='Orden Trabajo'),
        ),
    ]
