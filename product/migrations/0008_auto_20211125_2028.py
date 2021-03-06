# Generated by Django 3.2.9 on 2021-11-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_comment_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='기타', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='정보 없음'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product/default_image.png', upload_to=''),
        ),
    ]
