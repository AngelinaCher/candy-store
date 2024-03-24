from django.contrib import admin
from orders.models import Order


class OrderAdmin(admin.TabularInline):
    model = Order
    fields = ('order_id', 'customer_id', 'cart_id', 'order_date', 'required_date', 'total_price', 'status',
              'payment_method', 'created_at', 'updated_at')
    readonly_fields = ('order_id', 'customer_id', 'cart_id', 'order_date', 'created_at', 'updated_at')
    extra = 0
