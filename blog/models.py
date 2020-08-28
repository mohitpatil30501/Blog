from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=30)


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING)
    headline = models.CharField(max_length=200)
    body_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modifies_at = models.DateTimeField(auto_now=True)




