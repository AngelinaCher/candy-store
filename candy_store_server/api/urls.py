from django.urls import path
from api import products_views

urlpatterns = [
    path('v1/categories', products_views.CategoryListView.as_view()),
]
