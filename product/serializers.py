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

    class Meta:
        def hasComment(value):
            if value == 'true':
                print('YOYO')
                print(field)
            else:
                print('POP')

        model = Product        # product 모델 사용
        fields = field            # 모든 필드 포함
        print(fields)
        # exclude = ['comments']

    # name = models.CharField(max_length=70)
    # company = models.CharField(default='', max_length=30)
    # price = models.IntegerField()
    # image = models.ImageField(default='product/default_image.png')
    # category = models.CharField(max_length=20, default='기타')
    # description = models.TextField(default='정보 없음')
    # created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
