from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(default="", max_length=1000)
    prerequisites = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(default="", max_length=1000)
    content = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class TopicTaken(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    taken = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['taken']
