import uuid

from django.db import models

from cart.models import Cart
from users.models import CustomUser


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Заказ')
    customer_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, null=False, blank=False,
                                    verbose_name='Пользователь')
    cart_id = models.ForeignKey(to=Cart, on_delete=models.CASCADE, verbose_name='Козина')
    order_date = models.DateTimeField(verbose_name='Дата заказа', auto_now_add=True, null=False)
    required_date = models.DateTimeField(verbose_name='Требуемая дата')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма', default=0)
    status = models.CharField(max_length=20, choices=(
        ('new', 'Новый'),
        ('in_progress', 'В обработке'),
        ('confirmed', 'Подтверждён'),
        ('completed', 'Выполнен')), default='new', verbose_name='Статус заказа')
    payment_method = models.CharField(max_length=20, choices=(
        ('CH', 'Наличные'),
        ('BC', 'Банковская карта'),
    ), verbose_name='Метод оплаты')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.order_id

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
