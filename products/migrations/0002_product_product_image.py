# Generated by Django 3.2.9 on 2021-11-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, default='product_img/cute.jfif', null=True, upload_to='product_img/'),
        ),
    ]