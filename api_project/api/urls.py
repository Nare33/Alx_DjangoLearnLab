from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include(router.urls)),
]
