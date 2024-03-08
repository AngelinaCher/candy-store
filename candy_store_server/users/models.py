import uuid
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """ Модель таблицы Пользователь """
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True, null=False, )
    firstname = models.CharField(max_length=128, blank=True, null=False)
    lastname = models.CharField(max_length=128, blank=True, null=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, default=timezone.now)
    slug = models.SlugField(unique=True, max_length=255, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f'{self.lastname} {self.firstname}')
            slug = base_slug
            while CustomUser.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{uuid.uuid4().hex[:5]}'
            self.slug = slug
        super().save(*args, **kwargs)

        class Meta:
            verbose_name = 'Пользователь'
            verbose_name_plural = 'Пользователи'
