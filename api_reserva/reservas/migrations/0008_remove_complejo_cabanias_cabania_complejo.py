# Generated by Django 4.2.3 on 2023-07-04 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0007_rename_nombre_servicio_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complejo',
            name='cabanias',
        ),
        migrations.AddField(
            model_name='cabania',
            name='complejo',
            field=models.ManyToManyField(default=None, to='reservas.complejo'),
        ),
    ]
