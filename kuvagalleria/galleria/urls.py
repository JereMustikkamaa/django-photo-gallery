from django.urls import path
from . import views

# app_name = 'galleria'
urlpatterns = [
    path('', views.index, name='index'),
    path('images/<int:pk>', views.imagepage, name='imagepage'),
    path('profile/<str:user>', views.profilepage, name='profile'),
    path('upload/', views.uploadpage, name='upload'),
    path('search/', views.search, name='search')
]

