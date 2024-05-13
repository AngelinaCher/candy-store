from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'customer_id', 'cart_id', 'required_date', 'payment_method', 'total_price',]
