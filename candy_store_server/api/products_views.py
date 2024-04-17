from typing import Union
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.db.models import Count

from candy_store.models import Category, Product
from candy_store.serializers import CategorySerializer, ProductSerializer


class CategoryListView(ListAPIView):
    """
    Список всех категорий

    Возвращает список всех категорий, где есть товары
    """
    serializer_class = CategorySerializer

    def get_queryset(self) -> list[Category]:
        queryset = Category.objects.annotate(num_products=Count('product'))
        queryset = queryset.filter(num_products__gt=0)

        return queryset


class ProductListView(ListAPIView):
    """
    Список товаров по категории

    Возвращает список всех товаров, если в запросе не указан category_id,
    и список товаров по указанной категории, если category_id присутствует в запросе.
    """
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs) -> Union[Response, list[Product]]:
        category_id = self.request.query_params.get('category_id')

        if category_id is not None:
            try:
                category_id = int(category_id)
            except ValueError:
                return Response({"error": "Невалидное значение category_id"}, status=HTTP_400_BAD_REQUEST)

            queryset = Product.objects.filter(category_id=category_id)
            if not queryset.exists():
                return Response({"error": f"Категории с {category_id} не существует"}, status=HTTP_400_BAD_REQUEST)
        else:
            queryset = Product.objects.all()

        return queryset


class ProductDetailView(RetrieveAPIView):
    """ Вывод конкретного товара """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

