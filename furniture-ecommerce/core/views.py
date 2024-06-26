from django.shortcuts import render, get_object_or_404
from .models import Product

def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'products': products,
    }
    return render(request, 'core/search_results.html', context)

def product_detail(request, sku):
    product = get_object_or_404(Product, sku=sku)
    return render(request, 'core/product_detail.html', {'product': product})

def index(request):
    products = Product.objects.all()
    return render(request, 'core/index.html', {'products': products})