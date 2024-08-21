
from django.contrib import admin
from apps.Products.models import Product,Category,PhotoProductGallery






admin.site.register(Category)
admin.site.register(Product)
admin.site.register(PhotoProductGallery)