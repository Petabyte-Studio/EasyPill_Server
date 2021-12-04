# Generated by Django 3.2.7 on 2021-12-03 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20211125_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(default='product/default_image.png', upload_to='')),
                ('email', models.CharField(max_length=30)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
