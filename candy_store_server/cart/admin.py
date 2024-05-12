from django.contrib import admin

from cart.models import Cart, CartItem


class CartItemAdmin(admin.TabularInline):
    model = CartItem
    fields = ('cart_id', 'product_id', 'product_quantity',)
    readonly_fields = ('cart_id',)
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'total_quantity', 'total_price', 'discount',)
    fields = ('total_quantity', 'total_price', 'discount', 'created_at', 'updated_at', 'user_id')
    readonly_fields = ('created_at', 'updated_at',)
    inlines = [CartItemAdmin]
