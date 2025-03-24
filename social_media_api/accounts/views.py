from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer

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
