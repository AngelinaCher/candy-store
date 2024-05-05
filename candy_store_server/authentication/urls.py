from django.urls import include, path
from djoser.views import UserViewSet
from authentication import views

urlpatterns = [
    path('v1/auth/register/', UserViewSet.as_view({'get': 'create'}), name="register"),
    path('v1/auth/login/', views.LoginView.as_view(), name="login", ),
    path('v1/auth/jwt/refresh/', views.RefreshTokenView.as_view(), name="refresh-token", ),
    path('v1/auth/jwt/verify/', views.VerifyTokenView.as_view(), name="verify-token", ),
    path('auth/activate/<uid>/<token>', views.ActivateUser.as_view({'get': 'activation'}), name='activation'),
]
