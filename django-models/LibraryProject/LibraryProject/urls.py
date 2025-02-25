from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('custom-admin/', admin.site.urls),
]

