# Generated by Django 4.2 on 2024-05-11 17:15

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candy_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_price', models.PositiveIntegerField(default=0, verbose_name='Общая сумма')),
                ('total_quantity', models.PositiveIntegerField(default=0, verbose_name='Всего товаров')),
                ('discount', models.PositiveIntegerField(default=0, null=True, verbose_name='Скидка')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.IntegerField(default=1, verbose_name='Количество товара')),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='cart.cart', verbose_name='Корзина')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candy_store.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар корзины',
                'verbose_name_plural': 'Товары корзины',
            },
        ),
    ]
