from rest_framework.generics import ListAPIView
from candy_store.serializers import CategorySerializer, ProductSerializer
from candy_store.models import Category, Product


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
