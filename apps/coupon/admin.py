from django.contrib import admin

from .models import Coupon

# registers coupon so it can be used within the app
admin.site.register(Coupon)
