from django.urls import path
from .views import UserRegistrationView, UserLoginView, follow_user, unfollow_user, UserDetail


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user_detail'),
]

