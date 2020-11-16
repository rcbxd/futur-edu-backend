from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status, generics

from django.contrib.auth.models import User
from app.models import Card, Category

from app.serializers import CardSerializer, UserSerializer, CategorySerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['GET'])  # code post later
def category_detail(request, pk, format=None):
    if request.method == 'GET':
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        print(serializer.data)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def card_list(request, format=None):
    if request.method == 'POST':
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def card_detail(request, pk, format=None):
    card = get_object_or_404(Card, pk=pk)

    if request.method == 'GET':
        serializer = CardSerializer(card, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CardSerializer(card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
