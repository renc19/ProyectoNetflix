# Generated by Django 4.2.5 on 2023-10-01 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppNetflix', '0003_pelicula_imagen_serie_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='imagen',
        ),
    ]
