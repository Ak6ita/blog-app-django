from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
# from posts.serializers import PostSerializer


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'password']
	
	def create(self, validated_data):
		validated_data['password'] = make_password(validated_data['password'])
		return super().create(validated_data)

class LoginSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=255)
	password = serializers.CharField(max_length=255)

	class Meta:
		fields = ['username', 'password']

class ReadUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["id","username", "email"]