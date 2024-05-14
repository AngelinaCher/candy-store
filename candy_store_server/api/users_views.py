from djoser.views import UserViewSet
from rest_framework.decorators import action


class ProfileViewSet(UserViewSet):
    """
    Возвращает или обновляет данные о пользователе
    """

    @action(["get", "patch", ], detail=False)
    def me(self, request, *args, **kwargs):
        self.get_object = self.get_instance
        if request.method == "GET":
            return self.retrieve(request, *args, **kwargs)
        elif request.method == "PATCH":
            return self.partial_update(request, *args, **kwargs)
