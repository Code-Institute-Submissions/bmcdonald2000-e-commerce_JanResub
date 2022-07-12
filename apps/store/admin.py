from django.contrib import admin

# Register your models here.
from .models import Category


# registers my models with the django admin so I can use them.
admin.site.register(Category)

