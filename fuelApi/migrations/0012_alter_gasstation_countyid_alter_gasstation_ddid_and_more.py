# Generated by Django 4.2 on 2023-05-03 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuelApi', '0011_alter_gasstation_phone1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasstation',
            name='countyID',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='gasstation',
            name='ddID',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='gasstation',
            name='phone1',
            field=models.CharField(max_length=20),
        ),
    ]
