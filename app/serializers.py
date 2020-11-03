from rest_framework import serializers
from .models import Card, Topic, TopicTaken
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    topics_taken = serializers.PrimaryKeyRelatedField(
        many=True, queryset=TopicTaken.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'topics_taken', 'email']


class TopicTakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicTaken
        fields = ['id', 'topic', 'user', 'taken']

    def create(self, validated_data):
        return TopicTaken.objects.create(**validated_data)


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'description', 'content', 'created']

    def create(self, validated_data):
        return Topic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.content = validated_data.get(
            'content', instance.content)
        instance.save()
        return instance


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'name', 'description', 'prerequisites']

    def create(self, validated_data):
        return Card.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.prerequisites = validated_data.get(
            'prerequisites', instance.prerequisites)
        instance.save()
        return instance
