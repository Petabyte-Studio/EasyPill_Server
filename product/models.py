from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=70)
    company = models.CharField(default='', max_length=30)
    price = models.IntegerField()
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(
        Product, related_name='comments', on_delete=models.CASCADE, default=None)
    user = models.CharField(default='oo', max_length=20)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.comment
