from django.contrib import admin
from django.urls import path, include
from data import views



urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include('data.urls')),
]

