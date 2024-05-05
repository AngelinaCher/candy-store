from djoser.views import UserViewSet
from rest_framework.decorators import action


class ProfileView(UserViewSet):

    @action(["get"], detail=False)
    def me(self, request, *args, **kwargs):
        """
        Возвращает данные пользователя
        """
        self.get_object = self.get_instance
        return self.retrieve(request, *args, **kwargs)

    @action(["patch"], detail=False)
    def me(self, request, *args, **kwargs):
        """
        Принимает поля для обновления и изменяет данные пользователя, идентификаторов выступает email
        """
        self.get_object = self.get_instance
        return self.partial_update(request, *args, **kwargs)
