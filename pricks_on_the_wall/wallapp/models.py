from django.db import models

# Create your models here.
from django.db import models
from login.models import User


class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(
        User, related_name='message', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    comment_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    message = models.ForeignKey(
        Message, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='comment', on_delete=models.CASCADE, default=1)
