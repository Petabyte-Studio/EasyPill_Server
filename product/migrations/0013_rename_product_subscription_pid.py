# Generated by Django 3.2.9 on 2021-12-11 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20211205_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='product',
            new_name='pid',
        ),
    ]