# Generated by Django 4.2 on 2023-05-03 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fuelApi', '0003_remove_gasstation_username_delete_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GasStation',
            fields=[
                ('gasStationID', models.IntegerField(primary_key=True, serialize=False)),
                ('gasStationLat', models.DecimalField(decimal_places=10, max_digits=19)),
                ('gasStationLong', models.DecimalField(decimal_places=10, max_digits=19)),
                ('fuelCompID', models.IntegerField()),
                ('fuelCompNormalName', models.CharField(max_length=45)),
                ('gasStationOwner', models.CharField(max_length=128)),
                ('ddID', models.CharField(max_length=10)),
                ('ddNormalName', models.CharField(max_length=45)),
                ('municipalityID', models.CharField(max_length=10)),
                ('municipalityNormalName', models.CharField(max_length=45)),
                ('countyID', models.CharField(max_length=10)),
                ('countyName', models.CharField(max_length=64)),
                ('gasStationAddress', models.CharField(max_length=255)),
                ('phone1', models.CharField(max_length=10)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
