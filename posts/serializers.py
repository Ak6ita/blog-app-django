from dataclasses import fields
from rest_framework import serializers

from users.serializers import ReadUserSerializer
from .models import Post,Comment

class CommentSerializer(serializers.ModelSerializer):
    user = ReadUserSerializer(read_only = True)
    class Meta:
        model = Comment
        fields = "__all__"


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many =True,read_only =True)
    class Meta:
        model = Post
        fields = ["id","title","description", "author","comment_set"]
        


