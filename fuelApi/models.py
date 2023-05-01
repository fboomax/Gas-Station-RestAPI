from django.contrib.auth.models import User
from django.db import models


class GasStation(models.Model):
    gasStationID = models.IntegerField(primary_key=True)
    gasStationLat = models.DecimalField(max_digits=10, decimal_places=6)
    gasStationLong = models.DecimalField(max_digits=10, decimal_places=6)
    fuelCompID = models.IntegerField()
    fuelCompNormalName = models.CharField(max_length=45)
    gasStationOwner = models.CharField(max_length=128)
    ddID = models.CharField(max_length=10)
    ddNormalName = models.CharField(max_length=45)
    municipalityID = models.CharField(max_length=10)
    municipalityNormalName = models.CharField(max_length=45)
    countyID = models.CharField(max_length=10)
    countyName = models.CharField(max_length=64)
    gasStationAddress = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=10)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.fuelCompNormalName


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=22)
    password = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
