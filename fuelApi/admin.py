from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(GasStation)
admin.site.register(User)
admin.site.register(PriceData)
admin.site.register(Order)

