from django.contrib.auth import get_user_model, authenticate
from django.db import models
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from users.serializers import UserSerializer

User = get_user_model()


class UserRegistrationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        if User.objects.filter(email=data['email']).exists():
            return Response({'error': {'email': 'email already exists'}}, status=status.HTTP_403_FORBIDDEN)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        token = Token.objects.create(user=user)
        return Response({'token': token.key})


class CustomAuthToken(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        if not email:
            return Response({'error': 'email обязательное поле'}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({'error': 'password обязательное поле'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(email=email, password=password)
        if not user:
            return Response({'error': 'Неверный email или пароль'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status.HTTP_200_OK)
