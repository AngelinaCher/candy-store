from django.urls import include, path

from authentication import views

urlpatterns = [
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
    path('v1/auth/login/', views.LoginView.as_view(), name="login", ),
    path('auth/activate/<uid>/<token>', views.ActivateUser.as_view({'get': 'activation'}), name='activation'),
]
