# Generated by Django 4.2 on 2023-05-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuelApi', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedata',
            name='dataUpdated',
            field=models.DateTimeField(),
        ),
    ]
