# Generated by Django 4.2.7 on 2023-12-20 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='imagen',
            field=models.ImageField(upload_to='imagenes'),
        ),
        migrations.AlterField(
            model_name='perfilusuario',
            name='rol',
            field=models.CharField(blank=True, choices=[('docente', 'docente'), ('familia', 'familia')], max_length=10, null=True),
        ),
    ]