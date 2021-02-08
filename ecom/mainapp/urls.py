from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('checkout/', checkout , name='checkout'),
    path('contact/', contact , name='contact'),
    path('about-us/', about , name='about'),
    path('team/', team , name='team'),
    path('blog/', blog , name='blog'),
    path('testimonials/', testes , name='testicles'),
    path('terms/', terms , name='terms'),
    path('details/', details, name='details'),
    path('blog_details', blog_details, name='blogd')

]
