from datetime import datetime

from django.utils import timezone
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from cart.serializers import CartSerializer
from orders.models import Order
from orders.serializers import OrderSerializer


class UserOrderListAPIView(APIView):
    """
    Отображение информации о всех заказах пользователя
    """
    permission_classes = [permissions.IsAuthenticated]

    PAYMENT_METHOD_MAPPING = {
        'CH': 'Наличные',
        'BC': 'Банковская карта',
    }

    def get(self, request):
        user = request.user

        # Получаем все заказы пользователя
        orders = Order.objects.filter(customer_id=user)

        orders_info = []
        for order in orders:
            cart = order.cart_id
            cart_serializer = CartSerializer(cart)

            cart_items = cart_serializer.data.get('cart_items', [])
            total_price = cart_serializer.data.get('total_price', 0)
            total_quantity = cart_serializer.data.get('total_quantity', 0)

            payment_method_display = self.PAYMENT_METHOD_MAPPING.get(order.payment_method)

            order_info = {
                'order_id': order.order_id,
                'customer_id': order.customer_id.user_id,
                'required_date': order.required_date,
                'payment_method': payment_method_display,
                'cart_items': cart_items,
                'total_price': total_price,
                'total_quantity': total_quantity
            }

            orders_info.append(order_info)

        return Response(orders_info)


class OrderDetailAPIView(APIView):
    """
    Отображение информации о заказе

    Передается параметр order_id и возвращается информация о конкретном заказе
    """
    permission_classes = [permissions.IsAuthenticated]

    PAYMENT_METHOD_MAPPING = {
        'CH': 'Наличные',
        'BC': 'Банковская карта',
    }

    def get(self, request):
        order_id = request.GET.get('order_id')
        if not order_id:
            return Response({"message": "Не указан order_id"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            order = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            return Response({"message": "Заказ не найден"}, status=status.HTTP_404_NOT_FOUND)

        cart = order.cart_id
        cart_serializer = CartSerializer(cart)

        cart_items = cart_serializer.data.get('cart_items', [])
        total_price = cart_serializer.data.get('total_price', 0)
        total_quantity = cart_serializer.data.get('total_quantity', 0)

        payment_method_display = self.PAYMENT_METHOD_MAPPING.get(order.payment_method)

        order_info = {
            'order_id': order.order_id,
            'customer_id': order.customer_id.user_id,
            'required_date': order.required_date,
            'payment_method': payment_method_display,
            'cart_items': cart_items,
            'total_price': total_price,
            'total_quantity': total_quantity
        }

        return Response(order_info)


@extend_schema(request=OrderSerializer, examples=[
    OpenApiExample(name='Request', value={
        'cart_id': '0b75b3d3-61ac-4587-a253-02bdfc2b13c5',
        'required_date': "22.05.2024",
        'payment_method': 'Наличные'
    }), ])
class OrderCreateAPIView(APIView):
    """ Создание заказа """
    permission_classes = [permissions.IsAuthenticated]

    PAYMENT_METHOD_MAPPING = {
        'Наличные': 'CH',
        'Банковская карта': 'BC',
    }

    def post(self, request, *args, **kwargs):
        required_date_str = request.data.get('required_date')
        try:
            required_date = datetime.strptime(required_date_str, '%d.%m.%Y')
        except ValueError:
            return Response({"message": "Некорректный формат даты"}, status=status.HTTP_400_BAD_REQUEST)

        payment_method_display = request.data.get('payment_method')

        payment_method = self.PAYMENT_METHOD_MAPPING.get(payment_method_display)
        if not payment_method:
            return Response({"message": "Некорректный метод оплаты"}, status=status.HTTP_400_BAD_REQUEST)

        cart_id = request.data.get('cart_id')

        try:
            cart = Cart.objects.get(pk=cart_id)
        except Cart.DoesNotExist:
            return Response({"message": "Указанный корзина не существует"}, status=status.HTTP_400_BAD_REQUEST)

        if not cart.is_active:
            return Response({"message": "Корзина неактивна"}, status=status.HTTP_400_BAD_REQUEST)

        order_data = {
            'customer_id': request.user.user_id,
            'cart_id': cart.cart_id,
            'order_date': timezone.now(),
            'required_date': required_date,
            'total_price': cart.total_price,
            'status': 'new',
            'payment_method': payment_method
        }

        serializer = OrderSerializer(data=order_data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            cart.is_active = False
            cart.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
