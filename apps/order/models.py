from django.db import models
from apps.store.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    # options for shipping status
    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    ARRIVED = 'arrived'

    # defined status_choices
    STATUS_CHOICES = (
        (ORDERED, 'ordered'),
        (SHIPPED, 'shipped'),
        (ARRIVED, 'arrived'),
    )

    user = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)
    # customer details
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    # order date
    created_at = models.DateTimeField(auto_now_add=True)

    # order details
    paid = models.BooleanField(default=False)
    amount_paid = models.FloatField(blank=True, null=True)
    used_coupon = models.CharField(max_length=50, blank=True, null=True)
    payment_intent = models.CharField(max_length=255)

    # shipping details
    date_shipped = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
                                max_length=20,
                                choices=STATUS_CHOICES,
                                default=ORDERED)

    def __str__(self):
        return '%s' % self.first_name

    def get_total_quantity(self):
        return sum(int(item.quantity) for item in self.items.all())


class Item(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items',
                                on_delete=models.DO_NOTHING)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id
