from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Product
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

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
    context = {
        'product': product,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'core/product_detail.html', context)

@csrf_exempt
def create_checkout_session(request, sku):
    product = get_object_or_404(Product, sku=sku)
    price = product.get_effective_price()

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(float(price) * 100),  # amount in cents
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri(f'/products/{sku}/'),
    )
    return redirect(session.url, code=303)

def payment_success(request):
    return render(request, 'core/success.html')

def index(request):
    products = Product.objects.all()
    return render(request, 'core/index.html', {'products': products})

def products(request):
    products = Product.objects.all()
    return render(request, 'core/index.html', {'products': products})