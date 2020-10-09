from django.urls import path
from login.views import signin, home_view

urlpatterns = [
    path('', home_view, name="main"),
    path('login/', signin, name="login")
]
