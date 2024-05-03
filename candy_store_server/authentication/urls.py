from django.urls import include, path, re_path
from djoser import views as djoser_views

urlpatterns = [
    path('v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
