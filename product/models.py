from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=70)
    company = models.CharField(default='', max_length=30)
    price = models.IntegerField()
    image = models.ImageField(default='product/default_image.png')
    category = models.CharField(max_length=20, default='기타')
    description = models.TextField(default='정보 없음')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(
        Product, related_name='comments', on_delete=models.CASCADE, default=None)
    user = models.CharField(default='oo', max_length=20)
    comment = models.TextField()
    rate = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.comment


class User(models.Model):
    uid = models.CharField(max_length=40)
    name = models.CharField(max_length=30)
    image = models.ImageField(default='product/default_image.png', upload_to="profile")

    def __str__(self):
        return self.uid


class Subscription(models.Model):
    uid = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    start_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.uid
