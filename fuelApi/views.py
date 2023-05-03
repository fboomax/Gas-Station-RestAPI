from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import GasStation


@api_view(['GET', 'POST'])
def gas_station_all(request):

    if request.method == 'GET':
        gas_stations = GasStation.objects.all()
        serializer = GasStationSerializer(gas_stations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = GasStationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view
def gas_station_detail(request, pk):
    try:
        gas_station = GasStation.objects.get(pk=pk)

    except GasStation.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GasStationSerializer(gas_station)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GasStationSerializer(gas_station, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        gas_station.delete()
        return HttpResponse(status=204)


