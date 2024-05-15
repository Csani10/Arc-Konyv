from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("user/", views.user, name="user"),
    path("test/", views.test, name="test"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register")
]