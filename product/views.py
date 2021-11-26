# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters
from .models import Product, Comment
from rest_framework.views import APIView
from django.db.models import Avg, F
from .serializers import ProductSerializer, CommentSerializer


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
    serializer_class.Meta.hasComment(value='true')

    def get_queryset(self):
        is_active = self.request.GET.get('comments', None)
        if is_active is None:
            print('VISIBLE')
            self.serializer_class.Meta.hasComment('true')
            # self.value.append('comments')
        # elif is_active == 'true':
        #     # qs = self.filter_active(qs)
        elif is_active == 'false':
            self.serializer_class.Meta.hasComment('false')
            print('INVISIBLE')
        else:
            pass
        return super().get_queryset().annotate(avg_rate=Avg(F('comments__rate')))

    # def get(self, request):
    #     queryset = Product.objects.all()
    #     print(queryset)
    #     serializer = ProductSerializer(queryset, many=True)
    #     return Response(serializer.data)


class CommentAPI(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
