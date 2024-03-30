# Generated by Django 4.2 on 2024-03-18 17:24

import uuid

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255, unique=True, verbose_name='Название категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('unit', models.CharField(max_length=20, verbose_name='Единица измерения')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за единицу')),
                ('units_in_stock', models.PositiveIntegerField(verbose_name='Название товара')),
                ('image_path', models.ImageField(blank=True, null=True, upload_to='product_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])], verbose_name='Изображение')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['product_name'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255, verbose_name='Название компании')),
                ('contact_name', models.CharField(max_length=128, verbose_name='Контактное лицо')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('home_page', models.URLField(blank=True, max_length=255, null=True, verbose_name='Сайт')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
                'ordering': ['company_name', 'contact_name'],
            },
        ),
        migrations.AddIndex(
            model_name='supplier',
            index=models.Index(fields=['company_name', 'email'], name='candy_store_company_fbac32_idx'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='candy_store.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='candy_store.supplier', verbose_name='Поставщик'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['category_name'], name='candy_store_categor_6c6af2_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['product_name'], name='candy_store_product_08285e_idx'),
        ),
    ]
