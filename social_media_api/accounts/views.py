from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import CustomUser
from posts.models import Post
from posts.serializers import PostSerializer

class FollowUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user = request.user  
        user_to_follow = get_object_or_404(CustomUser, id=user_id)

        if user_to_follow != user:
            user.following.add(user_to_follow)
            return Response({"detail": f"Now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

        return Response({"detail": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

class UnfollowUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user = request.user 
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

        if user_to_unfollow != user:
            user.following.remove(user_to_unfollow)
            return Response({"detail": f"Unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)

        return Response({"detail": "You cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)

class UserFeed(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  
        followed_users = user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

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
