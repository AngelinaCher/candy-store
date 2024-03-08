import uuid
from django.db import models
from orders.models import Order
from users.models import CustomUser
from candy_store.models import Product


class PaymentMethod(models.TextChoices):
    BANK_CARD = 'BC', 'Банковская карта'
    CASH = 'CH', 'Наличные'


class Cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(to=Order, on_delete=models.PROTECT, null=False, blank=False,
                                 verbose_name='Номер заказа')
    user_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, null=False, blank=False,
                                verbose_name='Пользователь')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False,
                                   verbose_name='Товар')
    quantity = models.IntegerField(verbose_name='Количество')
    discount = models.PositiveIntegerField(verbose_name='Скидка', null=True, default=None)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Общая сумма')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_active = models.BooleanField(default=True, verbose_name='Активность корзины')
    notes = models.TextField(blank=True, null=True, verbose_name='Комментарий пользователя')
    payment_method = models.CharField(max_length=255, blank=True, choices=PaymentMethod.choices,
                                      verbose_name='Способ оплаты')
    discount_code = models.CharField(max_length=255, blank=True, verbose_name='Промокод')

    def __str__(self):
        return self.cart_id


    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
