import uuid
from django.db import models
from users.models import CustomUser


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_id = models.ForeignKey(to=CustomUser, on_delete=models.PROTECT, null=False, blank=False,
                                    verbose_name='Пользователь')
    order_date = models.DateTimeField(verbose_name='Дата заказа', auto_now_add=True, null=False)
    required_date = models.DateTimeField(verbose_name='Требуемая дата')
    status = models.CharField(max_length=20, choices=(
        ('new', 'Новый'),
        ('in_progress', 'В обработке'),
        ('confirmed', 'Подтверждён'),
        ('completed', 'Выполнен')), default='new')


