# Generated by Django 3.2.7 on 2021-11-16 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20211116_0255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rate',
        ),
        migrations.AddField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(default=-1),
        ),
    ]