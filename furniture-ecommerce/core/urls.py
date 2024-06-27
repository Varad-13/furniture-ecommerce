from django.urls import path
from .views import *

urlpatterns = [
    path('search/', search_products, name='search_products'),
    path('', index, name='index'),
    path('products/<str:sku>/', product_detail, name='product_detail'),
    path('create-checkout-session/<str:sku>/', create_checkout_session, name='create_checkout_session'),
    path('success/', payment_success, name='payment_success'),
]
