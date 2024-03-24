# Generated by Django 4.2 on 2024-03-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_rename_created_up_cart_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.AddField(
            model_name='cart',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активность'),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.PositiveIntegerField(default=0, verbose_name='Общая сумма'),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Всего товаров'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='discount',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Скидка'),
        ),
    ]