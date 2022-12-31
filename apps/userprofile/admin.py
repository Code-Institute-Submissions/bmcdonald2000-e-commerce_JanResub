from django.contrib import admin

# Register your models here.
from .models import Userprofile

# Registers the subscriber models
admin.site.register(Userprofile)
