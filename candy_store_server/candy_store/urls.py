from django.urls import path

from candy_store import views

urlpatterns = [
    path('api/v1/categories', views.CategoryListView.as_view()),
]
