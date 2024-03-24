import uuid
from django.db import models
from users.models import CustomUser
from candy_store.models import Product


class PaymentMethod(models.TextChoices):
    BANK_CARD = 'BC', 'Банковская карта'
    CASH = 'CH', 'Наличные'


class Cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_price = models.PositiveIntegerField(verbose_name='Общая сумма', default=0)
    total_quantity = models.PositiveIntegerField(verbose_name='Всего товаров', default=0)
    discount = models.PositiveIntegerField(verbose_name='Скидка', null=True, default=0)
    notes = models.TextField(blank=True, null=True, verbose_name='Комментарий пользователя')
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.cart_id

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items', verbose_name='Корзина')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False,
                                   verbose_name='Товар')
    product_quantity = models.IntegerField(default=1, verbose_name='Количество товара')
    user_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, null=False, blank=False,
                                verbose_name='Пользователь')

    def __str__(self):
        return f'Корзина: {self.cart_id.cart_id}, товар: {self.product_id.product_name}'

    class Meta:
        verbose_name = "Товар корзины"
        verbose_name_plural = "Товары корзины"
