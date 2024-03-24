from django.contrib import admin
from cart.models import Cart, CartItem


class CartItemAdmin(admin.TabularInline):
    model = CartItem
    fields = ('cart_id', 'product_id', 'product_quantity', 'user_id',)
    readonly_fields = ('cart_id', 'product_id', 'user_id')
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'total_quantity', 'total_price', 'discount', 'notes')
    fields = ('cart_id', 'total_quantity', 'total_price', 'discount', 'notes', 'created_at', 'updated_at')
    readonly_fields = ('cart_id', 'created_at', 'updated_at')
    inlines = [CartItemAdmin]
