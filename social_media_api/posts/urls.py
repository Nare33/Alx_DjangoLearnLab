from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/like/', views.like_post, name='like_post'),
    path('<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
]
