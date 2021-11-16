from rest_framework import serializers
from .models import Product, Comment


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product        # product 모델 사용
#         fields = '__all__'            # 모든 필드 포함

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product        # product 모델 사용
        fields = '__all__'            # 모든 필드 포함
