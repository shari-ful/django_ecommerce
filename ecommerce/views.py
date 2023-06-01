

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, Category, Brand, Seller, Warranty

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    sellers = Seller.objects.all()
    warranties = Warranty.objects.all()


    name = request.GET.getlist('name')
    category = request.GET.getlist('category')
    brand = request.GET.getlist('brand')
    seller = request.GET.getlist('seller')
    warranty = request.GET.getlist('warranty')
    

    if name:
        products = products.filter(name__in=name)
    if category:
        products = products.filter(category__name__in=category)
    if brand:
        products = products.filter(brand__name__in=brand)
    if seller:
        products = products.filter(seller__name__in=seller)
    if warranty:
        products = products.filter(warranty__name__in=warranty)

    paginator = Paginator(products, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj':page_obj, 'categories': categories, 'brands': brands, 'sellers': sellers, 'warranties': warranties}
    
    return render(request, 'home.html', context=context)

