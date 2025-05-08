# usuarios/urls.py
from django.urls import path
from . import views
from .views import CustomLoginView, ver_cuenta, confirmar_logout, redireccion_post_login

urlpatterns = [
    path("registro/", views.registro, name="registro"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("account/", ver_cuenta, name="account"),
    path("logout/", confirmar_logout, name="logout"),
    path('redirigir/', redireccion_post_login, name='redireccion_post_login'),
]
