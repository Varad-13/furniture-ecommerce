from django.shortcuts import render
from .models import Product

def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'products': products,
    }
    return render(request, 'core/search_results.html', context)
