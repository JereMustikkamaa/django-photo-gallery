from django.urls import path
from register.views import home_view, register_view


urlpatterns = [
    path('', home_view, name="main"),
    path('register/', register_view, name="register")
    ]
