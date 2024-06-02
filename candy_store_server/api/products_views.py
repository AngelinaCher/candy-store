import random

from django.db.models import Count, QuerySet
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.versioning import URLPathVersioning

from candy_store.models import Category, Product
from candy_store.serializers import CategorySerializer, ProductSerializer


class CategoryAPIView(ListAPIView):
    """
    Список всех категорий

    Возвращает список всех категорий, где есть товары
    """
    serializer_class = CategorySerializer
    versioning_class = URLPathVersioning

    def get_queryset(self) -> QuerySet:
        queryset = Category.objects.annotate(num_products=Count('product'))
        queryset = queryset.filter(num_products__gt=0)

        return queryset


class ProductAPIView(ListAPIView):
    """
    Список товаров по категории

    Возвращает список всех товаров, если в запросе не указан category_id,
    и список товаров по указанной категории, если category_id присутствует в запросе.
    """
    serializer_class = ProductSerializer
    versioning_class = URLPathVersioning

    def get_queryset(self) -> QuerySet:
        category_id = self.request.query_params.get('category_id')

        if category_id is not None:
            try:
                category_id = int(category_id)
            except ValueError:
                raise ValidationError("Невалидное значение category_id")

            queryset = Product.objects.filter(category_id=category_id)
            if not queryset.exists():
                raise ValidationError(f"Категории с {category_id} не существует")
        else:
            queryset = Product.objects.all()

        return queryset

    def list(self, request, *args, **kwargs) -> Response:
        try:
            queryset = self.get_queryset()
        except ValidationError as e:
            return Response({"error": e.args[0]}, status=HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=HTTP_200_OK)


class ProductDetailView(RetrieveAPIView):
    """ Вывод конкретного товара """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    versioning_class = URLPathVersioning
    lookup_field = 'slug'


class NewProductsAPIView(ListAPIView):
    """ Вывод новинок """
    queryset = Product.objects.order_by('-created_at')[:4]
    serializer_class = ProductSerializer
    versioning_class = URLPathVersioning


class RecommendedProductsAPIView(ListAPIView):
    """ Рекомендуемые товары """

    serializer_class = ProductSerializer
    versioning_class = URLPathVersioning

    def get_queryset(self):
        all_products = Product.objects.all()
        random_products = random.sample(list(all_products), k=4)
        return random_products
