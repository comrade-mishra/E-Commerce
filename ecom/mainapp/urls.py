from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products', prd_render , name='products')
]