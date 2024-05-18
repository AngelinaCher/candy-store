from rest_framework import serializers

from candy_store.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id', 'category_name', 'slug', 'description')


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SlugRelatedField(
        read_only=True,
        slug_field='category_name',
        source='category_id'
    )
    image_path = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'product_id', 'product_name', 'category_name', 'description', 'unit', 'unit_price', 'image_path', 'slug',
        )

    def get_image_path(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.image_path.url)
        return obj.image_path.url