from rest_framework.generics import ListAPIView

from candy_store.models import Category
from candy_store.serializers import CategorySerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
