

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, Category, Brand, Seller, Warranty

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    sellers = Seller.objects.all()
    warranties = Warranty.objects.all()


    # Filter products based on query parameters
    name = request.GET.get('name')
    category = request.GET.get('category')
    brand = request.GET.get('brand')
    seller = request.GET.get('seller')
    warranty = request.GET.get('warranty')
    

    if name:
        products = products.filter(name__icontains=name)
    if category:
        products = products.filter(category__name__icontains=category)
    if brand:
        products = products.filter(brand__name__icontains=brand)
    if seller:
        products = products.filter(seller__name__icontains=seller)
    if warranty:
        products = products.filter(warranty__name__icontains=warranty)

    paginator = Paginator(products, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj':page_obj, 'categories': categories, 'brands': brands, 'sellers': sellers, 'warranties': warranties}
    
    return render(request, 'home.html', context=context)

