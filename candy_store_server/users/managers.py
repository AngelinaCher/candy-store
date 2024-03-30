from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """ Модель менеджера пользователей """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    def check_password(self, raw_password):
        return self.model.check_password(raw_password)

    def change_email(self, new_email, password=None):
        if password is None:
            raise ValueError(_('Password must be provided.'))
        user = self.model.objects.get(email=self.normalize_email(new_email))
        if user.check_password(password) and user.email != new_email:
            user.email = new_email
            user.save()
            return user
        raise ValueError(_('Invalid password or email.'))

    def change_password(self, email, old_password, new_password):
        """
        Change the password for a user.
        """
        user = self.model.objects.get(email=email)
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return user
        raise ValueError(_('Invalid password or email.'))
