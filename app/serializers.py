from rest_framework import serializers
from .models import Card, Topic, TopicTaken, Category
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
        fields = ['name', 'content', 'created', 'id_name']

    def create(self, validated_data):
        return Topic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.content = validated_data.get(
            'content', instance.content)
        instance.id_name = validated_data.get('id_name', instance.id_name)
        instance.save()
        return instance


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['name', 'card_category', 'prerequisites', 'id']

    def create(self, validated_data):
        return Card.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_name = validated_data.get('id_name', instance.id_name)
        instance.name = validated_data.get('name', instance.name)
        instance.card_category = validated_data.get(
            'card_category', instance.card_category)
        instance.prerequisites = validated_data.get(
            'prerequisites', instance.prerequisites)
        instance.id = validated_data.get('id', instance.id_name)
        instance.save()
        return instance


class CategoryDetailSerializer(serializers.ModelSerializer):
    card_set = CardSerializer(many=True)
    topic_set = TopicSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
