# Generated by Django 4.2.5 on 2023-10-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNetflix', '0005_pelicula_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.CharField(max_length=8),
        ),
    ]
