from rest_framework import serializers
from .models import Product, Comment


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product        # product 모델 사용
#         fields = '__all__'            # 모든 필드 포함

field = ['name', 'company', 'price', 'image',
         'category', 'description', 'avg_rate', 'comments', ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    # comments = CommentSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True, required=False)
    image = serializers.ImageField(use_url=True)
    avg_rate = serializers.FloatField(read_only=True, default=0)
    comment_count = serializers.IntegerField(read_only=True, default=0)

    class Meta:
        model = Product        # product 모델 사용
        fields = '__all__'            # 모든 필드 포함


class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, required=False)
    image = serializers.ImageField(use_url=True)
    avg_rate = serializers.FloatField(read_only=True, default=0)

    class Meta:
        model = Product
        fields = '__all__'
