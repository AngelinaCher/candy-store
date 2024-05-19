from django.core.exceptions import ObjectDoesNotExist
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from candy_store.models import Product
from cart.models import Cart, CartItem
from cart.serializers import CartSerializer


class CartAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Корзина покупателя

        Сумма товаров считается в зависимости от типа unit.
        Если тип unit = гр, значит сумма рассчитывается на 100гр
        """
        try:
            cart = Cart.objects.get(user_id=request.user, is_active=True)
            serializer = CartSerializer(cart, context={'request': request})
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"message": "Корзина пуста"}, status=200)


@extend_schema(request=CartSerializer, examples=[
    OpenApiExample(name='Request', value={
        'product_id': '0b75b3d3-61ac-4587-a253-02bdfc2b13c5',
        'product_quantity': "5"
    }), ])
class AddToCartAPIView(APIView):
    """ Создание корзины и добавление в неё товаров """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """
        Сумма товаров считается в зависимости от типа unit.
        Если тип unit = гр, значит сумма рассчитывается на 100гр
        """
        product_id = request.data.get('product_id')
        product_quantity = request.data.get('product_quantity')

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"message": "Указанный продукт не существует"}, status=400)

        try:
            cart = Cart.objects.get(user_id=request.user, is_active=True)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user_id=request.user)

        cart_item, created = CartItem.objects.get_or_create(
            cart_id=cart,
            product_id=product,
            defaults={'product_quantity': int(product_quantity)}
        )
        if not created:
            cart_item.product_quantity += int(product_quantity)
            cart_item.save()

        cart_serializer = CartSerializer(cart, context={'request': request})
        total_price = cart_serializer.get_total_price(cart)
        total_quantity = cart_serializer.get_total_quantity(cart)

        cart.total_price = total_price
        cart.total_quantity = total_quantity
        cart.save()

        return Response(cart_serializer.data)


@extend_schema(request=CartSerializer, examples=[
    OpenApiExample(name='Request', value={
        'product_id': '0b75b3d3-61ac-4587-a253-02bdfc2b13c5',
        'product_quantity': "1"
    }), ])
class RemoveFromCartAPIView(APIView):
    """ Уменьшение количества товаров в корзине и удаление корзины, если в ней не осталось товаров """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        product_quantity = int(request.data.get('product_quantity', 1))  # По умолчанию уменьшаем на 1

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"message": "Указанный продукт не существует"}, status=400)

        cart, created = Cart.objects.get(user_id=request.user, is_active=True)

        try:
            cart_item = CartItem.objects.get(cart_id=cart, product_id=product)
        except CartItem.DoesNotExist:
            return Response({"message": "Указанный товар не найден в корзине"}, status=400)

        cart_item.product_quantity -= product_quantity
        if cart_item.product_quantity <= 0:
            cart_item.delete()
            if cart.cart_items.count() == 0:
                cart.delete()
                return Response({"message": "Корзина была удалена, так как в ней не осталось товаров"}, status=200)
        else:
            cart_item.save()

        cart_serializer = CartSerializer(cart, context={'request': request})
        total_price = cart_serializer.get_total_price(cart)
        total_quantity = cart_serializer.get_total_quantity(cart)

        cart.total_price = total_price
        cart.total_quantity = total_quantity
        cart.save()

        return Response(cart_serializer.data)


class ClearCartAPIView(APIView):
    """ Удаление всех товаров из корзины и корзины пользователя """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            carts = Cart.objects.filter(user_id=request.user, is_active=True)
            if not carts.exists():
                return Response({"message": "Корзина не найдена"}, status=404)

            for cart in carts:
                cart_items = CartItem.objects.filter(cart_id=cart)
                cart_items.delete()
                cart.delete()

            return Response({"message": "Корзина и все товары в ней были удалены"}, status=200)
        except Exception as e:
            return Response({"message": f"Произошла ошибка при удалении корзины: {e}"}, status=500)
