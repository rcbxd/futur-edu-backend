from django.db import models
from django.contrib.auth.models import User
import uuid


class Category(models.Model):
    name = models.CharField(max_length=200, default="")
    id = models.CharField(
        max_length=32, unique=True, default="", primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']


class Card(models.Model):
    name = models.CharField(max_length=200)
    id = models.CharField(
        max_length=32, unique=True, default="", primary_key=True)
    prerequisites = models.CharField(default="", max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    card_category = models.ForeignKey(
        Category, default=None, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} -> {self.card_category}"

    class Meta:
        ordering = ['created']


class Topic(models.Model):
    name = models.CharField(max_length=200)
    id_name = models.CharField(
        max_length=32, unique=True, default="", primary_key=True)
    content = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} -> {self.category}"

    class Meta:
        ordering = ['created']


class TopicTaken(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    taken = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['taken']
