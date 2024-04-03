from django.urls import path
from api import products_views

urlpatterns = [
    path('v1/categories', products_views.CategoryListView.as_view()),
    path('v1/products', products_views.ProductListView.as_view()),
]
