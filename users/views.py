from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response

from .serializers import UserSerializer, LoginSerializer,ReadUserSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



# Create your views here.

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_user(request):
	serializer = UserSerializer(data=request.data)
	if not serializer.is_valid():
		return Response(serializer.errors, status=400)
	serializer.save()
	token, created = Token.objects.get_or_create(user=serializer.instance)
	return Response({'token': token.key}, status=201)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def login_user(request):
	serializer = LoginSerializer(data=request.data)
	if not serializer.is_valid():
		return Response(serializer.errors, status=400)

	user = authenticate(
		username=serializer.validated_data['username'],
		password=serializer.validated_data['password']
	)
	if not user:
		return Response({'detail': 'Invalid credentials'}, status=400)

	token, created = Token.objects.get_or_create(user=user)
	return Response({'token': token.key}, status=200)

@api_view(['GET'])
def logout_user(request):
	token = Token.objects.get(user=request.user)
	token.delete()
	return Response(status=200)

@api_view(["GET"])
def get_logged_in_user_data(request):
	serializer = ReadUserSerializer(request.user)
	return Response(serializer.data, status=200)

@api_view(["GET"])
def get_user(request,username):
	user= get_object_or_404(User, username=username)
	serializer = ReadUserSerializer(user)
	return Response(serializer.data,status=200)