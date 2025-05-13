
from django.urls import path
from app.views import *
urlpatterns = [
    path('', home, name='home'),
    path('product', product, name='product'),
    path('contact', contact, name='contact'),
]
