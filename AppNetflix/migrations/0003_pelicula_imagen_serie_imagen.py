# Generated by Django 4.2.5 on 2023-10-01 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNetflix', '0002_rename_series_serie'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(default='default.jpg', upload_to='AppNetflix/assets/img/peliculas/'),
        ),
        migrations.AddField(
            model_name='serie',
            name='imagen',
            field=models.ImageField(default='default.jpg', upload_to='AppNetflix/assets/img/series/'),
        ),
    ]
