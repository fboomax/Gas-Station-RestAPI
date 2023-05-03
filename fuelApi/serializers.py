from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GasStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasStation
        fields = '__all__'


class PriceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceData
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
