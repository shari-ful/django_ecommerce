from django.shortcuts import render
from django.db.models import Q
from .models import Product, Category, Seller

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    products = Product.objects.filter(
        Q(category__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    categories = Category.objects.all()[0:5]
    product_count = products.count()
    
    context = {'products': products, 'categories': categories, 'product_count': product_count}
    return render(request, 'home.html', context=context)
