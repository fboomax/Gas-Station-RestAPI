# Generated by Django 4.2 on 2023-05-06 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fuelApi', '0013_alter_gasstation_countyid_alter_gasstation_ddid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedata',
            name='gasStationID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_data', to='fuelApi.gasstation'),
        ),
    ]
