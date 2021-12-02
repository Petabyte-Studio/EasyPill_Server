# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters
from .models import Product, Comment
from rest_framework.views import APIView
from django.db.models import Avg, F, Count
from .serializers import ProductSerializer, CommentSerializer, ProductDetailSerializer


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class ProductListAPI(viewsets.ModelViewSet):
    # search_fields = ['name']
    # value = ['company', 'image', 'name', 'price']
    # value.append('comments')
    filter_backends = (DynamicSearchFilter, filters.OrderingFilter)
    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    def get_queryset(self):
        return super().get_queryset().annotate(avg_rate=Avg(F('comments__rate'))).annotate(comment_count=Count('comments__rate'))


def ProductDetailAPI(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductDetailSerializer(product, context=('request'))
        return JsonResponse(serializer.data)


class CommentAPI(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
