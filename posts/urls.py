from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_all_personal_posts, name="get_all_personal_posts"),
    path("users/<str:username>",views.get_all_posts, name="get_all_posts"),
    path("<int:post_id>/comment",views.post_comment,name="post_comment"),
    path("comments/<int:pk>/edit",views.edit_comment,name = "edit_comment"),
    path("comments/<int:pk>/delete",views.delete_comment, name = "delete_comment"),
    path("blog/create", views.create_blog_post, name = "create_blog_post"),
    path("blog/<int:pk>",views.get_blog, name="get_blog" ),
    path('blog/<int:pk>/edit', views.edit_blog_post, name='edit_blog_post'),
    path("blog/<int:pk>/delete",views.delete_blog_post,name = "delete_blog_post"),
]