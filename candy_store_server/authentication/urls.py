from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication import views

urlpatterns = [
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
    path('v1/auth/login/', TokenObtainPairView.as_view(), name="jwt-create"),
    path('auth/activate/<uid>/<token>', views.ActivateUser.as_view({'get': 'activation'}), name='activation'),
]
