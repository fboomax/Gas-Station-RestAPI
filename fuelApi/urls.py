from django.urls import path
from .views import gas_station_all

urlpatterns = [
    path('api/v1/gas-stations', gas_station_all),
]
