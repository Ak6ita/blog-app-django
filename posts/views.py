from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post,Comment
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import TokenAuthentication
from .serializers import PostSerializer,CommentSerializer,CreateCommentSerializer

@api_view(['GET'])
def get_all_personal_posts(request):
	posts = Post.objects.filter(author=request.user)
	serializer = PostSerializer(posts, many=True)
	return Response(serializer.data, status=200)

@api_view(['GET'])
def get_all_posts(request,username):
	posts = Post.objects.filter(author__username=username)
	serializer = PostSerializer(posts, many=True)
	return Response(serializer.data, status=200)

@api_view(["POST"])
def post_comment(request,post_id):
	request.data['user'] = request.user.id
	request.data["post"]=post_id
	# {'user': 1, 'post': 2, 'body': 'Ova e odli4en post'}
	serializer = CreateCommentSerializer(data=request.data)
	if not serializer.is_valid():
		return Response(serializer.errors, status=400)
	serializer.save()
	return Response(serializer.data, status=201)

@api_view(["POST"])
def edit_comment(request,pk):
	comment = get_object_or_404(Comment, pk=pk)
	if request.user != comment.author:
		return Response(status=403)
	serializer = CommentSerializer(comment,data=request.data,partial=True)
	if not serializer.is_valid():
		return Response(serializer.errors, status =400)
	serializer.save()
	return Response(serializer.data, status=200)

@api_view(["DELETE"])
def delete_comment(request,pk):
	comment = get_object_or_404(Comment,pk=pk)
	if request.user != comment.author:
		return Response(status=403)
	comment.delete()
	return Response(status=204)

@api_view(["POST"])
def create_blog_post(request):
	request.data["author"] = request.user.id
	serializer = PostSerializer(data = request.data)
	if not serializer.is_valid():
		return Response(serializer.errors, status =400)
	serializer.save()
	return Response(serializer.data, status=201)

@api_view(["GET"])
def get_blog(request, pk):
	post = get_object_or_404(Post, pk=pk)
	serializer = PostSerializer(post)
	return Response(serializer.data, status=200)


@api_view(["POST"])
def edit_blog_post(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.user != post.author:
		return Response(status=403)
	serializer = PostSerializer(post,data=request.data,partial=True)
	if not serializer.is_valid():
		return Response(serializer.errors, status =400)
	serializer.save()
	return Response(serializer.data, status=200)

@api_view(["DELETE"])
def delete_blog_post(request,pk):
	post = get_object_or_404(Post,pk=pk)
	if request.user != post.author:
		return Response(status=403)
	post.delete()
	return Response(status=204)





