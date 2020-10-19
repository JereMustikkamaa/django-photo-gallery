from django.urls import path, include
from . import views
from register.views import register_view
from login.views import signin, signout
from django.contrib import admin

app_name = 'galleria'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.imagepage, name='imagepage'),
    path('<str:user>', views.profilepage, name='profile'),
    path('upload/', views.uploadpage, name='upload'),
    path('register/', register_view, name='register'),
    path('login/', signin, name='login'),
    path('logout/', signout, name='logout'),
]

