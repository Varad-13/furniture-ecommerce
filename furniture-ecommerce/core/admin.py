from django.contrib import admin
from .models import Category, Product, ProductImage, Address, UserProfile, Cart, Order, Coupon

# Inline model admin for ProductImage
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of extra forms to show

# Admin model for Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'inventory', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    inlines = [ProductImageInline]

    def save_model(self, request, obj, form, change):
        obj.save()
        # You can add custom logic here if needed

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        # Custom logic after saving related objects

# Registering models in the admin site
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Address)
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Coupon)
