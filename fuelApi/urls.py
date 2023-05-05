from django.urls import path
from .views import *

urlpatterns = [

    path('api/v1/gas-stations', GasStationsAll.as_view()),
    path('api/v1/gas-stations/<int:pk>', GasStationDetail.as_view()),
    path('api/v1/users', Users.as_view()),
    path('api/v1/users/<int:pk>', UserDetail.as_view()),
    path('api/v1/prices-data', PricesData.as_view()),

]
