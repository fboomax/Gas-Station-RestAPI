from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/gas-stations', gas_station_all),
    path('api/v1/gas-stations/<int:pk>', gas_station_detail),
    # path('api/v1/gas-stations', gas_station_all),
]
