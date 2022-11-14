from django.contrib import admin
from .models import Category, Product, ProductImages, ProductReview


# registers my models with the django admin so I can use them.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(ProductReview)
