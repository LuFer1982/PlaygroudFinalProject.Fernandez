# Generated by Django 4.2.7 on 2023-12-16 02:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0002_novedad_delete_sala'),
    ]

    operations = [
        migrations.AddField(
            model_name='novedad',
            name='imagen',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='imagenes/'),
            preserve_default=False,
        ),
    ]