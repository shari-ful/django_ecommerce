# Generated by Django 4.2.1 on 2023-05-31 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_seller_address_alter_brand_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images/product_images/'),
        ),
    ]
