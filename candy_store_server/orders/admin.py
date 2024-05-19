from django.contrib import admin

from orders.models import Order


class OrderInline(admin.TabularInline):
    model = Order
    fields = ('order_id', 'customer_id', 'cart_id', 'order_date', 'required_date', 'total_price', 'status',
              'payment_method', 'created_at', 'updated_at')
    readonly_fields = ('order_id', 'customer_id', 'cart_id', 'order_date', 'created_at', 'updated_at')
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_id',  'required_date', 'total_price', 'status',
                    'payment_method',)
    readonly_fields = ('order_id', 'customer_id', 'cart_id', 'order_date', 'created_at', 'updated_at')
    search_fields = ('order_id', 'customer_id__email', 'status')
    list_filter = ('status', 'payment_method', 'order_date')
    date_hierarchy = 'order_date'


admin.site.register(Order, OrderAdmin)
