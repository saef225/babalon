from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()