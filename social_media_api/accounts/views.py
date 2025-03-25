from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthentcated
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if request.user != user_to_follow and user_to_follow not in request.user.followers.all():
        request.user.followers.add(user_to_follow)
        return Response({'message': 'User followed successfully.'}, status=status.HTTP_200_OK)
    return Response({'message': 'You are already following this user or cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    if user_to_unfollow in request.user.followers.all():
        request.user.followers.remove(user_to_unfollow)
        return Response({'message': 'User unfollowed successfully.'}, status=status.HTTP_200_OK)
    return Response({'message': 'You are not following this user.'}, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
