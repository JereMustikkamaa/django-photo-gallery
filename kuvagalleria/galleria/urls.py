from django.urls import path
from . import views
from login import views as login_views

app_name = 'galleria'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.imagepage, name='imagepage'),
    path('<str:user>', views.profilepage, name='profile'),
    path('upload/', views.uploadpage, name='upload'),
    path('login/', login_views.login, name='login')
]

