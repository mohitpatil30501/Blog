from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=30)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING)
    headline = models.CharField(max_length=200)
    body_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modifies_at = models.DateTimeField(auto_now=True)


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modifies_at = models.DateTimeField(auto_now=True)


class LikePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    is_like = models.BooleanField(default=False)


class LikeComment(models.Model):
    comment = models.ForeignKey(PostComment, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    is_like = models.BooleanField(default=False)
