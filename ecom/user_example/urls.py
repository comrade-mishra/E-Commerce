from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.Register, name = 'register'),
    path('login/', views.loginpage, name = 'login'),
    path('logout/', views.logout, name = 'logout')
]