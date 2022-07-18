"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# django imports
from django.contrib import admin
from django.urls import path

from apps.core.views import home, contact
from apps.store.views import view_product

# url configarations for apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('Contact_Us/', contact, name='contact'),
    path('<slug:slug>/View_Details/',view_product, name='view_product'),
]
