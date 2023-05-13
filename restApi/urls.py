from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fuelApi.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
