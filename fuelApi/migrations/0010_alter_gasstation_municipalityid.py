# Generated by Django 4.2 on 2023-05-03 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuelApi', '0009_alter_gasstation_fuelcompnormalname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasstation',
            name='municipalityID',
            field=models.CharField(max_length=60),
        ),
    ]
