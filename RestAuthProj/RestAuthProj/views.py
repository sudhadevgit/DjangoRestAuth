from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserSerializer

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username = request.data["username"])
        user.set_password(request.data["password"])
        user.save()
        token = Token.objects.create(user = user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username = request.data["username"] )
    if not user.check_password(request.data["password"]):
        return Response({"detail": 'NOT_FOUND', "status": status.HTTP_404_NOT_FOUND })
    token, created = Token.objects.get_or_create(user = user)
    serializer = UserSerializer(instance = user)
    return Response({"token": token.key, 'user': serializer.data})