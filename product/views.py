# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters, status
from .models import Product, Comment, User, Subscription
from rest_framework.views import APIView
from django.db.models import Avg, F, Count
from .serializers import ProductSerializer, CommentSerializer, ProductDetailSerializer, UserSerializer, SubscriptionSerializer


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


class UserAPI(viewsets.ModelViewSet):
    search_fields = ['uid']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class SubscriptionAPI(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
