from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render
from djoser import email, utils
from djoser.conf import settings
from djoser.views import UserViewSet
from rest_framework.decorators import action
from rest_framework.versioning import URLPathVersioning
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)


class SetPasswordView(UserViewSet):
    versioning_class = URLPathVersioning

    @action(["post"], detail=False)
    def set_password(self, request, *args, **kwargs):
        """
        API для смены пароля. Принимает новый и текущий пароль.
        """

        return super().set_password(request, *args, **kwargs)


class RegisterUserView(UserViewSet):
    """
    Получает email и password, затем оправляет письмо на почту для активации аккаунта
    """

    versioning_class = URLPathVersioning

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class LoginView(TokenObtainPairView):
    """
    Принимает email и password активированного пользователя и возвращает access и refresh
    jwt-токены.
    """

    versioning_class = URLPathVersioning


class RefreshTokenView(TokenRefreshView):
    """
    Принимает refresh-token и обновляет access-токен
    """

    versioning_class = URLPathVersioning


class VerifyTokenView(TokenVerifyView):
    """
    Принимает токен и указывает, является ли он действительным.
    """

    versioning_class = URLPathVersioning


class SetPasswordEmail(email.ActivationEmail):
    """
    Формирует письмо об смене пароля
    """
    template_name = 'authentication/set_password.html'


class ActivateEmail(email.ActivationEmail):
    """
    Формирует письмо для активации аккаунта
    """
    template_name = 'authentication/activation_email.html'

    def get_context_data(self):
        context = super().get_context_data()

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.ACTIVATION_URL.format(**context)
        return context


class ActivateUser(UserViewSet):
    """ Активирует аккаунт и отображает страницу об успешной активации после перехода по ссылке """

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())

        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}

        return serializer_class(*args, **kwargs)

    def activation(self, request, uid, token, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return render(request, template_name='authentication/activation_confirmation.html', )
