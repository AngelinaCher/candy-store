from rest_framework import serializers
from candy_store.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id', 'category_name', 'slug',)


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    image_path = serializers.ImageField(max_length=None, use_url=True)

    def get_category_name(self, obj):
        return obj.category_id.category_name

    class Meta:
        model = Product
        fields = (
            'product_id', 'product_name', 'category_name', 'description', 'unit', 'unit_price', 'image_path', 'slug',)
