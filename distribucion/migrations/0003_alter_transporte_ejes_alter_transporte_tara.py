# Generated by Django 4.0.5 on 2022-07-26 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribucion', '0002_remove_transporte_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transporte',
            name='ejes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transporte',
            name='tara',
            field=models.IntegerField(),
        ),
    ]