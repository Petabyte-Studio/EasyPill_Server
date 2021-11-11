from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=70)
    company = models.CharField(default='', max_length=30)
    price = models.IntegerField()
    rank = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
