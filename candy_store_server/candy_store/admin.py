from django.contrib import admin
from candy_store.models import Category, Product, Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_name', 'email', 'phone_number',)
    fields = ('company_name', 'contact_name', 'address', 'email', 'phone_number', 'home_page', 'created_at',
              'updated_at',)
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('company_name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    fields = ('category_name', 'description', 'slug', 'created_at', 'updated_at',)
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'supplier_id', 'category_id', 'unit_price', 'unit', 'is_active', 'image_path',)
    fields = ('product_name', 'supplier_id', 'category_id', 'description', ('unit_price', 'unit',),
              ('units_in_stock', 'is_active'),
              'image_path', 'created_at', 'updated_at', 'slug',)
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('product_name',)
