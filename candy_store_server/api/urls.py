from django.urls import path
from api import products_views, users_views

urlpatterns = [
    path('v1/categories/', products_views.CategoryListView.as_view(), name='category-list'),
    path('v1/products/', products_views.ProductListView.as_view(), name='product-list'),
    path('v1/products/<slug:slug>/', products_views.ProductDetailView.as_view(), name='product-detail'),
    path('v1/profile/', users_views.ProfileView.as_view({'get': 'me'}), name='profile'),
    path('v1/profile/update/', users_views.ProfileView.as_view({'patch': 'me'}), name='profile-update'),
]
