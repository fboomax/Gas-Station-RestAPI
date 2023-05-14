from django.urls import path
from .views import *

urlpatterns = [

    path('api/v1/gas-stations', GasStationsAllJson.as_view()),
    path('api/v1/gas-stations-xml', GasStationsAllXML.as_view()),
    path('api/v1/gas-stations/<int:pk>', GasStationDetail.as_view()),
    path('api/v1/gas-stations/<int:pk>/prices-data', GasStationPriceData.as_view()),
    path('api/v1/gas-stations/all', GasStationCount.as_view()),
    path('api/v1/prices-data', PricesData.as_view()),
    path('api/v1/prices-data/aggregate', PriceDataAggregate.as_view()),
    path('api/v1/users', Users.as_view()),
    path('api/v1/users/<int:pk>', UserDetail.as_view()),


]
