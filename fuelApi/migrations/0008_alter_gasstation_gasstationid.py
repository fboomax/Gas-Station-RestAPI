# Generated by Django 4.2 on 2023-05-03 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuelApi', '0007_alter_pricedata_dataupdated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasstation',
            name='gasStationID',
            field=models.IntegerField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
