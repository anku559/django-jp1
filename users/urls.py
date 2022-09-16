from django.urls import path
from . import views


# URL Configuration Module
urlpatterns = [
    path("test-template/", views.test_template, name="test-template"),
    path("register/", views.say_hello, name="register"),
]
