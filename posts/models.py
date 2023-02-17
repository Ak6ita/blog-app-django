from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=256)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)


