from django.urls import path, include
from . import views
from register.views import register_view
from login.views import signin, signout
from django.contrib import admin

app_name = 'galleria'

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('<int:pk>', views.imagepage, name='imagepage'),
    path('<str:user>', views.profilepage, name='profile'),
    path('upload/', views.uploadpage, name='upload'),
    path('register/', register_view, name='register'),
    path('login/', signin, name='login'),
    path('logout/', signout, name='logout'),
=======
    path('images/<int:pk>', views.imagepage, name='imagepage'),
    path('profile/<str:user>', views.profilepage, name='profile'),
    path('upload/', views.uploadpage, name='upload'),
    path('search/', views.search, name='search')
>>>>>>> 7450142d4cac1a3773b14a554d72f204ddc43300
]

