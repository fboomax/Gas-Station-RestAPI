from django.db import models

class User(models.Model):
    userID = models.IntegerField(primary_key=True, serialize=False)
    username = models.CharField(max_length=22)
    password = models.CharField(max_length=45)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.username


class GasStation(models.Model):
    gasStationID = models.IntegerField(primary_key=True, serialize=False)
    gasStationLat = models.DecimalField(max_digits=19, decimal_places=10)
    gasStationLong = models.DecimalField(max_digits=19, decimal_places=10)
    fuelCompID = models.IntegerField()
    fuelCompNormalName = models.CharField(max_length=255)
    gasStationOwner = models.CharField(max_length=255)
    ddID = models.CharField(max_length=40)
    ddNormalName = models.CharField(max_length=45)
    municipalityID = models.CharField(max_length=60)
    municipalityNormalName = models.CharField(max_length=45)
    countyID = models.CharField(max_length=40)
    countyName = models.CharField(max_length=64)
    gasStationAddress = models.CharField(max_length=400)
    phone1 = models.CharField(max_length=40)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.fuelCompNormalName


class PriceData(models.Model):
    productID = models.IntegerField(primary_key=True, serialize=False)
    gasStationID = models.ForeignKey(GasStation, on_delete=models.CASCADE)
    fuelTypeID = models.IntegerField()
    fuelSubTypeID = models.IntegerField()
    fuelNormalName = models.CharField(max_length=64)
    fuelName = models.CharField(max_length=128)
    fuelPrice = models.DecimalField(max_digits=4, decimal_places=3)
    dataUpdated = models.DateTimeField(auto_now=False)
    isPremium = models.BooleanField(default="False")

    def __str__(self):
        return self.fuelNormalName


class Order(models.Model):
    orderID = models.IntegerField(primary_key=True, serialize=False)
    productID = models.ForeignKey(PriceData, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.userID
