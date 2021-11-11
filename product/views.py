# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Product, Comment
from rest_framework.views import APIView
from .serializers import ProductSerializer, CommentSerializer


class ProductListAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    print(queryset)
    serializer_class = ProductSerializer
    # def get(self, request):
    #     queryset = Product.objects.all()
    #     print(queryset)
    #     serializer = ProductSerializer(queryset, many=True)
    #     return Response(serializer.data)


class CommentAPI(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
