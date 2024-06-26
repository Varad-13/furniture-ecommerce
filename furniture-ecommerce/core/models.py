from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    inventory = models.PositiveIntegerField()
    sku = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='product_images/')
    def get_effective_price(self):
        if self.discount:
            return self.price - self.discount
        return self.price

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

class Address(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)
    past_orders = models.ManyToManyField('Order', blank=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    txn_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    fulfilment_status = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

class Coupon(models.Model):
    coupon_code = models.CharField(max_length=50)
    user = models.ManyToManyField(User, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='coupons')
    is_common = models.BooleanField(default=False)