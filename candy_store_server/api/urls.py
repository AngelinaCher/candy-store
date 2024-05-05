from django.urls import path, include

from api import products_views


urlpatterns = [
    path('v1/categories', products_views.CategoryListView.as_view(), name='category-list'),
    path('v1/products', products_views.ProductListView.as_view(), name='product-list'),
    path('v1/products/<slug:slug>/', products_views.ProductDetailView.as_view(), name='product-detail'),
]
