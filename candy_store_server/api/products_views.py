from rest_framework.generics import ListAPIView
from candy_store.serializers import CategorySerializer
from candy_store.models import Category


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
