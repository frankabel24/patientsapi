# Generated by Django 5.0.6 on 2024-06-26 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ZipCode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]
