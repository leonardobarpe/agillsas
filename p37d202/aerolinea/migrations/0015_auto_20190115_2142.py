# Generated by Django 2.0.2 on 2019-01-16 02:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerolinea', '0014_orden'),
    ]

    operations = [
        migrations.AddField(
            model_name='componente',
            name='vUtil',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Vida Util'),
        ),
        migrations.AlterField(
            model_name='componente',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='descripcion',
            field=ckeditor.fields.RichTextField(verbose_name='Descripcion'),
        ),
    ]
