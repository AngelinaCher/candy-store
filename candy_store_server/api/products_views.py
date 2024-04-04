from rest_framework.generics import ListAPIView
from candy_store.serializers import CategorySerializer, ProductSerializer
from candy_store.models import Category, Product


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.query_params.get('category_id', None)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset
