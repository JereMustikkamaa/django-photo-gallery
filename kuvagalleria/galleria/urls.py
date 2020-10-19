from django.urls import path, include
from . import views
from register.views import register_view
from login.views import signin, signout
from django.contrib import admin

app_name = 'galleria'

urlpatterns = [
    path('', views.index, name='index'),
    path('images/<int:pk>', views.imagepage, name='imagepage'),
    path('profile/<str:user>', views.profilepage, name='profile'),
    path('upload/', views.uploadpage, name='upload'),
    path('search/', views.search, name='search'),
    path('register/', register_view, name='register'),
    path('login/', signin, name='login'),
    path('logout/', signout, name='logout'),
]

