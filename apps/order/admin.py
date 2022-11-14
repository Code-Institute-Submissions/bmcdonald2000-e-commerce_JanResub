from django.contrib import admin
from .models import Order, Item


# Registers models in the admin
admin.site.register(Order)
admin.site.register(Item)
