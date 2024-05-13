# в файле signals.py вашего приложения

from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from orders.models import Order


@receiver(post_save, sender=Order)
def send_confirmation_email(sender, instance, created, **kwargs):
    PAYMENT_METHOD_MAPPING = {
        'CH': 'Наличные',
        'BC': 'Банковская карта',
    }

    if instance.status == 'confirmed':
        subject = 'Ваш заказ подтвержден'

        if instance.customer_id.firstname and instance.customer_id.lastname:
            recipient_name = f'{instance.customer_id.firstname} {instance.customer_id.lastname}'
        else:
            recipient_name = None

        required_date_formatted = instance.required_date.strftime('%d.%m.%Y')

        message_html = render_to_string('orders/confirm_orders_email.html', {
            'recipient_name': recipient_name,
            'order_id': instance.order_id,
            'required_date': required_date_formatted,
            'payment_method': PAYMENT_METHOD_MAPPING.get(instance.payment_method),
        })

        message_plain = strip_tags(message_html)

        recipient_email = instance.customer_id.email
        from_email = settings.DEFAULT_FROM_EMAIL
        send_mail(subject, message_plain, from_email, [recipient_email], html_message=message_html)
