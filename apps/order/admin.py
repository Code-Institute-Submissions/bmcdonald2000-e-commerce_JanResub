import datetime

from django.urls import reverse
from django.contrib import admin
from .models import Order, Item
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


# fucntion that displays order name in Admin
def order_name(obj):
    return '%s %s' % (obj.first_name, obj.last_name)


order_name.short_description = 'Name'


# function that creates a PDF confirmation of the orders
def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse('admin_order_pdf', args=[obj.id])))


order_name.short_description = 'PDF'


# Function to change order status
def admin_shipped(ModelAdmin, request, queryset):
    for order in queryset:
        order.shipped_date = datetime.datetime.now()
        order.status = Order.SHIPPED
        order.save()

        # A confirmation email is sent to the user
        html = render_to_string('order_shipped.html', {'order': order})
        send_mail('Order Shipped', 'Your order has been shipped!', 'estoreorders83@gmail.com', [order.email], fail_silently=False, html_message=html)

    return
    admin_shipped.short_description = 'Shipped'


# function to display order items in a table
class ItemInline(admin.TabularInline):
    model = Item
    raw_id_fields = ['product']


# function for Order Id, order date, order status and order times to displayed in the admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', order_name, 'status', 'created_at', order_pdf]
    # Admin can filter orders by order date or order status
    list_filter = ['created_at', 'status']
    # Admin can serach orders
    search_fields = ['first_name', 'last_name', 'address']
    # displays order items in Admin
    inlines = [ItemInline]
    actions = [admin_shipped]


# Registers models in the admin
admin.site.register(Order, OrderAdmin)
admin.site.register(Item)
