# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters
from .models import Product, Comment
from rest_framework.views import APIView
from django.db.models import Avg, F
from .serializers import ProductSerializer, CommentSerializer


class ProductListAPI(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    print(queryset)
    serializer_class = ProductSerializer

    def get_queryset(self):
        return super().get_queryset().annotate(avg_rate=Avg(F('comments__rate')))
    # def get(self, request):
    #     queryset = Product.objects.all()
    #     print(queryset)
    #     serializer = ProductSerializer(queryset, many=True)
    #     return Response(serializer.data)


class CommentAPI(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
