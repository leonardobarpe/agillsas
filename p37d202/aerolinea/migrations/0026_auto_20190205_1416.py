# Generated by Django 2.0.2 on 2019-02-05 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aerolinea', '0025_componente_porcenuso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuelo',
            name='aeronave',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aerolinea.Aeronave'),
        ),
    ]