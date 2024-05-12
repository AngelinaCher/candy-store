from decimal import Decimal

from rest_framework import serializers

from candy_store.models import Product
from cart.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(source='product_id.product_id', queryset=Product.objects.all())
    product_name = serializers.CharField(source='product_id.product_name', read_only=True)
    price = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()
    image = serializers.ImageField(source='product_id.image_path', read_only=True)

    class Meta:
        model = CartItem
        fields = ['product_id', 'product_name', 'price', 'image', 'unit', 'product_quantity']

    def get_price(self, obj):
        """ Подсчёт суммы в зависимости от типа товара """
        if obj.product_id.unit == 'grams':
            price_per_100g = obj.product_id.unit_price
            return (price_per_100g / Decimal(100)) * Decimal(obj.product_quantity)
        else:
            return obj.product_id.unit_price * obj.product_quantity

    def get_unit(self, obj):
        return obj.product_id.get_unit_display()


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('user_id', 'cart_items', 'total_price', 'total_quantity',)

    def get_total_price(self, obj):
        """ Подсчёт общей суммы всех товаров в зависимости от типа товара """
        total_price = Decimal(0)
        for item in obj.cart_items.all():
            unit_price = Decimal(item.product_id.unit_price)
            if item.product_id.unit == 'grams':
                price_per_100g = unit_price
                total_price += (price_per_100g / Decimal(100)) * Decimal(item.product_quantity)
            else:
                total_price += unit_price * Decimal(item.product_quantity)

        return total_price

    def get_total_quantity(self, obj):
        """ Подсчёт позиций в корзине """
        unique_items_count = obj.cart_items.count()
        return unique_items_count
