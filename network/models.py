from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
#     created_at = models.DateTimeField(auto_now_add=True)
