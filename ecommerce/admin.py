from django.contrib import admin
from .models import Product, Category, Seller, Brand, Warranty

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Warranty)
admin.site.register(Seller)
admin.site.register(Product)
