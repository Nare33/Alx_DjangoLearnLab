from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
def follow_user(request, user_id):
    """
    Follow a user
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    user_to_follow = get_object_or_404(User, id=user_id)

    if user_to_follow == request.user:
        return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.following.add(user_to_follow)
    
    return Response({'detail': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def unfollow_user(request, user_id):
    """
    Unfollow a user
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    user_to_unfollow = get_object_or_404(User, id=user_id)

    if user_to_unfollow == request.user:
        return Response({'detail': 'You cannot unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.following.remove(user_to_unfollow)
    
    return Response({'detail': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)

class UserCreate(generics.CreateAPIView):
    queryset = UserSerializer.Meta.model.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = serializer.get_token(user)
        return Response({
            'token': token,
            'user_id': user.id,
            'username': user.username,
        })
