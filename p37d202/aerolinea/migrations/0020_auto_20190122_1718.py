# Generated by Django 2.0.2 on 2019-01-22 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerolinea', '0019_auto_20190122_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='vUtil',
            field=models.DateField(verbose_name='Vida Util Calendario'),
        ),
    ]
