import uuid
from django.db import models
from django.utils.text import slugify


class Supplier(models.Model):
    """ Модель таблицы Поставщики """
    supplier_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, null=False, verbose_name='Название компании')
    contact_name = models.CharField(max_length=128, verbose_name='Контактное лицо')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=False, verbose_name='Номер телефона')
    home_page = models.URLField(max_length=255, null=True, blank=True, verbose_name='Сайт')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
        ordering = ['company_name', 'contact_name']
        indexes = [
            models.Index(fields=['company_name', 'email']),
        ]


class Category(models.Model):
    """ Модель таблицы Категории """
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, null=False, verbose_name='Название категории', unique=True)
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['category_name', ]
        indexes = [models.Index(fields=['category_name', ]), ]


class Product(models.Model):
    """ Модель таблицы Продукты """
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255, null=False, verbose_name='Название товара')
    supplier_id = models.ForeignKey(to=Supplier, on_delete='PROTECT', null=False, blank=False, verbose_name='Поставщик')
    category_id = models.ForeignKey(to=Category, on_delete='PROTECT', null=False, blank=False, verbose_name='Категория')
    unit = models.CharField(max_length='20', verbose_name='Единица измерения')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу')
    units_in_stock = models.PositiveIntegerField(verbose_name='Название товара')
    is_active = models.BooleanField(default=False, verbose_name='Название товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    slug = models.SlugField(unique=True, max_length=255, blank=True)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['product_name', ]
        indexes = [models.Index(fields=['product_name', ]), ]
