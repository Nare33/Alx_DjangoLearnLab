from django.urls import path
from .views import UserCreate, LoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]

