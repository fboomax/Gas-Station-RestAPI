# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import GasStation
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Max, Min
from django.template.defaultfilters import floatformat
from django.core import serializers


class GasStationsAllJson(APIView):
    def get(self, request):
        gas_stations = GasStation.objects.all()
        serializer = GasStationSerializer(gas_stations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GasStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GasStationsAllXML(APIView):
    def get(self, request):
        gas_stations = GasStation.objects.all()
        xml_data = serializers.serialize('xml', gas_stations)
        return HttpResponse(xml_data, content_type='application/xml')


class GasStationDetail(APIView):

    def get_object(self, pk):
        try:
            return GasStation.objects.get(gasStationID=pk)
        except GasStation.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        gas_station = self.get_object(pk)
        serializer = GasStationSerializer(gas_station)
        return Response(serializer.data)

    def put(self, request, pk):
        gas_station = self.get_object(pk)
        serializer = GasStationSerializer(gas_station, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        gas_station = self.get_object(pk)
        gas_station.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GasStationCount(APIView):
    def get(self, request):
        count = GasStation.objects.count()
        data = {'count': count}
        return Response(data)
        # return Response(count)


#
class GasStationPriceData(APIView):

    def get(self, request, pk):
        prices_data = PriceData.objects.filter(gasStationID=pk)
        serializer = PriceDataSerializer(prices_data, many=True)
        return Response(serializer.data)


class PricesData(APIView):
    def get(self, request):
        prices_data = PriceData.objects.all()
        serializer = PriceDataSerializer(prices_data, many=True)
        return Response(serializer.data)


class PriceDataAggregate(APIView):
    def get(self, request):
        prices = PriceData.objects.aggregate(Min('fuelPrice'), Max('fuelPrice'), Avg('fuelPrice'))

        avg_price = floatformat(prices['fuelPrice__avg'], 3)

        data = {
            'min_price': prices['fuelPrice__min'],
            'max_price': prices['fuelPrice__max'],
            'avg_price': float(avg_price),

        }
        return Response(data)


class Users(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(userID=pk)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        user = User.objects.get(userID=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
